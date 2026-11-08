# v15.7.3 → v15.7.4 · 最優先の変更候補 (26)

[一覧の目次](README.md)

### [`0060b10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b10c.md) → [`0060b10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b10c.md) FUN_0060b10c

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
      "definition_site": "0060b110",
      "incomplete_value": false,
      "site": "0060b114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b110",
      "incomplete_value": false,
      "site": "0060b114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
        "00bf5d00",
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
        "00bf5d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060b110 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0060b110 ["COPY", "tmp:0:8", ["const:d50:8"]]
~~~


### [`0060b280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b280.md) → [`0060b280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md) FUN_0060b280

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
      "definition_site": "0060b294",
      "incomplete_value": false,
      "site": "0060b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b294",
      "incomplete_value": false,
      "site": "0060b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
        "00bf5d80",
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
        "00bf5dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060b294 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0060b294 ["COPY", "tmp:0:8", ["const:dd0:8"]]
~~~


### [`0060b2a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b2a4.md) → [`0060b2a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b2a4.md) FUN_0060b2a4

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
      "definition_site": "0060b2a8",
      "incomplete_value": false,
      "site": "0060b2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b2a8",
      "incomplete_value": false,
      "site": "0060b2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
        "00bf5d80",
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
        "00bf5dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060b2a8 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0060b2a8 ["COPY", "tmp:0:8", ["const:dd0:8"]]
~~~


### [`0060b354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b354.md) → [`0060b354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b354.md) _INIT_76

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0060b57c",
      "incomplete_value": false,
      "site": "0060b588",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060b57c",
      "incomplete_value": false,
      "site": "0060b588",
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
            "const:ac8:8"
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
      "definition_site": "0060b584",
      "incomplete_value": false,
      "site": "0060b588",
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
      "definition_site": "0060b584",
      "incomplete_value": false,
      "site": "0060b588",
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
    "ordinal": 8,
    "slot": 3
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
- 0060b380 ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 0060b380 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0060b38c ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 0060b38c ["COPY", "tmp:0:8", ["const:377:8"]]
- 0060b3a8 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 0060b3a8 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`0060b7bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b7bc.md) → [`0060b7bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md) FUN_0060b7bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060e/0060e154.md) · 呼出先 45件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044b898`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md)
- 新版 呼出元 1件 [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060e154.md) · 呼出先 45件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044b898`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 21件, `store_destination` 22件, `store_value` 14件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060bf10",
      "incomplete_value": false,
      "site": "0060bf14",
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
      "definition_site": "0060bf10",
      "incomplete_value": false,
      "site": "0060bf14",
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
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060c3b8",
      "incomplete_value": true,
      "site": "0060c3c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060c3b8",
      "incomplete_value": true,
      "site": "0060c3c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:605:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 87,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0060c670",
      "incomplete_value": false,
      "site": "0060c670",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060c670",
      "incomplete_value": false,
      "site": "0060c670",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 104,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      824,
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      864,
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
      824,
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      864,
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


~~~diff
- 0060badc ["COPY", "tmp:0:8", ["const:38:8"]]
- 0060badc ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 0060badc ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 0060badc ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 0060badc ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0060badc ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 0060badc ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 0060badc ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
~~~


### [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d1dc.md) → [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d1dc.md) FUN_0060d1dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060e/0060e154.md) [`0060ef2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060e/0060ef2c.md) · 呼出先 15件 [`00459a90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`004752f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md)
- 新版 呼出元 2件 [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060e154.md) [`0060ef2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060ef2c.md) · 呼出先 15件 [`00459a90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`004752f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 2件, `store_destination` 1件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060d330",
      "incomplete_value": true,
      "site": "0060d334",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d330",
      "incomplete_value": true,
      "site": "0060d334",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:605:8"
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
      "definition_site": "0060d37c",
      "incomplete_value": true,
      "site": "0060d394",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d37c",
      "incomplete_value": true,
      "site": "0060d394",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0060d678",
      "incomplete_value": true,
      "site": "0060d678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d678",
      "incomplete_value": true,
      "site": "0060d678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f2c:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
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
        "00c23f2c",
        null,
        "undefined4"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c23f2c",
        null,
        "undefined4"
      ]
    ],
    [
      288,
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
      64,
      "READ",
      [
        "storage",
        "00c23f7c",
        null,
        "undefined4"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c23f7c",
        null,
        "undefined4"
      ]
    ],
    [
      288,
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


~~~diff
- 0060d210 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0060d210 ["COPY", "tmp:0:8", ["const:78:8"]]
- 0060d21c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:f2c:8"]]
+ 0060d21c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:f7c:8"]]
- 0060d26c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0060d26c ["COPY", "tmp:0:8", ["const:40:8"]]
~~~


### [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) → [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) FUN_0060d83c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 20件 [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d1dc.md) [`00640008`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md) [`00640910`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md) [`00649518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md) [`006571b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md) · 呼出先 17件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0045c034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c034.md) [`0045c274`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c274.md)
- 新版 呼出元 20件 [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d1dc.md) [`00640008`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`00640910`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md) [`00649518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md) [`006571b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md) · 呼出先 17件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0045c034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c034.md) [`0045c274`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c274.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060d908",
      "incomplete_value": false,
      "site": "0060d914",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060d908",
      "incomplete_value": false,
      "site": "0060d914",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060da08",
      "incomplete_value": false,
      "site": "0060da08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060da08",
      "incomplete_value": false,
      "site": "0060da08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      216,
      "DATA",
      [
        "storage",
        "00be8498",
        null,
        "pointer"
      ]
    ],
    [
      460,
      "DATA",
      [
        "storage",
        "00bf5e90",
        null,
        "undefined *"
      ]
    ],
    [
      528,
      "READ",
      [
        "storage",
        "00bf5eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      216,
      "DATA",
      [
        "storage",
        "00be84e8",
        null,
        "pointer"
      ]
    ],
    [
      460,
      "DATA",
      [
        "storage",
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ],
    [
      528,
      "READ",
      [
        "storage",
        "00bf5f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060d908 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0060d908 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 0060da04 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0060da04 ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`0060dcac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md) → [`0060dcac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) FUN_0060dcac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d1dc.md) [`00649518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md) [`00689eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md) [`007802c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00780/007802c0.md) [`00890c70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md) · 呼出先 15件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0045c378`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c378.md) [`0045c584`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c584.md) [`00466290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/00466290.md) [`00475470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475470.md)
