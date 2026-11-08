# v15.7.3 → v15.7.4 · 最優先の変更候補 (65)

[一覧の目次](README.md)

### [`00ae6f68`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md) → [`00ae6fac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00ae6ff0",
      "incomplete_value": true,
      "site": "00ae6ff0",
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
            "const:4b0:8"
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
    "old": {
      "definition_site": "00ae6f9c",
      "incomplete_value": true,
      "site": "00ae6fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
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
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a04b0",
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
  ]
}
~~~


~~~diff
- 00ae6f7c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
+ 00ae6fc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
- 00ae6f9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4a8:8"]]
+ 00ae6fe0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4e8:8"]]
- 00ae6fa8 ["INT_ADD", "register:40f0:8", ["const:ae6fa8:8", "const:4:8"]]
+ 00ae6fec ["INT_ADD", "register:40f0:8", ["const:ae6fec:8", "const:4:8"]]
~~~


### [`00ae7004`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md) → [`00ae7048`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7040",
      "incomplete_value": true,
      "site": "00ae7040",
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
            "const:4b0:8"
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
    "old": {
      "definition_site": "00ae7090",
      "incomplete_value": true,
      "site": "00ae7090",
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
            "const:4a8:8"
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
    "old": {
      "definition_site": "00ae701c",
      "incomplete_value": true,
      "site": "00ae701c",
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
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a04b0",
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
  ]
}
~~~


~~~diff
- 00ae7018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00ae705c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00ae7024 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
+ 00ae7068 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
- 00ae703c ["INT_ADD", "register:40f0:8", ["const:ae703c:8", "const:4:8"]]
+ 00ae7080 ["INT_ADD", "register:40f0:8", ["const:ae7080:8", "const:4:8"]]
~~~


### [`00ae70a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md) → [`00ae70e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae70e4",
      "incomplete_value": true,
      "site": "00ae70e4",
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
            "const:4a8:8"
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
    "old": {
      "definition_site": "00ae70c0",
      "incomplete_value": true,
      "site": "00ae70c0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae70c0"
      ],
      [
        "FALL_THROUGH",
        "00ae7104"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7104",
      "incomplete_value": true,
      "site": "00ae7128",
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
      "definition_site": "00ae70c0",
      "incomplete_value": true,
      "site": "00ae70e4",
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
      20,
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04a8",
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
  ]
}
~~~


~~~diff
- 00ae70b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00ae70fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00ae70c8 ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae710c ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae70dc ["INT_ADD", "register:40f0:8", ["const:ae70dc:8", "const:4:8"]]
+ 00ae7120 ["INT_ADD", "register:40f0:8", ["const:ae7120:8", "const:4:8"]]
~~~


### [`00ae7114`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md) → [`00ae7158`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7130",
      "incomplete_value": false,
      "site": "00ae7134",
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
            "const:5d4:8"
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
    "old": {
      "definition_site": "00ae7140",
      "incomplete_value": true,
      "site": "00ae714c",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
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
  ]
}
~~~


~~~diff
- 00ae7130 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae7174 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7134 ["INT_ADD", "register:40f0:8", ["const:ae7134:8", "const:4:8"]]
+ 00ae7178 ["INT_ADD", "register:40f0:8", ["const:ae7178:8", "const:4:8"]]
- 00ae713c ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00ae7180 ["COPY", "tmp:0:8", ["const:4f8:8"]]
~~~


### [`00ae7150`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md) → [`00ae7194`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7190",
      "incomplete_value": true,
      "site": "00ae7190",
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
            "const:4a8:8"
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
    "old": {
      "definition_site": "00ae716c",
      "incomplete_value": true,
      "site": "00ae716c",
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
    "old": {
      "definition_site": "00ae7174",
      "incomplete_value": false,
      "site": "00ae7188",
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
            "const:e51:8"
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
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04a8",
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
  ]
}
~~~


~~~diff
- 00ae7164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00ae71a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00ae7174 ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae71b8 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae7188 ["INT_ADD", "register:40f0:8", ["const:ae7188:8", "const:4:8"]]
+ 00ae71cc ["INT_ADD", "register:40f0:8", ["const:ae71cc:8", "const:4:8"]]
~~~


### [`00ae71c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md) → [`00ae7204`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae71dc",
      "incomplete_value": false,
      "site": "00ae71e0",
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
            "const:67f:8"
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
    "old": {
      "definition_site": "00ae71ec",
      "incomplete_value": true,
      "site": "00ae71f8",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04c0",
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
  ]
}
~~~


~~~diff
- 00ae71dc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae7220 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae71e0 ["INT_ADD", "register:40f0:8", ["const:ae71e0:8", "const:4:8"]]
+ 00ae7224 ["INT_ADD", "register:40f0:8", ["const:ae7224:8", "const:4:8"]]
- 00ae71e8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00ae722c ["COPY", "tmp:0:8", ["const:500:8"]]
~~~


### [`00ae71fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md) → [`00ae7240`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7228",
      "incomplete_value": true,
      "site": "00ae7228",
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae7210",
      "incomplete_value": true,
      "site": "00ae7210",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7210"
      ],
      [
        "FALL_THROUGH",
        "00ae7254"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7254",
      "incomplete_value": true,
      "site": "00ae726c",
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
      "definition_site": "00ae7210",
      "incomplete_value": true,
      "site": "00ae7228",
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
      16,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04c8",
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
        "010a0508",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae720c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae7250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae7220 ["INT_ADD", "register:40f0:8", ["const:ae7220:8", "const:4:8"]]
+ 00ae7264 ["INT_ADD", "register:40f0:8", ["const:ae7264:8", "const:4:8"]]
- 00ae7228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae726c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
~~~


### [`00ae723c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md) → [`00ae7280`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7268",
      "incomplete_value": true,
      "site": "00ae7268",
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae7250",
      "incomplete_value": true,
      "site": "00ae7250",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7250"
      ],
      [
        "FALL_THROUGH",
        "00ae7294"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7294",
      "incomplete_value": true,
      "site": "00ae72ac",
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
      "definition_site": "00ae7250",
      "incomplete_value": true,
      "site": "00ae7268",
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
      16,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a04c8",
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
        "010a0508",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae724c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae7290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae7260 ["INT_ADD", "register:40f0:8", ["const:ae7260:8", "const:4:8"]]
+ 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
- 00ae7268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
~~~


### [`00ae727c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md) → [`00ae72c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae7290",
      "incomplete_value": true,
      "site": "00ae7290",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7290"
      ],
      [
        "FALL_THROUGH",
        "00ae72d4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72f0",
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
      "definition_site": "00ae7290",
      "incomplete_value": true,
      "site": "00ae72ac",
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
      16,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04c8",
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
        "010a0508",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae728c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
+ 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
- 00ae72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
~~~


### [`00ae72c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md) → [`00ae7304`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:4c8:8"
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae72d4"
      ],
      [
        "FALL_THROUGH",
        "00ae7318"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7318",
      "incomplete_value": true,
      "site": "00ae7334",
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
      "site": "00ae72f0",
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
      16,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a04c8",
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
        "010a0508",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae7314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
+ 00ae732c ["INT_ADD", "register:40f0:8", ["const:ae732c:8", "const:4:8"]]
- 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae7334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
~~~


### [`00ae7310`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md) → [`00ae7354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00ae7398",
      "incomplete_value": true,
      "site": "00ae7398",
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
            "const:4d0:8"
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
    "old": {
      "definition_site": "00ae7344",
      "incomplete_value": true,
      "site": "00ae7350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
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
        "010a04d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a04d0",
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
  ]
}
~~~


~~~diff
- 00ae7324 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d0:8"]]
+ 00ae7368 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00ae7344 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c8:8"]]
+ 00ae7388 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:508:8"]]
- 00ae7350 ["INT_ADD", "register:40f0:8", ["const:ae7350:8", "const:4:8"]]
+ 00ae7394 ["INT_ADD", "register:40f0:8", ["const:ae7394:8", "const:4:8"]]
~~~


### [`00ae73ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md) → [`00ae73f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae73e8",
      "incomplete_value": true,
      "site": "00ae73e8",
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
            "const:4d0:8"
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
    "old": {
      "definition_site": "00ae7438",
      "incomplete_value": true,
      "site": "00ae7438",
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae73c4",
      "incomplete_value": true,
      "site": "00ae73c4",
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
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a04d0",
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
  ]
}
~~~


~~~diff
- 00ae73c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00ae7404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae73cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d0:8"]]
+ 00ae7410 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00ae73e4 ["INT_ADD", "register:40f0:8", ["const:ae73e4:8", "const:4:8"]]
+ 00ae7428 ["INT_ADD", "register:40f0:8", ["const:ae7428:8", "const:4:8"]]
~~~


### [`00ae744c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md) → [`00ae7490`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae748c",
      "incomplete_value": true,
      "site": "00ae748c",
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae7468",
      "incomplete_value": true,
      "site": "00ae7468",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7468"
      ],
      [
        "FALL_THROUGH",
        "00ae74ac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae74ac",
      "incomplete_value": true,
      "site": "00ae74d0",
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
      "definition_site": "00ae7468",
      "incomplete_value": true,
      "site": "00ae748c",
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
      20,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c0fe10",
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
        "010a0508",
        null,
        "undefined8"
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
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c0fe60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7460 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00ae74a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae7484 ["INT_ADD", "register:40f0:8", ["const:ae7484:8", "const:4:8"]]
+ 00ae74c8 ["INT_ADD", "register:40f0:8", ["const:ae74c8:8", "const:4:8"]]
- 00ae748c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00ae74d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
~~~


### [`00ae74bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md) → [`00ae7500`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde680`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde680.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6d0.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae74d8",
      "incomplete_value": false,
      "site": "00ae74dc",
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
            "const:5d4:8"
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
    "old": {
      "definition_site": "00ae74e8",
      "incomplete_value": true,
      "site": "00ae74f4",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a04d8",
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
  ]
}
~~~


