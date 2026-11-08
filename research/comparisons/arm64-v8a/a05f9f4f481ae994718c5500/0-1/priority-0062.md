# v15.7.2 → v15.7.3 · 最優先の変更候補 (62)

[一覧の目次](README.md)

### [`00aec0f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec0f8.md) → [`00aec1c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec200",
      "incomplete_value": true,
      "site": "00aec200",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec138",
      "incomplete_value": true,
      "site": "00aec138",
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
      "definition_site": "00aec1dc",
      "incomplete_value": true,
      "site": "00aec1dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec114",
      "incomplete_value": true,
      "site": "00aec114",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec1e8",
      "incomplete_value": true,
      "site": "00aec1f8",
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
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0848",
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
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "010a0908",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec10c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:820:8"]]
+ 00aec1d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec114 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aec1dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec130 ["INT_ADD", "register:40f0:8", ["const:aec130:8", "const:4:8"]]
+ 00aec1f8 ["INT_ADD", "register:40f0:8", ["const:aec1f8:8", "const:4:8"]]
~~~


### [`00aec168`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec168.md) → [`00aec230`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec24c",
      "incomplete_value": false,
      "site": "00aec250",
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
    "old": {
      "definition_site": "00aec184",
      "incomplete_value": false,
      "site": "00aec188",
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
      "definition_site": "00aec25c",
      "incomplete_value": true,
      "site": "00aec268",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec194",
      "incomplete_value": true,
      "site": "00aec1a0",
      "value": [
        "LOAD",
        "8",
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
        "010a0848",
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
        "010a0908",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec184 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec24c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec188 ["INT_ADD", "register:40f0:8", ["const:aec188:8", "const:4:8"]]
+ 00aec250 ["INT_ADD", "register:40f0:8", ["const:aec250:8", "const:4:8"]]
- 00aec190 ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00aec258 ["COPY", "tmp:0:8", ["const:908:8"]]
~~~


### [`00aec1a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1a4.md) → [`00aec26c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec298",
      "incomplete_value": true,
      "site": "00aec298",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec1d0",
      "incomplete_value": true,
      "site": "00aec1d0",
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
      "definition_site": "00aec280",
      "incomplete_value": true,
      "site": "00aec280",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec1b8",
      "incomplete_value": true,
      "site": "00aec1b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec28c",
      "incomplete_value": false,
      "site": "00aec290",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec1c4",
      "incomplete_value": false,
      "site": "00aec1c8",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec1b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aec27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec1c4 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec28c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec1c8 ["INT_ADD", "register:40f0:8", ["const:aec1c8:8", "const:4:8"]]
+ 00aec290 ["INT_ADD", "register:40f0:8", ["const:aec290:8", "const:4:8"]]
~~~


### [`00aec1e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md) → [`00aec2ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec2d8",
      "incomplete_value": true,
      "site": "00aec2d8",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec210",
      "incomplete_value": true,
      "site": "00aec210",
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
      "definition_site": "00aec2c0",
      "incomplete_value": true,
      "site": "00aec2c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec1f8",
      "incomplete_value": true,
      "site": "00aec1f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec2c8",
      "incomplete_value": false,
      "site": "00aec2d0",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec200",
      "incomplete_value": false,
      "site": "00aec208",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aec2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec200 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec2c8 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec208 ["INT_ADD", "register:40f0:8", ["const:aec208:8", "const:4:8"]]
+ 00aec2d0 ["INT_ADD", "register:40f0:8", ["const:aec2d0:8", "const:4:8"]]
~~~


### [`00aec224`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md) → [`00aec2ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec31c",
      "incomplete_value": true,
      "site": "00aec31c",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec254",
      "incomplete_value": true,
      "site": "00aec254",
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
      "definition_site": "00aec300",
      "incomplete_value": true,
      "site": "00aec300",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec238",
      "incomplete_value": true,
      "site": "00aec238",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec30c",
      "incomplete_value": false,
      "site": "00aec314",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec244",
      "incomplete_value": false,
      "site": "00aec24c",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aec2fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec244 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec30c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec24c ["INT_ADD", "register:40f0:8", ["const:aec24c:8", "const:4:8"]]
+ 00aec314 ["INT_ADD", "register:40f0:8", ["const:aec314:8", "const:4:8"]]
~~~


### [`00aec268`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec268.md) → [`00aec330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec360",
      "incomplete_value": true,
      "site": "00aec360",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec298",
      "incomplete_value": true,
      "site": "00aec298",
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
      "definition_site": "00aec344",
      "incomplete_value": true,
      "site": "00aec344",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec27c",
      "incomplete_value": true,
      "site": "00aec27c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec34c",
      "incomplete_value": false,
      "site": "00aec358",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec284",
      "incomplete_value": false,
      "site": "00aec290",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aec340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec284 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec34c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec290 ["INT_ADD", "register:40f0:8", ["const:aec290:8", "const:4:8"]]
+ 00aec358 ["INT_ADD", "register:40f0:8", ["const:aec358:8", "const:4:8"]]
~~~


### [`00aec2b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec2b8.md) → [`00aec380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aec408",
      "incomplete_value": true,
      "site": "00aec408",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec340",
      "incomplete_value": true,
      "site": "00aec340",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec3b4",
      "incomplete_value": true,
      "site": "00aec3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec2ec",
      "incomplete_value": true,
      "site": "00aec2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:850:8"
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
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0858",
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
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec2cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00aec394 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
- 00aec2ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:850:8"]]
+ 00aec3b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:910:8"]]
- 00aec2f8 ["INT_ADD", "register:40f0:8", ["const:aec2f8:8", "const:4:8"]]
+ 00aec3c0 ["INT_ADD", "register:40f0:8", ["const:aec3c0:8", "const:4:8"]]
~~~


### [`00aec354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec354.md) → [`00aec41c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec458",
      "incomplete_value": true,
      "site": "00aec458",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec390",
      "incomplete_value": true,
      "site": "00aec390",
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
      "definition_site": "00aec4a8",
      "incomplete_value": true,
      "site": "00aec4a8",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec3e0",
      "incomplete_value": true,
      "site": "00aec3e0",
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
      "definition_site": "00aec434",
      "incomplete_value": true,
      "site": "00aec434",
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
      "definition_site": "00aec36c",
      "incomplete_value": true,
      "site": "00aec36c",
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0858",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec368 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aec430 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec36c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00aec434 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aec374 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00aec43c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
~~~


### [`00aec3f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md) → [`00aec4bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec4fc",
      "incomplete_value": true,
      "site": "00aec4fc",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec434",
      "incomplete_value": true,
      "site": "00aec434",
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
      "definition_site": "00aec4d8",
      "incomplete_value": true,
      "site": "00aec4d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec410",
      "incomplete_value": true,
      "site": "00aec410",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec4e0",
      "incomplete_value": false,
      "site": "00aec4f4",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec418",
      "incomplete_value": false,
      "site": "00aec42c",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec408 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aec4d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec418 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec4e0 ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec42c ["INT_ADD", "register:40f0:8", ["const:aec42c:8", "const:4:8"]]
+ 00aec4f4 ["INT_ADD", "register:40f0:8", ["const:aec4f4:8", "const:4:8"]]
~~~


### [`00aec464`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec464.md) → [`00aec52c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec52c.md) _ZN8firebase4util10long_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bde2f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2f0.md) · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde3a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3a0.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec548",
      "incomplete_value": false,
      "site": "00aec54c",
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00aec558",
      "incomplete_value": true,
      "site": "00aec564",
      "value": [
        "LOAD",
        "8",
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
        "010a0860",
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
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec478 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aec540 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec480 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aec548 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aec484 ["INT_ADD", "register:40f0:8", ["const:aec484:8", "const:4:8"]]
+ 00aec54c ["INT_ADD", "register:40f0:8", ["const:aec54c:8", "const:4:8"]]
~~~


### [`00aec4a0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec4a0.md) → [`00aec568`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec5a8",
      "incomplete_value": true,
      "site": "00aec5a8",
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
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec4e0",
      "incomplete_value": true,
      "site": "00aec4e0",
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
      "definition_site": "00aec584",
      "incomplete_value": true,
      "site": "00aec584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec4bc",
      "incomplete_value": true,
      "site": "00aec4bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec58c",
      "incomplete_value": false,
      "site": "00aec5a0",
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec4c4",
      "incomplete_value": false,
      "site": "00aec4d8",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec4b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aec57c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec4c4 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 00aec58c ["COPY", "tmp:0:8", ["const:d56:8"]]
- 00aec4d8 ["INT_ADD", "register:40f0:8", ["const:aec4d8:8", "const:4:8"]]
+ 00aec5a0 ["INT_ADD", "register:40f0:8", ["const:aec5a0:8", "const:4:8"]]
~~~


### [`00aec510`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec510.md) → [`00aec5d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec5f4",
      "incomplete_value": false,
      "site": "00aec5f8",
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
    "old": {
      "definition_site": "00aec52c",
      "incomplete_value": false,
      "site": "00aec530",
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
      "definition_site": "00aec604",
      "incomplete_value": true,
      "site": "00aec610",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec53c",
      "incomplete_value": true,
      "site": "00aec548",
      "value": [
        "LOAD",
        "8",
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
        "010a0870",
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
        "010a0930",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec52c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec5f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec530 ["INT_ADD", "register:40f0:8", ["const:aec530:8", "const:4:8"]]
+ 00aec5f8 ["INT_ADD", "register:40f0:8", ["const:aec5f8:8", "const:4:8"]]
- 00aec538 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00aec600 ["COPY", "tmp:0:8", ["const:930:8"]]
~~~


### [`00aec54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec54c.md) → [`00aec614`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec640",
      "incomplete_value": true,
      "site": "00aec640",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec578",
      "incomplete_value": true,
      "site": "00aec578",
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
            "const:878:8"
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
      "definition_site": "00aec628",
      "incomplete_value": true,
      "site": "00aec628",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec560",
      "incomplete_value": true,
      "site": "00aec560",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec634",
      "incomplete_value": false,
      "site": "00aec638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec56c",
      "incomplete_value": false,
      "site": "00aec570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:e6d:8"
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec55c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00aec624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec56c ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec634 ["COPY", "tmp:0:8", ["const:efa:8"]]
- 00aec570 ["INT_ADD", "register:40f0:8", ["const:aec570:8", "const:4:8"]]
+ 00aec638 ["INT_ADD", "register:40f0:8", ["const:aec638:8", "const:4:8"]]
~~~


### [`00aec58c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec58c.md) → [`00aec654`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec680",
      "incomplete_value": true,
      "site": "00aec680",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5b8",
      "incomplete_value": true,
      "site": "00aec5b8",
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
            "const:878:8"
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
      "definition_site": "00aec668",
      "incomplete_value": true,
      "site": "00aec668",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec5a0",
      "incomplete_value": true,
      "site": "00aec5a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec670",
      "incomplete_value": false,
      "site": "00aec678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5a8",
      "incomplete_value": false,
      "site": "00aec5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:e6d:8"
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00aec664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec5a8 ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec670 ["COPY", "tmp:0:8", ["const:efa:8"]]
- 00aec5b0 ["INT_ADD", "register:40f0:8", ["const:aec5b0:8", "const:4:8"]]
+ 00aec678 ["INT_ADD", "register:40f0:8", ["const:aec678:8", "const:4:8"]]
~~~


### [`00aec5cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec5cc.md) → [`00aec694`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec6c4",
      "incomplete_value": true,
      "site": "00aec6c4",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5fc",
      "incomplete_value": true,
      "site": "00aec5fc",
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
            "const:878:8"
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
      "definition_site": "00aec6a8",
      "incomplete_value": true,
      "site": "00aec6a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec5e0",
      "incomplete_value": true,
      "site": "00aec5e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec6b4",
      "incomplete_value": false,
      "site": "00aec6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5ec",
      "incomplete_value": false,
      "site": "00aec5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:e6d:8"
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00aec6a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec5e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aec6a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aec5ec ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec6b4 ["COPY", "tmp:0:8", ["const:efa:8"]]
~~~


### [`00aec610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec610.md) → [`00aec6d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec708",
      "incomplete_value": true,
      "site": "00aec708",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec640",
      "incomplete_value": true,
      "site": "00aec640",
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
            "const:878:8"
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
      "definition_site": "00aec6ec",
      "incomplete_value": true,
      "site": "00aec6ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec624",
      "incomplete_value": true,
      "site": "00aec624",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec6f4",
      "incomplete_value": false,
      "site": "00aec700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec62c",
      "incomplete_value": false,
      "site": "00aec638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:e6d:8"
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
+ 00aec6e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec62c ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec6f4 ["COPY", "tmp:0:8", ["const:efa:8"]]
- 00aec638 ["INT_ADD", "register:40f0:8", ["const:aec638:8", "const:4:8"]]
+ 00aec700 ["INT_ADD", "register:40f0:8", ["const:aec700:8", "const:4:8"]]
~~~


### [`00aec660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec660.md) → [`00aec728`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec7b0",
      "incomplete_value": true,
      "site": "00aec7b0",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6e8",
      "incomplete_value": true,
      "site": "00aec6e8",
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
            "const:880:8"
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
      "definition_site": "00aec75c",
      "incomplete_value": true,
      "site": "00aec768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec694",
      "incomplete_value": true,
      "site": "00aec6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:878:8"
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
        "010a0880",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0880",
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
        "010a0940",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec674 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:880:8"]]
+ 00aec73c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:940:8"]]
- 00aec680 ["BRANCH", null, ["local:b6:8"]]
+ 00aec748 ["BRANCH", null, ["local:b5:8"]]
- 00aec694 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:878:8"]]
+ 00aec75c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:938:8"]]
~~~


### [`00aec6fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec6fc.md) → [`00aec7c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec7c8",
      "incomplete_value": true,
      "site": "00aec7c8",
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
      "definition_site": "00aec700",
      "incomplete_value": true,
      "site": "00aec700",
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
      "definition_site": "00aec7c8",
      "incomplete_value": true,
      "site": "00aec7c8",
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
      "definition_site": "00aec700",
      "incomplete_value": true,
      "site": "00aec700",
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
      "definition_site": "00aec7cc",
      "incomplete_value": true,
      "site": "00aec7cc",
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
      "definition_site": "00aec704",
      "incomplete_value": true,
      "site": "00aec704",
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0880",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0880",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
+ 00aec7d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec714 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00aec7dc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aec71c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:880:8"]]
+ 00aec7e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:940:8"]]
~~~


### [`00aec79c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec79c.md) → [`00aec864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec8a4",
      "incomplete_value": true,
      "site": "00aec8a4",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec7dc",
      "incomplete_value": true,
      "site": "00aec7dc",
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
            "const:878:8"
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
      "definition_site": "00aec880",
      "incomplete_value": true,
      "site": "00aec880",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec7b8",
      "incomplete_value": true,
      "site": "00aec7b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec88c",
      "incomplete_value": true,
      "site": "00aec89c",
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec7b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
+ 00aec878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec7b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aec880 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec7c0 ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec888 ["COPY", "tmp:0:8", ["const:efa:8"]]
~~~


### [`00aec80c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec80c.md) → [`00aec8d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde000.md) · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0b0.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec8f0",
      "incomplete_value": false,
      "site": "00aec8f4",
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
    "old": {
      "definition_site": "00aec828",
      "incomplete_value": false,
      "site": "00aec82c",
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
      "definition_site": "00aec900",
      "incomplete_value": true,
      "site": "00aec90c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec838",
      "incomplete_value": true,
      "site": "00aec844",
      "value": [
        "LOAD",
        "8",
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
        "010a0888",
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
        "010a0948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec828 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aec8f0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aec82c ["INT_ADD", "register:40f0:8", ["const:aec82c:8", "const:4:8"]]
+ 00aec8f4 ["INT_ADD", "register:40f0:8", ["const:aec8f4:8", "const:4:8"]]
- 00aec834 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00aec8fc ["COPY", "tmp:0:8", ["const:948:8"]]
~~~


### [`00aec848`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec848.md) → [`00aec910`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec950",
      "incomplete_value": true,
      "site": "00aec950",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec888",
      "incomplete_value": true,
      "site": "00aec888",
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
            "const:878:8"
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
      "definition_site": "00aec92c",
      "incomplete_value": true,
      "site": "00aec92c",
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
      "definition_site": "00aec864",
      "incomplete_value": true,
      "site": "00aec864",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec934",
      "incomplete_value": false,
      "site": "00aec948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:efa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec86c",
      "incomplete_value": false,
      "site": "00aec880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:e6d:8"
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
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec85c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
+ 00aec924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec86c ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 00aec934 ["COPY", "tmp:0:8", ["const:efa:8"]]
- 00aec880 ["INT_ADD", "register:40f0:8", ["const:aec880:8", "const:4:8"]]
+ 00aec948 ["INT_ADD", "register:40f0:8", ["const:aec948:8", "const:4:8"]]
~~~


### [`00aec8b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8b8.md) → [`00aec980`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aec99c",
      "incomplete_value": false,
      "site": "00aec9a0",
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
    "old": {
      "definition_site": "00aec8d4",
      "incomplete_value": false,
      "site": "00aec8d8",
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
      "definition_site": "00aec9ac",
      "incomplete_value": true,
      "site": "00aec9b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec8e4",
      "incomplete_value": true,
      "site": "00aec8f0",
      "value": [
        "LOAD",
        "8",
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
        "010a08a0",
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
        "010a0960",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec8d4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec99c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec8d8 ["INT_ADD", "register:40f0:8", ["const:aec8d8:8", "const:4:8"]]
+ 00aec9a0 ["INT_ADD", "register:40f0:8", ["const:aec9a0:8", "const:4:8"]]
- 00aec8e0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00aec9a8 ["COPY", "tmp:0:8", ["const:960:8"]]
~~~


### [`00aec8f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8f4.md) → [`00aec9bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec9e8",
      "incomplete_value": true,
      "site": "00aec9e8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec920",
      "incomplete_value": true,
      "site": "00aec920",
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
            "const:8a8:8"
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
      "definition_site": "00aec9d0",
      "incomplete_value": true,
      "site": "00aec9d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec908",
      "incomplete_value": true,
      "site": "00aec908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec9dc",
      "incomplete_value": false,
      "site": "00aec9e0",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec914",
      "incomplete_value": false,
      "site": "00aec918",
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
            "const:1d3:8"
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00aec9cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec914 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aec9dc ["COPY", "tmp:0:8", ["const:260:8"]]
- 00aec918 ["INT_ADD", "register:40f0:8", ["const:aec918:8", "const:4:8"]]
+ 00aec9e0 ["INT_ADD", "register:40f0:8", ["const:aec9e0:8", "const:4:8"]]
~~~


### [`00aec934`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md) → [`00aec9fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeca28",
      "incomplete_value": true,
      "site": "00aeca28",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec960",
      "incomplete_value": true,
      "site": "00aec960",
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
            "const:8a8:8"
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
      "definition_site": "00aeca10",
      "incomplete_value": true,
      "site": "00aeca10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec948",
      "incomplete_value": true,
      "site": "00aec948",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeca18",
      "incomplete_value": false,
      "site": "00aeca20",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec950",
      "incomplete_value": false,
      "site": "00aec958",
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
            "const:1d3:8"
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00aeca0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec950 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aeca18 ["COPY", "tmp:0:8", ["const:260:8"]]
- 00aec958 ["INT_ADD", "register:40f0:8", ["const:aec958:8", "const:4:8"]]
+ 00aeca20 ["INT_ADD", "register:40f0:8", ["const:aeca20:8", "const:4:8"]]
~~~


### [`00aec974`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md) → [`00aeca3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeca6c",
      "incomplete_value": true,
      "site": "00aeca6c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9a4",
      "incomplete_value": true,
      "site": "00aec9a4",
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
            "const:8a8:8"
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
      "definition_site": "00aeca50",
      "incomplete_value": true,
      "site": "00aeca50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec988",
      "incomplete_value": true,
      "site": "00aec988",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeca5c",
      "incomplete_value": true,
      "site": "00aeca64",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec994",
      "incomplete_value": false,
      "site": "00aec99c",
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
            "const:1d3:8"
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00aeca4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec988 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aeca50 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aec994 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aeca5c ["COPY", "tmp:0:8", ["const:260:8"]]
~~~


### [`00aec9b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9b8.md) → [`00aeca80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecab0",
      "incomplete_value": true,
      "site": "00aecab0",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9e8",
      "incomplete_value": true,
      "site": "00aec9e8",
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
            "const:8a8:8"
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
      "definition_site": "00aeca94",
      "incomplete_value": true,
      "site": "00aeca94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aec9cc",
      "incomplete_value": true,
      "site": "00aec9cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeca9c",
      "incomplete_value": false,
      "site": "00aecaa8",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9d4",
      "incomplete_value": true,
      "site": "00aec9e0",
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
            "const:1d3:8"
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aec9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
+ 00aeca90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec9cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aeca94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec9d4 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aeca9c ["COPY", "tmp:0:8", ["const:260:8"]]
~~~


### [`00aec9fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9fc.md) → [`00aecac4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecac4.md) _ZN8firebase4util22parcel_file_descriptor8GetClassEv

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
    "new": null,
    "old": {
      "definition_site": "00aeca00",
      "incomplete_value": true,
      "site": "00aeca04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
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
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aeca00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8a8:8"]]
+ 00aecac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
~~~


### [`00aeca08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md) → [`00aecad0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aecb58",
      "incomplete_value": true,
      "site": "00aecb58",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca90",
      "incomplete_value": true,
      "site": "00aeca90",
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
            "const:8b0:8"
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
      "definition_site": "00aecb10",
      "incomplete_value": true,
      "site": "00aecb10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeca48",
      "incomplete_value": true,
      "site": "00aeca48",
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
      "definition_site": "00aecb04",
      "incomplete_value": true,
      "site": "00aecb10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:968:8"
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
        "010a08b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a08b0",
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
        "010a0970",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aeca1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8b0:8"]]
+ 00aecae4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
- 00aeca20 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aecae8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aeca28 ["BRANCH", null, ["local:b7:8"]]
+ 00aecaf0 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00aecaa4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md) → [`00aecb6c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecb70",
      "incomplete_value": true,
      "site": "00aecb70",
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
      "definition_site": "00aecaa8",
      "incomplete_value": true,
      "site": "00aecaa8",
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
      "definition_site": "00aecb70",
      "incomplete_value": true,
      "site": "00aecb70",
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
      "definition_site": "00aecaa8",
      "incomplete_value": true,
      "site": "00aecaa8",
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
      "definition_site": "00aecb74",
      "incomplete_value": true,
      "site": "00aecb74",
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
      "definition_site": "00aecaac",
      "incomplete_value": true,
      "site": "00aecaac",
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a08b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a08b0",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecab8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00aecb80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecabc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00aecb84 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aecac4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8b0:8"]]
+ 00aecb8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
~~~


### [`00aecb44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md) → [`00aecc0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecc4c",
      "incomplete_value": true,
      "site": "00aecc4c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecb84",
      "incomplete_value": true,
      "site": "00aecb84",
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
            "const:8a8:8"
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
      "definition_site": "00aecc28",
      "incomplete_value": true,
      "site": "00aecc28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecb60",
      "incomplete_value": true,
      "site": "00aecb60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecc34",
      "incomplete_value": true,
      "site": "00aecc44",
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecb58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00aecc20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecb60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecc28 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecb68 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aecc30 ["COPY", "tmp:0:8", ["const:260:8"]]
~~~


### [`00aecbb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md) → [`00aecc7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aecc98",
      "incomplete_value": false,
      "site": "00aecc9c",
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
    "old": {
      "definition_site": "00aecbd0",
      "incomplete_value": false,
      "site": "00aecbd4",
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
      "definition_site": "00aecca8",
      "incomplete_value": true,
      "site": "00aeccb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aecbe0",
      "incomplete_value": true,
      "site": "00aecbec",
      "value": [
        "LOAD",
        "8",
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
        "010a08b8",
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
        "010a0978",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecbd0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aecc98 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aecbd4 ["INT_ADD", "register:40f0:8", ["const:aecbd4:8", "const:4:8"]]
+ 00aecc9c ["INT_ADD", "register:40f0:8", ["const:aecc9c:8", "const:4:8"]]
- 00aecbdc ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00aecca4 ["COPY", "tmp:0:8", ["const:978:8"]]
~~~


### [`00aecbf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md) → [`00aeccb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeccbc",
      "incomplete_value": true,
      "site": "00aeccbc",
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
      "definition_site": "00aecbf4",
      "incomplete_value": true,
      "site": "00aecbf4",
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
      "definition_site": "00aeccbc",
      "incomplete_value": true,
      "site": "00aeccbc",
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
      "definition_site": "00aecbf4",
      "incomplete_value": true,
      "site": "00aecbf4",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeccf8",
      "incomplete_value": true,
      "site": "00aeccf8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecc30",
      "incomplete_value": true,
      "site": "00aecc30",
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
            "const:8a8:8"
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
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecc04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
+ 00aecccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecc0c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aeccd4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aecc14 ["COPY", "tmp:0:8", ["const:1d3:8"]]
+ 00aeccdc ["COPY", "tmp:0:8", ["const:260:8"]]
~~~


### [`00aecc60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc60.md) → [`00aecd28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd28.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecd2c",
      "incomplete_value": true,
      "site": "00aecd2c",
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
      "definition_site": "00aecc64",
      "incomplete_value": true,
      "site": "00aecc64",
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
      "definition_site": "00aecd2c",
      "incomplete_value": true,
      "site": "00aecd2c",
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
      "definition_site": "00aecc64",
      "incomplete_value": true,
      "site": "00aecc64",
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
      "definition_site": "00aecd44",
      "incomplete_value": false,
      "site": "00aecd48",
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
    "old": {
      "definition_site": "00aecc7c",
      "incomplete_value": false,
      "site": "00aecc80",
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
        "010a08c0",
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
        "010a0980",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecc74 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecd3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecc7c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aecd44 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aecc80 ["INT_ADD", "register:40f0:8", ["const:aecc80:8", "const:4:8"]]
+ 00aecd48 ["INT_ADD", "register:40f0:8", ["const:aecd48:8", "const:4:8"]]
~~~


### [`00aecc9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc9c.md) → [`00aecd64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecd90",
      "incomplete_value": true,
      "site": "00aecd90",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeccc8",
      "incomplete_value": true,
      "site": "00aeccc8",
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
      "definition_site": "00aecd78",
      "incomplete_value": true,
      "site": "00aecd78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeccb0",
      "incomplete_value": true,
      "site": "00aeccb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecd84",
      "incomplete_value": false,
      "site": "00aecd88",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeccbc",
      "incomplete_value": true,
      "site": "00aeccc0",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aeccac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00aecd74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aeccb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecd78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeccbc ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aecd84 ["COPY", "tmp:0:8", ["const:fbf:8"]]
~~~


### [`00aeccdc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeccdc.md) → [`00aecda4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecdd0",
      "incomplete_value": true,
      "site": "00aecdd0",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd08",
      "incomplete_value": true,
      "site": "00aecd08",
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
      "definition_site": "00aecdb8",
      "incomplete_value": true,
      "site": "00aecdb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeccf0",
      "incomplete_value": true,
      "site": "00aeccf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecdc0",
      "incomplete_value": false,
      "site": "00aecdc8",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeccf8",
      "incomplete_value": false,
      "site": "00aecd00",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aeccec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00aecdb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aeccf8 ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aecdc0 ["COPY", "tmp:0:8", ["const:fbf:8"]]
- 00aecd00 ["INT_ADD", "register:40f0:8", ["const:aecd00:8", "const:4:8"]]
+ 00aecdc8 ["INT_ADD", "register:40f0:8", ["const:aecdc8:8", "const:4:8"]]
~~~


### [`00aecd1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md) → [`00aecde4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aece14",
      "incomplete_value": true,
      "site": "00aece14",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd4c",
      "incomplete_value": true,
      "site": "00aecd4c",
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
      "definition_site": "00aecdf8",
      "incomplete_value": true,
      "site": "00aecdf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecd30",
      "incomplete_value": true,
      "site": "00aecd30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aece04",
      "incomplete_value": false,
      "site": "00aece0c",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd3c",
      "incomplete_value": false,
      "site": "00aecd44",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecd2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00aecdf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecd30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecdf8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecd3c ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aece04 ["COPY", "tmp:0:8", ["const:fbf:8"]]
~~~


### [`00aecd60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd60.md) → [`00aece28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aece58",
      "incomplete_value": true,
      "site": "00aece58",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd90",
      "incomplete_value": true,
      "site": "00aecd90",
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
      "definition_site": "00aece3c",
      "incomplete_value": true,
      "site": "00aece3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecd74",
      "incomplete_value": true,
      "site": "00aecd74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aece44",
      "incomplete_value": false,
      "site": "00aece50",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd7c",
      "incomplete_value": false,
      "site": "00aecd88",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecd70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
+ 00aece38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecd7c ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aece44 ["COPY", "tmp:0:8", ["const:fbf:8"]]
- 00aecd88 ["INT_ADD", "register:40f0:8", ["const:aecd88:8", "const:4:8"]]
+ 00aece50 ["INT_ADD", "register:40f0:8", ["const:aece50:8", "const:4:8"]]
~~~


### [`00aecdb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecdb0.md) → [`00aece78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aecf00",
      "incomplete_value": true,
      "site": "00aecf00",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece38",
      "incomplete_value": true,
      "site": "00aece38",
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
      "definition_site": "00aeceac",
      "incomplete_value": true,
      "site": "00aeceb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecde4",
      "incomplete_value": true,
      "site": "00aecdf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
        "010a08d0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a08d0",
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
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecdc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00aece8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
- 00aecde4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8c8:8"]]
+ 00aeceac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:988:8"]]
- 00aecdf0 ["INT_ADD", "register:40f0:8", ["const:aecdf0:8", "const:4:8"]]
+ 00aeceb8 ["INT_ADD", "register:40f0:8", ["const:aeceb8:8", "const:4:8"]]
~~~


### [`00aece4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aece4c.md) → [`00aecf14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aecf50",
      "incomplete_value": true,
      "site": "00aecf50",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece88",
      "incomplete_value": true,
      "site": "00aece88",
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
      "definition_site": "00aecfa0",
      "incomplete_value": true,
      "site": "00aecfa0",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeced8",
      "incomplete_value": true,
      "site": "00aeced8",
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
      "definition_site": "00aecf2c",
      "incomplete_value": true,
      "site": "00aecf2c",
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
      "definition_site": "00aece64",
      "incomplete_value": true,
      "site": "00aece64",
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a08d0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a08d0",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aece60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00aecf28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aece6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
+ 00aecf34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
- 00aece84 ["INT_ADD", "register:40f0:8", ["const:aece84:8", "const:4:8"]]
+ 00aecf4c ["INT_ADD", "register:40f0:8", ["const:aecf4c:8", "const:4:8"]]
~~~


### [`00aeceec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md) → [`00aecfb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecff4",
      "incomplete_value": true,
      "site": "00aecff4",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecf2c",
      "incomplete_value": true,
      "site": "00aecf2c",
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
      "definition_site": "00aecfd0",
      "incomplete_value": true,
      "site": "00aecfd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecf08",
      "incomplete_value": true,
      "site": "00aecf08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecfd8",
      "incomplete_value": false,
      "site": "00aecfec",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecf10",
      "incomplete_value": false,
      "site": "00aecf24",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecf00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00aecfc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aecf10 ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aecfd8 ["COPY", "tmp:0:8", ["const:fbf:8"]]
- 00aecf24 ["INT_ADD", "register:40f0:8", ["const:aecf24:8", "const:4:8"]]
+ 00aecfec ["INT_ADD", "register:40f0:8", ["const:aecfec:8", "const:4:8"]]
~~~


### [`00aecf5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf5c.md) → [`00aed024`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde580.md) · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde630`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde630.md) · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed040",
      "incomplete_value": false,
      "site": "00aed044",
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
    "old": {
      "definition_site": "00aecf78",
      "incomplete_value": false,
      "site": "00aecf7c",
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
      "definition_site": "00aed050",
      "incomplete_value": true,
      "site": "00aed05c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aecf88",
      "incomplete_value": true,
      "site": "00aecf94",
      "value": [
        "LOAD",
        "8",
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
        "010a08d8",
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
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecf78 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed040 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aecf7c ["INT_ADD", "register:40f0:8", ["const:aecf7c:8", "const:4:8"]]
+ 00aed044 ["INT_ADD", "register:40f0:8", ["const:aed044:8", "const:4:8"]]
- 00aecf84 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 00aed04c ["COPY", "tmp:0:8", ["const:998:8"]]
~~~


### [`00aecf98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf98.md) → [`00aed060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed0a0",
      "incomplete_value": true,
      "site": "00aed0a0",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecfd8",
      "incomplete_value": true,
      "site": "00aecfd8",
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
      "definition_site": "00aed07c",
      "incomplete_value": true,
      "site": "00aed07c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aecfb4",
      "incomplete_value": true,
      "site": "00aecfb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed084",
      "incomplete_value": false,
      "site": "00aed098",
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
            "const:fbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecfbc",
      "incomplete_value": false,
      "site": "00aecfd0",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08c8",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aecfac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
+ 00aed074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aecfbc ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 00aed084 ["COPY", "tmp:0:8", ["const:fbf:8"]]
- 00aecfd0 ["INT_ADD", "register:40f0:8", ["const:aecfd0:8", "const:4:8"]]
+ 00aed098 ["INT_ADD", "register:40f0:8", ["const:aed098:8", "const:4:8"]]
~~~


### [`00aed008`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed008.md) → [`00aed0d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed0ec",
      "incomplete_value": false,
      "site": "00aed0f0",
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
    "old": {
      "definition_site": "00aed024",
      "incomplete_value": false,
      "site": "00aed028",
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
      "definition_site": "00aed0fc",
      "incomplete_value": true,
      "site": "00aed108",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aed034",
      "incomplete_value": true,
      "site": "00aed040",
      "value": [
        "LOAD",
        "8",
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
        "010a08e0",
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
        "010a09a0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed024 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed0ec ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed028 ["INT_ADD", "register:40f0:8", ["const:aed028:8", "const:4:8"]]
+ 00aed0f0 ["INT_ADD", "register:40f0:8", ["const:aed0f0:8", "const:4:8"]]
- 00aed030 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00aed0f8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
~~~


### [`00aed044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed044.md) → [`00aed10c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed138",
      "incomplete_value": true,
      "site": "00aed138",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed070",
      "incomplete_value": true,
      "site": "00aed070",
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
            "const:8e8:8"
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
      "definition_site": "00aed120",
      "incomplete_value": true,
      "site": "00aed120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed058",
      "incomplete_value": true,
      "site": "00aed058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed12c",
      "incomplete_value": false,
      "site": "00aed130",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed064",
      "incomplete_value": false,
      "site": "00aed068",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00aed11c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed064 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed12c ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed068 ["INT_ADD", "register:40f0:8", ["const:aed068:8", "const:4:8"]]
+ 00aed130 ["INT_ADD", "register:40f0:8", ["const:aed130:8", "const:4:8"]]
~~~


### [`00aed084`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed084.md) → [`00aed14c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed178",
      "incomplete_value": true,
      "site": "00aed178",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0b0",
      "incomplete_value": true,
      "site": "00aed0b0",
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
            "const:8e8:8"
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
      "definition_site": "00aed160",
      "incomplete_value": true,
      "site": "00aed160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed098",
      "incomplete_value": true,
      "site": "00aed098",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed168",
      "incomplete_value": false,
      "site": "00aed170",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0a0",
      "incomplete_value": false,
      "site": "00aed0a8",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00aed15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed0a0 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed168 ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed0a8 ["INT_ADD", "register:40f0:8", ["const:aed0a8:8", "const:4:8"]]
+ 00aed170 ["INT_ADD", "register:40f0:8", ["const:aed170:8", "const:4:8"]]
~~~


### [`00aed0c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed0c4.md) → [`00aed18c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed1bc",
      "incomplete_value": true,
      "site": "00aed1bc",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0f4",
      "incomplete_value": true,
      "site": "00aed0f4",
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
            "const:8e8:8"
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
      "definition_site": "00aed1a0",
      "incomplete_value": true,
      "site": "00aed1a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed0d8",
      "incomplete_value": true,
      "site": "00aed0d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed1ac",
      "incomplete_value": false,
      "site": "00aed1b4",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0e4",
      "incomplete_value": false,
      "site": "00aed0ec",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00aed19c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed0e4 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed1ac ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed0ec ["INT_ADD", "register:40f0:8", ["const:aed0ec:8", "const:4:8"]]
+ 00aed1b4 ["INT_ADD", "register:40f0:8", ["const:aed1b4:8", "const:4:8"]]
~~~


### [`00aed108`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed108.md) → [`00aed1d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed200",
      "incomplete_value": true,
      "site": "00aed200",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed138",
      "incomplete_value": true,
      "site": "00aed138",
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
            "const:8e8:8"
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
      "definition_site": "00aed1e4",
      "incomplete_value": true,
      "site": "00aed1e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed11c",
      "incomplete_value": true,
      "site": "00aed11c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed1ec",
      "incomplete_value": false,
      "site": "00aed1f8",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed124",
      "incomplete_value": false,
      "site": "00aed130",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00aed1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aed124 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed1ec ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed130 ["INT_ADD", "register:40f0:8", ["const:aed130:8", "const:4:8"]]
+ 00aed1f8 ["INT_ADD", "register:40f0:8", ["const:aed1f8:8", "const:4:8"]]
~~~


### [`00aed158`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed158.md) → [`00aed220`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aed2a8",
      "incomplete_value": true,
      "site": "00aed2a8",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed1e0",
      "incomplete_value": true,
      "site": "00aed1e0",
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
            "const:8f0:8"
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
      "definition_site": "00aed254",
      "incomplete_value": true,
      "site": "00aed260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed18c",
      "incomplete_value": true,
      "site": "00aed198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
        "010a08f0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a08f0",
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
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed16c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
+ 00aed234 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00aed18c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8e8:8"]]
+ 00aed254 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9a8:8"]]
- 00aed198 ["INT_ADD", "register:40f0:8", ["const:aed198:8", "const:4:8"]]
+ 00aed260 ["INT_ADD", "register:40f0:8", ["const:aed260:8", "const:4:8"]]
~~~


### [`00aed1f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md) → [`00aed2bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aed2f8",
      "incomplete_value": true,
      "site": "00aed2f8",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed230",
      "incomplete_value": true,
      "site": "00aed230",
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
            "const:8f0:8"
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
      "definition_site": "00aed348",
      "incomplete_value": true,
      "site": "00aed348",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed280",
      "incomplete_value": true,
      "site": "00aed280",
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
            "const:8e8:8"
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
      "definition_site": "00aed2d4",
      "incomplete_value": true,
      "site": "00aed2d4",
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
      "definition_site": "00aed20c",
      "incomplete_value": true,
      "site": "00aed20c",
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a08f0",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00aed2d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed214 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
+ 00aed2dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00aed22c ["INT_ADD", "register:40f0:8", ["const:aed22c:8", "const:4:8"]]
+ 00aed2f4 ["INT_ADD", "register:40f0:8", ["const:aed2f4:8", "const:4:8"]]
~~~


### [`00aed294`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed294.md) → [`00aed35c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed39c",
      "incomplete_value": true,
      "site": "00aed39c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed2d4",
      "incomplete_value": true,
      "site": "00aed2d4",
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
            "const:8e8:8"
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
      "definition_site": "00aed378",
      "incomplete_value": true,
      "site": "00aed378",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed2b0",
      "incomplete_value": true,
      "site": "00aed2b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed380",
      "incomplete_value": false,
      "site": "00aed394",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed2b8",
      "incomplete_value": false,
      "site": "00aed2cc",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed2a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00aed370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed2b8 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed380 ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed2cc ["INT_ADD", "register:40f0:8", ["const:aed2cc:8", "const:4:8"]]
+ 00aed394 ["INT_ADD", "register:40f0:8", ["const:aed394:8", "const:4:8"]]
~~~


### [`00aed304`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed304.md) → [`00aed3cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed3e8",
      "incomplete_value": false,
      "site": "00aed3ec",
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
    "old": {
      "definition_site": "00aed320",
      "incomplete_value": false,
      "site": "00aed324",
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
      "definition_site": "00aed3f8",
      "incomplete_value": true,
      "site": "00aed404",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aed330",
      "incomplete_value": true,
      "site": "00aed33c",
      "value": [
        "LOAD",
        "8",
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
        "010a08f8",
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
        "010a09b8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed320 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed3e8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aed324 ["INT_ADD", "register:40f0:8", ["const:aed324:8", "const:4:8"]]
+ 00aed3ec ["INT_ADD", "register:40f0:8", ["const:aed3ec:8", "const:4:8"]]
- 00aed32c ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00aed3f4 ["COPY", "tmp:0:8", ["const:9b8:8"]]
~~~


### [`00aed340`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed340.md) → [`00aed408`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed448",
      "incomplete_value": true,
      "site": "00aed448",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed380",
      "incomplete_value": true,
      "site": "00aed380",
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
            "const:8e8:8"
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
      "definition_site": "00aed424",
      "incomplete_value": true,
      "site": "00aed424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed35c",
      "incomplete_value": true,
      "site": "00aed35c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed42c",
      "incomplete_value": false,
      "site": "00aed440",
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
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed364",
      "incomplete_value": false,
      "site": "00aed378",
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
            "const:429:8"
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
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a08e8",
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
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00aed41c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aed364 ["COPY", "tmp:0:8", ["const:429:8"]]
+ 00aed42c ["COPY", "tmp:0:8", ["const:395:8"]]
- 00aed378 ["INT_ADD", "register:40f0:8", ["const:aed378:8", "const:4:8"]]
+ 00aed440 ["INT_ADD", "register:40f0:8", ["const:aed440:8", "const:4:8"]]
~~~


### [`00aed3b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3b0.md) → [`00aed478`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed494",
      "incomplete_value": false,
      "site": "00aed498",
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
    "old": {
      "definition_site": "00aed3cc",
      "incomplete_value": false,
      "site": "00aed3d0",
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
      "definition_site": "00aed4a4",
      "incomplete_value": true,
      "site": "00aed4b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aed3dc",
      "incomplete_value": true,
      "site": "00aed3e8",
      "value": [
        "LOAD",
        "8",
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
        "010a0908",
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
        "010a09c8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed3cc ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed494 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed3d0 ["INT_ADD", "register:40f0:8", ["const:aed3d0:8", "const:4:8"]]
+ 00aed498 ["INT_ADD", "register:40f0:8", ["const:aed498:8", "const:4:8"]]
- 00aed3d8 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00aed4a0 ["COPY", "tmp:0:8", ["const:9c8:8"]]
~~~


### [`00aed3ec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3ec.md) → [`00aed4b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed4e0",
      "incomplete_value": true,
      "site": "00aed4e0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed418",
      "incomplete_value": true,
      "site": "00aed418",
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
            "const:910:8"
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
      "definition_site": "00aed4c8",
      "incomplete_value": true,
      "site": "00aed4c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed400",
      "incomplete_value": true,
      "site": "00aed400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed4d4",
      "incomplete_value": false,
      "site": "00aed4d8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed40c",
      "incomplete_value": false,
      "site": "00aed410",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed3fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aed4c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed40c ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed4d4 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed410 ["INT_ADD", "register:40f0:8", ["const:aed410:8", "const:4:8"]]
+ 00aed4d8 ["INT_ADD", "register:40f0:8", ["const:aed4d8:8", "const:4:8"]]
~~~


### [`00aed42c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed42c.md) → [`00aed4f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed520",
      "incomplete_value": true,
      "site": "00aed520",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed458",
      "incomplete_value": true,
      "site": "00aed458",
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
            "const:910:8"
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
      "definition_site": "00aed508",
      "incomplete_value": true,
      "site": "00aed508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed440",
      "incomplete_value": true,
      "site": "00aed440",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed510",
      "incomplete_value": false,
      "site": "00aed518",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed448",
      "incomplete_value": false,
      "site": "00aed450",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aed504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed448 ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed510 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed450 ["INT_ADD", "register:40f0:8", ["const:aed450:8", "const:4:8"]]
+ 00aed518 ["INT_ADD", "register:40f0:8", ["const:aed518:8", "const:4:8"]]
~~~


### [`00aed46c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed46c.md) → [`00aed534`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed564",
      "incomplete_value": true,
      "site": "00aed564",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed49c",
      "incomplete_value": true,
      "site": "00aed49c",
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
            "const:910:8"
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
      "definition_site": "00aed548",
      "incomplete_value": true,
      "site": "00aed548",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed480",
      "incomplete_value": true,
      "site": "00aed480",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed554",
      "incomplete_value": false,
      "site": "00aed55c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed48c",
      "incomplete_value": false,
      "site": "00aed494",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aed544 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed48c ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed554 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed494 ["INT_ADD", "register:40f0:8", ["const:aed494:8", "const:4:8"]]
+ 00aed55c ["INT_ADD", "register:40f0:8", ["const:aed55c:8", "const:4:8"]]
~~~


### [`00aed4b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed4b0.md) → [`00aed578`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed5a8",
      "incomplete_value": true,
      "site": "00aed5a8",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed4e0",
      "incomplete_value": true,
      "site": "00aed4e0",
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
            "const:910:8"
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
      "definition_site": "00aed58c",
      "incomplete_value": true,
      "site": "00aed58c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed4c4",
      "incomplete_value": true,
      "site": "00aed4c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed594",
      "incomplete_value": false,
      "site": "00aed5a0",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed4cc",
      "incomplete_value": false,
      "site": "00aed4d8",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aed588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
- 00aed4cc ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed594 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed4d8 ["INT_ADD", "register:40f0:8", ["const:aed4d8:8", "const:4:8"]]
+ 00aed5a0 ["INT_ADD", "register:40f0:8", ["const:aed5a0:8", "const:4:8"]]
~~~


### [`00aed500`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed500.md) → [`00aed5c8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aed650",
      "incomplete_value": true,
      "site": "00aed650",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed588",
      "incomplete_value": true,
      "site": "00aed588",
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
            "const:918:8"
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
      "definition_site": "00aed5fc",
      "incomplete_value": true,
      "site": "00aed608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed534",
      "incomplete_value": true,
      "site": "00aed540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
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
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0918",
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
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
+ 00aed5dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d8:8"]]
- 00aed534 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:910:8"]]
+ 00aed5fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d0:8"]]
- 00aed540 ["INT_ADD", "register:40f0:8", ["const:aed540:8", "const:4:8"]]
+ 00aed608 ["INT_ADD", "register:40f0:8", ["const:aed608:8", "const:4:8"]]
~~~


### [`00aed59c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed59c.md) → [`00aed664`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aed6a0",
      "incomplete_value": true,
      "site": "00aed6a0",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed5d8",
      "incomplete_value": true,
      "site": "00aed5d8",
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
            "const:918:8"
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
      "definition_site": "00aed6f0",
      "incomplete_value": true,
      "site": "00aed6f0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed628",
      "incomplete_value": true,
      "site": "00aed628",
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
            "const:910:8"
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
      "definition_site": "00aed67c",
      "incomplete_value": true,
      "site": "00aed67c",
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
      "definition_site": "00aed5b4",
      "incomplete_value": true,
      "site": "00aed5b4",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0918",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed5b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aed678 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed5bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
+ 00aed684 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d8:8"]]
- 00aed5d4 ["INT_ADD", "register:40f0:8", ["const:aed5d4:8", "const:4:8"]]
+ 00aed69c ["INT_ADD", "register:40f0:8", ["const:aed69c:8", "const:4:8"]]
~~~


### [`00aed63c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed63c.md) → [`00aed704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed744",
      "incomplete_value": true,
      "site": "00aed744",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed67c",
      "incomplete_value": true,
      "site": "00aed67c",
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
            "const:910:8"
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
      "definition_site": "00aed720",
      "incomplete_value": true,
      "site": "00aed720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed658",
      "incomplete_value": true,
      "site": "00aed658",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed728",
      "incomplete_value": false,
      "site": "00aed73c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed660",
      "incomplete_value": false,
      "site": "00aed674",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aed718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed660 ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed728 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed674 ["INT_ADD", "register:40f0:8", ["const:aed674:8", "const:4:8"]]
+ 00aed73c ["INT_ADD", "register:40f0:8", ["const:aed73c:8", "const:4:8"]]
~~~


### [`00aed6ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6ac.md) → [`00aed774`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed790",
      "incomplete_value": false,
      "site": "00aed794",
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
    "old": {
      "definition_site": "00aed6c8",
      "incomplete_value": false,
      "site": "00aed6cc",
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
      "definition_site": "00aed7a0",
      "incomplete_value": true,
      "site": "00aed7ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aed6d8",
      "incomplete_value": true,
      "site": "00aed6e4",
      "value": [
        "LOAD",
        "8",
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
        "010a0920",
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
        "010a09e0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed6c8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aed790 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aed6cc ["INT_ADD", "register:40f0:8", ["const:aed6cc:8", "const:4:8"]]
+ 00aed794 ["INT_ADD", "register:40f0:8", ["const:aed794:8", "const:4:8"]]
- 00aed6d4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00aed79c ["COPY", "tmp:0:8", ["const:9e0:8"]]
~~~


### [`00aed6e8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6e8.md) → [`00aed7b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed7f0",
      "incomplete_value": true,
      "site": "00aed7f0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed728",
      "incomplete_value": true,
      "site": "00aed728",
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
            "const:910:8"
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
      "definition_site": "00aed7cc",
      "incomplete_value": true,
      "site": "00aed7cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed704",
      "incomplete_value": true,
      "site": "00aed704",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed7d4",
      "incomplete_value": false,
      "site": "00aed7e8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed70c",
      "incomplete_value": false,
      "site": "00aed720",
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
            "const:5c3:8"
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0910",
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
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed6fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aed7c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
- 00aed70c ["COPY", "tmp:0:8", ["const:5c3:8"]]
+ 00aed7d4 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00aed720 ["INT_ADD", "register:40f0:8", ["const:aed720:8", "const:4:8"]]
+ 00aed7e8 ["INT_ADD", "register:40f0:8", ["const:aed7e8:8", "const:4:8"]]
~~~


### [`00aed758`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed758.md) → [`00aed820`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed83c",
      "incomplete_value": false,
      "site": "00aed840",
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
    "old": {
      "definition_site": "00aed774",
      "incomplete_value": false,
      "site": "00aed778",
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
      "definition_site": "00aed84c",
      "incomplete_value": true,
      "site": "00aed858",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aed784",
      "incomplete_value": true,
      "site": "00aed790",
      "value": [
        "LOAD",
        "8",
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
        "010a0928",
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
        "010a09e8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed774 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aed83c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aed778 ["INT_ADD", "register:40f0:8", ["const:aed778:8", "const:4:8"]]
+ 00aed840 ["INT_ADD", "register:40f0:8", ["const:aed840:8", "const:4:8"]]
- 00aed780 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00aed848 ["COPY", "tmp:0:8", ["const:9e8:8"]]
~~~


### [`00aed794`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed794.md) → [`00aed85c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed888",
      "incomplete_value": true,
      "site": "00aed888",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7c0",
      "incomplete_value": true,
      "site": "00aed7c0",
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
            "const:930:8"
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
      "definition_site": "00aed870",
      "incomplete_value": true,
      "site": "00aed870",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed7a8",
      "incomplete_value": true,
      "site": "00aed7a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed87c",
      "incomplete_value": false,
      "site": "00aed880",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7b4",
      "incomplete_value": false,
      "site": "00aed7b8",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed7a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00aed86c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed7b4 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aed87c ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 00aed7b8 ["INT_ADD", "register:40f0:8", ["const:aed7b8:8", "const:4:8"]]
+ 00aed880 ["INT_ADD", "register:40f0:8", ["const:aed880:8", "const:4:8"]]
~~~


### [`00aed7d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed7d4.md) → [`00aed89c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed8c8",
      "incomplete_value": true,
      "site": "00aed8c8",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed800",
      "incomplete_value": true,
      "site": "00aed800",
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
            "const:930:8"
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
      "definition_site": "00aed8b0",
      "incomplete_value": true,
      "site": "00aed8b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed7e8",
      "incomplete_value": true,
      "site": "00aed7e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed8b8",
      "incomplete_value": false,
      "site": "00aed8c0",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7f0",
      "incomplete_value": false,
      "site": "00aed7f8",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00aed8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed7f0 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aed8b8 ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 00aed7f8 ["INT_ADD", "register:40f0:8", ["const:aed7f8:8", "const:4:8"]]
+ 00aed8c0 ["INT_ADD", "register:40f0:8", ["const:aed8c0:8", "const:4:8"]]
~~~


### [`00aed814`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md) → [`00aed8dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed90c",
      "incomplete_value": true,
      "site": "00aed90c",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed844",
      "incomplete_value": true,
      "site": "00aed844",
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
            "const:930:8"
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
      "definition_site": "00aed8f0",
      "incomplete_value": true,
      "site": "00aed8f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed828",
      "incomplete_value": true,
      "site": "00aed828",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed8fc",
      "incomplete_value": false,
      "site": "00aed904",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed834",
      "incomplete_value": false,
      "site": "00aed83c",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00aed8ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed834 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aed8fc ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 00aed83c ["INT_ADD", "register:40f0:8", ["const:aed83c:8", "const:4:8"]]
+ 00aed904 ["INT_ADD", "register:40f0:8", ["const:aed904:8", "const:4:8"]]
~~~


### [`00aed858`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed858.md) → [`00aed920`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aed950",
      "incomplete_value": true,
      "site": "00aed950",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed888",
      "incomplete_value": true,
      "site": "00aed888",
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
            "const:930:8"
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
      "definition_site": "00aed934",
      "incomplete_value": true,
      "site": "00aed934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed86c",
      "incomplete_value": true,
      "site": "00aed86c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aed93c",
      "incomplete_value": false,
      "site": "00aed948",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed874",
      "incomplete_value": false,
      "site": "00aed880",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
+ 00aed930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
- 00aed874 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aed93c ["COPY", "tmp:0:8", ["const:c0a:8"]]
- 00aed880 ["INT_ADD", "register:40f0:8", ["const:aed880:8", "const:4:8"]]
+ 00aed948 ["INT_ADD", "register:40f0:8", ["const:aed948:8", "const:4:8"]]
~~~


### [`00aed8a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed8a8.md) → [`00aed970`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aed9f8",
      "incomplete_value": true,
      "site": "00aed9f8",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed930",
      "incomplete_value": true,
      "site": "00aed930",
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
            "const:938:8"
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
      "definition_site": "00aed9a4",
      "incomplete_value": true,
      "site": "00aed9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed8dc",
      "incomplete_value": true,
      "site": "00aed8e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
        "010a0938",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0938",
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
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed8bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:938:8"]]
+ 00aed984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
- 00aed8dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:930:8"]]
+ 00aed9a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9f0:8"]]
- 00aed8e8 ["INT_ADD", "register:40f0:8", ["const:aed8e8:8", "const:4:8"]]
+ 00aed9b0 ["INT_ADD", "register:40f0:8", ["const:aed9b0:8", "const:4:8"]]
~~~


### [`00aed944`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md) → [`00aeda0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aeda48",
      "incomplete_value": true,
      "site": "00aeda48",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed980",
      "incomplete_value": true,
      "site": "00aed980",
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
            "const:938:8"
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
      "definition_site": "00aeda98",
      "incomplete_value": true,
      "site": "00aeda98",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed9d0",
      "incomplete_value": true,
      "site": "00aed9d0",
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
            "const:930:8"
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
      "definition_site": "00aeda24",
      "incomplete_value": true,
      "site": "00aeda24",
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
      "definition_site": "00aed95c",
      "incomplete_value": true,
      "site": "00aed95c",
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0938",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed958 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00aeda20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aed964 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:938:8"]]
+ 00aeda2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
- 00aed97c ["INT_ADD", "register:40f0:8", ["const:aed97c:8", "const:4:8"]]
+ 00aeda44 ["INT_ADD", "register:40f0:8", ["const:aeda44:8", "const:4:8"]]
~~~


### [`00aed9e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md) → [`00aedaac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedaec",
      "incomplete_value": true,
      "site": "00aedaec",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeda24",
      "incomplete_value": true,
      "site": "00aeda24",
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
            "const:930:8"
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
      "definition_site": "00aedac8",
      "incomplete_value": true,
      "site": "00aedac8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aeda00",
      "incomplete_value": true,
      "site": "00aeda00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedad0",
      "incomplete_value": false,
      "site": "00aedae4",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeda08",
      "incomplete_value": false,
      "site": "00aeda1c",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aed9f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00aedac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aeda00 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aedac8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aeda08 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aedad0 ["COPY", "tmp:0:8", ["const:c0a:8"]]
~~~


### [`00aeda54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda54.md) → [`00aedb1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedb38",
      "incomplete_value": false,
      "site": "00aedb3c",
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
    "old": {
      "definition_site": "00aeda70",
      "incomplete_value": false,
      "site": "00aeda74",
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
      "definition_site": "00aedb48",
      "incomplete_value": true,
      "site": "00aedb54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeda80",
      "incomplete_value": true,
      "site": "00aeda8c",
      "value": [
        "LOAD",
        "8",
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
        "010a0940",
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
        "010a0a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aeda70 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aedb38 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeda74 ["INT_ADD", "register:40f0:8", ["const:aeda74:8", "const:4:8"]]
+ 00aedb3c ["INT_ADD", "register:40f0:8", ["const:aedb3c:8", "const:4:8"]]
- 00aeda7c ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00aedb44 ["COPY", "tmp:0:8", ["const:a00:8"]]
~~~


### [`00aeda90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda90.md) → [`00aedb58`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedb98",
      "incomplete_value": true,
      "site": "00aedb98",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedad0",
      "incomplete_value": true,
      "site": "00aedad0",
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
            "const:930:8"
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
      "definition_site": "00aedb74",
      "incomplete_value": true,
      "site": "00aedb74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedaac",
      "incomplete_value": true,
      "site": "00aedaac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedb7c",
      "incomplete_value": false,
      "site": "00aedb90",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedab4",
      "incomplete_value": true,
      "site": "00aedac8",
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
            "const:c9e:8"
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
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0930",
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
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedaa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00aedb6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00aedaac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aedb74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aedab4 ["COPY", "tmp:0:8", ["const:c9e:8"]]
+ 00aedb7c ["COPY", "tmp:0:8", ["const:c0a:8"]]
~~~


### [`00aedb00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md) → [`00aedbc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedbe4",
      "incomplete_value": false,
      "site": "00aedbe8",
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
    "old": {
      "definition_site": "00aedb1c",
      "incomplete_value": false,
      "site": "00aedb20",
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
      "definition_site": "00aedbf4",
      "incomplete_value": true,
      "site": "00aedc00",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aedb2c",
      "incomplete_value": true,
      "site": "00aedb38",
      "value": [
        "LOAD",
        "8",
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
        "010a0958",
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
        "010a0a18",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedb1c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aedbe4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aedb20 ["INT_ADD", "register:40f0:8", ["const:aedb20:8", "const:4:8"]]
+ 00aedbe8 ["INT_ADD", "register:40f0:8", ["const:aedbe8:8", "const:4:8"]]
- 00aedb28 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00aedbf0 ["COPY", "tmp:0:8", ["const:a18:8"]]
~~~


### [`00aedb3c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb3c.md) → [`00aedc04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedc30",
      "incomplete_value": true,
      "site": "00aedc30",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb68",
      "incomplete_value": true,
      "site": "00aedb68",
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
            "const:960:8"
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
      "definition_site": "00aedc18",
      "incomplete_value": true,
      "site": "00aedc18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedb50",
      "incomplete_value": true,
      "site": "00aedb50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedc24",
      "incomplete_value": false,
      "site": "00aedc28",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb5c",
      "incomplete_value": false,
      "site": "00aedb60",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedb4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00aedc14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedb5c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aedc24 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aedb60 ["INT_ADD", "register:40f0:8", ["const:aedb60:8", "const:4:8"]]
+ 00aedc28 ["INT_ADD", "register:40f0:8", ["const:aedc28:8", "const:4:8"]]
~~~


### [`00aedb7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb7c.md) → [`00aedc44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedc70",
      "incomplete_value": true,
      "site": "00aedc70",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedba8",
      "incomplete_value": true,
      "site": "00aedba8",
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
            "const:960:8"
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
      "definition_site": "00aedc58",
      "incomplete_value": true,
      "site": "00aedc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedb90",
      "incomplete_value": true,
      "site": "00aedb90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedc60",
      "incomplete_value": false,
      "site": "00aedc68",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb98",
      "incomplete_value": false,
      "site": "00aedba0",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedb8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00aedc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedb98 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aedc60 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aedba0 ["INT_ADD", "register:40f0:8", ["const:aedba0:8", "const:4:8"]]
+ 00aedc68 ["INT_ADD", "register:40f0:8", ["const:aedc68:8", "const:4:8"]]
~~~


### [`00aedbbc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedbbc.md) → [`00aedc84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedcb4",
      "incomplete_value": true,
      "site": "00aedcb4",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedbec",
      "incomplete_value": true,
      "site": "00aedbec",
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
            "const:960:8"
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
      "definition_site": "00aedc98",
      "incomplete_value": true,
      "site": "00aedc98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedbd0",
      "incomplete_value": true,
      "site": "00aedbd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedca4",
      "incomplete_value": false,
      "site": "00aedcac",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedbdc",
      "incomplete_value": false,
      "site": "00aedbe4",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00aedc94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedbdc ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aedca4 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aedbe4 ["INT_ADD", "register:40f0:8", ["const:aedbe4:8", "const:4:8"]]
+ 00aedcac ["INT_ADD", "register:40f0:8", ["const:aedcac:8", "const:4:8"]]
~~~


### [`00aedc00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md) → [`00aedcc8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedcf8",
      "incomplete_value": true,
      "site": "00aedcf8",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc30",
      "incomplete_value": true,
      "site": "00aedc30",
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
            "const:960:8"
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
      "definition_site": "00aedcdc",
      "incomplete_value": true,
      "site": "00aedcdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedc14",
      "incomplete_value": true,
      "site": "00aedc14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedce4",
      "incomplete_value": false,
      "site": "00aedcf0",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc1c",
      "incomplete_value": false,
      "site": "00aedc28",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
+ 00aedcd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00aedc1c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aedce4 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aedc28 ["INT_ADD", "register:40f0:8", ["const:aedc28:8", "const:4:8"]]
+ 00aedcf0 ["INT_ADD", "register:40f0:8", ["const:aedcf0:8", "const:4:8"]]
~~~


### [`00aedc50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc50.md) → [`00aedd18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aedda0",
      "incomplete_value": true,
      "site": "00aedda0",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedcd8",
      "incomplete_value": true,
      "site": "00aedcd8",
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
            "const:968:8"
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
      "definition_site": "00aedd4c",
      "incomplete_value": true,
      "site": "00aedd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc84",
      "incomplete_value": true,
      "site": "00aedc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:960:8"
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
        "010a0968",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0968",
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
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedc64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
+ 00aedd2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a28:8"]]
- 00aedc84 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:960:8"]]
+ 00aedd4c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a20:8"]]
- 00aedc90 ["INT_ADD", "register:40f0:8", ["const:aedc90:8", "const:4:8"]]
+ 00aedd58 ["INT_ADD", "register:40f0:8", ["const:aedd58:8", "const:4:8"]]
~~~


### [`00aedcec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md) → [`00aeddb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aeddf0",
      "incomplete_value": true,
      "site": "00aeddf0",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedd28",
      "incomplete_value": true,
      "site": "00aedd28",
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
            "const:968:8"
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
      "definition_site": "00aede40",
      "incomplete_value": true,
      "site": "00aede40",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedd78",
      "incomplete_value": true,
      "site": "00aedd78",
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
            "const:960:8"
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
      "definition_site": "00aeddcc",
      "incomplete_value": true,
      "site": "00aeddcc",
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
      "definition_site": "00aedd04",
      "incomplete_value": true,
      "site": "00aedd04",
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0968",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedd00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00aeddc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aedd0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
+ 00aeddd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a28:8"]]
- 00aedd24 ["INT_ADD", "register:40f0:8", ["const:aedd24:8", "const:4:8"]]
+ 00aeddec ["INT_ADD", "register:40f0:8", ["const:aeddec:8", "const:4:8"]]
~~~


### [`00aedd8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedd8c.md) → [`00aede54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aede94",
      "incomplete_value": true,
      "site": "00aede94",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeddcc",
      "incomplete_value": true,
      "site": "00aeddcc",
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
            "const:960:8"
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
      "definition_site": "00aede70",
      "incomplete_value": true,
      "site": "00aede70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedda8",
      "incomplete_value": true,
      "site": "00aedda8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aede78",
      "incomplete_value": false,
      "site": "00aede8c",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeddb0",
      "incomplete_value": false,
      "site": "00aeddc4",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedda0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00aede68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aeddb0 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aede78 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aeddc4 ["INT_ADD", "register:40f0:8", ["const:aeddc4:8", "const:4:8"]]
+ 00aede8c ["INT_ADD", "register:40f0:8", ["const:aede8c:8", "const:4:8"]]
~~~


### [`00aeddfc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md) → [`00aedec4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedee0",
      "incomplete_value": false,
      "site": "00aedee4",
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
    "old": {
      "definition_site": "00aede18",
      "incomplete_value": false,
      "site": "00aede1c",
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
      "definition_site": "00aedef0",
      "incomplete_value": true,
      "site": "00aedefc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aede28",
      "incomplete_value": true,
      "site": "00aede34",
      "value": [
        "LOAD",
        "8",
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
        "010a0970",
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
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aede18 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aedee0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aede1c ["INT_ADD", "register:40f0:8", ["const:aede1c:8", "const:4:8"]]
+ 00aedee4 ["INT_ADD", "register:40f0:8", ["const:aedee4:8", "const:4:8"]]
- 00aede24 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00aedeec ["COPY", "tmp:0:8", ["const:a30:8"]]
~~~


### [`00aede38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aede38.md) → [`00aedf00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedf40",
      "incomplete_value": true,
      "site": "00aedf40",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede78",
      "incomplete_value": true,
      "site": "00aede78",
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
            "const:960:8"
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
      "definition_site": "00aedf1c",
      "incomplete_value": true,
      "site": "00aedf1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aede54",
      "incomplete_value": true,
      "site": "00aede54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedf24",
      "incomplete_value": false,
      "site": "00aedf38",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede5c",
      "incomplete_value": false,
      "site": "00aede70",
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
            "const:4f8:8"
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
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0960",
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
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aede4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
+ 00aedf14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00aede5c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00aedf24 ["COPY", "tmp:0:8", ["const:585:8"]]
- 00aede70 ["INT_ADD", "register:40f0:8", ["const:aede70:8", "const:4:8"]]
+ 00aedf38 ["INT_ADD", "register:40f0:8", ["const:aedf38:8", "const:4:8"]]
~~~


### [`00aedea8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedea8.md) → [`00aedf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedf8c",
      "incomplete_value": false,
      "site": "00aedf90",
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
    "old": {
      "definition_site": "00aedec4",
      "incomplete_value": false,
      "site": "00aedec8",
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
      "definition_site": "00aedf9c",
      "incomplete_value": true,
      "site": "00aedfa8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeded4",
      "incomplete_value": true,
      "site": "00aedee0",
      "value": [
        "LOAD",
        "8",
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
        "010a0980",
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
        "010a0a40",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedec4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aedf8c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aedec8 ["INT_ADD", "register:40f0:8", ["const:aedec8:8", "const:4:8"]]
+ 00aedf90 ["INT_ADD", "register:40f0:8", ["const:aedf90:8", "const:4:8"]]
- 00aeded0 ["COPY", "tmp:0:8", ["const:980:8"]]
+ 00aedf98 ["COPY", "tmp:0:8", ["const:a40:8"]]
~~~


### [`00aedee4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md) → [`00aedfac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aedfd8",
      "incomplete_value": true,
      "site": "00aedfd8",
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
    "old": {
      "definition_site": "00aedf10",
      "incomplete_value": true,
      "site": "00aedf10",
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
            "const:988:8"
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
      "definition_site": "00aedfc0",
      "incomplete_value": true,
      "site": "00aedfc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedef8",
      "incomplete_value": true,
      "site": "00aedef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedfcc",
      "incomplete_value": false,
      "site": "00aedfd0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf04",
      "incomplete_value": false,
      "site": "00aedf08",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aedfbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedf04 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aedfcc ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aedf08 ["INT_ADD", "register:40f0:8", ["const:aedf08:8", "const:4:8"]]
+ 00aedfd0 ["INT_ADD", "register:40f0:8", ["const:aedfd0:8", "const:4:8"]]
~~~


### [`00aedf24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md) → [`00aedfec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee018",
      "incomplete_value": true,
      "site": "00aee018",
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
    "old": {
      "definition_site": "00aedf50",
      "incomplete_value": true,
      "site": "00aedf50",
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
            "const:988:8"
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
      "definition_site": "00aee000",
      "incomplete_value": true,
      "site": "00aee000",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedf38",
      "incomplete_value": true,
      "site": "00aedf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee008",
      "incomplete_value": false,
      "site": "00aee010",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf40",
      "incomplete_value": false,
      "site": "00aedf48",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aedffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedf40 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aee008 ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aedf48 ["INT_ADD", "register:40f0:8", ["const:aedf48:8", "const:4:8"]]
+ 00aee010 ["INT_ADD", "register:40f0:8", ["const:aee010:8", "const:4:8"]]
~~~


### [`00aedf64`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf64.md) → [`00aee02c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee05c",
      "incomplete_value": true,
      "site": "00aee05c",
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
    "old": {
      "definition_site": "00aedf94",
      "incomplete_value": true,
      "site": "00aedf94",
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
            "const:988:8"
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
      "definition_site": "00aee040",
      "incomplete_value": true,
      "site": "00aee040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedf78",
      "incomplete_value": true,
      "site": "00aedf78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee04c",
      "incomplete_value": false,
      "site": "00aee054",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf84",
      "incomplete_value": false,
      "site": "00aedf8c",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedf74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aee03c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedf84 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aee04c ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aedf8c ["INT_ADD", "register:40f0:8", ["const:aedf8c:8", "const:4:8"]]
+ 00aee054 ["INT_ADD", "register:40f0:8", ["const:aee054:8", "const:4:8"]]
~~~


### [`00aedfa8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedfa8.md) → [`00aee070`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee0a0",
      "incomplete_value": true,
      "site": "00aee0a0",
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
    "old": {
      "definition_site": "00aedfd8",
      "incomplete_value": true,
      "site": "00aedfd8",
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
            "const:988:8"
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
      "definition_site": "00aee084",
      "incomplete_value": true,
      "site": "00aee084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aedfbc",
      "incomplete_value": true,
      "site": "00aedfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee08c",
      "incomplete_value": false,
      "site": "00aee098",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedfc4",
      "incomplete_value": false,
      "site": "00aedfd0",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aedfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aee080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
- 00aedfc4 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aee08c ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aedfd0 ["INT_ADD", "register:40f0:8", ["const:aedfd0:8", "const:4:8"]]
+ 00aee098 ["INT_ADD", "register:40f0:8", ["const:aee098:8", "const:4:8"]]
~~~


### [`00aedff8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedff8.md) → [`00aee0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md) _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00aee148",
      "incomplete_value": true,
      "site": "00aee148",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee080",
      "incomplete_value": true,
      "site": "00aee080",
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
            "const:990:8"
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
      "definition_site": "00aee0f4",
      "incomplete_value": true,
      "site": "00aee100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee02c",
      "incomplete_value": true,
      "site": "00aee038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0990",
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
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee00c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
+ 00aee0d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
- 00aee02c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:988:8"]]
+ 00aee0f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a48:8"]]
- 00aee038 ["INT_ADD", "register:40f0:8", ["const:aee038:8", "const:4:8"]]
+ 00aee100 ["INT_ADD", "register:40f0:8", ["const:aee100:8", "const:4:8"]]
~~~


### [`00aee094`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee094.md) → [`00aee15c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md) _ZN8firebase4util6object12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00aee198",
      "incomplete_value": true,
      "site": "00aee198",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee0d0",
      "incomplete_value": true,
      "site": "00aee0d0",
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
            "const:990:8"
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
      "definition_site": "00aee1e8",
      "incomplete_value": true,
      "site": "00aee1e8",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee120",
      "incomplete_value": true,
      "site": "00aee120",
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
            "const:988:8"
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
      "definition_site": "00aee174",
      "incomplete_value": true,
      "site": "00aee174",
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
      "definition_site": "00aee0ac",
      "incomplete_value": true,
      "site": "00aee0ac",
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0990",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee0a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aee170 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee0b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
+ 00aee17c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
- 00aee0cc ["INT_ADD", "register:40f0:8", ["const:aee0cc:8", "const:4:8"]]
+ 00aee194 ["INT_ADD", "register:40f0:8", ["const:aee194:8", "const:4:8"]]
~~~


### [`00aee134`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md) → [`00aee1fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee23c",
      "incomplete_value": true,
      "site": "00aee23c",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee174",
      "incomplete_value": true,
      "site": "00aee174",
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
            "const:988:8"
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
      "definition_site": "00aee218",
      "incomplete_value": true,
      "site": "00aee218",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee150",
      "incomplete_value": true,
      "site": "00aee150",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee220",
      "incomplete_value": false,
      "site": "00aee234",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee158",
      "incomplete_value": false,
      "site": "00aee16c",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee148 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aee210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee158 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aee220 ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aee16c ["INT_ADD", "register:40f0:8", ["const:aee16c:8", "const:4:8"]]
+ 00aee234 ["INT_ADD", "register:40f0:8", ["const:aee234:8", "const:4:8"]]
~~~


### [`00aee1a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1a4.md) → [`00aee26c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md) _ZN8firebase4util6object11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee288",
      "incomplete_value": false,
      "site": "00aee28c",
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
    "old": {
      "definition_site": "00aee1c0",
      "incomplete_value": false,
      "site": "00aee1c4",
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
      "definition_site": "00aee298",
      "incomplete_value": true,
      "site": "00aee2a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aee1d0",
      "incomplete_value": true,
      "site": "00aee1dc",
      "value": [
        "LOAD",
        "8",
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
        "010a0998",
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
        "010a0a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee1c0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aee288 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aee1c4 ["INT_ADD", "register:40f0:8", ["const:aee1c4:8", "const:4:8"]]
+ 00aee28c ["INT_ADD", "register:40f0:8", ["const:aee28c:8", "const:4:8"]]
- 00aee1cc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00aee294 ["COPY", "tmp:0:8", ["const:a58:8"]]
~~~


### [`00aee1e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md) → [`00aee2a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee2e8",
      "incomplete_value": true,
      "site": "00aee2e8",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee220",
      "incomplete_value": true,
      "site": "00aee220",
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
            "const:988:8"
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
      "definition_site": "00aee2c4",
      "incomplete_value": true,
      "site": "00aee2c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee1fc",
      "incomplete_value": true,
      "site": "00aee1fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00aee2cc",
      "incomplete_value": false,
      "site": "00aee2e0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee204",
      "incomplete_value": false,
      "site": "00aee218",
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
            "const:cdf:8"
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
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0988",
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
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee1f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aee2bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
- 00aee204 ["COPY", "tmp:0:8", ["const:cdf:8"]]
+ 00aee2cc ["COPY", "tmp:0:8", ["const:d6c:8"]]
- 00aee218 ["INT_ADD", "register:40f0:8", ["const:aee218:8", "const:4:8"]]
+ 00aee2e0 ["INT_ADD", "register:40f0:8", ["const:aee2e0:8", "const:4:8"]]
~~~


### [`00aee250`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee250.md) → [`00aee318`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md) _ZN8firebase4util6object10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee334",
      "incomplete_value": false,
      "site": "00aee338",
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
    "old": {
      "definition_site": "00aee26c",
      "incomplete_value": false,
      "site": "00aee270",
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
      "definition_site": "00aee344",
      "incomplete_value": true,
      "site": "00aee350",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aee27c",
      "incomplete_value": true,
      "site": "00aee288",
      "value": [
        "LOAD",
        "8",
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
        "010a09a0",
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
        "010a0a60",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee26c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aee334 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aee270 ["INT_ADD", "register:40f0:8", ["const:aee270:8", "const:4:8"]]
+ 00aee338 ["INT_ADD", "register:40f0:8", ["const:aee338:8", "const:4:8"]]
- 00aee278 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00aee340 ["COPY", "tmp:0:8", ["const:a60:8"]]
~~~


### [`00aee28c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md) → [`00aee354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde570`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde570.md) · 呼出先 9件 [`0047495c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00aee7fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md) [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bde620`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde620.md) · 呼出先 9件 [`0047495c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00aee8c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 11件, `store_condition` 2件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee380",
      "incomplete_value": false,
      "site": "00aee380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee2b8",
      "incomplete_value": false,
      "site": "00aee2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "definition_site": "00aee3c4",
      "incomplete_value": true,
      "site": "00aee3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee2fc",
      "incomplete_value": true,
      "site": "00aee2fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee41c",
      "incomplete_value": true,
      "site": "00aee41c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee354",
      "incomplete_value": true,
      "site": "00aee354",
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
            "const:268:8"
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
      32,
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee2ac ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:9a8:8"]]
+ 00aee374 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:a68:8"]]
- 00aee2b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:9a8:8"]]
+ 00aee380 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:a68:8"]]
- 00aee2d0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:408:8"]]
+ 00aee398 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:4c8:8"]]
~~~


### [`00aee64c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee64c.md) → [`00aee714`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde560`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde560.md) · 呼出先 2件 [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde610`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde610.md) · 呼出先 2件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee748",
      "incomplete_value": true,
      "site": "00aee748",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee680",
      "incomplete_value": true,
      "site": "00aee680",
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
            "const:9a8:8"
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
      "definition_site": "00aee778",
      "incomplete_value": true,
      "site": "00aee778",
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
    "old": {
      "definition_site": "00aee6b0",
      "incomplete_value": true,
      "site": "00aee6b0",
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
            "const:410:8"
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
      "definition_site": "00aee7c8",
      "incomplete_value": true,
      "site": "00aee7c8",
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
    "old": {
      "definition_site": "00aee700",
      "incomplete_value": true,
      "site": "00aee700",
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
            "const:408:8"
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
      20,
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac13c",
        null,
        "string"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac133",
        null,
        "string"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee660 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aee728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
- 00aee670 ["COPY", "tmp:0:8", ["const:13c:8"]]
+ 00aee738 ["COPY", "tmp:0:8", ["const:133:8"]]
- 00aee674 ["INT_ADD", "register:40f0:8", ["const:aee674:8", "const:4:8"]]
+ 00aee73c ["INT_ADD", "register:40f0:8", ["const:aee73c:8", "const:4:8"]]
~~~


### [`00aee7fc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md) → [`00aee8c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) FUN_00aee8c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aee28c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md) · 呼出先 1件 [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00aee354`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) · 呼出先 1件 [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee940",
      "incomplete_value": true,
      "site": "00aee940",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee878",
      "incomplete_value": true,
      "site": "00aee878",
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
            "const:9b0:8"
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
      "definition_site": "00aee8e8",
      "incomplete_value": true,
      "site": "00aee8ec",
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
      "definition_site": "00aee820",
      "incomplete_value": true,
      "site": "00aee824",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00aee914",
      "incomplete_value": true,
      "site": "00aee914",
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
      "definition_site": "00aee84c",
      "incomplete_value": true,
      "site": "00aee84c",
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
        "010a09b0",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined8"
      ]
    ],
    [
      124,
      "WRITE",
      [
        "storage",
        "010a09b0",
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
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      124,
      "WRITE",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee810 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aee8d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
- 00aee83c ["INT_ADD", "register:40f0:8", ["const:aee83c:8", "const:4:8"]]
+ 00aee904 ["INT_ADD", "register:40f0:8", ["const:aee904:8", "const:4:8"]]
- 00aee840 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aee908 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
~~~


### [`00aee884`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) → [`00aee94c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf20.md) · 呼出先 13件 [`00aef908`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) [`00af0b2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bddfd0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md) · 呼出先 13件 [`00aef9d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00af0bf4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 164件, `call_target` 2件, `store_condition` 3件, `store_destination` 46件

アドレスに依存する影響 `branch_value` 37件, `store_condition` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee984",
      "incomplete_value": true,
      "site": "00aee984",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee8bc",
      "incomplete_value": true,
      "site": "00aee8bc",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee9cc",
      "incomplete_value": true,
      "site": "00aee9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee904",
      "incomplete_value": true,
      "site": "00aee904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "definition_site": "00aeea24",
      "incomplete_value": true,
      "site": "00aeea24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee95c",
      "incomplete_value": true,
      "site": "00aee95c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:4a0:8"
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
      44,
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      56,
      "WRITE",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "010a0470",
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
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      56,
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aee8b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
+ 00aee978 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00aee8bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
+ 00aee984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
- 00aee8d0 ["INT_ADD", "register:40f0:8", ["const:aee8d0:8", "const:4:8"]]
+ 00aee998 ["INT_ADD", "register:40f0:8", ["const:aee998:8", "const:4:8"]]
~~~


### [`00aef908`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) → [`00aef9d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) FUN_00aef9d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aee884`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) [`00af0b2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) · 呼出先 1件 [`00bde400`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde400.md)
- 新版 呼出元 2件 [`00aee94c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00af0bf4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) · 呼出先 1件 [`00bde4b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 37件, `store_destination` 75件

アドレスに依存する影響 `branch_value` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aefa0c",
      "incomplete_value": true,
      "site": "00aefa0c",
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
    "old": {
      "definition_site": "00aef944",
      "incomplete_value": true,
      "site": "00aef944",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00aefa5c",
      "incomplete_value": true,
      "site": "00aefa5c",
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
    "old": {
      "definition_site": "00aef994",
      "incomplete_value": true,
      "site": "00aef994",
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
            "const:4a0:8"
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
      "definition_site": "00aefa88",
      "incomplete_value": true,
      "site": "00aefa88",
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
    "old": {
      "definition_site": "00aef9c0",
      "incomplete_value": true,
      "site": "00aef9c0",
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
            "const:478:8"
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
      20,
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a04a8",
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
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      36,
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
  ]
}
~~~


~~~diff
- 00aef91c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
+ 00aef9e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00aef92c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4a8:8"]]
+ 00aef9f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
- 00aef940 ["INT_ADD", "register:40f0:8", ["const:aef940:8", "const:4:8"]]
+ 00aefa08 ["INT_ADD", "register:40f0:8", ["const:aefa08:8", "const:4:8"]]
~~~


### [`00af0b2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) → [`00af0bf4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) _ZN8firebase4util9TerminateEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aee884`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) [`00bde050`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde050.md) · 呼出先 10件 [`00aef908`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddf80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md) [`00bde080`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde2c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2c0.md)
- 新版 呼出元 2件 [`00aee94c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00bde100`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) · 呼出先 10件 [`00aef9d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde030`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde370`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af0c28",
      "incomplete_value": true,
      "site": "00af0c28",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0b60",
      "incomplete_value": true,
      "site": "00af0b60",
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
            "const:9b8:8"
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
      "definition_site": "00af0c8c",
      "incomplete_value": true,
      "site": "00af0c8c",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0bc4",
      "incomplete_value": true,
      "site": "00af0bc4",
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
            "const:9c0:8"
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
      "definition_site": "00af0c48",
      "incomplete_value": true,
      "site": "00af0c48",
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
      "definition_site": "00af0b80",
      "incomplete_value": true,
      "site": "00af0b80",
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
      20,
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      52,
      "WRITE",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      52,
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af0b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
+ 00af0c08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a78:8"]]
- 00af0b54 ["INT_ADD", "register:40f0:8", ["const:af0b54:8", "const:4:8"]]
+ 00af0c1c ["INT_ADD", "register:40f0:8", ["const:af0c1c:8", "const:4:8"]]
- 00af0b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
+ 00af0c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a78:8"]]
~~~


### [`00af0c44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0c44.md) → [`00af0d0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bde420`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde420.md) · 呼出先 6件 [`0047495c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00551e14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00bde4d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4d0.md) · 呼出先 6件 [`0047495c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00551e14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 26件, `call_target` 11件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00af0ea0",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00af0dd4",
      "incomplete_value": true,
      "site": "00af0dd8",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af0f44",
      "incomplete_value": true,
      "site": "00af0f44",
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
      "definition_site": "00af0e7c",
      "incomplete_value": true,
      "site": "00af0e7c",
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af1094",
      "incomplete_value": true,
      "site": "00af1094",
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
    "old": {
      "definition_site": "00af0fcc",
      "incomplete_value": true,
      "site": "00af0fcc",
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
    "ordinal": 11,
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
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined8"
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002a2ce2",
        null,
        "string"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "010a06d0",
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
        "010a04e0",
        null,
        "undefined8"
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002a2cdb",
        null,
        "string"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00af0c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 00af0d30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4e0:8"]]
- 00af0c70 ["INT_ADD", "register:40f0:8", ["const:af0c70:8", "const:4:8"]]
+ 00af0d38 ["INT_ADD", "register:40f0:8", ["const:af0d38:8", "const:4:8"]]
- 00af0c84 ["INT_ADD", "register:40f0:8", ["const:af0c84:8", "const:4:8"]]
+ 00af0d4c ["INT_ADD", "register:40f0:8", ["const:af0d4c:8", "const:4:8"]]
~~~