- 新版 呼出元 9件 [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d1dc.md) [`00649518`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md) [`00689eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689eb0.md) [`007802c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00780/007802c0.md) [`00890c70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md) · 呼出先 15件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0045c378`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c378.md) [`0045c584`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045c/0045c584.md) [`00466290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/00466290.md) [`00475470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/00475470.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0060de10",
      "incomplete_value": true,
      "site": "0060de1c",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060de10",
      "incomplete_value": true,
      "site": "0060de1c",
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
            "const:498:8"
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
      "definition_site": "0060df18",
      "incomplete_value": false,
      "site": "0060df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060df18",
      "incomplete_value": false,
      "site": "0060df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
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
      "DATA",
      [
        "storage",
        "00be8498",
        null,
        "pointer"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00bf5f10",
        null,
        "undefined *"
      ]
    ],
    [
      688,
      "READ",
      [
        "storage",
        "00bf5f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      368,
      "DATA",
      [
        "storage",
        "00be84e8",
        null,
        "pointer"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00bf5f60",
        null,
        "undefined *"
      ]
    ],
    [
      688,
      "READ",
      [
        "storage",
        "00bf5f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060de10 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0060de10 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 0060df14 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0060df14 ["COPY", "tmp:0:8", ["const:f60:8"]]
~~~


### [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060e/0060e154.md) → [`0060e154`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060e154.md) FUN_0060e154

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006041b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/006041b0.md) · 呼出先 26件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0060b7bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060b/0060b7bc.md)
- 新版 呼出元 1件 [`006041b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md) · 呼出先 26件 [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0060b7bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b7bc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060ebf0",
      "incomplete_value": false,
      "site": "0060ebf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060ebf0",
      "incomplete_value": false,
      "site": "0060ebf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 101,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0060e194",
      "incomplete_value": true,
      "site": "0060e194",
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
      "definition_site": "0060e194",
      "incomplete_value": true,
      "site": "0060e194",
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
      "definition_site": "0060e19c",
      "incomplete_value": false,
      "site": "0060e1b0",
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
      "definition_site": "0060e19c",
      "incomplete_value": false,
      "site": "0060e1b0",
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
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf5f80",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf5fd0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060e18c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0060e18c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 0060e19c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0060e19c ["COPY", "tmp:0:8", ["const:e98:8"]]
- 0060e1a4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 0060e1a4 ["COPY", "tmp:0:8", ["const:fd0:8"]]
~~~


### [`0060ef2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060e/0060ef2c.md) → [`0060ef2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060ef2c.md) FUN_0060ef2c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006041b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/006041b0.md) · 呼出先 18件 [`0044beb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d1dc.md) [`00610db8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610db8.md)
- 新版 呼出元 1件 [`006041b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md) · 呼出先 18件 [`0044beb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0060d1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d1dc.md) [`00610db8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610db8.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060efcc",
      "incomplete_value": false,
      "site": "0060efd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060efcc",
      "incomplete_value": false,
      "site": "0060efd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "definition_site": "0060f048",
      "incomplete_value": false,
      "site": "0060f050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060f048",
      "incomplete_value": false,
      "site": "0060f050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      168,
      "DATA",
      [
        "storage",
        "00bf6028",
        null,
        "undefined *"
      ]
    ],
    [
      256,
      "READ",
      [
        "storage",
        "00bf6048",
        null,
        "pointer"
      ]
    ],
    [
      256,
      "READ",
      [
        "storage",
        "00bf6050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      168,
      "DATA",
      [
        "storage",
        "00bf6078",
        null,
        "undefined *"
      ]
    ],
    [
      256,
      "READ",
      [
        "storage",
        "00bf6098",
        null,
        "pointer"
      ]
    ],
    [
      256,
      "READ",
      [
        "storage",
        "00bf60a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060efcc ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0060efcc ["COPY", "tmp:0:8", ["const:78:8"]]
- 0060f048 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 0060f048 ["COPY", "tmp:0:8", ["const:f8:8"]]
~~~


### [`0060f9b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060f9b8.md) → [`0060f9b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060f9b8.md) FUN_0060f9b8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0060dcac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md) [`008216e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/008216e4.md) · 呼出先 8件 [`00474c0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md) [`00474da4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474da4.md) [`00474f1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474f1c.md) [`0060fb80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb80.md) [`0060fb84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb84.md)
- 新版 呼出元 3件 [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0060dcac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`008216e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/008216e4.md) · 呼出先 8件 [`00474c0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474c0c.md) [`00474da4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474da4.md) [`00474f1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474f1c.md) [`0060fb80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb80.md) [`0060fb84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb84.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060fa18",
      "incomplete_value": false,
      "site": "0060fa20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fa18",
      "incomplete_value": false,
      "site": "0060fa20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      104,
      "DATA",
      [
        "storage",
        "00bf5e00",
        null,
        "undefined *"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00bf5e20",
        null,
        "pointer"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00bf5e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00bf5e50",
        null,
        "undefined *"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00bf5e70",
        null,
        "pointer"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00bf5e78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fa18 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0060fa18 ["COPY", "tmp:0:8", ["const:e50:8"]]
~~~


### [`0060fb4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb4c.md) → [`0060fb4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb4c.md) FUN_0060fb4c

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
      "definition_site": "0060fb60",
      "incomplete_value": false,
      "site": "0060fb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fb60",
      "incomplete_value": false,
      "site": "0060fb64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
        "00bf5e00",
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
        "00bf5e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fb60 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0060fb60 ["COPY", "tmp:0:8", ["const:e50:8"]]
~~~


### [`0060fb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fb70.md) → [`0060fb70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fb70.md) FUN_0060fb70

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
      "definition_site": "0060fb74",
      "incomplete_value": false,
      "site": "0060fb78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fb74",
      "incomplete_value": false,
      "site": "0060fb78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
        "00bf5e00",
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
        "00bf5e50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fb74 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 0060fb74 ["COPY", "tmp:0:8", ["const:e50:8"]]
~~~


### [`0060fbb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fbb4.md) → [`0060fbb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fbb4.md) FUN_0060fbb4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060fbcc",
      "incomplete_value": false,
      "site": "0060fbd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fbcc",
      "incomplete_value": false,
      "site": "0060fbd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
        "00bf5e90",
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
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fbcc ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0060fbcc ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`0060fc20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fc20.md) → [`0060fc20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fc20.md) FUN_0060fc20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060fc38",
      "incomplete_value": false,
      "site": "0060fc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fc38",
      "incomplete_value": false,
      "site": "0060fc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
        "00bf5e90",
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
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fc38 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0060fc38 ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`0060fc8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fc8c.md) → [`0060fc8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fc8c.md) FUN_0060fc8c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0060fec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fec8.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0060fec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fec8.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060fcb0",
      "incomplete_value": false,
      "site": "0060fcb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fcb0",
      "incomplete_value": false,
      "site": "0060fcb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:e90:8"
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
      36,
      "DATA",
      [
        "storage",
        "00bf5e90",
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
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fcac ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0060fcac ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`0060fce0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fce0.md) → [`0060fce0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fce0.md) FUN_0060fce0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0060fec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060fec8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0060fec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fec8.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0060fcec",
      "incomplete_value": false,
      "site": "0060fcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0060fcec",
      "incomplete_value": false,
      "site": "0060fcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
      "DATA",
      [
        "storage",
        "00bf5e90",
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
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0060fce4 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 0060fce4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`0061014c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/0061014c.md) → [`0061014c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/0061014c.md) FUN_0061014c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00610164",
      "incomplete_value": false,
      "site": "00610168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610164",
      "incomplete_value": false,
      "site": "00610168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
        "00bf5f10",
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
        "00bf5f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610164 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00610164 ["COPY", "tmp:0:8", ["const:f60:8"]]
~~~


### [`006101b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/006101b8.md) → [`006101b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006101b8.md) FUN_006101b8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006101d0",
      "incomplete_value": false,
      "site": "006101d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006101d0",
      "incomplete_value": false,
      "site": "006101d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
        "00bf5f10",
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
        "00bf5f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006101d0 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 006101d0 ["COPY", "tmp:0:8", ["const:f60:8"]]
~~~


### [`00610278`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610278.md) → [`00610278`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610278.md) FUN_00610278

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00610460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610460.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00610460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610460.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00610284",
      "incomplete_value": false,
      "site": "00610284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610284",
      "incomplete_value": false,
      "site": "00610284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
        "00bf5f10",
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
        "00bf5f60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0061027c ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 0061027c ["COPY", "tmp:0:8", ["const:f60:8"]]
~~~


### [`00610994`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610994.md) → [`00610994`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610994.md) FUN_00610994

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00610738`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610738.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00610738`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610738.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006109a0",
      "incomplete_value": false,
      "site": "006109a4",
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
      "definition_site": "006109a0",
      "incomplete_value": false,
      "site": "006109a4",
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
- 006109a0 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 006109a0 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`00610c14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610c14.md) → [`00610c14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c14.md) FUN_00610c14

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00610a8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610a8c.md) [`0062d23c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d23c.md) [`00717134`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00717/00717134.md) [`007689a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00768/007689a0.md) [`00769cc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00769/00769cc0.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 6件 [`00610a8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610a8c.md) [`0062d23c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d23c.md) [`00717134`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717134.md) [`007689a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/007689a0.md) [`00769cc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00610c20",
      "incomplete_value": false,
      "site": "00610c24",
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
      "definition_site": "00610c20",
      "incomplete_value": false,
      "site": "00610c24",
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
- 00610c20 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00610c20 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`00610c2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610c2c.md) → [`00610c2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c2c.md) FUN_00610c2c

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
      "definition_site": "00610c40",
      "incomplete_value": false,
      "site": "00610c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610c40",
      "incomplete_value": false,
      "site": "00610c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
        "00bf5fa8",
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
        "00bf5ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610c40 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00610c40 ["COPY", "tmp:0:8", ["const:ff8:8"]]
~~~


### [`00610c50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610c50.md) → [`00610c50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c50.md) FUN_00610c50

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
      "definition_site": "00610c54",
      "incomplete_value": false,
      "site": "00610c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610c54",
      "incomplete_value": false,
      "site": "00610c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
        "00bf5fa8",
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
        "00bf5ff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610c54 ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00610c54 ["COPY", "tmp:0:8", ["const:ff8:8"]]
~~~


### [`00610d84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610d84.md) → [`00610d84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610d84.md) FUN_00610d84

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
      "definition_site": "00610d98",
      "incomplete_value": false,
      "site": "00610d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610d98",
      "incomplete_value": false,
      "site": "00610d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
        "00bf6028",
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
        "00bf6078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610d98 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00610d98 ["COPY", "tmp:0:8", ["const:78:8"]]
~~~


### [`00610da8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610da8.md) → [`00610da8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610da8.md) FUN_00610da8

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
      "definition_site": "00610dac",
      "incomplete_value": false,
      "site": "00610db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610dac",
      "incomplete_value": false,
      "site": "00610db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
        "00bf6028",
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
        "00bf6078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610dac ["COPY", "tmp:0:8", ["const:28:8"]]
+ 00610dac ["COPY", "tmp:0:8", ["const:78:8"]]
~~~


### [`00610e34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610e34.md) → [`00610e34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610e34.md) FUN_00610e34

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
      "definition_site": "00610e48",
      "incomplete_value": false,
      "site": "00610e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610e48",
      "incomplete_value": false,
      "site": "00610e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
        "00bf60a8",
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
        "00bf60f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610e48 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00610e48 ["COPY", "tmp:0:8", ["const:f8:8"]]
~~~


### [`00610e58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610e58.md) → [`00610e58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610e58.md) FUN_00610e58

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
      "definition_site": "00610e5c",
      "incomplete_value": false,
      "site": "00610e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00610e5c",
      "incomplete_value": false,
      "site": "00610e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
        "00bf60a8",
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
        "00bf60f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00610e5c ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 00610e5c ["COPY", "tmp:0:8", ["const:f8:8"]]
~~~


### [`00610e70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610e70.md) → [`00610e70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610e70.md) FUN_00610e70

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467074`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006110c4",
      "incomplete_value": true,
      "site": "006110c4",
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
      "definition_site": "006110c4",
      "incomplete_value": true,
      "site": "006110c4",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006110cc",
      "incomplete_value": false,
      "site": "006110dc",
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
      "definition_site": "006110cc",
      "incomplete_value": false,
      "site": "006110dc",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006110d4",
      "incomplete_value": false,
      "site": "006110dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006110d4",
      "incomplete_value": false,
      "site": "006110dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      592,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      604,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      612,
      "PARAM",
      [
        "storage",
        "00bf5f80",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      592,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      604,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      612,
      "PARAM",
      [
        "storage",
        "00bf5fd0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 006110c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006110c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 006110cc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006110cc ["COPY", "tmp:0:8", ["const:e98:8"]]
- 006110d4 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 006110d4 ["COPY", "tmp:0:8", ["const:fd0:8"]]
~~~


### [`006111d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00611/006111d0.md) → [`006111d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/006111d0.md) _INIT_77

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00611270",
      "incomplete_value": true,
      "site": "00611288",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00611270",
      "incomplete_value": true,
      "site": "00611288",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "0061128c",
      "incomplete_value": true,
      "site": "006112a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0061128c",
      "incomplete_value": true,
      "site": "006112a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006113f8",
      "incomplete_value": false,
      "site": "00611404",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006113f8",
      "incomplete_value": false,
      "site": "00611404",
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
            "const:ae0:8"
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
- 006111fc ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 006111fc ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00611208 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 00611208 ["COPY", "tmp:0:8", ["const:377:8"]]
- 00611224 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00611224 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`00611bb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00611/00611bb0.md) → [`00611bb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611bb0.md) FUN_00611bb0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`004667c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004667c4.md) [`00611ad8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00611/00611ad8.md) [`006132b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/006132b4.md) · 呼出先 4件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0052dd54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd54.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`004667c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004667c4.md) [`00611ad8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611ad8.md) [`006132b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/006132b4.md) · 呼出先 4件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0052dd54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd54.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00611bf8",
      "incomplete_value": true,
      "site": "00611bf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:699:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00611bf8",
      "incomplete_value": true,
      "site": "00611bf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:60e:8"
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
        "002a360e",
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
        "002a3699",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00611bdc ["COPY", "tmp:0:8", ["const:60e:8"]]
+ 00611bdc ["COPY", "tmp:0:8", ["const:699:8"]]
~~~


### [`00611d18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00611/00611d18.md) → [`00611d18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/00611d18.md) FUN_00611d18

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00ac9054`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 31件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)
- 新版 呼出元 2件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00ac9098`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 31件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00611e10",
      "incomplete_value": true,
      "site": "00611e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00611e10",
      "incomplete_value": true,
      "site": "00611e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c4:8"
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
      "definition_site": "00611ee0",
      "incomplete_value": true,
      "site": "00611ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00611ee0",
      "incomplete_value": true,
      "site": "00611ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00612174",
      "incomplete_value": true,
      "site": "00612184",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7a4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00612174",
      "incomplete_value": true,
      "site": "00612184",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:70a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      228,
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      440,
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
      228,
      "READ",
      [
        "storage",
        "002a584f",
        null,
        "string"
      ]
    ],
    [
      272,
      "PARAM",
      [
        "storage",
        "002a9259",
        null,
        null
      ]
    ],
    [
      440,
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
- 00611df4 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 00611df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00611df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00611df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00611df4 ["COPY", "tmp:0:8", ["const:84f:8"]]
+ 00611df4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00611df4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00611df4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
~~~


### [`006132b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/006132b4.md) → [`006132b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/006132b4.md) FUN_006132b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 18件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd44.md) [`0052dd48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd48.md) [`0053ee5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00574738`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574738.md)
- 新版 呼出元 1件 [`0073496c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 18件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0052dd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd44.md) [`0052dd48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dd48.md) [`0053ee5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00574738`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574738.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006133e0",
      "incomplete_value": false,
      "site": "006133e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006133e0",
      "incomplete_value": false,
      "site": "006133e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00613408",
      "incomplete_value": false,
      "site": "00613408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00613408",
      "incomplete_value": false,
      "site": "00613408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "definition_site": "006133bc",
      "incomplete_value": true,
      "site": "006133c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006133bc",
      "incomplete_value": true,
      "site": "006133c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d88:8"
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
      264,
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      264,
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "00bf6128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      264,
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      264,
      "PARAM",
      [
        "storage",
        "00c25e10",
        null,
        "undefined1"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "00bf6178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00613358 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00613358 ["COPY", "tmp:0:8", ["const:278:8"]]
- 006133bc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 006133bc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:dd8:8"]]
- 006133d8 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 006133d8 ["COPY", "tmp:0:8", ["const:178:8"]]
~~~


### [`006140c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006140c4.md) → [`006140c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006140c4.md) FUN_006140c4

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
      "definition_site": "006140d8",
      "incomplete_value": false,
      "site": "006140dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006140d8",
      "incomplete_value": false,
      "site": "006140dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
        "00bf6128",
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
        "00bf6178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006140d8 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 006140d8 ["COPY", "tmp:0:8", ["const:178:8"]]
~~~


### [`006140e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006140e8.md) → [`006140e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006140e8.md) FUN_006140e8

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
      "definition_site": "006140ec",
      "incomplete_value": false,
      "site": "006140f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006140ec",
      "incomplete_value": false,
      "site": "006140f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
        "00bf6128",
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
        "00bf6178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006140ec ["COPY", "tmp:0:8", ["const:128:8"]]
+ 006140ec ["COPY", "tmp:0:8", ["const:178:8"]]
~~~


### [`0061412c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/0061412c.md) → [`0061412c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/0061412c.md) FUN_0061412c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614140",
      "incomplete_value": false,
      "site": "00614144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614140",
      "incomplete_value": false,
      "site": "00614144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
        "00bf61a8",
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
        "00bf61f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614140 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00614140 ["COPY", "tmp:0:8", ["const:1f8:8"]]
~~~


### [`00614188`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614188.md) → [`00614188`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614188.md) FUN_00614188

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006141a0",
      "incomplete_value": false,
      "site": "006141a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006141a0",
      "incomplete_value": false,
      "site": "006141a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
        "00bf61a8",
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
        "00bf61f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006141a0 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 006141a0 ["COPY", "tmp:0:8", ["const:1f8:8"]]
~~~


### [`006141e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006141e4.md) → [`006141e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006141e4.md) FUN_006141e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614208",
      "incomplete_value": false,
      "site": "00614208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614208",
      "incomplete_value": false,
      "site": "00614208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
        "00bf61a8",
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
        "00bf61f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614204 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 00614204 ["COPY", "tmp:0:8", ["const:1f8:8"]]
~~~


### [`00614234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614234.md) → [`00614234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614234.md) FUN_00614234

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614240",
      "incomplete_value": false,
      "site": "00614240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614240",
      "incomplete_value": false,
      "site": "00614240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
        "00bf61a8",
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
        "00bf61f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0061423c ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 0061423c ["COPY", "tmp:0:8", ["const:1f8:8"]]
~~~


### [`006143f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006143f8.md) → [`006143f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006143f8.md) FUN_006143f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614410",
      "incomplete_value": false,
      "site": "00614414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614410",
      "incomplete_value": false,
      "site": "00614414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
        "00bf6228",
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
        "00bf6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614410 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00614410 ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`00614470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614470.md) → [`00614470`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614470.md) FUN_00614470

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614488",
      "incomplete_value": false,
      "site": "0061448c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614488",
      "incomplete_value": false,
      "site": "0061448c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
        "00bf6228",
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
        "00bf6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614488 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00614488 ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`006144e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006144e8.md) → [`006144e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006144e8.md) FUN_006144e8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614518",
      "incomplete_value": false,
      "site": "00614518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614518",
      "incomplete_value": false,
      "site": "00614518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
        "00bf6228",
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
        "00bf6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0061450c ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0061450c ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`0061457c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/0061457c.md) → [`0061457c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/0061457c.md) FUN_0061457c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061459c",
      "incomplete_value": false,
      "site": "0061459c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061459c",
      "incomplete_value": false,
      "site": "0061459c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
        "00bf6228",
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
        "00bf6278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614590 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00614590 ["COPY", "tmp:0:8", ["const:278:8"]]
~~~


### [`006146c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006146c8.md) → [`006146c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006146c8.md) FUN_006146c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f524`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f524.md) [`0045f660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f660.md) [`0045fc34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045fc34.md) [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e558.md) [`0045f524`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f524.md) [`0045f660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045f660.md) [`0045fc34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045f/0045fc34.md) [`00bd6e60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00614778",
      "incomplete_value": false,
      "site": "0061477c",
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
      "definition_site": "00614778",
      "incomplete_value": false,
      "site": "0061477c",
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
      180,
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
      180,
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
- 00614770 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00614770 ["COPY", "tmp:0:8", ["const:570:8"]]
~~~


### [`006148a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/006148a0.md) → [`006148a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006148a0.md) _INIT_78

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00614920",
      "incomplete_value": true,
      "site": "0061493c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00614920",
      "incomplete_value": true,
      "site": "0061493c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00614940",
      "incomplete_value": true,
      "site": "00614958",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00614940",
      "incomplete_value": true,
      "site": "00614958",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "store_value",
    "new": {
      "definition_site": "0061495c",
      "incomplete_value": true,
      "site": "00614978",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0061495c",
      "incomplete_value": true,
      "site": "00614978",
      "value": [
        "LOAD",
        "16",
        [
          [
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
- 006148cc ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 006148cc ["COPY", "tmp:0:8", ["const:b38:8"]]
- 006148d8 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 006148d8 ["COPY", "tmp:0:8", ["const:377:8"]]
- 006148f4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 006148f4 ["COPY", "tmp:0:8", ["const:38a:8"]]
~~~


### [`00614c6c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00614/00614c6c.md) → [`00614c6c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/00614c6c.md) FUN_00614c6c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00627/00627ec8.md) · 呼出先 17件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044c86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c86c.md)
- 新版 呼出元 1件 [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627ec8.md) · 呼出先 17件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md) [`0044c86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c86c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00614de8",
      "incomplete_value": true,
      "site": "00614df8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:81c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614de8",
      "incomplete_value": true,
      "site": "00614df8",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:791:8"
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
      "definition_site": "00614de8",
      "incomplete_value": true,
      "site": "00614df8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00614de8",
      "incomplete_value": true,
      "site": "00614df8",
      "value": [
        "LOAD",
        "16",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00615014",
      "incomplete_value": false,
      "site": "00615018",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00615014",
      "incomplete_value": false,
      "site": "00615018",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 64,
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
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00291cfc",
        null,
        "string"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "00291d0b",
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
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00291c6f",
        null,
        "string"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "00291c7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00614c94 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00614c94 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00614cac ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00614cac ["COPY", "tmp:0:8", ["const:c6f:8"]]
- 00614d34 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00614d34 ["COPY", "tmp:0:8", ["const:40:8"]]
~~~


### [`00615c9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00615/00615c9c.md) → [`00615c9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00615/00615c9c.md) FUN_00615c9c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00615b10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00615/00615b10.md) [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00627/00627ec8.md) · 呼出先 16件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md) [`0044c86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c86c.md)
- 新版 呼出元 2件 [`00615b10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00615/00615b10.md) [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627ec8.md) · 呼出先 16件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md) [`0044c86c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c86c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00615f00",
      "incomplete_value": true,
      "site": "00615f10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00615f00",
      "incomplete_value": true,
      "site": "00615f10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bbc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00615f00",
      "incomplete_value": true,
      "site": "00615f10",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00615f00",
      "incomplete_value": true,
      "site": "00615f10",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00615f88",
      "incomplete_value": false,
      "site": "00615f8c",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00615f88",
      "incomplete_value": false,
      "site": "00615f8c",
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
            "const:c70:8"
          ]
        ]
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
      152,
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "002a07ab",
        null,
        "string"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "002a07bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      152,
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "002a0836",
        null,
        "string"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "002a0846",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00615cd0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00615cd0 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00615cd8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00615cd8 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00615ce0 ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00615ce0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
~~~


### [`00617724`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00617/00617724.md) → [`00617724`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/00617724.md) FUN_00617724

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006181e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00618/006181e8.md) · 呼出先 12件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006181e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/006181e8.md) · 呼出先 12件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00617760",
      "incomplete_value": false,
      "site": "00617764",
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
      "definition_site": "00617760",
      "incomplete_value": false,
      "site": "00617764",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00617cf4",
      "incomplete_value": true,
      "site": "00617cf8",
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
      "definition_site": "00617cf4",
      "incomplete_value": true,
      "site": "00617cf8",
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
    "ordinal": 100,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00617cf0",
      "incomplete_value": true,
      "site": "00617cfc",
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
      "definition_site": "00617cf0",
      "incomplete_value": true,
      "site": "00617cfc",
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
    "ordinal": 101,
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
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      1476,
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      1480,
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
      64,
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      1476,
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      1480,
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
- 00617760 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00617760 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00617ce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00617ce8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 00617cec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 00617cec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
~~~


### [`006181e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00618/006181e8.md) → [`006181e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/006181e8.md) FUN_006181e8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1e88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 28件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 1件 [`00ab1ecc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 28件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00618228",
      "incomplete_value": false,
      "site": "0061822c",
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
      "definition_site": "00618228",
      "incomplete_value": false,
      "site": "0061822c",
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
      "definition_site": "006185bc",
      "incomplete_value": true,
      "site": "006185d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006185bc",
      "incomplete_value": true,
      "site": "006185d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:71c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006185d8",
      "incomplete_value": true,
      "site": "006185d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006185d8",
      "incomplete_value": true,
      "site": "006185d8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 63,
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
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a57de",
        null,
        "string"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002a57ec",
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
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a5869",
        null,
        "string"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002a5877",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00618228 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00618228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00618228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00618228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00618228 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00618228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00618228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00618228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
~~~


### [`0061c4e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061c/0061c4e8.md) → [`0061c4e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061c/0061c4e8.md) FUN_0061c4e8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0061d5c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061d/0061d5c8.md) [`0061f76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061f/0061f76c.md) · 呼出先 19件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045b734`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md)
- 新版 呼出元 2件 [`0061d5c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061d/0061d5c8.md) [`0061f76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061f/0061f76c.md) · 呼出先 19件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045b734`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061c82c",
      "incomplete_value": true,
      "site": "0061c838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:47b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061c82c",
      "incomplete_value": true,
      "site": "0061c838",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3e1:8"
              ]
            ]
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
      "definition_site": "0061cb58",
      "incomplete_value": true,
      "site": "0061cb68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cb58",
      "incomplete_value": true,
      "site": "0061cb68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061cb64",
      "incomplete_value": true,
      "site": "0061cb6c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0061cb64",
      "incomplete_value": true,
      "site": "0061cb6c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 71,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      836,
      "READ",
      [
        "storage",
        "002a83e1",
        null,
        "string"
      ]
    ],
    [
      936,
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      1140,
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
      836,
      "READ",
      [
        "storage",
        "002a847b",
        null,
        "string"
      ]
    ],
    [
      936,
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      1140,
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


~~~diff
- 0061c828 ["COPY", "tmp:0:8", ["const:3e1:8"]]
+ 0061c828 ["COPY", "tmp:0:8", ["const:47b:8"]]
- 0061c888 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0061c888 ["COPY", "tmp:0:8", ["const:78:8"]]
- 0061c95c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0061c95c ["COPY", "tmp:0:8", ["const:40:8"]]
~~~


### [`0061d5c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061d/0061d5c8.md) → [`0061d5c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061d/0061d5c8.md) FUN_0061d5c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) · 呼出先 45件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 45件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 8件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e004",
      "incomplete_value": false,
      "site": "0061e004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e004",
      "incomplete_value": false,
      "site": "0061e004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 122,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e690",
      "incomplete_value": false,
      "site": "0061e690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e690",
      "incomplete_value": false,
      "site": "0061e690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 150,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e9b8",
      "incomplete_value": false,
      "site": "0061e9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e9b8",
      "incomplete_value": false,
      "site": "0061e9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 173,
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
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0061d600 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0061d600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0061d604 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0061d604 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0061d600 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0061d600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0061d604 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0061d604 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
~~~


### [`0061f76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061f/0061f76c.md) → [`0061f76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061f/0061f76c.md) FUN_0061f76c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) · 呼出先 29件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 29件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006203f0",
      "incomplete_value": true,
      "site": "00620400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006203f0",
      "incomplete_value": true,
      "site": "00620400",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061fe98",
      "incomplete_value": false,
      "site": "0061fe9c",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061fe98",
      "incomplete_value": false,
      "site": "0061fe9c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061fec4",
      "incomplete_value": false,
      "site": "0061fed4",
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
      "definition_site": "0061fec4",
      "incomplete_value": false,
      "site": "0061fed4",
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
    "ordinal": 87,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      748,
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      1560,
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      1576,
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
      748,
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      1560,
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      1576,
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


~~~diff
- 0061fa58 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e60:8"]]
+ 0061fa58 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:eb0:8"]]
- 0061fa64 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0061fa64 ["COPY", "tmp:0:8", ["const:40:8"]]
- 0061fd80 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0061fd80 ["COPY", "tmp:0:8", ["const:78:8"]]
~~~


### [`00620558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00620/00620558.md) → [`00620558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00620/00620558.md) FUN_00620558

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062b/0062bf80.md) · 呼出先 13件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bf80.md) · 呼出先 13件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00620590",
      "incomplete_value": true,
      "site": "00620590",
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
      "definition_site": "00620590",
      "incomplete_value": true,
      "site": "00620590",
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
      "definition_site": "00620598",
      "incomplete_value": false,
      "site": "006205a8",
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
      "definition_site": "00620598",
      "incomplete_value": false,
      "site": "006205a8",
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
      "definition_site": "006205a0",
      "incomplete_value": false,
      "site": "006205a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006205a0",
      "incomplete_value": false,
      "site": "006205a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
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
      48,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00620588 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00620588 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 00620598 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00620598 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 006205a0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006205a0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00624f34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00624/00624f34.md) → [`00624f34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624f34.md) FUN_00624f34

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00628858`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/00628858.md) [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/00628a1c.md) · 呼出先 19件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0069a9cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069a9cc.md)
- 新版 呼出元 2件 [`00628858`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/00628858.md) [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/00628a1c.md) · 呼出先 19件 [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0069a9cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a9cc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00625218",
      "incomplete_value": true,
      "site": "00625228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00625218",
      "incomplete_value": true,
      "site": "00625228",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00625238",
      "incomplete_value": true,
      "site": "00625238",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00625238",
      "incomplete_value": true,
      "site": "00625238",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00625244",
      "incomplete_value": true,
      "site": "00625254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00625244",
      "incomplete_value": true,
      "site": "00625254",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:633:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
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
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00624f70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00624f70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 00624f7c ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00624f7c ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00624f84 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00624f84 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00625684`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00625/00625684.md) → [`00625684`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00625/00625684.md) FUN_00625684

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) · 呼出先 29件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md)
- 新版 呼出元 1件 [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 29件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00450668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00625b10",
      "incomplete_value": true,
      "site": "00625b10",
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
      "definition_site": "00625b10",
      "incomplete_value": true,
      "site": "00625b10",
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
    "ordinal": 23,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00625b9c",
      "incomplete_value": true,
      "site": "00625b9c",
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
      "definition_site": "00625b9c",
      "incomplete_value": true,
      "site": "00625b9c",
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
    "ordinal": 27,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00625d64",
      "incomplete_value": true,
      "site": "00625d64",
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
      "definition_site": "00625d64",
      "incomplete_value": true,
      "site": "00625d64",
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
    "ordinal": 46,
    "slot": 0
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
        "00c1b6d0",
        null,
        "pointer"
      ]
    ],
    [
      556,
      "DATA",
      [
        "storage",
        "00c23f98",
        null,
        null
      ]
    ],
    [
      808,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      552,
      "READ",
      [
        "storage",
        "00c1b720",
        null,
        "pointer"
      ]
    ],
    [
      556,
      "DATA",
      [
        "storage",
        "00c23fe8",
        null,
        null
      ]
    ],
    [
      808,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 006258ac ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:6d0:8"]]
+ 006258ac ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:720:8"]]
- 006259ac ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006259ac ["COPY", "tmp:0:8", ["const:e98:8"]]
- 006259b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006259b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
~~~


### [`00626364`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00626/00626364.md) → [`00626364`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00626/00626364.md) FUN_00626364

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062b/0062bf80.md) · 呼出先 20件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`004460b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bf80.md) · 呼出先 20件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`004460b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006263a4",
      "incomplete_value": true,
      "site": "006263a4",
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
      "definition_site": "006263a4",
      "incomplete_value": true,
      "site": "006263a4",
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
      "definition_site": "006263ac",
      "incomplete_value": false,
      "site": "006263c0",
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
      "definition_site": "006263ac",
      "incomplete_value": false,
      "site": "006263c0",
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
      "definition_site": "006263b4",
      "incomplete_value": false,
      "site": "006263c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006263b4",
      "incomplete_value": false,
      "site": "006263c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
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
      60,
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
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 006263a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 006263a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 006263ac ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 006263ac ["COPY", "tmp:0:8", ["const:e98:8"]]
- 006263b4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006263b4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00627d10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00627/00627d10.md) → [`00627d10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627d10.md) FUN_00627d10

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ab1e88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1e88.md) · 呼出先 10件 [`00464a44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00ab11f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md)
- 新版 呼出元 1件 [`00ab1ecc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 10件 [`00464a44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00ab1234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00627d44",
      "incomplete_value": false,
      "site": "00627d50",
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
      "definition_site": "00627d44",
      "incomplete_value": false,
      "site": "00627d50",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00627d58",
      "incomplete_value": true,
      "site": "00627d68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fba:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627d58",
      "incomplete_value": true,
      "site": "00627d68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fbc:8"
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
      "definition_site": "00627d6c",
      "incomplete_value": true,
      "site": "00627d6c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00627d6c",
      "incomplete_value": true,
      "site": "00627d6c",
      "value": [
        "LOAD",
        "8",
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
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00299fbc",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00299fc9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      64,
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00299fba",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00299fc7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00627d44 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00627d44 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00627d4c ["COPY", "tmp:0:8", ["const:fbc:8"]]
+ 00627d4c ["COPY", "tmp:0:8", ["const:fba:8"]]
- 00627dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00627dc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
~~~


### [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00627/00627ec8.md) → [`00627ec8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00627/00627ec8.md) FUN_00627ec8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/00628a1c.md) · 呼出先 13件 [`0044b898`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c80c.md)
- 新版 呼出元 1件 [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/00628a1c.md) · 呼出先 13件 [`0044b898`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00627fcc",
      "incomplete_value": true,
      "site": "00627fe0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00627fcc",
      "incomplete_value": true,
      "site": "00627fe0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:647:8"
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
      "definition_site": "00627fe4",
      "incomplete_value": true,
      "site": "00627fe4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00627fe4",
      "incomplete_value": true,
      "site": "00627fe4",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00628010",
      "incomplete_value": true,
      "site": "00628024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:acc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00628010",
      "incomplete_value": true,
      "site": "00628024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b59:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      260,
      "READ",
      [
        "storage",
        "002a3647",
        null,
        "string"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "002a3655",
        null,
        "string"
      ]
    ],
    [
      328,
      "READ",
      [
        "storage",
        "00292b59",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      260,
      "READ",
      [
        "storage",
        "002a36d2",
        null,
        "string"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "002a36e0",
        null,
        "string"
      ]
    ],
    [
      328,
      "READ",
      [
        "storage",
        "00292acc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00627fc4 ["COPY", "tmp:0:8", ["const:647:8"]]
+ 00627fc4 ["COPY", "tmp:0:8", ["const:6d2:8"]]
- 00628008 ["COPY", "tmp:0:8", ["const:b59:8"]]
+ 00628008 ["COPY", "tmp:0:8", ["const:acc:8"]]
~~~


### [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00628/00628a1c.md) → [`00628a1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00628/00628a1c.md) FUN_00628a1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068c620`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c620.md) · 呼出先 31件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d208`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d208.md) [`00469f74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f74.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 1件 [`0068c620`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c620.md) · 呼出先 31件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d208`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d208.md) [`00469f74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f74.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00628dcc",
      "incomplete_value": false,
      "site": "00628dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00628dcc",
      "incomplete_value": false,
      "site": "00628dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00628f50",
      "incomplete_value": false,
      "site": "00628f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00628f50",
      "incomplete_value": false,
      "site": "00628f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00628a60",
      "incomplete_value": true,
      "site": "00628a60",
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
      "definition_site": "00628a60",
      "incomplete_value": true,
      "site": "00628a60",
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
      56,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00628a54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00628a54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 00628a68 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00628a68 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00628a70 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00628a70 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) → [`00629194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) FUN_00629194

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068c7d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c7d4.md) · 呼出先 99件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`0068c7d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c7d4.md) · 呼出先 99件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 32件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006296ac",
      "incomplete_value": false,
      "site": "006296b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006296ac",
      "incomplete_value": false,
      "site": "006296b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062a2a4",
      "incomplete_value": false,
      "site": "0062a2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062a2a4",
      "incomplete_value": false,
      "site": "0062a2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "ordinal": 75,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062a67c",
      "incomplete_value": false,
      "site": "0062a684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062a67c",
      "incomplete_value": false,
      "site": "0062a684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 92,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      1316,
      "DATA",
      [
        "storage",
        "00bf6b50",
        null,
        "undefined *"
      ]
    ],
    [
      1380,
      "READ",
      [
        "storage",
        "00bf6b70",
        null,
        "pointer"
      ]
    ],
    [
      1380,
      "READ",
      [
        "storage",
        "00bf6b78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      1316,
      "DATA",
      [
        "storage",
        "00bf6ba0",
        null,
        "undefined *"
      ]
    ],
    [
      1380,
      "READ",
      [
        "storage",
        "00bf6bc0",
        null,
        "pointer"
      ]
    ],
    [
      1380,
      "READ",
      [
        "storage",
        "00bf6bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006296ac ["COPY", "tmp:0:8", ["const:b50:8"]]
- 006296ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006296ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006296ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006296ac ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 006296ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006296ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006296ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
~~~


### [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062b/0062bf80.md) → [`0062bf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bf80.md) FUN_0062bf80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 24件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`0068d0f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 24件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0062c8a4",
      "incomplete_value": true,
      "site": "0062c8a4",
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
      "definition_site": "0062c8a4",
      "incomplete_value": true,
      "site": "0062c8a4",
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
    "ordinal": 56,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062c8ac",
      "incomplete_value": false,
      "site": "0062c8bc",
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
      "definition_site": "0062c8ac",
      "incomplete_value": false,
      "site": "0062c8bc",
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
    "ordinal": 142,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062c8b4",
      "incomplete_value": false,
      "site": "0062c8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062c8b4",
      "incomplete_value": false,
      "site": "0062c8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 142,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      2336,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      2348,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      2356,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      2336,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      2348,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      2356,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062c8a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 0062c8a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 0062c8ac ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 0062c8ac ["COPY", "tmp:0:8", ["const:e98:8"]]
- 0062c8b4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0062c8b4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`0062cfe8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062c/0062cfe8.md) → [`0062cfe8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062c/0062cfe8.md) FUN_0062cfe8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00616aa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00616/00616aa4.md) [`006171f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00617/006171f4.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00616aa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00616/00616aa4.md) [`006171f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00617/006171f4.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062cff4",
      "incomplete_value": false,
      "site": "0062cff8",
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
      "definition_site": "0062cff4",
      "incomplete_value": false,
      "site": "0062cff8",
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
- 0062cff4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0062cff4 ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`0062d610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d610.md) → [`0062d610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d610.md) FUN_0062d610

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061f4a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0061f/0061f4a8.md) [`0062d37c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d37c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0061f4a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061f/0061f4a8.md) [`0062d37c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d37c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062d61c",
      "incomplete_value": false,
      "site": "0062d620",
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
      "definition_site": "0062d61c",
      "incomplete_value": false,
      "site": "0062d620",
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
- 0062d61c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0062d61c ["COPY", "tmp:0:8", ["const:39d:8"]]
~~~


### [`0062d984`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d984.md) → [`0062d984`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d984.md) FUN_0062d984

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
      "definition_site": "0062d998",
      "incomplete_value": false,
      "site": "0062d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062d998",
      "incomplete_value": false,
      "site": "0062d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
        "00bf62c0",
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
        "00bf6310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062d998 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0062d998 ["COPY", "tmp:0:8", ["const:310:8"]]
~~~


### [`0062d9a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9a8.md) → [`0062d9a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9a8.md) FUN_0062d9a8

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
      "definition_site": "0062d9ac",
      "incomplete_value": false,
      "site": "0062d9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062d9ac",
      "incomplete_value": false,
      "site": "0062d9b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
        "00bf62c0",
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
        "00bf6310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062d9ac ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 0062d9ac ["COPY", "tmp:0:8", ["const:310:8"]]
~~~


### [`0062d9f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d9f4.md) → [`0062d9f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9f4.md) FUN_0062d9f4

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
      "definition_site": "0062da18",
      "incomplete_value": false,
      "site": "0062da18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062da18",
      "incomplete_value": false,
      "site": "0062da18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:350:8"
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
        "00bf6350",
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
        "00bf63a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062da14 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0062da14 ["COPY", "tmp:0:8", ["const:3a0:8"]]
~~~


### [`0062da28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da28.md) → [`0062da28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da28.md) FUN_0062da28

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
      "definition_site": "0062da34",
      "incomplete_value": true,
      "site": "0062da34",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062da34",
      "incomplete_value": true,
      "site": "0062da34",
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
            "const:350:8"
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
        "00bf6350",
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
        "00bf63a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062da30 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0062da30 ["COPY", "tmp:0:8", ["const:3a0:8"]]
~~~


### [`0062da7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da7c.md) → [`0062da7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da7c.md) FUN_0062da7c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062da44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062da44.md) · 呼出先 45件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`0062da44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da44.md) · 呼出先 45件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 16件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0062dd2c",
      "incomplete_value": false,
      "site": "0062dd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062dd2c",
      "incomplete_value": false,
      "site": "0062dd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
      "definition_site": "0062e068",
      "incomplete_value": true,
      "site": "0062e078",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:87c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062e068",
      "incomplete_value": true,
      "site": "0062e078",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f1:8"
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
      "definition_site": "0062e07c",
      "incomplete_value": true,
      "site": "0062e07c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0062e07c",
      "incomplete_value": true,
      "site": "0062e07c",
      "value": [
        "LOAD",
        "8",
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
      696,
      "DATA",
      [
        "storage",
        "00bf63c0",
        null,
        "undefined *"
      ]
    ],
    [
      860,
      "READ",
      [
        "storage",
        "00bf63e0",
        null,
        "pointer"
      ]
    ],
    [
      860,
      "READ",
      [
        "storage",
        "00bf63e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      696,
      "DATA",
      [
        "storage",
        "00bf6410",
        null,
        "undefined *"
      ]
    ],
    [
      860,
      "READ",
      [
        "storage",
        "00bf6430",
        null,
        "pointer"
      ]
    ],
    [
      860,
      "READ",
      [
        "storage",
        "00bf6438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062dd2c ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 0062dd2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0062dd2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0062dd2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0062dd2c ["COPY", "tmp:0:8", ["const:410:8"]]
+ 0062dd2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0062dd2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0062dd2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
~~~


### [`0062f594`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f594.md) → [`0062f594`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f594.md) FUN_0062f594

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
      "definition_site": "0062f5a8",
      "incomplete_value": false,
      "site": "0062f5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f5a8",
      "incomplete_value": false,
      "site": "0062f5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
        "00bf63c0",
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
        "00bf6410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f5a8 ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 0062f5a8 ["COPY", "tmp:0:8", ["const:410:8"]]
~~~


### [`0062f5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f5b8.md) → [`0062f5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f5b8.md) FUN_0062f5b8

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
      "definition_site": "0062f5bc",
      "incomplete_value": false,
      "site": "0062f5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:410:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f5bc",
      "incomplete_value": false,
      "site": "0062f5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
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
        "00bf63c0",
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
        "00bf6410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f5bc ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 0062f5bc ["COPY", "tmp:0:8", ["const:410:8"]]
~~~


### [`0062f65c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f65c.md) → [`0062f65c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f65c.md) FUN_0062f65c

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
      "definition_site": "0062f670",
      "incomplete_value": false,
      "site": "0062f674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f670",
      "incomplete_value": false,
      "site": "0062f674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
        "00bf6440",
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
        "00bf6490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f670 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0062f670 ["COPY", "tmp:0:8", ["const:490:8"]]
~~~


### [`0062f680`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f680.md) → [`0062f680`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f680.md) FUN_0062f680

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
      "definition_site": "0062f684",
      "incomplete_value": false,
      "site": "0062f688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f684",
      "incomplete_value": false,
      "site": "0062f688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:440:8"
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
        "00bf6440",
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
        "00bf6490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f684 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 0062f684 ["COPY", "tmp:0:8", ["const:490:8"]]
~~~


### [`0062f724`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f724.md) → [`0062f724`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f724.md) FUN_0062f724

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
      "definition_site": "0062f738",
      "incomplete_value": false,
      "site": "0062f73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f738",
      "incomplete_value": false,
      "site": "0062f73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
        "00bf64c0",
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
        "00bf6510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f738 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0062f738 ["COPY", "tmp:0:8", ["const:510:8"]]
~~~


### [`0062f748`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f748.md) → [`0062f748`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f748.md) FUN_0062f748

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
      "definition_site": "0062f74c",
      "incomplete_value": false,
      "site": "0062f750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f74c",
      "incomplete_value": false,
      "site": "0062f750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
        "00bf64c0",
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
        "00bf6510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f74c ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 0062f74c ["COPY", "tmp:0:8", ["const:510:8"]]
~~~


### [`0062f7ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f7ec.md) → [`0062f7ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f7ec.md) FUN_0062f7ec

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
      "definition_site": "0062f800",
      "incomplete_value": false,
      "site": "0062f804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f800",
      "incomplete_value": false,
      "site": "0062f804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
        "00bf6540",
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
        "00bf6590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f800 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0062f800 ["COPY", "tmp:0:8", ["const:590:8"]]
~~~


### [`0062f810`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f810.md) → [`0062f810`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f810.md) FUN_0062f810

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
      "definition_site": "0062f814",
      "incomplete_value": false,
      "site": "0062f818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f814",
      "incomplete_value": false,
      "site": "0062f818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
        "00bf6540",
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
        "00bf6590",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f814 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0062f814 ["COPY", "tmp:0:8", ["const:590:8"]]
~~~


### [`0062f8d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f8d8.md) → [`0062f8d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f8d8.md) FUN_0062f8d8

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
      "definition_site": "0062f8dc",
      "incomplete_value": true,
      "site": "0062f8e0",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f8dc",
      "incomplete_value": true,
      "site": "0062f8e0",
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
        "00bf65c0",
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
        "00bf6610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f8dc ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 0062f8dc ["COPY", "tmp:0:8", ["const:610:8"]]
~~~


### [`0062f97c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f97c.md) → [`0062f97c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f97c.md) FUN_0062f97c

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
      "definition_site": "0062f9a0",
      "incomplete_value": false,
      "site": "0062f9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f9a0",
      "incomplete_value": false,
      "site": "0062f9a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
        "00bf6640",
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
        "00bf6690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f99c ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0062f99c ["COPY", "tmp:0:8", ["const:690:8"]]
~~~


### [`0062f9b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062f9b0.md) → [`0062f9b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062f9b0.md) FUN_0062f9b0

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
      "definition_site": "0062f9bc",
      "incomplete_value": false,
      "site": "0062f9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062f9bc",
      "incomplete_value": false,
      "site": "0062f9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
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
      12,
      "DATA",
      [
        "storage",
        "00bf6640",
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
        "00bf6690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062f9b8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 0062f9b8 ["COPY", "tmp:0:8", ["const:690:8"]]
~~~


### [`0062fd20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062fd20.md) → [`0062fd20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fd20.md) FUN_0062fd20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0062fd34",
      "incomplete_value": true,
      "site": "0062fd38",
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
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062fd34",
      "incomplete_value": true,
      "site": "0062fd38",
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
            "const:6d0:8"
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
        "00bf66d0",
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
        "00bf6720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062fd34 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0062fd34 ["COPY", "tmp:0:8", ["const:720:8"]]
~~~


### [`0062fd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062fd44.md) → [`0062fd44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fd44.md) FUN_0062fd44

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
      "definition_site": "0062fd48",
      "incomplete_value": false,
      "site": "0062fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062fd48",
      "incomplete_value": false,
      "site": "0062fd4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
        "00bf66d0",
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
        "00bf6720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062fd48 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 0062fd48 ["COPY", "tmp:0:8", ["const:720:8"]]
~~~


### [`0062fe7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062fe7c.md) → [`0062fe7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fe7c.md) FUN_0062fe7c

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
      "definition_site": "0062fea0",
      "incomplete_value": false,
      "site": "0062fea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062fea0",
      "incomplete_value": false,
      "site": "0062fea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
        "00bf6750",
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
        "00bf67a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062fe9c ["COPY", "tmp:0:8", ["const:750:8"]]
+ 0062fe9c ["COPY", "tmp:0:8", ["const:7a0:8"]]
~~~


### [`0062feb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062feb0.md) → [`0062feb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062feb0.md) FUN_0062feb0

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
      "definition_site": "0062febc",
      "incomplete_value": false,
      "site": "0062febc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062febc",
      "incomplete_value": false,
      "site": "0062febc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
        "00bf6750",
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
        "00bf67a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0062feb8 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 0062feb8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
~~~


### [`0062fecc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062f/0062fecc.md) → [`0062fecc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062f/0062fecc.md) FUN_0062fecc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) [`006302cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/006302cc.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005be404`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`006302cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/006302cc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00630088",
      "incomplete_value": true,
      "site": "00630088",
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
      "definition_site": "00630088",
      "incomplete_value": true,
      "site": "00630088",
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00630090",
      "incomplete_value": false,
      "site": "006300a0",
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
      "definition_site": "00630090",
      "incomplete_value": false,
      "site": "006300a0",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00630098",
      "incomplete_value": false,
      "site": "006300a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630098",
      "incomplete_value": false,
      "site": "006300a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      440,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      452,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      460,
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      440,
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      452,
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      460,
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00630084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00630084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 00630090 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00630090 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 00630098 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00630098 ["COPY", "tmp:0:8", ["const:2e8:8"]]
~~~


### [`00630298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/00630298.md) → [`00630298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/00630298.md) FUN_00630298

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
      "definition_site": "006302ac",
      "incomplete_value": false,
      "site": "006302b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006302ac",
      "incomplete_value": false,
      "site": "006302b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
        "00bf67c0",
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
        "00bf6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006302ac ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 006302ac ["COPY", "tmp:0:8", ["const:810:8"]]
~~~


### [`006302bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/006302bc.md) → [`006302bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/006302bc.md) FUN_006302bc

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
      "definition_site": "006302c0",
      "incomplete_value": false,
      "site": "006302c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006302c0",
      "incomplete_value": false,
      "site": "006302c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
        "00bf67c0",
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
        "00bf6810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006302c0 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 006302c0 ["COPY", "tmp:0:8", ["const:810:8"]]
~~~


### [`00630340`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/00630340.md) → [`00630340`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/00630340.md) FUN_00630340

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
      "definition_site": "00630364",
      "incomplete_value": false,
      "site": "00630364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630364",
      "incomplete_value": false,
      "site": "00630364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:850:8"
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
        "00bf6850",
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
        "00bf68a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00630360 ["COPY", "tmp:0:8", ["const:850:8"]]
+ 00630360 ["COPY", "tmp:0:8", ["const:8a0:8"]]
~~~


### [`00630a28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/00630a28.md) → [`00630a28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/00630a28.md) FUN_00630a28

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
      "definition_site": "00630a4c",
      "incomplete_value": false,
      "site": "00630a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630a4c",
      "incomplete_value": false,
      "site": "00630a4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
        "00bf68d0",
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
        "00bf6920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00630a48 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 00630a48 ["COPY", "tmp:0:8", ["const:920:8"]]
~~~


### [`00630a5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00630/00630a5c.md) → [`00630a5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00630/00630a5c.md) FUN_00630a5c

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
      "definition_site": "00630a68",
      "incomplete_value": false,
      "site": "00630a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00630a68",
      "incomplete_value": false,
      "site": "00630a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
        "00bf68d0",
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
        "00bf6920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00630a64 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 00630a64 ["COPY", "tmp:0:8", ["const:920:8"]]
~~~


### [`0063136c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/0063136c.md) → [`0063136c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/0063136c.md) FUN_0063136c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00631234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631234.md) [`0063136c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/0063136c.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00631234`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631234.md) [`0063136c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/0063136c.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006314e0",
      "incomplete_value": false,
      "site": "006314e8",
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
      "definition_site": "006314e0",
      "incomplete_value": false,
      "site": "006314e8",
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
      "definition_site": "006315bc",
      "incomplete_value": false,
      "site": "006315c8",
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
      "definition_site": "006315bc",
      "incomplete_value": false,
      "site": "006315c8",
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
      "definition_site": "0063166c",
      "incomplete_value": false,
      "site": "00631678",
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
      "definition_site": "0063166c",
      "incomplete_value": false,
      "site": "00631678",
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
      372,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      564,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      592,
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
      372,
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      564,
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      592,
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
- 006314e0 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 006314e0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
- 006315a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 006315a0 ["COPY", "tmp:0:8", ["const:379:8"]]
- 006315bc ["COPY", "tmp:0:8", ["const:919:8"]]
+ 006315bc ["COPY", "tmp:0:8", ["const:885:8"]]
~~~


### [`00631dc4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631dc4.md) → [`00631dc4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631dc4.md) FUN_00631dc4

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
      "definition_site": "00631de4",
      "incomplete_value": false,
      "site": "00631de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00631de4",
      "incomplete_value": false,
      "site": "00631de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
        "00bf69d0",
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
        "00bf6a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00631de4 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00631de4 ["COPY", "tmp:0:8", ["const:a20:8"]]
~~~


### [`00631dfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631dfc.md) → [`00631dfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631dfc.md) FUN_00631dfc

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
      "definition_site": "00631e00",
      "incomplete_value": false,
      "site": "00631e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00631e00",
      "incomplete_value": false,
      "site": "00631e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
        "00bf69d0",
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
        "00bf6a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00631e00 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00631e00 ["COPY", "tmp:0:8", ["const:a20:8"]]
~~~


### [`00631e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631e1c.md) → [`00631e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631e1c.md) FUN_00631e1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00632018`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632018.md) [`0063201c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/0063201c.md) [`00634d50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00632018`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632018.md) [`0063201c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/0063201c.md) [`00634d50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00631edc",
      "incomplete_value": false,
      "site": "00631edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00631edc",
      "incomplete_value": false,
      "site": "00631edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
      192,
      "DATA",
      [
        "storage",
        "00bf6a40",
        null,
        "undefined *"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "00bf6a60",
        null,
        "pointer"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "00bf6a68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      192,
      "DATA",
      [
        "storage",
        "00bf6a90",
        null,
        "undefined *"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "00bf6ab0",
        null,
        "pointer"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "00bf6ab8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00631ed8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00631ed8 ["COPY", "tmp:0:8", ["const:a90:8"]]
~~~


### [`00631fc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631fc8.md) → [`00631fc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631fc8.md) FUN_00631fc8

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
      "definition_site": "00631fe8",
      "incomplete_value": false,
      "site": "00631fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00631fe8",
      "incomplete_value": false,
      "site": "00631fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
        "00bf6a40",
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
        "00bf6a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00631fe8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00631fe8 ["COPY", "tmp:0:8", ["const:a90:8"]]
~~~


### [`00632000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632000.md) → [`00632000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632000.md) FUN_00632000

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
      "definition_site": "00632004",
      "incomplete_value": false,
      "site": "00632008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00632004",
      "incomplete_value": false,
      "site": "00632008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:a40:8"
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
        "00bf6a40",
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
        "00bf6a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00632004 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00632004 ["COPY", "tmp:0:8", ["const:a90:8"]]
~~~


### [`006320fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006320fc.md) → [`006320fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006320fc.md) FUN_006320fc

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
      "definition_site": "00632100",
      "incomplete_value": true,
      "site": "00632104",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00632100",
      "incomplete_value": true,
      "site": "00632104",
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
            "const:ad0:8"
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
        "00bf6ad0",
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
        "00bf6b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00632100 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00632100 ["COPY", "tmp:0:8", ["const:b20:8"]]
~~~


### [`006321ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006321ac.md) → [`006321ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006321ac.md) FUN_006321ac

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
      "definition_site": "006321c0",
      "incomplete_value": false,
      "site": "006321c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006321c0",
      "incomplete_value": false,
      "site": "006321c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
        "00bf6b50",
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
        "00bf6ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006321c0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 006321c0 ["COPY", "tmp:0:8", ["const:ba0:8"]]
~~~


### [`006322d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006322d4.md) → [`006322d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006322d4.md) FUN_006322d4

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
      "definition_site": "006322e8",
      "incomplete_value": false,
      "site": "006322ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006322e8",
      "incomplete_value": false,
      "site": "006322ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
        "00bf6bd0",
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
        "00bf6c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006322e8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 006322e8 ["COPY", "tmp:0:8", ["const:c20:8"]]
~~~


### [`006322f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006322f8.md) → [`006322f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006322f8.md) FUN_006322f8

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
      "definition_site": "006322fc",
      "incomplete_value": false,
      "site": "00632300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006322fc",
      "incomplete_value": false,
      "site": "00632300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
        "00bf6bd0",
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
        "00bf6c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006322fc ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 006322fc ["COPY", "tmp:0:8", ["const:c20:8"]]
~~~


### [`006323a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/006323a0.md) → [`006323a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/006323a0.md) FUN_006323a0

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
      "definition_site": "006323b4",
      "incomplete_value": false,
      "site": "006323b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006323b4",
      "incomplete_value": false,
      "site": "006323b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
        "00bf6c50",
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
        "00bf6ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 006323b4 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 006323b4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
~~~