~~~diff
- 00ae74d8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae751c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae74dc ["INT_ADD", "register:40f0:8", ["const:ae74dc:8", "const:4:8"]]
+ 00ae7520 ["INT_ADD", "register:40f0:8", ["const:ae7520:8", "const:4:8"]]
- 00ae74e4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00ae7528 ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`00ae74f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md) → [`00ae753c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7538",
      "incomplete_value": true,
      "site": "00ae7538",
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
            "const:4c8:8"
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
    "old": {
      "definition_site": "00ae7514",
      "incomplete_value": true,
      "site": "00ae7514",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7514"
      ],
      [
        "FALL_THROUGH",
        "00ae7558"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7558",
      "incomplete_value": true,
      "site": "00ae757c",
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
      "definition_site": "00ae7514",
      "incomplete_value": true,
      "site": "00ae7538",
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
      20,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0528",
        null,
        null
      ]
    ]
  ],
  "added": [
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
      64,
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0568",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae750c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00ae7550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae7530 ["INT_ADD", "register:40f0:8", ["const:ae7530:8", "const:4:8"]]
+ 00ae7574 ["INT_ADD", "register:40f0:8", ["const:ae7574:8", "const:4:8"]]
- 00ae7538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00ae757c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
~~~


### [`00ae7568`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md) → [`00ae75ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7584",
      "incomplete_value": false,
      "site": "00ae7588",
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
            "const:67f:8"
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
    "old": {
      "definition_site": "00ae7594",
      "incomplete_value": true,
      "site": "00ae75a0",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0528",
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
  ]
}
~~~


~~~diff
- 00ae7584 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae75c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7588 ["INT_ADD", "register:40f0:8", ["const:ae7588:8", "const:4:8"]]
+ 00ae75cc ["INT_ADD", "register:40f0:8", ["const:ae75cc:8", "const:4:8"]]
- 00ae7590 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 00ae75d4 ["COPY", "tmp:0:8", ["const:568:8"]]
~~~


### [`00ae75a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md) → [`00ae75e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae75d0",
      "incomplete_value": true,
      "site": "00ae75d0",
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae75b8",
      "incomplete_value": true,
      "site": "00ae75b8",
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
    "old": {
      "definition_site": "00ae75c4",
      "incomplete_value": false,
      "site": "00ae75c8",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae75b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00ae75f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae75c4 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae7608 ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae75c8 ["INT_ADD", "register:40f0:8", ["const:ae75c8:8", "const:4:8"]]
+ 00ae760c ["INT_ADD", "register:40f0:8", ["const:ae760c:8", "const:4:8"]]
~~~


### [`00ae75e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md) → [`00ae7628`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7610",
      "incomplete_value": true,
      "site": "00ae7610",
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
            "const:530:8"
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
      "definition_site": "00ae763c",
      "incomplete_value": true,
      "site": "00ae763c",
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
      "definition_site": "00ae75f8",
      "incomplete_value": true,
      "site": "00ae75f8",
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
      "definition_site": "00ae7644",
      "incomplete_value": false,
      "site": "00ae764c",
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
    "old": {
      "definition_site": "00ae7600",
      "incomplete_value": false,
      "site": "00ae7608",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae75f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00ae7638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae7600 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae7644 ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae7608 ["INT_ADD", "register:40f0:8", ["const:ae7608:8", "const:4:8"]]
+ 00ae764c ["INT_ADD", "register:40f0:8", ["const:ae764c:8", "const:4:8"]]
~~~


### [`00ae7624`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md) → [`00ae7668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae7638",
      "incomplete_value": true,
      "site": "00ae7638",
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
    "old": {
      "definition_site": "00ae7644",
      "incomplete_value": true,
      "site": "00ae764c",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae7634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00ae7678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae7644 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae7688 ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae764c ["INT_ADD", "register:40f0:8", ["const:ae764c:8", "const:4:8"]]
+ 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
~~~


### [`00ae7668`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md) → [`00ae76ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae7684",
      "incomplete_value": false,
      "site": "00ae7690",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae7678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
+ 00ae76bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae7684 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae76c8 ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
+ 00ae76d4 ["INT_ADD", "register:40f0:8", ["const:ae76d4:8", "const:4:8"]]
~~~


### [`00ae76b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md) → [`00ae76fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00ae7740",
      "incomplete_value": true,
      "site": "00ae7740",
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
            "const:538:8"
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
    "old": {
      "definition_site": "00ae76ec",
      "incomplete_value": true,
      "site": "00ae76f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
        "010a0538",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0538",
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
  ]
}
~~~


~~~diff
- 00ae76cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
+ 00ae7710 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00ae76ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:530:8"]]
+ 00ae7730 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:570:8"]]
- 00ae76f8 ["INT_ADD", "register:40f0:8", ["const:ae76f8:8", "const:4:8"]]
+ 00ae773c ["INT_ADD", "register:40f0:8", ["const:ae773c:8", "const:4:8"]]
~~~


### [`00ae7754`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md) → [`00ae7798`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00ae7790",
      "incomplete_value": true,
      "site": "00ae7790",
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
            "const:538:8"
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
    "old": {
      "definition_site": "00ae77e0",
      "incomplete_value": true,
      "site": "00ae77e0",
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae776c",
      "incomplete_value": true,
      "site": "00ae776c",
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0538",
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
  ]
}
~~~


~~~diff
- 00ae7768 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ae77ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae7774 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
+ 00ae77b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00ae778c ["INT_ADD", "register:40f0:8", ["const:ae778c:8", "const:4:8"]]
+ 00ae77d0 ["INT_ADD", "register:40f0:8", ["const:ae77d0:8", "const:4:8"]]
~~~


### [`00ae77f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md) → [`00ae7838`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7834",
      "incomplete_value": true,
      "site": "00ae7834",
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae7810",
      "incomplete_value": true,
      "site": "00ae7810",
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
    "old": {
      "definition_site": "00ae7818",
      "incomplete_value": false,
      "site": "00ae782c",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae7808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ae784c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae7818 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae785c ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae782c ["INT_ADD", "register:40f0:8", ["const:ae782c:8", "const:4:8"]]
+ 00ae7870 ["INT_ADD", "register:40f0:8", ["const:ae7870:8", "const:4:8"]]
~~~


### [`00ae7864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md) → [`00ae78a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddfe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfe0.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde030.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7880",
      "incomplete_value": false,
      "site": "00ae7884",
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
            "const:5d4:8"
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
    "old": {
      "definition_site": "00ae7890",
      "incomplete_value": true,
      "site": "00ae789c",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0540",
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
  ]
}
~~~


~~~diff
- 00ae7880 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae78c4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7884 ["INT_ADD", "register:40f0:8", ["const:ae7884:8", "const:4:8"]]
+ 00ae78c8 ["INT_ADD", "register:40f0:8", ["const:ae78c8:8", "const:4:8"]]
- 00ae788c ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00ae78d0 ["COPY", "tmp:0:8", ["const:580:8"]]
~~~


### [`00ae78a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md) → [`00ae78e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae78e0",
      "incomplete_value": true,
      "site": "00ae78e0",
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
            "const:530:8"
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
    "old": {
      "definition_site": "00ae78bc",
      "incomplete_value": true,
      "site": "00ae78bc",
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
    "old": {
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78d8",
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
            "const:524:8"
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
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0530",
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
  ]
}
~~~


~~~diff
- 00ae78b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ae78f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae78c4 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00ae7908 ["COPY", "tmp:0:8", ["const:497:8"]]
- 00ae78d8 ["INT_ADD", "register:40f0:8", ["const:ae78d8:8", "const:4:8"]]
+ 00ae791c ["INT_ADD", "register:40f0:8", ["const:ae791c:8", "const:4:8"]]
~~~


### [`00ae7910`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md) → [`00ae7954`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae792c",
      "incomplete_value": false,
      "site": "00ae7930",
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
            "const:67f:8"
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
    "old": {
      "definition_site": "00ae793c",
      "incomplete_value": true,
      "site": "00ae7948",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0558",
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
  ]
}
~~~


~~~diff
- 00ae792c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae7970 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7930 ["INT_ADD", "register:40f0:8", ["const:ae7930:8", "const:4:8"]]
+ 00ae7974 ["INT_ADD", "register:40f0:8", ["const:ae7974:8", "const:4:8"]]
- 00ae7938 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00ae797c ["COPY", "tmp:0:8", ["const:598:8"]]
~~~


### [`00ae794c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md) → [`00ae7990`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7978",
      "incomplete_value": true,
      "site": "00ae7978",
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae7960",
      "incomplete_value": true,
      "site": "00ae7960",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7960"
      ],
      [
        "FALL_THROUGH",
        "00ae79a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae79a4",
      "incomplete_value": true,
      "site": "00ae79bc",
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
      "definition_site": "00ae7960",
      "incomplete_value": true,
      "site": "00ae7978",
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
      16,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0560",
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
        "010a05a0",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae795c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae79a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae7970 ["INT_ADD", "register:40f0:8", ["const:ae7970:8", "const:4:8"]]
+ 00ae79b4 ["INT_ADD", "register:40f0:8", ["const:ae79b4:8", "const:4:8"]]
- 00ae7978 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae79bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
~~~


### [`00ae798c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md) → [`00ae79d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae79b8",
      "incomplete_value": true,
      "site": "00ae79b8",
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae79a0",
      "incomplete_value": true,
      "site": "00ae79a0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae79a0"
      ],
      [
        "FALL_THROUGH",
        "00ae79e4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae79e4",
      "incomplete_value": true,
      "site": "00ae79fc",
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
      "definition_site": "00ae79a0",
      "incomplete_value": true,
      "site": "00ae79b8",
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
      16,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0560",
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
        "010a05a0",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae799c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae79e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae79b0 ["INT_ADD", "register:40f0:8", ["const:ae79b0:8", "const:4:8"]]
+ 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
- 00ae79b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
~~~


### [`00ae79cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md) → [`00ae7a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae79e0",
      "incomplete_value": true,
      "site": "00ae79e0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae79e0"
      ],
      [
        "FALL_THROUGH",
        "00ae7a24"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7a24",
      "incomplete_value": true,
      "site": "00ae7a40",
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
      "definition_site": "00ae79e0",
      "incomplete_value": true,
      "site": "00ae79fc",
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
      16,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0560",
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
        "010a05a0",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae79dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae7a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
+ 00ae7a38 ["INT_ADD", "register:40f0:8", ["const:ae7a38:8", "const:4:8"]]
- 00ae79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae7a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
~~~


### [`00ae7a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md) → [`00ae7a54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:560:8"
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
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0560",
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
        "010a05a0",
        null,
        "undefined8"
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
  ]
}
~~~


~~~diff
- 00ae7a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae7a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae7a38 ["INT_ADD", "register:40f0:8", ["const:ae7a38:8", "const:4:8"]]
+ 00ae7a7c ["INT_ADD", "register:40f0:8", ["const:ae7a7c:8", "const:4:8"]]
- 00ae7a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae7a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
~~~


### [`00ae7a60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md) → [`00ae7aa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
    "old": {
      "definition_site": "00ae7ae8",
      "incomplete_value": true,
      "site": "00ae7ae8",
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
            "const:568:8"
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
    "old": {
      "definition_site": "00ae7a94",
      "incomplete_value": true,
      "site": "00ae7aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:560:8"
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
        "010a0568",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0568",
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
  ]
}
~~~


~~~diff
- 00ae7a74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
+ 00ae7ab8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
- 00ae7a94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:560:8"]]
+ 00ae7ad8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5a0:8"]]
- 00ae7aa0 ["INT_ADD", "register:40f0:8", ["const:ae7aa0:8", "const:4:8"]]
+ 00ae7ae4 ["INT_ADD", "register:40f0:8", ["const:ae7ae4:8", "const:4:8"]]
~~~


### [`00ae7afc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md) → [`00ae7b40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00ae7b38",
      "incomplete_value": true,
      "site": "00ae7b38",
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
            "const:568:8"
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
    "old": {
      "definition_site": "00ae7b88",
      "incomplete_value": true,
      "site": "00ae7b88",
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae7b14",
      "incomplete_value": true,
      "site": "00ae7b14",
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
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0568",
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
  ]
}
~~~


~~~diff
- 00ae7b10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00ae7b1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
+ 00ae7b60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
- 00ae7b34 ["INT_ADD", "register:40f0:8", ["const:ae7b34:8", "const:4:8"]]
+ 00ae7b78 ["INT_ADD", "register:40f0:8", ["const:ae7b78:8", "const:4:8"]]
~~~


### [`00ae7b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md) → [`00ae7be0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7bdc",
      "incomplete_value": true,
      "site": "00ae7bdc",
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae7bb8",
      "incomplete_value": true,
      "site": "00ae7bb8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7bb8"
      ],
      [
        "FALL_THROUGH",
        "00ae7bfc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7bfc",
      "incomplete_value": true,
      "site": "00ae7c20",
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
      "definition_site": "00ae7bb8",
      "incomplete_value": true,
      "site": "00ae7bdc",
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
      20,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c0ff48",
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
        "010a05a0",
        null,
        "undefined8"
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
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c0ff98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7bb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7bf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00ae7bd4 ["INT_ADD", "register:40f0:8", ["const:ae7bd4:8", "const:4:8"]]
+ 00ae7c18 ["INT_ADD", "register:40f0:8", ["const:ae7c18:8", "const:4:8"]]
- 00ae7bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
~~~


### [`00ae7c0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md) → [`00ae7c50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7c28",
      "incomplete_value": false,
      "site": "00ae7c2c",
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
            "const:5d4:8"
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
    "old": {
      "definition_site": "00ae7c38",
      "incomplete_value": true,
      "site": "00ae7c44",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0570",
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
  ]
}
~~~


~~~diff
- 00ae7c28 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae7c6c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7c2c ["INT_ADD", "register:40f0:8", ["const:ae7c2c:8", "const:4:8"]]
+ 00ae7c70 ["INT_ADD", "register:40f0:8", ["const:ae7c70:8", "const:4:8"]]
- 00ae7c34 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 00ae7c78 ["COPY", "tmp:0:8", ["const:5b0:8"]]
~~~


### [`00ae7c48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md) → [`00ae7c8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7c88",
      "incomplete_value": true,
      "site": "00ae7c88",
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
            "const:560:8"
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
    "old": {
      "definition_site": "00ae7c64",
      "incomplete_value": true,
      "site": "00ae7c64",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7c64"
      ],
      [
        "FALL_THROUGH",
        "00ae7ca8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7ca8",
      "incomplete_value": true,
      "site": "00ae7ccc",
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
      "definition_site": "00ae7c64",
      "incomplete_value": true,
      "site": "00ae7c88",
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
      20,
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0578",
        null,
        null
      ]
    ]
  ],
  "added": [
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
      64,
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae7c5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7ca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00ae7c80 ["INT_ADD", "register:40f0:8", ["const:ae7c80:8", "const:4:8"]]
+ 00ae7cc4 ["INT_ADD", "register:40f0:8", ["const:ae7cc4:8", "const:4:8"]]
- 00ae7c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
~~~


### [`00ae7cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md) → [`00ae7cfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7cd4",
      "incomplete_value": false,
      "site": "00ae7cd8",
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
            "const:67f:8"
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
    "old": {
      "definition_site": "00ae7ce4",
      "incomplete_value": true,
      "site": "00ae7cf0",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0578",
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
  ]
}
~~~


~~~diff
- 00ae7cd4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae7d18 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7cd8 ["INT_ADD", "register:40f0:8", ["const:ae7cd8:8", "const:4:8"]]
+ 00ae7d1c ["INT_ADD", "register:40f0:8", ["const:ae7d1c:8", "const:4:8"]]
- 00ae7ce0 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00ae7d24 ["COPY", "tmp:0:8", ["const:5b8:8"]]
~~~


### [`00ae7cf4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md) → [`00ae7d38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7d20",
      "incomplete_value": true,
      "site": "00ae7d20",
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7d08",
      "incomplete_value": true,
      "site": "00ae7d08",
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
    "old": {
      "definition_site": "00ae7d14",
      "incomplete_value": false,
      "site": "00ae7d18",
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
            "const:669:8"
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae7d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae7d14 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae7d58 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae7d18 ["INT_ADD", "register:40f0:8", ["const:ae7d18:8", "const:4:8"]]
+ 00ae7d5c ["INT_ADD", "register:40f0:8", ["const:ae7d5c:8", "const:4:8"]]
~~~


### [`00ae7d34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md) → [`00ae7d78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7d60",
      "incomplete_value": true,
      "site": "00ae7d60",
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7d48",
      "incomplete_value": true,
      "site": "00ae7d48",
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
    "old": {
      "definition_site": "00ae7d50",
      "incomplete_value": true,
      "site": "00ae7d58",
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
            "const:669:8"
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae7d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7d88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae7d50 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae7d94 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae7d58 ["INT_ADD", "register:40f0:8", ["const:ae7d58:8", "const:4:8"]]
+ 00ae7d9c ["INT_ADD", "register:40f0:8", ["const:ae7d9c:8", "const:4:8"]]
~~~


### [`00ae7d74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md) → [`00ae7db8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7d88",
      "incomplete_value": true,
      "site": "00ae7d88",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae7d88"
      ],
      [
        "FALL_THROUGH",
        "00ae7dcc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7de8",
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
      "definition_site": "00ae7d88",
      "incomplete_value": true,
      "site": "00ae7da4",
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
      16,
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae7d84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae7d94 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae7dd8 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae7d9c ["INT_ADD", "register:40f0:8", ["const:ae7d9c:8", "const:4:8"]]
+ 00ae7de0 ["INT_ADD", "register:40f0:8", ["const:ae7de0:8", "const:4:8"]]
~~~


### [`00ae7db8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md) → [`00ae7dfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7dd4",
      "incomplete_value": false,
      "site": "00ae7de0",
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
            "const:669:8"
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae7dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae7dd4 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae7e18 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae7de0 ["INT_ADD", "register:40f0:8", ["const:ae7de0:8", "const:4:8"]]
+ 00ae7e24 ["INT_ADD", "register:40f0:8", ["const:ae7e24:8", "const:4:8"]]
~~~


### [`00ae7e08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md) → [`00ae7e4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00ae7e90",
      "incomplete_value": true,
      "site": "00ae7e90",
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
            "const:588:8"
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
        "010a0588",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0588",
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
  ]
}
~~~


~~~diff
- 00ae7e1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
+ 00ae7e60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
- 00ae7e3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:580:8"]]
+ 00ae7e80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c0:8"]]
- 00ae7e48 ["INT_ADD", "register:40f0:8", ["const:ae7e48:8", "const:4:8"]]
+ 00ae7e8c ["INT_ADD", "register:40f0:8", ["const:ae7e8c:8", "const:4:8"]]
~~~


### [`00ae7ea4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md) → [`00ae7ee8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

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
    "old": {
      "definition_site": "00ae7ee0",
      "incomplete_value": true,
      "site": "00ae7ee0",
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
            "const:588:8"
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
    "old": {
      "definition_site": "00ae7f30",
      "incomplete_value": true,
      "site": "00ae7f30",
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7ebc",
      "incomplete_value": true,
      "site": "00ae7ebc",
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0588",
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
  ]
}
~~~


~~~diff
- 00ae7eb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00ae7efc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae7ec4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
+ 00ae7f08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
- 00ae7edc ["INT_ADD", "register:40f0:8", ["const:ae7edc:8", "const:4:8"]]
+ 00ae7f20 ["INT_ADD", "register:40f0:8", ["const:ae7f20:8", "const:4:8"]]
~~~


### [`00ae7f44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md) → [`00ae7f88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae7f84",
      "incomplete_value": true,
      "site": "00ae7f84",
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae7f60",
      "incomplete_value": true,
      "site": "00ae7f60",
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
    "old": {
      "definition_site": "00ae7f68",
      "incomplete_value": false,
      "site": "00ae7f7c",
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
            "const:669:8"
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae7f58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00ae7f9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae7f68 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae7fac ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae7f7c ["INT_ADD", "register:40f0:8", ["const:ae7f7c:8", "const:4:8"]]
+ 00ae7fc0 ["INT_ADD", "register:40f0:8", ["const:ae7fc0:8", "const:4:8"]]
~~~


### [`00ae7fb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md) → [`00ae7ff8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde440`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde440.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae7fd0",
      "incomplete_value": false,
      "site": "00ae7fd4",
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
            "const:5d4:8"
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
    "old": {
      "definition_site": "00ae7fe0",
      "incomplete_value": true,
      "site": "00ae7fec",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0590",
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
  ]
}
~~~


~~~diff
- 00ae7fd0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae8014 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7fd4 ["INT_ADD", "register:40f0:8", ["const:ae7fd4:8", "const:4:8"]]
+ 00ae8018 ["INT_ADD", "register:40f0:8", ["const:ae8018:8", "const:4:8"]]
- 00ae7fdc ["COPY", "tmp:0:8", ["const:590:8"]]
+ 00ae8020 ["COPY", "tmp:0:8", ["const:5d0:8"]]
~~~


### [`00ae7ff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md) → [`00ae8034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae8030",
      "incomplete_value": true,
      "site": "00ae8030",
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
            "const:580:8"
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
    "old": {
      "definition_site": "00ae800c",
      "incomplete_value": true,
      "site": "00ae800c",
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
    "old": {
      "definition_site": "00ae8014",
      "incomplete_value": false,
      "site": "00ae8028",
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
            "const:669:8"
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
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
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
  ]
}
~~~


~~~diff
- 00ae8004 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00ae8048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae8014 ["COPY", "tmp:0:8", ["const:669:8"]]
+ 00ae8058 ["COPY", "tmp:0:8", ["const:5dc:8"]]
- 00ae8028 ["INT_ADD", "register:40f0:8", ["const:ae8028:8", "const:4:8"]]
+ 00ae806c ["INT_ADD", "register:40f0:8", ["const:ae806c:8", "const:4:8"]]
~~~


### [`00ae8060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md) → [`00ae80a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae807c",
      "incomplete_value": false,
      "site": "00ae8080",
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
            "const:67f:8"
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
    "old": {
      "definition_site": "00ae808c",
      "incomplete_value": true,
      "site": "00ae8098",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a05a0",
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
  ]
}
~~~


~~~diff
- 00ae807c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae80c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae8080 ["INT_ADD", "register:40f0:8", ["const:ae8080:8", "const:4:8"]]
+ 00ae80c4 ["INT_ADD", "register:40f0:8", ["const:ae80c4:8", "const:4:8"]]
- 00ae8088 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00ae80cc ["COPY", "tmp:0:8", ["const:5e0:8"]]
~~~


### [`00ae809c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md) → [`00ae80e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae80c8",
      "incomplete_value": true,
      "site": "00ae80c8",
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
            "const:5a8:8"
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
    "old": {
      "definition_site": "00ae80bc",
      "incomplete_value": false,
      "site": "00ae80c0",
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
            "const:bf8:8"
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
  ]
}
~~~


~~~diff
- 00ae80ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00ae80f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae80bc ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae8100 ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae80c0 ["INT_ADD", "register:40f0:8", ["const:ae80c0:8", "const:4:8"]]
+ 00ae8104 ["INT_ADD", "register:40f0:8", ["const:ae8104:8", "const:4:8"]]
~~~


### [`00ae80dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md) → [`00ae8120`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00ae8108",
      "incomplete_value": true,
      "site": "00ae8108",
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
            "const:5a8:8"
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
    "old": {
      "definition_site": "00ae80f0",
      "incomplete_value": true,
      "site": "00ae80f0",
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
    "old": {
      "definition_site": "00ae80f8",
      "incomplete_value": false,
      "site": "00ae8100",
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
            "const:bf8:8"
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
  ]
}
~~~


~~~diff
- 00ae80ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00ae8130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae80f8 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae813c ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae8100 ["INT_ADD", "register:40f0:8", ["const:ae8100:8", "const:4:8"]]
+ 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
~~~


### [`00ae811c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md) → [`00ae8160`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8190",
      "incomplete_value": true,
      "site": "00ae8190",
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
            "const:5a8:8"
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
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8174",
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
      "definition_site": "00ae8130",
      "incomplete_value": true,
      "site": "00ae8130",
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
      "definition_site": "00ae8180",
      "incomplete_value": false,
      "site": "00ae8188",
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
            "const:bf8:8"
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
      48,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae812c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00ae8170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae813c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae8180 ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
+ 00ae8188 ["INT_ADD", "register:40f0:8", ["const:ae8188:8", "const:4:8"]]
~~~


### [`00ae8160`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md) → [`00ae81a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae81d4",
      "incomplete_value": true,
      "site": "00ae81d4",
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
    "old": {
      "definition_site": "00ae8190",
      "incomplete_value": true,
      "site": "00ae8190",
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
            "const:5a8:8"
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
      "definition_site": "00ae81b8",
      "incomplete_value": true,
      "site": "00ae81b8",
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
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8174",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8174"
      ],
      [
        "FALL_THROUGH",
        "00ae81b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae81b8",
      "incomplete_value": true,
      "site": "00ae81d4",
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
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8190",
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
      16,
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
      48,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00ae81b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae817c ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae81c0 ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae8188 ["INT_ADD", "register:40f0:8", ["const:ae8188:8", "const:4:8"]]
+ 00ae81cc ["INT_ADD", "register:40f0:8", ["const:ae81cc:8", "const:4:8"]]
~~~


### [`00ae81b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md) → [`00ae81f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae827c",
      "incomplete_value": true,
      "site": "00ae827c",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8238",
      "incomplete_value": true,
      "site": "00ae8238",
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
            "const:5b0:8"
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
      "definition_site": "00ae8228",
      "incomplete_value": true,
      "site": "00ae8234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae81e4",
      "incomplete_value": true,
      "site": "00ae81f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a8:8"
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
        "010a05b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a05b0",
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
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae81c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
+ 00ae8208 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae81e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5a8:8"]]
+ 00ae8228 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e8:8"]]
- 00ae81f0 ["INT_ADD", "register:40f0:8", ["const:ae81f0:8", "const:4:8"]]
+ 00ae8234 ["INT_ADD", "register:40f0:8", ["const:ae8234:8", "const:4:8"]]
~~~


### [`00ae824c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md) → [`00ae8290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae82cc",
      "incomplete_value": true,
      "site": "00ae82cc",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8288",
      "incomplete_value": true,
      "site": "00ae8288",
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
            "const:5b0:8"
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
      "definition_site": "00ae831c",
      "incomplete_value": true,
      "site": "00ae831c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae82d8",
      "incomplete_value": true,
      "site": "00ae82d8",
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
            "const:5a8:8"
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
      "definition_site": "00ae82a8",
      "incomplete_value": true,
      "site": "00ae82a8",
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
      "definition_site": "00ae8264",
      "incomplete_value": true,
      "site": "00ae8264",
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a05b0",
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
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8260 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00ae82a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae826c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
+ 00ae82b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae8284 ["INT_ADD", "register:40f0:8", ["const:ae8284:8", "const:4:8"]]
+ 00ae82c8 ["INT_ADD", "register:40f0:8", ["const:ae82c8:8", "const:4:8"]]
~~~


### [`00ae82ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md) → [`00ae8330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8370",
      "incomplete_value": true,
      "site": "00ae8370",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae832c",
      "incomplete_value": true,
      "site": "00ae832c",
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
            "const:5a8:8"
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
      "definition_site": "00ae834c",
      "incomplete_value": true,
      "site": "00ae834c",
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
      "definition_site": "00ae8308",
      "incomplete_value": true,
      "site": "00ae8308",
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
      "definition_site": "00ae8354",
      "incomplete_value": false,
      "site": "00ae8368",
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
    "old": {
      "definition_site": "00ae8310",
      "incomplete_value": false,
      "site": "00ae8324",
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
            "const:bf8:8"
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00ae8344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae8310 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae8354 ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae8324 ["INT_ADD", "register:40f0:8", ["const:ae8324:8", "const:4:8"]]
+ 00ae8368 ["INT_ADD", "register:40f0:8", ["const:ae8368:8", "const:4:8"]]
~~~


### [`00ae835c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md) → [`00ae83a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde110`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae83bc",
      "incomplete_value": false,
      "site": "00ae83c0",
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
    "old": {
      "definition_site": "00ae8378",
      "incomplete_value": false,
      "site": "00ae837c",
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
            "const:5d4:8"
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
        "002985d4",
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
        "010a05f8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8378 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae83bc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae837c ["INT_ADD", "register:40f0:8", ["const:ae837c:8", "const:4:8"]]
+ 00ae83c0 ["INT_ADD", "register:40f0:8", ["const:ae83c0:8", "const:4:8"]]
- 00ae8384 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00ae83c8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
~~~


### [`00ae8398`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md) → [`00ae83dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae841c",
      "incomplete_value": true,
      "site": "00ae841c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae83d8",
      "incomplete_value": true,
      "site": "00ae83d8",
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
            "const:5a8:8"
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
      "definition_site": "00ae83f8",
      "incomplete_value": true,
      "site": "00ae83f8",
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
      "definition_site": "00ae83b4",
      "incomplete_value": true,
      "site": "00ae83b4",
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
      "definition_site": "00ae8400",
      "incomplete_value": false,
      "site": "00ae8414",
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
    "old": {
      "definition_site": "00ae83bc",
      "incomplete_value": false,
      "site": "00ae83d0",
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
            "const:bf8:8"
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
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05a8",
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
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae83ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00ae83f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae83bc ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00ae8400 ["COPY", "tmp:0:8", ["const:c92:8"]]
- 00ae83d0 ["INT_ADD", "register:40f0:8", ["const:ae83d0:8", "const:4:8"]]
+ 00ae8414 ["INT_ADD", "register:40f0:8", ["const:ae8414:8", "const:4:8"]]
~~~


### [`00ae8408`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md) → [`00ae844c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8468",
      "incomplete_value": false,
      "site": "00ae846c",
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
    "old": {
      "definition_site": "00ae8424",
      "incomplete_value": false,
      "site": "00ae8428",
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
            "const:67f:8"
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
      "definition_site": "00ae8478",
      "incomplete_value": true,
      "site": "00ae8484",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8434",
      "incomplete_value": true,
      "site": "00ae8440",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0600",
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
        "010a0640",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8424 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae8468 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae8428 ["INT_ADD", "register:40f0:8", ["const:ae8428:8", "const:4:8"]]
+ 00ae846c ["INT_ADD", "register:40f0:8", ["const:ae846c:8", "const:4:8"]]
- 00ae8430 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00ae8474 ["COPY", "tmp:0:8", ["const:640:8"]]
~~~


### [`00ae8444`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md) → [`00ae8488`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae84b4",
      "incomplete_value": true,
      "site": "00ae84b4",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8470",
      "incomplete_value": true,
      "site": "00ae8470",
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
            "const:608:8"
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
      "definition_site": "00ae849c",
      "incomplete_value": true,
      "site": "00ae849c",
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
      "definition_site": "00ae8458",
      "incomplete_value": true,
      "site": "00ae8458",
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
      "definition_site": "00ae84a8",
      "incomplete_value": false,
      "site": "00ae84ac",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8464",
      "incomplete_value": false,
      "site": "00ae8468",
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
            "const:4e6:8"
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
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8454 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00ae8498 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae8464 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae84a8 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae8468 ["INT_ADD", "register:40f0:8", ["const:ae8468:8", "const:4:8"]]
+ 00ae84ac ["INT_ADD", "register:40f0:8", ["const:ae84ac:8", "const:4:8"]]
~~~


### [`00ae8484`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md) → [`00ae84c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae84f4",
      "incomplete_value": true,
      "site": "00ae84f4",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84b0",
      "incomplete_value": true,
      "site": "00ae84b0",
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
            "const:608:8"
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
      "definition_site": "00ae84dc",
      "incomplete_value": true,
      "site": "00ae84dc",
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
      "definition_site": "00ae8498",
      "incomplete_value": true,
      "site": "00ae8498",
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
      "definition_site": "00ae84e4",
      "incomplete_value": false,
      "site": "00ae84ec",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84a0",
      "incomplete_value": false,
      "site": "00ae84a8",
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
            "const:4e6:8"
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
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00ae84d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae84a0 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae84e4 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae84a8 ["INT_ADD", "register:40f0:8", ["const:ae84a8:8", "const:4:8"]]
+ 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
~~~


### [`00ae84c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md) → [`00ae8508`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8538",
      "incomplete_value": true,
      "site": "00ae8538",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84f4",
      "incomplete_value": true,
      "site": "00ae84f4",
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
            "const:608:8"
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
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae851c",
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
      "definition_site": "00ae84d8",
      "incomplete_value": true,
      "site": "00ae84d8",
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
      "definition_site": "00ae8528",
      "incomplete_value": false,
      "site": "00ae8530",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84e4",
      "incomplete_value": false,
      "site": "00ae84ec",
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
            "const:4e6:8"
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
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae84d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00ae8518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae84e4 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae8528 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
+ 00ae8530 ["INT_ADD", "register:40f0:8", ["const:ae8530:8", "const:4:8"]]
~~~


### [`00ae8508`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md) → [`00ae854c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae857c",
      "incomplete_value": true,
      "site": "00ae857c",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8538",
      "incomplete_value": true,
      "site": "00ae8538",
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
            "const:608:8"
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
      "definition_site": "00ae8560",
      "incomplete_value": true,
      "site": "00ae8560",
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
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae851c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae851c"
      ],
      [
        "FALL_THROUGH",
        "00ae8560"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8560",
      "incomplete_value": true,
      "site": "00ae857c",
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
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae8538",
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
      16,
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00ae855c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae8524 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae8568 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae8530 ["INT_ADD", "register:40f0:8", ["const:ae8530:8", "const:4:8"]]
+ 00ae8574 ["INT_ADD", "register:40f0:8", ["const:ae8574:8", "const:4:8"]]
~~~


### [`00ae8558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8558.md) → [`00ae859c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae859c.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae8624",
      "incomplete_value": true,
      "site": "00ae8624",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae85e0",
      "incomplete_value": true,
      "site": "00ae85e0",
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
            "const:610:8"
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
      "definition_site": "00ae85d0",
      "incomplete_value": true,
      "site": "00ae85dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:648:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae858c",
      "incomplete_value": true,
      "site": "00ae8598",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:608:8"
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
        "010a0610",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0610",
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
        "010a0650",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae856c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
+ 00ae85b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
- 00ae858c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:608:8"]]
+ 00ae85d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:648:8"]]
- 00ae8598 ["INT_ADD", "register:40f0:8", ["const:ae8598:8", "const:4:8"]]
+ 00ae85dc ["INT_ADD", "register:40f0:8", ["const:ae85dc:8", "const:4:8"]]
~~~


### [`00ae85f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md) → [`00ae8638`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8674",
      "incomplete_value": true,
      "site": "00ae8674",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8630",
      "incomplete_value": true,
      "site": "00ae8630",
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
            "const:610:8"
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
      "definition_site": "00ae86c4",
      "incomplete_value": true,
      "site": "00ae86c4",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8680",
      "incomplete_value": true,
      "site": "00ae8680",
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
            "const:608:8"
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
      "definition_site": "00ae8650",
      "incomplete_value": true,
      "site": "00ae8650",
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
      "definition_site": "00ae860c",
      "incomplete_value": true,
      "site": "00ae860c",
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
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0610",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0610",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8608 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00ae864c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00ae8614 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:610:8"]]
+ 00ae8658 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
- 00ae862c ["INT_ADD", "register:40f0:8", ["const:ae862c:8", "const:4:8"]]
+ 00ae8670 ["INT_ADD", "register:40f0:8", ["const:ae8670:8", "const:4:8"]]
~~~


### [`00ae8694`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md) → [`00ae86d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8718",
      "incomplete_value": true,
      "site": "00ae8718",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae86d4",
      "incomplete_value": true,
      "site": "00ae86d4",
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
            "const:608:8"
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
      "definition_site": "00ae86f4",
      "incomplete_value": true,
      "site": "00ae86f4",
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
      "definition_site": "00ae86b0",
      "incomplete_value": true,
      "site": "00ae86b0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae86b0"
      ],
      [
        "FALL_THROUGH",
        "00ae86f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae86f4",
      "incomplete_value": true,
      "site": "00ae8718",
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
      "definition_site": "00ae86b0",
      "incomplete_value": true,
      "site": "00ae86d4",
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
      20,
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae86a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00ae86ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00ae86b8 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae86fc ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae86cc ["INT_ADD", "register:40f0:8", ["const:ae86cc:8", "const:4:8"]]
+ 00ae8710 ["INT_ADD", "register:40f0:8", ["const:ae8710:8", "const:4:8"]]
~~~


### [`00ae8740`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md) → [`00ae8784`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae87c4",
      "incomplete_value": true,
      "site": "00ae87c4",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8780",
      "incomplete_value": true,
      "site": "00ae8780",
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
            "const:608:8"
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
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0608",
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
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8754 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00ae8798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00ae8764 ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 00ae87a8 ["COPY", "tmp:0:8", ["const:459:8"]]
- 00ae8778 ["INT_ADD", "register:40f0:8", ["const:ae8778:8", "const:4:8"]]
+ 00ae87bc ["INT_ADD", "register:40f0:8", ["const:ae87bc:8", "const:4:8"]]
~~~


### [`00ae87ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae87ec.md) → [`00ae8830`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8830.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae885c",
      "incomplete_value": true,
      "site": "00ae885c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8818",
      "incomplete_value": true,
      "site": "00ae8818",
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
            "const:630:8"
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
      "definition_site": "00ae8844",
      "incomplete_value": true,
      "site": "00ae8844",
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
      "definition_site": "00ae8800",
      "incomplete_value": true,
      "site": "00ae8800",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8800"
      ],
      [
        "FALL_THROUGH",
        "00ae8844"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8844",
      "incomplete_value": true,
      "site": "00ae885c",
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
      "definition_site": "00ae8800",
      "incomplete_value": true,
      "site": "00ae8818",
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
      16,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0630",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae87fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae8840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
- 00ae8810 ["INT_ADD", "register:40f0:8", ["const:ae8810:8", "const:4:8"]]
+ 00ae8854 ["INT_ADD", "register:40f0:8", ["const:ae8854:8", "const:4:8"]]
- 00ae8818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae885c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
~~~


### [`00ae882c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae882c.md) → [`00ae8870`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae889c",
      "incomplete_value": true,
      "site": "00ae889c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8858",
      "incomplete_value": true,
      "site": "00ae8858",
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
            "const:630:8"
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
      "definition_site": "00ae8884",
      "incomplete_value": true,
      "site": "00ae8884",
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
      "definition_site": "00ae8840",
      "incomplete_value": true,
      "site": "00ae8840",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8840"
      ],
      [
        "FALL_THROUGH",
        "00ae8884"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8884",
      "incomplete_value": true,
      "site": "00ae889c",
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
      "definition_site": "00ae8840",
      "incomplete_value": true,
      "site": "00ae8858",
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
      16,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0630",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae883c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae8880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
- 00ae8850 ["INT_ADD", "register:40f0:8", ["const:ae8850:8", "const:4:8"]]
+ 00ae8894 ["INT_ADD", "register:40f0:8", ["const:ae8894:8", "const:4:8"]]
- 00ae8858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae889c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
~~~


### [`00ae886c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae886c.md) → [`00ae88b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88b0.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae88e0",
      "incomplete_value": true,
      "site": "00ae88e0",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae889c",
      "incomplete_value": true,
      "site": "00ae889c",
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
            "const:630:8"
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
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0630",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae887c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae88c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
- 00ae8894 ["INT_ADD", "register:40f0:8", ["const:ae8894:8", "const:4:8"]]
+ 00ae88d8 ["INT_ADD", "register:40f0:8", ["const:ae88d8:8", "const:4:8"]]
- 00ae889c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae88e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
~~~


### [`00ae88b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md) → [`00ae88f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8924",
      "incomplete_value": true,
      "site": "00ae8924",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae88e0",
      "incomplete_value": true,
      "site": "00ae88e0",
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
            "const:630:8"
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
      "definition_site": "00ae8908",
      "incomplete_value": true,
      "site": "00ae8908",
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
      "definition_site": "00ae88c4",
      "incomplete_value": true,
      "site": "00ae88c4",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae88c4"
      ],
      [
        "FALL_THROUGH",
        "00ae8908"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8908",
      "incomplete_value": true,
      "site": "00ae8924",
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
      "definition_site": "00ae88c4",
      "incomplete_value": true,
      "site": "00ae88e0",
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
      16,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0630",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae88c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae8904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
- 00ae88d8 ["INT_ADD", "register:40f0:8", ["const:ae88d8:8", "const:4:8"]]
+ 00ae891c ["INT_ADD", "register:40f0:8", ["const:ae891c:8", "const:4:8"]]
- 00ae88e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:630:8"]]
+ 00ae8924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
~~~


### [`00ae8900`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8900.md) → [`00ae8944`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8944.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00ae89cc",
      "incomplete_value": true,
      "site": "00ae89cc",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8988",
      "incomplete_value": true,
      "site": "00ae8988",
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
            "const:638:8"
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
        "010a0638",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0638",
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
        "010a0678",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8914 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:638:8"]]
+ 00ae8958 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 00ae8934 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:630:8"]]
+ 00ae8978 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:670:8"]]
- 00ae8940 ["INT_ADD", "register:40f0:8", ["const:ae8940:8", "const:4:8"]]
+ 00ae8984 ["INT_ADD", "register:40f0:8", ["const:ae8984:8", "const:4:8"]]
~~~


### [`00ae899c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae899c.md) → [`00ae89e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae8a1c",
      "incomplete_value": true,
      "site": "00ae8a1c",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae89d8",
      "incomplete_value": true,
      "site": "00ae89d8",
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
            "const:638:8"
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
      "definition_site": "00ae8a6c",
      "incomplete_value": true,
      "site": "00ae8a6c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a28",
      "incomplete_value": true,
      "site": "00ae8a28",
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
            "const:630:8"
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
      "definition_site": "00ae89f8",
      "incomplete_value": true,
      "site": "00ae89f8",
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
      "definition_site": "00ae89b4",
      "incomplete_value": true,
      "site": "00ae89b4",
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
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0638",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0638",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0678",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae89b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
+ 00ae89f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
- 00ae89bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:638:8"]]
+ 00ae8a00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
- 00ae89d4 ["INT_ADD", "register:40f0:8", ["const:ae89d4:8", "const:4:8"]]
+ 00ae8a18 ["INT_ADD", "register:40f0:8", ["const:ae8a18:8", "const:4:8"]]
~~~


### [`00ae8a3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8a3c.md) → [`00ae8a80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8ac0",
      "incomplete_value": true,
      "site": "00ae8ac0",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8a7c",
      "incomplete_value": true,
      "site": "00ae8a7c",
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
            "const:630:8"
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
      "definition_site": "00ae8a9c",
      "incomplete_value": true,
      "site": "00ae8a9c",
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
      "definition_site": "00ae8a58",
      "incomplete_value": true,
      "site": "00ae8a58",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8a58"
      ],
      [
        "FALL_THROUGH",
        "00ae8a9c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8a9c",
      "incomplete_value": true,
      "site": "00ae8ac0",
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
      "definition_site": "00ae8a58",
      "incomplete_value": true,
      "site": "00ae8a7c",
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
      20,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c10098",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00c100e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
+ 00ae8a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
- 00ae8a74 ["INT_ADD", "register:40f0:8", ["const:ae8a74:8", "const:4:8"]]
+ 00ae8ab8 ["INT_ADD", "register:40f0:8", ["const:ae8ab8:8", "const:4:8"]]
- 00ae8a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
+ 00ae8ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
~~~


### [`00ae8aac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8aac.md) → [`00ae8af0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8af0.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8b0c",
      "incomplete_value": false,
      "site": "00ae8b10",
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
    "old": {
      "definition_site": "00ae8ac8",
      "incomplete_value": false,
      "site": "00ae8acc",
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
            "const:5d4:8"
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
      "definition_site": "00ae8b1c",
      "incomplete_value": true,
      "site": "00ae8b28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8ad8",
      "incomplete_value": true,
      "site": "00ae8ae4",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0640",
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
        "010a0680",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ac8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae8b0c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae8acc ["INT_ADD", "register:40f0:8", ["const:ae8acc:8", "const:4:8"]]
+ 00ae8b10 ["INT_ADD", "register:40f0:8", ["const:ae8b10:8", "const:4:8"]]
- 00ae8ad4 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00ae8b18 ["COPY", "tmp:0:8", ["const:680:8"]]
~~~


### [`00ae8ae8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md) → [`00ae8b2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8b6c",
      "incomplete_value": true,
      "site": "00ae8b6c",
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
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8b28",
      "incomplete_value": true,
      "site": "00ae8b28",
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
            "const:630:8"
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
      "definition_site": "00ae8b48",
      "incomplete_value": true,
      "site": "00ae8b48",
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
      "definition_site": "00ae8b04",
      "incomplete_value": true,
      "site": "00ae8b04",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8b04"
      ],
      [
        "FALL_THROUGH",
        "00ae8b48"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8b48",
      "incomplete_value": true,
      "site": "00ae8b6c",
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
      "definition_site": "00ae8b04",
      "incomplete_value": true,
      "site": "00ae8b28",
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
      20,
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0690",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8afc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
+ 00ae8b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
- 00ae8b20 ["INT_ADD", "register:40f0:8", ["const:ae8b20:8", "const:4:8"]]
+ 00ae8b64 ["INT_ADD", "register:40f0:8", ["const:ae8b64:8", "const:4:8"]]
- 00ae8b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:630:8"]]
+ 00ae8b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
~~~


### [`00ae8b58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b58.md) → [`00ae8b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b9c.md) _ZN8firebase4util15character_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8bb8",
      "incomplete_value": false,
      "site": "00ae8bbc",
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
    "old": {
      "definition_site": "00ae8b74",
      "incomplete_value": false,
      "site": "00ae8b78",
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
            "const:67f:8"
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0650",
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
        "010a0690",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8b74 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae8bb8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae8b78 ["INT_ADD", "register:40f0:8", ["const:ae8b78:8", "const:4:8"]]
+ 00ae8bbc ["INT_ADD", "register:40f0:8", ["const:ae8bbc:8", "const:4:8"]]
- 00ae8b80 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00ae8bc4 ["COPY", "tmp:0:8", ["const:690:8"]]
~~~


### [`00ae8b94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md) → [`00ae8bd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8c04",
      "incomplete_value": true,
      "site": "00ae8c04",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bc0",
      "incomplete_value": true,
      "site": "00ae8bc0",
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
            "const:658:8"
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
      "definition_site": "00ae8bec",
      "incomplete_value": true,
      "site": "00ae8bec",
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
      "definition_site": "00ae8ba8",
      "incomplete_value": true,
      "site": "00ae8ba8",
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
      "definition_site": "00ae8bf8",
      "incomplete_value": false,
      "site": "00ae8bfc",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bb4",
      "incomplete_value": false,
      "site": "00ae8bb8",
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
            "const:67b:8"
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
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8be8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8bb4 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8bf8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8bb8 ["INT_ADD", "register:40f0:8", ["const:ae8bb8:8", "const:4:8"]]
+ 00ae8bfc ["INT_ADD", "register:40f0:8", ["const:ae8bfc:8", "const:4:8"]]
~~~


### [`00ae8bd4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md) → [`00ae8c18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c18.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8c44",
      "incomplete_value": true,
      "site": "00ae8c44",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c00",
      "incomplete_value": true,
      "site": "00ae8c00",
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
            "const:658:8"
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
      "definition_site": "00ae8c2c",
      "incomplete_value": true,
      "site": "00ae8c2c",
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
      "definition_site": "00ae8be8",
      "incomplete_value": true,
      "site": "00ae8be8",
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
      "definition_site": "00ae8c34",
      "incomplete_value": true,
      "site": "00ae8c3c",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bf0",
      "incomplete_value": true,
      "site": "00ae8bf8",
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
            "const:67b:8"
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
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8be4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8c28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8bf0 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8c34 ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8bf8 ["INT_ADD", "register:40f0:8", ["const:ae8bf8:8", "const:4:8"]]
+ 00ae8c3c ["INT_ADD", "register:40f0:8", ["const:ae8c3c:8", "const:4:8"]]
~~~


### [`00ae8c14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c14.md) → [`00ae8c58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c58.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8c88",
      "incomplete_value": true,
      "site": "00ae8c88",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c44",
      "incomplete_value": true,
      "site": "00ae8c44",
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
            "const:658:8"
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
      "definition_site": "00ae8c78",
      "incomplete_value": false,
      "site": "00ae8c80",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c34",
      "incomplete_value": false,
      "site": "00ae8c3c",
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
            "const:67b:8"
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
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8c24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8c34 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8c78 ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8c3c ["INT_ADD", "register:40f0:8", ["const:ae8c3c:8", "const:4:8"]]
+ 00ae8c80 ["INT_ADD", "register:40f0:8", ["const:ae8c80:8", "const:4:8"]]
~~~


### [`00ae8c58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md) → [`00ae8c9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8ccc",
      "incomplete_value": true,
      "site": "00ae8ccc",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c88",
      "incomplete_value": true,
      "site": "00ae8c88",
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
            "const:658:8"
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
      "definition_site": "00ae8cb0",
      "incomplete_value": true,
      "site": "00ae8cb0",
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
      "definition_site": "00ae8c6c",
      "incomplete_value": true,
      "site": "00ae8c6c",
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
      "definition_site": "00ae8cb8",
      "incomplete_value": false,
      "site": "00ae8cc4",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8c74",
      "incomplete_value": false,
      "site": "00ae8c80",
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
            "const:67b:8"
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
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8c74 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8cb8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8c80 ["INT_ADD", "register:40f0:8", ["const:ae8c80:8", "const:4:8"]]
+ 00ae8cc4 ["INT_ADD", "register:40f0:8", ["const:ae8cc4:8", "const:4:8"]]
~~~


### [`00ae8c9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c9c.md) → [`00ae8ce0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ce0.md) _ZN8firebase4util11class_class8GetClassEv

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
      "definition_site": "00ae8ce4",
      "incomplete_value": true,
      "site": "00ae8ce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8ca0",
      "incomplete_value": true,
      "site": "00ae8ca4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:658:8"
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
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ca0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:658:8"]]
+ 00ae8ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
~~~


### [`00ae8ca8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md) → [`00ae8cec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8cec.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae8d74",
      "incomplete_value": true,
      "site": "00ae8d74",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8d30",
      "incomplete_value": true,
      "site": "00ae8d30",
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
            "const:660:8"
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
      "definition_site": "00ae8d20",
      "incomplete_value": true,
      "site": "00ae8d2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8cdc",
      "incomplete_value": true,
      "site": "00ae8ce8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:658:8"
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
        "010a0660",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0660",
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
        "010a06a0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8cbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:660:8"]]
+ 00ae8d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
- 00ae8cdc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:658:8"]]
+ 00ae8d20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:698:8"]]
- 00ae8ce8 ["INT_ADD", "register:40f0:8", ["const:ae8ce8:8", "const:4:8"]]
+ 00ae8d2c ["INT_ADD", "register:40f0:8", ["const:ae8d2c:8", "const:4:8"]]
~~~


### [`00ae8d44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8d44.md) → [`00ae8d88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8d88.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8dc4",
      "incomplete_value": true,
      "site": "00ae8dc4",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8d80",
      "incomplete_value": true,
      "site": "00ae8d80",
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
            "const:660:8"
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
      "definition_site": "00ae8e14",
      "incomplete_value": true,
      "site": "00ae8e14",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8dd0",
      "incomplete_value": true,
      "site": "00ae8dd0",
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
            "const:658:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8e04",
      "incomplete_value": true,
      "site": "00ae8e10",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:698:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8dc0",
      "incomplete_value": true,
      "site": "00ae8dcc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:658:8"
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
      20,
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0660",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0660",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a06a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8d58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
+ 00ae8d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00ae8d64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:660:8"]]
+ 00ae8da8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
- 00ae8d7c ["INT_ADD", "register:40f0:8", ["const:ae8d7c:8", "const:4:8"]]
+ 00ae8dc0 ["INT_ADD", "register:40f0:8", ["const:ae8dc0:8", "const:4:8"]]
~~~


### [`00ae8de4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md) → [`00ae8e28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8e68",
      "incomplete_value": true,
      "site": "00ae8e68",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e24",
      "incomplete_value": true,
      "site": "00ae8e24",
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
            "const:658:8"
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
      "definition_site": "00ae8e44",
      "incomplete_value": true,
      "site": "00ae8e44",
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
      "definition_site": "00ae8e00",
      "incomplete_value": true,
      "site": "00ae8e00",
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
      "definition_site": "00ae8e4c",
      "incomplete_value": true,
      "site": "00ae8e60",
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
            "const:5ee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e08",
      "incomplete_value": true,
      "site": "00ae8e1c",
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
            "const:67b:8"
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
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8df8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
+ 00ae8e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00ae8e08 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8e4c ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8e1c ["INT_ADD", "register:40f0:8", ["const:ae8e1c:8", "const:4:8"]]
+ 00ae8e60 ["INT_ADD", "register:40f0:8", ["const:ae8e60:8", "const:4:8"]]
~~~


### [`00ae8e90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md) → [`00ae8ed4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8f14",
      "incomplete_value": true,
      "site": "00ae8f14",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8ed0",
      "incomplete_value": true,
      "site": "00ae8ed0",
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
            "const:658:8"
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
      "definition_site": "00ae8ef0",
      "incomplete_value": true,
      "site": "00ae8ef0",
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
      "definition_site": "00ae8eac",
      "incomplete_value": true,
      "site": "00ae8eac",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ae8eac"
      ],
      [
        "FALL_THROUGH",
        "00ae8ef0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae8ef0",
      "incomplete_value": true,
      "site": "00ae8f14",
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
      "definition_site": "00ae8eac",
      "incomplete_value": true,
      "site": "00ae8ed0",
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
      20,
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0658",
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
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:658:8"]]
+ 00ae8ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00ae8eb4 ["COPY", "tmp:0:8", ["const:67b:8"]]
+ 00ae8ef8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
- 00ae8ec8 ["INT_ADD", "register:40f0:8", ["const:ae8ec8:8", "const:4:8"]]
+ 00ae8f0c ["INT_ADD", "register:40f0:8", ["const:ae8f0c:8", "const:4:8"]]
~~~


### [`00ae8f00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f00.md) → [`00ae8f44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f44.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae8f60",
      "incomplete_value": false,
      "site": "00ae8f64",
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
    "old": {
      "definition_site": "00ae8f1c",
      "incomplete_value": false,
      "site": "00ae8f20",
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
            "const:67f:8"
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
      "definition_site": "00ae8f70",
      "incomplete_value": true,
      "site": "00ae8f7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8f2c",
      "incomplete_value": true,
      "site": "00ae8f38",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0678",
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
        "010a06b8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8f1c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae8f60 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae8f20 ["INT_ADD", "register:40f0:8", ["const:ae8f20:8", "const:4:8"]]
+ 00ae8f64 ["INT_ADD", "register:40f0:8", ["const:ae8f64:8", "const:4:8"]]
- 00ae8f28 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00ae8f6c ["COPY", "tmp:0:8", ["const:6b8:8"]]
~~~


### [`00ae8f3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f3c.md) → [`00ae8f80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8fac",
      "incomplete_value": true,
      "site": "00ae8fac",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f68",
      "incomplete_value": true,
      "site": "00ae8f68",
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
            "const:680:8"
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
      "definition_site": "00ae8f94",
      "incomplete_value": true,
      "site": "00ae8f94",
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
      "definition_site": "00ae8f50",
      "incomplete_value": true,
      "site": "00ae8f50",
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
      "definition_site": "00ae8fa0",
      "incomplete_value": false,
      "site": "00ae8fa4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f5c",
      "incomplete_value": false,
      "site": "00ae8f60",
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
            "const:e51:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8f4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae8f90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae8f5c ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae8fa0 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae8f60 ["INT_ADD", "register:40f0:8", ["const:ae8f60:8", "const:4:8"]]
+ 00ae8fa4 ["INT_ADD", "register:40f0:8", ["const:ae8fa4:8", "const:4:8"]]
~~~


### [`00ae8f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md) → [`00ae8fc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8fec",
      "incomplete_value": true,
      "site": "00ae8fec",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8fa8",
      "incomplete_value": true,
      "site": "00ae8fa8",
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
            "const:680:8"
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
      "definition_site": "00ae8fd4",
      "incomplete_value": true,
      "site": "00ae8fd4",
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
      "definition_site": "00ae8f90",
      "incomplete_value": true,
      "site": "00ae8f90",
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
      "definition_site": "00ae8fdc",
      "incomplete_value": false,
      "site": "00ae8fe4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f98",
      "incomplete_value": false,
      "site": "00ae8fa0",
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
            "const:e51:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae8fd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae8f98 ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae8fdc ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae8fa0 ["INT_ADD", "register:40f0:8", ["const:ae8fa0:8", "const:4:8"]]
+ 00ae8fe4 ["INT_ADD", "register:40f0:8", ["const:ae8fe4:8", "const:4:8"]]
~~~


### [`00ae8fbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8fbc.md) → [`00ae9000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9000.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9030",
      "incomplete_value": true,
      "site": "00ae9030",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8fec",
      "incomplete_value": true,
      "site": "00ae8fec",
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
            "const:680:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae8fdc ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae9020 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae8fe4 ["INT_ADD", "register:40f0:8", ["const:ae8fe4:8", "const:4:8"]]
+ 00ae9028 ["INT_ADD", "register:40f0:8", ["const:ae9028:8", "const:4:8"]]
~~~


### [`00ae9000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md) → [`00ae9044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9074",
      "incomplete_value": true,
      "site": "00ae9074",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9030",
      "incomplete_value": true,
      "site": "00ae9030",
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
            "const:680:8"
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
      "definition_site": "00ae9058",
      "incomplete_value": true,
      "site": "00ae9058",
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
      "definition_site": "00ae9014",
      "incomplete_value": true,
      "site": "00ae9014",
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
      "definition_site": "00ae9060",
      "incomplete_value": false,
      "site": "00ae906c",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae901c",
      "incomplete_value": false,
      "site": "00ae9028",
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
            "const:e51:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae9054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae901c ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae9060 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae9028 ["INT_ADD", "register:40f0:8", ["const:ae9028:8", "const:4:8"]]
+ 00ae906c ["INT_ADD", "register:40f0:8", ["const:ae906c:8", "const:4:8"]]
~~~


### [`00ae9050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9050.md) → [`00ae9094`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae911c",
      "incomplete_value": true,
      "site": "00ae911c",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae90d8",
      "incomplete_value": true,
      "site": "00ae90d8",
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
            "const:688:8"
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
      "definition_site": "00ae90c8",
      "incomplete_value": true,
      "site": "00ae90d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9084",
      "incomplete_value": true,
      "site": "00ae9090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:680:8"
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
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0688",
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
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9064 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
+ 00ae90a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
- 00ae9084 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:680:8"]]
+ 00ae90c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6c0:8"]]
- 00ae9090 ["INT_ADD", "register:40f0:8", ["const:ae9090:8", "const:4:8"]]
+ 00ae90d4 ["INT_ADD", "register:40f0:8", ["const:ae90d4:8", "const:4:8"]]
~~~


### [`00ae90ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md) → [`00ae9130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae916c",
      "incomplete_value": true,
      "site": "00ae916c",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9128",
      "incomplete_value": true,
      "site": "00ae9128",
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
            "const:688:8"
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
      "definition_site": "00ae91bc",
      "incomplete_value": true,
      "site": "00ae91bc",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9178",
      "incomplete_value": true,
      "site": "00ae9178",
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
            "const:680:8"
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
      "definition_site": "00ae9148",
      "incomplete_value": true,
      "site": "00ae9148",
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
      "definition_site": "00ae9104",
      "incomplete_value": true,
      "site": "00ae9104",
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0688",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9100 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00ae9144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00ae910c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
+ 00ae9150 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
- 00ae9124 ["INT_ADD", "register:40f0:8", ["const:ae9124:8", "const:4:8"]]
+ 00ae9168 ["INT_ADD", "register:40f0:8", ["const:ae9168:8", "const:4:8"]]
~~~


### [`00ae918c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md) → [`00ae91d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9210",
      "incomplete_value": true,
      "site": "00ae9210",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae91cc",
      "incomplete_value": true,
      "site": "00ae91cc",
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
            "const:680:8"
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
      "definition_site": "00ae91ec",
      "incomplete_value": true,
      "site": "00ae91ec",
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
      "definition_site": "00ae91a8",
      "incomplete_value": true,
      "site": "00ae91a8",
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
      "definition_site": "00ae91f4",
      "incomplete_value": false,
      "site": "00ae9208",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae91b0",
      "incomplete_value": false,
      "site": "00ae91c4",
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
            "const:e51:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae91a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00ae91e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00ae91b0 ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae91f4 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae91c4 ["INT_ADD", "register:40f0:8", ["const:ae91c4:8", "const:4:8"]]
+ 00ae9208 ["INT_ADD", "register:40f0:8", ["const:ae9208:8", "const:4:8"]]
~~~


### [`00ae91fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md) → [`00ae9240`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae925c",
      "incomplete_value": false,
      "site": "00ae9260",
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
    "old": {
      "definition_site": "00ae9218",
      "incomplete_value": false,
      "site": "00ae921c",
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
            "const:5d4:8"
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
      "definition_site": "00ae926c",
      "incomplete_value": true,
      "site": "00ae9278",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9228",
      "incomplete_value": true,
      "site": "00ae9234",
      "value": [
        "LOAD",
        "8",
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
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a0690",
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
        "010a06d0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9218 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae925c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae921c ["INT_ADD", "register:40f0:8", ["const:ae921c:8", "const:4:8"]]
+ 00ae9260 ["INT_ADD", "register:40f0:8", ["const:ae9260:8", "const:4:8"]]
- 00ae9224 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00ae9268 ["COPY", "tmp:0:8", ["const:6d0:8"]]
~~~


### [`00ae9238`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md) → [`00ae927c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae92bc",
      "incomplete_value": true,
      "site": "00ae92bc",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9278",
      "incomplete_value": true,
      "site": "00ae9278",
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
            "const:680:8"
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
      "definition_site": "00ae9298",
      "incomplete_value": true,
      "site": "00ae9298",
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
      "definition_site": "00ae9254",
      "incomplete_value": true,
      "site": "00ae9254",
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
      "definition_site": "00ae92a0",
      "incomplete_value": false,
      "site": "00ae92b4",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae925c",
      "incomplete_value": false,
      "site": "00ae9270",
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
            "const:e51:8"
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
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0680",
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
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae924c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00ae9290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00ae925c ["COPY", "tmp:0:8", ["const:e51:8"]]
+ 00ae92a0 ["COPY", "tmp:0:8", ["const:edc:8"]]
- 00ae9270 ["INT_ADD", "register:40f0:8", ["const:ae9270:8", "const:4:8"]]
+ 00ae92b4 ["INT_ADD", "register:40f0:8", ["const:ae92b4:8", "const:4:8"]]
~~~


### [`00ae92a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md) → [`00ae92ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae92ec.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9308",
      "incomplete_value": false,
      "site": "00ae930c",
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
    "old": {
      "definition_site": "00ae92c4",
      "incomplete_value": false,
      "site": "00ae92c8",
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
            "const:67f:8"
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
      "definition_site": "00ae9318",
      "incomplete_value": true,
      "site": "00ae9324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae92d4",
      "incomplete_value": true,
      "site": "00ae92e0",
      "value": [
        "LOAD",
        "8",
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
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "010a06a0",
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
        "010a06e0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae92c4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae9308 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae92c8 ["INT_ADD", "register:40f0:8", ["const:ae92c8:8", "const:4:8"]]
+ 00ae930c ["INT_ADD", "register:40f0:8", ["const:ae930c:8", "const:4:8"]]
- 00ae92d0 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00ae9314 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00ae92e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md) → [`00ae9328`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9354",
      "incomplete_value": true,
      "site": "00ae9354",
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
      "definition_site": "00ae9310",
      "incomplete_value": true,
      "site": "00ae9310",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae933c",
      "incomplete_value": true,
      "site": "00ae933c",
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
      "definition_site": "00ae92f8",
      "incomplete_value": true,
      "site": "00ae92f8",
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
      "definition_site": "00ae9348",
      "incomplete_value": false,
      "site": "00ae934c",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9304",
      "incomplete_value": false,
      "site": "00ae9308",
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
            "const:d54:8"
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
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06a8",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae92f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae9338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae9304 ["COPY", "tmp:0:8", ["const:d54:8"]]
+ 00ae9348 ["COPY", "tmp:0:8", ["const:ddf:8"]]
- 00ae9308 ["INT_ADD", "register:40f0:8", ["const:ae9308:8", "const:4:8"]]
+ 00ae934c ["INT_ADD", "register:40f0:8", ["const:ae934c:8", "const:4:8"]]
~~~


### [`00ae9324`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md) → [`00ae9368`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9394",
      "incomplete_value": true,
      "site": "00ae9394",
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
      "definition_site": "00ae9350",
      "incomplete_value": true,
      "site": "00ae9350",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae937c",
      "incomplete_value": true,
      "site": "00ae937c",
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
      "definition_site": "00ae9338",
      "incomplete_value": true,
      "site": "00ae9338",
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
      "definition_site": "00ae9384",
      "incomplete_value": false,
      "site": "00ae938c",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9340",
      "incomplete_value": false,
      "site": "00ae9348",
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
            "const:d54:8"
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
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06a8",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae9378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae9340 ["COPY", "tmp:0:8", ["const:d54:8"]]
+ 00ae9384 ["COPY", "tmp:0:8", ["const:ddf:8"]]
- 00ae9348 ["INT_ADD", "register:40f0:8", ["const:ae9348:8", "const:4:8"]]
+ 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
~~~


### [`00ae9364`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md) → [`00ae93a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae93d8",
      "incomplete_value": true,
      "site": "00ae93d8",
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
      "definition_site": "00ae9394",
      "incomplete_value": true,
      "site": "00ae9394",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae93bc",
      "incomplete_value": true,
      "site": "00ae93bc",
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
      "definition_site": "00ae9378",
      "incomplete_value": true,
      "site": "00ae9378",
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
      "definition_site": "00ae93c8",
      "incomplete_value": false,
      "site": "00ae93d0",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9384",
      "incomplete_value": false,
      "site": "00ae938c",
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
            "const:d54:8"
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
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06a8",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9374 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae9384 ["COPY", "tmp:0:8", ["const:d54:8"]]
+ 00ae93c8 ["COPY", "tmp:0:8", ["const:ddf:8"]]
- 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
+ 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
~~~


### [`00ae93a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md) → [`00ae93ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae941c",
      "incomplete_value": true,
      "site": "00ae941c",
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
      "definition_site": "00ae93d8",
      "incomplete_value": true,
      "site": "00ae93d8",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9400",
      "incomplete_value": true,
      "site": "00ae9400",
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
      "definition_site": "00ae93bc",
      "incomplete_value": true,
      "site": "00ae93bc",
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
      "definition_site": "00ae9408",
      "incomplete_value": false,
      "site": "00ae9414",
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
            "const:ddf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93c4",
      "incomplete_value": false,
      "site": "00ae93d0",
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
            "const:d54:8"
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
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06a8",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae93fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae93c4 ["COPY", "tmp:0:8", ["const:d54:8"]]
+ 00ae9408 ["COPY", "tmp:0:8", ["const:ddf:8"]]
- 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
+ 00ae9414 ["INT_ADD", "register:40f0:8", ["const:ae9414:8", "const:4:8"]]
~~~


### [`00ae93f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md) → [`00ae943c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae94c4",
      "incomplete_value": true,
      "site": "00ae94c4",
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
      "definition_site": "00ae9480",
      "incomplete_value": true,
      "site": "00ae9480",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae9470",
      "incomplete_value": true,
      "site": "00ae947c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae942c",
      "incomplete_value": true,
      "site": "00ae9438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a8:8"
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
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a06b0",
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
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae940c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
+ 00ae9450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
- 00ae942c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6a8:8"]]
+ 00ae9470 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e8:8"]]
- 00ae9438 ["INT_ADD", "register:40f0:8", ["const:ae9438:8", "const:4:8"]]
+ 00ae947c ["INT_ADD", "register:40f0:8", ["const:ae947c:8", "const:4:8"]]
~~~


### [`00ae9494`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md) → [`00ae94d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9514",
      "incomplete_value": true,
      "site": "00ae9514",
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
      "definition_site": "00ae94d0",
      "incomplete_value": true,
      "site": "00ae94d0",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9564",
      "incomplete_value": true,
      "site": "00ae9564",
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
      "definition_site": "00ae9520",
      "incomplete_value": true,
      "site": "00ae9520",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae94f0",
      "incomplete_value": true,
      "site": "00ae94f0",
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
      "definition_site": "00ae94ac",
      "incomplete_value": true,
      "site": "00ae94ac",
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
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a06b0",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae94a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
+ 00ae94ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00ae94b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
+ 00ae94f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
- 00ae94cc ["INT_ADD", "register:40f0:8", ["const:ae94cc:8", "const:4:8"]]
+ 00ae9510 ["INT_ADD", "register:40f0:8", ["const:ae9510:8", "const:4:8"]]
~~~


