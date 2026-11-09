# v15.7.4 → v16.0.0 · 最優先の変更候補 (71)

[一覧の目次](README.md)

### [`00ae8160`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md) → [`00b47ee4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b47f14",
      "incomplete_value": true,
      "site": "00b47f14",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47ef8",
      "incomplete_value": true,
      "site": "00b47ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47f04",
      "incomplete_value": false,
      "site": "00b47f0c",
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
      48,
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
      48,
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
- 00ae816c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00b47ef0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae8174 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8178 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b47ef8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47efc ["COPY", "register:4018:8", ["const:2b9000:8"]]
- 00ae8180 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b47f04 ["COPY", "tmp:0:8", ["const:95b:8"]]
~~~


### [`00ae81a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md) → [`00b47f28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47f58",
      "incomplete_value": true,
      "site": "00b47f58",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47f3c",
      "incomplete_value": true,
      "site": "00b47f3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47f48",
      "incomplete_value": false,
      "site": "00b47f50",
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
      48,
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
- 00ae81b0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae81b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00b47f34 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47f38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae81b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae81bc ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae81c0 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b47f3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b47f40 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00b47f44 ["COPY", "tmp:0:8", ["const:95b:8"]]
- 00ae81cc ["INT_ADD", "register:40f0:8", ["const:ae81cc:8", "const:4:8"]]
+ 00b47f50 ["INT_ADD", "register:40f0:8", ["const:b47f50:8", "const:4:8"]]
~~~


### [`00ae81f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md) → [`00b47f78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48000",
      "incomplete_value": true,
      "site": "00b48000",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47fac",
      "incomplete_value": true,
      "site": "00b47fb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8204 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8208 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
+ 00b47f88 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47f8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
- 00ae821c ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b47fa0 ["COPY", "register:4048:8", ["const:1125000:8"]]
- 00ae8228 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5e8:8"]]
+ 00b47fac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4a8:8"]]
~~~


### [`00ae8290`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md) → [`00b48014`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b48050",
      "incomplete_value": true,
      "site": "00b48050",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b480a0",
      "incomplete_value": true,
      "site": "00b480a0",
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
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4802c",
      "incomplete_value": true,
      "site": "00b4802c",
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
  ],
  "added": [
    [
      20,
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
      "READ",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae82a0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae82a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00b48024 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48028 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae82ac ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae82b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
+ 00b48030 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48034 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
- 00ae82c8 ["INT_ADD", "register:40f0:8", ["const:ae82c8:8", "const:4:8"]]
+ 00b4804c ["INT_ADD", "register:40f0:8", ["const:b4804c:8", "const:4:8"]]
~~~


### [`00ae8330`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md) → [`00b480b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b480f4",
      "incomplete_value": true,
      "site": "00b480f4",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b480d0",
      "incomplete_value": true,
      "site": "00b480d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b480d8",
      "incomplete_value": false,
      "site": "00b480ec",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      64,
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
- 00ae833c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b480c0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00b480c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae8350 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae8354 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b480d4 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00b480d8 ["COPY", "tmp:0:8", ["const:95b:8"]]
~~~


### [`00ae83a0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md) → [`00b48124`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48124.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bde110`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5ab90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48140",
      "incomplete_value": true,
      "site": "00b48144",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b48150",
      "incomplete_value": true,
      "site": "00b4815c",
      "value": [
        "LOAD",
        "8",
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
        "010a05f8",
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
        "011254b8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae83b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae83b8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae83bc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b48138 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4813c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b48140 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae83c0 ["INT_ADD", "register:40f0:8", ["const:ae83c0:8", "const:4:8"]]
+ 00b48144 ["INT_ADD", "register:40f0:8", ["const:b48144:8", "const:4:8"]]
- 00ae83c4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae83c8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00b48148 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4814c ["COPY", "tmp:0:8", ["const:4b8:8"]]
~~~


### [`00ae83dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md) → [`00b48160`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b481a0",
      "incomplete_value": true,
      "site": "00b481a0",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4817c",
      "incomplete_value": true,
      "site": "00b4817c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae8404",
      "incomplete_value": true,
      "site": "00ae8414",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      64,
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
- 00ae83e8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4816c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae83f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00b48174 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae83fc ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae8400 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00b48180 ["COPY", "register:4018:8", ["const:2b9000:8"]]
+ 00b48184 ["COPY", "tmp:0:8", ["const:95b:8"]]
~~~


### [`00ae844c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md) → [`00b481d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b481e4",
      "incomplete_value": true,
      "site": "00b481e4",
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
      "definition_site": "00ae8460",
      "incomplete_value": true,
      "site": "00ae8460",
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
      "definition_site": "00b481ec",
      "incomplete_value": false,
      "site": "00b481f0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b481fc",
      "incomplete_value": true,
      "site": "00b48208",
      "value": [
        "LOAD",
        "8",
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
        "01125500",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8464 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae8468 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b481e8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b481ec ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae846c ["INT_ADD", "register:40f0:8", ["const:ae846c:8", "const:4:8"]]
+ 00b481f0 ["INT_ADD", "register:40f0:8", ["const:b481f0:8", "const:4:8"]]
- 00ae8470 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8474 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00b481f4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b481f8 ["COPY", "tmp:0:8", ["const:500:8"]]
~~~


### [`00ae8488`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md) → [`00b4820c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b48238",
      "incomplete_value": true,
      "site": "00b48238",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48220",
      "incomplete_value": true,
      "site": "00b48220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4822c",
      "incomplete_value": false,
      "site": "00b48230",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8494 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8498 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00b48218 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4821c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae84a4 ["COPY", "register:4018:8", ["const:296000:8"]]
- 00ae84a8 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b48228 ["COPY", "register:4018:8", ["const:2a5000:8"]]
+ 00b4822c ["COPY", "tmp:0:8", ["const:f6b:8"]]
- 00ae84ac ["INT_ADD", "register:40f0:8", ["const:ae84ac:8", "const:4:8"]]
+ 00b48230 ["INT_ADD", "register:40f0:8", ["const:b48230:8", "const:4:8"]]
~~~


### [`00ae84c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md) → [`00b4824c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b48278",
      "incomplete_value": true,
      "site": "00b48278",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48260",
      "incomplete_value": true,
      "site": "00b48260",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48268",
      "incomplete_value": false,
      "site": "00b48270",
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
            "const:f6b:8"
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
            "const:459:8"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae84d4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae84d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00b48258 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4825c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae84e0 ["COPY", "register:4018:8", ["const:296000:8"]]
- 00ae84e4 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b48264 ["COPY", "register:4018:8", ["const:2a5000:8"]]
+ 00b48268 ["COPY", "tmp:0:8", ["const:f6b:8"]]
- 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
+ 00b48270 ["INT_ADD", "register:40f0:8", ["const:b48270:8", "const:4:8"]]
~~~


### [`00ae8508`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md) → [`00b4828c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b482bc",
      "incomplete_value": true,
      "site": "00b482bc",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b482a0",
      "incomplete_value": true,
      "site": "00b482a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b482ac",
      "incomplete_value": false,
      "site": "00b482b4",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8514 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00b48298 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4829c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae8520 ["COPY", "register:4018:8", ["const:296000:8"]]
+ 00b482a4 ["COPY", "register:4018:8", ["const:2a5000:8"]]
- 00ae8528 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b482ac ["COPY", "tmp:0:8", ["const:f6b:8"]]
~~~


### [`00ae854c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md) → [`00b482d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b482d4",
      "incomplete_value": true,
      "site": "00b482d4",
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
      "definition_site": "00ae8550",
      "incomplete_value": true,
      "site": "00ae8550",
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
      "definition_site": "00b482d4",
      "incomplete_value": true,
      "site": "00b482d4",
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
      "definition_site": "00ae8550",
      "incomplete_value": true,
      "site": "00ae8550",
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
      "definition_site": "00b48300",
      "incomplete_value": true,
      "site": "00b48300",
      "value": [
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8558 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae855c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00b482dc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b482e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae8560 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8564 ["COPY", "register:4018:8", ["const:296000:8"]]
- 00ae8568 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b482e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b482e8 ["COPY", "register:4018:8", ["const:2a5000:8"]]
+ 00b482ec ["COPY", "tmp:0:8", ["const:f6b:8"]]
- 00ae8574 ["INT_ADD", "register:40f0:8", ["const:ae8574:8", "const:4:8"]]
+ 00b482f8 ["INT_ADD", "register:40f0:8", ["const:b482f8:8", "const:4:8"]]
~~~


### [`00ae859c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae859c.md) → [`00b48320`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48320.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b483a8",
      "incomplete_value": true,
      "site": "00b483a8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b48360",
      "incomplete_value": true,
      "site": "00b48360",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae85dc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48354",
      "incomplete_value": true,
      "site": "00b48360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae85ac ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae85b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
+ 00b48330 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48334 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00ae85b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b48338 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae85bc ["BRANCH", null, ["local:b9:8"]]
+ 00b48340 ["BRANCH", null, ["local:b5:8"]]
~~~


### [`00ae8638`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md) → [`00b483bc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 4件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b483f8",
      "incomplete_value": true,
      "site": "00b483f8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48448",
      "incomplete_value": true,
      "site": "00b48448",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b483d4",
      "incomplete_value": true,
      "site": "00b483d4",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8648 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae864c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00b483cc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b483d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae8650 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00ae8654 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8658 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:650:8"]]
+ 00b483d4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b483d8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b483dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
- 00ae8660 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b483e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae86d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md) → [`00b4845c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4849c",
      "incomplete_value": true,
      "site": "00b4849c",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48478",
      "incomplete_value": true,
      "site": "00b48478",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48484",
      "incomplete_value": true,
      "site": "00b48494",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae86e4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48468 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae86ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00b48470 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae86f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae86f8 ["COPY", "register:4018:8", ["const:296000:8"]]
- 00ae86fc ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b48478 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4847c ["COPY", "register:4018:8", ["const:2a5000:8"]]
+ 00b48480 ["COPY", "tmp:0:8", ["const:f6b:8"]]
~~~


### [`00ae8748`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8748.md) → [`00b484cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b484cc.md) _ZN8firebase4util10byte_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b484d0",
      "incomplete_value": true,
      "site": "00b484d0",
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
      "definition_site": "00ae874c",
      "incomplete_value": true,
      "site": "00ae874c",
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
      "definition_site": "00b484d0",
      "incomplete_value": true,
      "site": "00b484d0",
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
      "definition_site": "00ae874c",
      "incomplete_value": true,
      "site": "00ae874c",
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
      "definition_site": "00b484e8",
      "incomplete_value": false,
      "site": "00b484ec",
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
        "010a0658",
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
        "01125518",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae875c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8760 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae8764 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b484e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b484e4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b484e8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae8768 ["INT_ADD", "register:40f0:8", ["const:ae8768:8", "const:4:8"]]
+ 00b484ec ["INT_ADD", "register:40f0:8", ["const:b484ec:8", "const:4:8"]]
- 00ae876c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8770 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00b484f0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b484f4 ["COPY", "tmp:0:8", ["const:518:8"]]
~~~


### [`00ae8784`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md) → [`00b48508`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4850c",
      "incomplete_value": true,
      "site": "00b4850c",
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
      "definition_site": "00ae8788",
      "incomplete_value": true,
      "site": "00ae8788",
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
      "definition_site": "00b4850c",
      "incomplete_value": true,
      "site": "00b4850c",
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
      "definition_site": "00ae8788",
      "incomplete_value": true,
      "site": "00ae8788",
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
      "definition_site": "00b48548",
      "incomplete_value": true,
      "site": "00b48548",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8790 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48514 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00b4851c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae87a0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00ae87a4 ["COPY", "register:4018:8", ["const:296000:8"]]
- 00ae87a8 ["COPY", "tmp:0:8", ["const:459:8"]]
+ 00b48524 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48528 ["COPY", "register:4018:8", ["const:2a5000:8"]]
+ 00b4852c ["COPY", "tmp:0:8", ["const:f6b:8"]]
~~~


### [`00ae87f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae87f4.md) → [`00b48578`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48578.md) _ZN8firebase4util10byte_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48594",
      "incomplete_value": false,
      "site": "00b48598",
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
      "definition_site": "00b485a4",
      "incomplete_value": true,
      "site": "00b485b0",
      "value": [
        "LOAD",
        "8",
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
        "010a0668",
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
        "01125528",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8808 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae880c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae8810 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4858c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48590 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b48594 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae8814 ["INT_ADD", "register:40f0:8", ["const:ae8814:8", "const:4:8"]]
+ 00b48598 ["INT_ADD", "register:40f0:8", ["const:b48598:8", "const:4:8"]]
- 00ae8818 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae881c ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00b4859c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b485a0 ["COPY", "tmp:0:8", ["const:528:8"]]
~~~


### [`00ae8830`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8830.md) → [`00b485b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485b4.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b485e0",
      "incomplete_value": true,
      "site": "00b485e0",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b485c8",
      "incomplete_value": true,
      "site": "00b485c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b485d4",
      "incomplete_value": false,
      "site": "00b485d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:db9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8850",
      "incomplete_value": false,
      "site": "00ae8854",
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
            "const:ff0:8"
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae883c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00b485c0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b485c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae8844 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b485c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae884c ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae8850 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b485d0 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b485d4 ["COPY", "tmp:0:8", ["const:db9:8"]]
~~~


### [`00ae8870`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md) → [`00b485f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b485f8",
      "incomplete_value": true,
      "site": "00b485f8",
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
      "definition_site": "00ae8874",
      "incomplete_value": true,
      "site": "00ae8874",
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
      "definition_site": "00b485f8",
      "incomplete_value": true,
      "site": "00b485f8",
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
      "definition_site": "00ae8874",
      "incomplete_value": true,
      "site": "00ae8874",
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
      "definition_site": "00b48620",
      "incomplete_value": true,
      "site": "00b48620",
      "value": [
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
            "const:670:8"
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae887c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00b48600 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae8884 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8888 ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae888c ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b48608 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4860c ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b48610 ["COPY", "tmp:0:8", ["const:db9:8"]]
- 00ae8894 ["INT_ADD", "register:40f0:8", ["const:ae8894:8", "const:4:8"]]
+ 00b48618 ["INT_ADD", "register:40f0:8", ["const:b48618:8", "const:4:8"]]
~~~


### [`00ae88b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88b0.md) → [`00b48634`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48634.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48638",
      "incomplete_value": true,
      "site": "00b48638",
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
      "definition_site": "00ae88b4",
      "incomplete_value": true,
      "site": "00ae88b4",
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
      "definition_site": "00b48638",
      "incomplete_value": true,
      "site": "00b48638",
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
      "definition_site": "00ae88b4",
      "incomplete_value": true,
      "site": "00ae88b4",
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
      "definition_site": "00b48664",
      "incomplete_value": true,
      "site": "00b48664",
      "value": [
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
            "const:670:8"
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae88bc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae88c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00b48640 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48644 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae88c4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae88c8 ["COPY", "register:4018:8", ["const:2aa000:8"]]
+ 00b48648 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4864c ["COPY", "register:4018:8", ["const:2bb000:8"]]
- 00ae88d0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b48654 ["COPY", "tmp:0:8", ["const:db9:8"]]
~~~


### [`00ae88f4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md) → [`00b48678`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b486a8",
      "incomplete_value": true,
      "site": "00b486a8",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4868c",
      "incomplete_value": true,
      "site": "00b4868c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48694",
      "incomplete_value": false,
      "site": "00b486a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:db9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8910",
      "incomplete_value": true,
      "site": "00ae891c",
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
            "const:ff0:8"
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8900 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8904 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
+ 00b48684 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48688 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae8908 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae890c ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae8910 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b4868c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48690 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b48694 ["COPY", "tmp:0:8", ["const:db9:8"]]
- 00ae891c ["INT_ADD", "register:40f0:8", ["const:ae891c:8", "const:4:8"]]
+ 00b486a0 ["INT_ADD", "register:40f0:8", ["const:b486a0:8", "const:4:8"]]
~~~


### [`00ae8944`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8944.md) → [`00b486c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b486c8.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48750",
      "incomplete_value": true,
      "site": "00b48750",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b48708",
      "incomplete_value": true,
      "site": "00b48708",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8984",
      "incomplete_value": true,
      "site": "00ae8984",
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
      "definition_site": "00b486fc",
      "incomplete_value": true,
      "site": "00b48708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8954 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8958 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
+ 00b486d8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b486dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
- 00ae895c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b486e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8964 ["BRANCH", null, ["local:b14:8"]]
+ 00b486e8 ["BRANCH", null, ["local:b6:8"]]
~~~


### [`00ae89e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md) → [`00b48764`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48768",
      "incomplete_value": true,
      "site": "00b48768",
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
      "definition_site": "00ae89e4",
      "incomplete_value": true,
      "site": "00ae89e4",
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
      "definition_site": "00b48768",
      "incomplete_value": true,
      "site": "00b48768",
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
      "definition_site": "00ae89e4",
      "incomplete_value": true,
      "site": "00ae89e4",
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
      "definition_site": "00b4876c",
      "incomplete_value": true,
      "site": "00b4876c",
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
      "definition_site": "00ae89e8",
      "incomplete_value": true,
      "site": "00ae89e8",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125538",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae89f0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae89f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00b48774 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae89f8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00ae89fc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8a00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:678:8"]]
+ 00b4877c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b48780 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48784 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
- 00ae8a08 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b4878c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae8a80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md) → [`00b48804`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48844",
      "incomplete_value": true,
      "site": "00b48844",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48820",
      "incomplete_value": true,
      "site": "00b48820",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4882c",
      "incomplete_value": true,
      "site": "00b4883c",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8a8c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48810 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00b48818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae8a9c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8aa0 ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae8aa4 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b48820 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b48824 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b48828 ["COPY", "tmp:0:8", ["const:db9:8"]]
~~~


### [`00ae8af0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8af0.md) → [`00b48874`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48874.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48878",
      "incomplete_value": true,
      "site": "00b48878",
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
      "definition_site": "00ae8af4",
      "incomplete_value": true,
      "site": "00ae8af4",
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
      "definition_site": "00b48878",
      "incomplete_value": true,
      "site": "00b48878",
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
      "definition_site": "00ae8af4",
      "incomplete_value": true,
      "site": "00ae8af4",
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
      "definition_site": "00b48890",
      "incomplete_value": false,
      "site": "00b48894",
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
        "010a0680",
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
        "01125540",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8b04 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8b08 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae8b0c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b48888 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4888c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b48890 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae8b10 ["INT_ADD", "register:40f0:8", ["const:ae8b10:8", "const:4:8"]]
+ 00b48894 ["INT_ADD", "register:40f0:8", ["const:b48894:8", "const:4:8"]]
- 00ae8b14 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8b18 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00b48898 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4889c ["COPY", "tmp:0:8", ["const:540:8"]]
~~~


### [`00ae8b2c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md) → [`00b488b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b488f0",
      "incomplete_value": true,
      "site": "00b488f0",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b488cc",
      "incomplete_value": true,
      "site": "00b488cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b488d8",
      "incomplete_value": true,
      "site": "00b488e8",
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
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
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
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8b38 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b488bc ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
+ 00b488c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae8b48 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae8b4c ["COPY", "register:4018:8", ["const:2aa000:8"]]
- 00ae8b50 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00b488cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b488d0 ["COPY", "register:4018:8", ["const:2bb000:8"]]
+ 00b488d4 ["COPY", "tmp:0:8", ["const:db9:8"]]
~~~


### [`00ae8b9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b9c.md) → [`00b48920`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48920.md) _ZN8firebase4util15character_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4893c",
      "incomplete_value": false,
      "site": "00b48940",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4894c",
      "incomplete_value": true,
      "site": "00b48958",
      "value": [
        "LOAD",
        "8",
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
        "01125550",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8bb4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae8bb8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b48938 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b4893c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae8bbc ["INT_ADD", "register:40f0:8", ["const:ae8bbc:8", "const:4:8"]]
+ 00b48940 ["INT_ADD", "register:40f0:8", ["const:b48940:8", "const:4:8"]]
- 00ae8bc0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8bc4 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00b48944 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48948 ["COPY", "tmp:0:8", ["const:550:8"]]
~~~


### [`00ae8bd8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md) → [`00b4895c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b48988",
      "incomplete_value": true,
      "site": "00b48988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48970",
      "incomplete_value": true,
      "site": "00b48970",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4897c",
      "incomplete_value": false,
      "site": "00b48980",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8be4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8be8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00b48968 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4896c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00ae8bf4 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8bf8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b48978 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b4897c ["COPY", "tmp:0:8", ["const:341:8"]]
- 00ae8bfc ["INT_ADD", "register:40f0:8", ["const:ae8bfc:8", "const:4:8"]]
+ 00b48980 ["INT_ADD", "register:40f0:8", ["const:b48980:8", "const:4:8"]]
~~~


### [`00ae8c18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c18.md) → [`00b4899c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4899c.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b489c8",
      "incomplete_value": true,
      "site": "00b489c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:558:8"
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
            "const:698:8"
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
      "definition_site": "00b489b0",
      "incomplete_value": true,
      "site": "00b489b0",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b489b8",
      "incomplete_value": false,
      "site": "00b489c0",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8c24 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8c28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00b489a8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b489ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00ae8c30 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8c34 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b489b4 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b489b8 ["COPY", "tmp:0:8", ["const:341:8"]]
- 00ae8c3c ["INT_ADD", "register:40f0:8", ["const:ae8c3c:8", "const:4:8"]]
+ 00b489c0 ["INT_ADD", "register:40f0:8", ["const:b489c0:8", "const:4:8"]]
~~~


### [`00ae8c58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c58.md) → [`00b489dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b489dc.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48a0c",
      "incomplete_value": true,
      "site": "00b48a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:558:8"
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
            "const:698:8"
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
      "definition_site": "00b489f0",
      "incomplete_value": true,
      "site": "00b489f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00b489fc",
      "incomplete_value": false,
      "site": "00b48a04",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8c64 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00b489e8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b489ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00ae8c6c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae8c70 ["COPY", "register:4018:8", ["const:298000:8"]]
+ 00b489f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b489f4 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae8c78 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b489fc ["COPY", "tmp:0:8", ["const:341:8"]]
~~~


### [`00ae8c9c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md) → [`00b48a20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48a50",
      "incomplete_value": true,
      "site": "00b48a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48a34",
      "incomplete_value": true,
      "site": "00b48a34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48a3c",
      "incomplete_value": false,
      "site": "00b48a48",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ca8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8cac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
+ 00b48a2c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:558:8"]]
- 00ae8cb4 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8cb8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b48a38 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b48a3c ["COPY", "tmp:0:8", ["const:341:8"]]
- 00ae8cc4 ["INT_ADD", "register:40f0:8", ["const:ae8cc4:8", "const:4:8"]]
+ 00b48a48 ["INT_ADD", "register:40f0:8", ["const:b48a48:8", "const:4:8"]]
~~~


### [`00ae8ce0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ce0.md) → [`00b48a64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a64.md) _ZN8firebase4util11class_class8GetClassEv

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
      "definition_site": "00b48a68",
      "incomplete_value": true,
      "site": "00b48a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
        "010a0698",
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
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ce0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8ce4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
+ 00b48a64 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48a68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:558:8"]]
~~~


### [`00ae8cec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8cec.md) → [`00b48a70`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48af8",
      "incomplete_value": true,
      "site": "00b48af8",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b48ab0",
      "incomplete_value": true,
      "site": "00b48ab0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8d2c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48aa4",
      "incomplete_value": true,
      "site": "00b48ab0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:558:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8cfc ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8d00 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
+ 00b48a80 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48a84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:560:8"]]
- 00ae8d0c ["BRANCH", null, ["local:b11:8"]]
+ 00b48a90 ["BRANCH", null, ["local:b7:8"]]
- 00ae8d14 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b48a98 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae8d88`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8d88.md) → [`00b48b0c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48b0c.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 3件, `call_target` 3件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48b48",
      "incomplete_value": true,
      "site": "00b48b48",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48b98",
      "incomplete_value": true,
      "site": "00b48b98",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48b24",
      "incomplete_value": true,
      "site": "00b48b24",
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
      "definition_site": "00ae8da0",
      "incomplete_value": true,
      "site": "00ae8da0",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125560",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8d98 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae8d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00b48b1c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48b20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
- 00ae8da0 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00ae8da4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae8da8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
+ 00b48b24 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b48b28 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48b2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:560:8"]]
- 00ae8db0 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b48b34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae8e28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md) → [`00b48bac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48bec",
      "incomplete_value": true,
      "site": "00b48bec",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48bc8",
      "incomplete_value": true,
      "site": "00b48bc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae8e50",
      "incomplete_value": true,
      "site": "00ae8e60",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8e34 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48bb8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00b48bc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
- 00ae8e48 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8e4c ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b48bcc ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b48bd0 ["COPY", "tmp:0:8", ["const:341:8"]]
~~~


### [`00ae8e98`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e98.md) → [`00b48c1c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c1c.md) _ZN8firebase4util11class_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48c20",
      "incomplete_value": true,
      "site": "00b48c20",
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
      "definition_site": "00ae8e9c",
      "incomplete_value": true,
      "site": "00ae8e9c",
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
      "definition_site": "00b48c20",
      "incomplete_value": true,
      "site": "00b48c20",
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
      "definition_site": "00ae8e9c",
      "incomplete_value": true,
      "site": "00ae8e9c",
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
      "definition_site": "00b48c38",
      "incomplete_value": false,
      "site": "00b48c3c",
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
        "010a06a8",
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
        "01125568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8eac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8eb0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae8eb4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b48c30 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48c34 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b48c38 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae8eb8 ["INT_ADD", "register:40f0:8", ["const:ae8eb8:8", "const:4:8"]]
+ 00b48c3c ["INT_ADD", "register:40f0:8", ["const:b48c3c:8", "const:4:8"]]
- 00ae8ebc ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8ec0 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 00b48c40 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48c44 ["COPY", "tmp:0:8", ["const:568:8"]]
~~~


### [`00ae8ed4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md) → [`00b48c58`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48c98",
      "incomplete_value": true,
      "site": "00b48c98",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48c74",
      "incomplete_value": true,
      "site": "00b48c74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48c7c",
      "incomplete_value": false,
      "site": "00b48c90",
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
            "const:341:8"
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8ee0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48c64 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8ee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
+ 00b48c6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
- 00ae8ef0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8ef4 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae8ef8 ["COPY", "tmp:0:8", ["const:5ee:8"]]
+ 00b48c74 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48c78 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b48c7c ["COPY", "tmp:0:8", ["const:341:8"]]
~~~


### [`00ae8f44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f44.md) → [`00b48cc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48cc8.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48cdc",
      "incomplete_value": true,
      "site": "00b48cdc",
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
      "definition_site": "00ae8f58",
      "incomplete_value": true,
      "site": "00ae8f58",
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
      "definition_site": "00b48ce4",
      "incomplete_value": false,
      "site": "00b48ce8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b48cf4",
      "incomplete_value": true,
      "site": "00b48d00",
      "value": [
        "LOAD",
        "8",
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
        "010a06b8",
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
        "01125578",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8f58 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8f5c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae8f60 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b48cdc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48ce0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b48ce4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae8f64 ["INT_ADD", "register:40f0:8", ["const:ae8f64:8", "const:4:8"]]
+ 00b48ce8 ["INT_ADD", "register:40f0:8", ["const:b48ce8:8", "const:4:8"]]
- 00ae8f68 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae8f6c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00b48cec ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48cf0 ["COPY", "tmp:0:8", ["const:578:8"]]
~~~


### [`00ae8f80`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md) → [`00b48d04`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00b48d30",
      "incomplete_value": true,
      "site": "00b48d30",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48d18",
      "incomplete_value": true,
      "site": "00b48d18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48d24",
      "incomplete_value": false,
      "site": "00b48d28",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8f8c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8f90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b48d10 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48d14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae8f9c ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae8fa0 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b48d20 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b48d24 ["COPY", "tmp:0:8", ["const:2ff:8"]]
- 00ae8fa4 ["INT_ADD", "register:40f0:8", ["const:ae8fa4:8", "const:4:8"]]
+ 00b48d28 ["INT_ADD", "register:40f0:8", ["const:b48d28:8", "const:4:8"]]
~~~


### [`00ae8fc0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md) → [`00b48d44`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00b48d70",
      "incomplete_value": true,
      "site": "00b48d70",
      "value": [
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
            "const:6c0:8"
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
      "definition_site": "00b48d58",
      "incomplete_value": true,
      "site": "00b48d58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48d60",
      "incomplete_value": false,
      "site": "00b48d68",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae8fcc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae8fd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b48d50 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae8fd8 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae8fdc ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b48d5c ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b48d60 ["COPY", "tmp:0:8", ["const:2ff:8"]]
- 00ae8fe4 ["INT_ADD", "register:40f0:8", ["const:ae8fe4:8", "const:4:8"]]
+ 00b48d68 ["INT_ADD", "register:40f0:8", ["const:b48d68:8", "const:4:8"]]
~~~


### [`00ae9000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9000.md) → [`00b48d84`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d84.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48db4",
      "incomplete_value": true,
      "site": "00b48db4",
      "value": [
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
            "const:6c0:8"
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
      "definition_site": "00b48d98",
      "incomplete_value": true,
      "site": "00b48d98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00b48da8",
      "incomplete_value": false,
      "site": "00b48dac",
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae900c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b48d90 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae9014 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae9018 ["COPY", "register:4018:8", ["const:29e000:8"]]
+ 00b48d98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b48d9c ["COPY", "register:4018:8", ["const:2af000:8"]]
- 00ae9020 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b48da4 ["COPY", "tmp:0:8", ["const:2ff:8"]]
~~~


### [`00ae9044`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md) → [`00b48dc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48df8",
      "incomplete_value": true,
      "site": "00b48df8",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48ddc",
      "incomplete_value": true,
      "site": "00b48ddc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48de4",
      "incomplete_value": false,
      "site": "00b48df0",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9050 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b48dd4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae905c ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae9060 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b48de0 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b48de4 ["COPY", "tmp:0:8", ["const:2ff:8"]]
- 00ae906c ["INT_ADD", "register:40f0:8", ["const:ae906c:8", "const:4:8"]]
+ 00b48df0 ["INT_ADD", "register:40f0:8", ["const:b48df0:8", "const:4:8"]]
~~~


### [`00ae9094`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md) → [`00b48e18`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48e18.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48ea0",
      "incomplete_value": true,
      "site": "00b48ea0",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b48e58",
      "incomplete_value": true,
      "site": "00b48e58",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00ae90d4",
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
    "new": {
      "definition_site": "00b48e4c",
      "incomplete_value": true,
      "site": "00b48e58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae90a4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae90a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b48e28 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48e2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 00ae90b4 ["BRANCH", null, ["local:b5:8"]]
+ 00b48e38 ["BRANCH", null, ["local:b6:8"]]
- 00ae90bc ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b48e40 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae9130`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md) → [`00b48eb4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b48ef0",
      "incomplete_value": true,
      "site": "00b48ef0",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48f40",
      "incomplete_value": true,
      "site": "00b48f40",
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
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48ecc",
      "incomplete_value": true,
      "site": "00b48ecc",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9140 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae9144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b48ec4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48ec8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae9148 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae914c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9150 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b48ecc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b48ed0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48ed4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 00ae9158 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b48edc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae91d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md) → [`00b48f54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48f94",
      "incomplete_value": true,
      "site": "00b48f94",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48f70",
      "incomplete_value": true,
      "site": "00b48f70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae91dc ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48f60 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae91e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b48f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae91ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae91f0 ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae91f4 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b48f70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b48f74 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b48f78 ["COPY", "tmp:0:8", ["const:2ff:8"]]
~~~


### [`00ae9240`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md) → [`00b48fc4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48fe0",
      "incomplete_value": false,
      "site": "00b48fe4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b48ff0",
      "incomplete_value": true,
      "site": "00b48ffc",
      "value": [
        "LOAD",
        "8",
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
        "010a06d0",
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
        "01125590",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9258 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae925c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b48fdc ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b48fe0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae9260 ["INT_ADD", "register:40f0:8", ["const:ae9260:8", "const:4:8"]]
+ 00b48fe4 ["INT_ADD", "register:40f0:8", ["const:b48fe4:8", "const:4:8"]]
- 00ae9264 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9268 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00b48fe8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48fec ["COPY", "tmp:0:8", ["const:590:8"]]
~~~


### [`00ae927c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md) → [`00b49000`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49040",
      "incomplete_value": true,
      "site": "00b49040",
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
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4901c",
      "incomplete_value": true,
      "site": "00b4901c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49024",
      "incomplete_value": false,
      "site": "00b49038",
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
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9288 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4900c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b49014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae929c ["COPY", "register:4018:8", ["const:29e000:8"]]
- 00ae92a0 ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00b49020 ["COPY", "register:4018:8", ["const:2af000:8"]]
+ 00b49024 ["COPY", "tmp:0:8", ["const:2ff:8"]]
~~~


### [`00ae92ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae92ec.md) → [`00b49070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49070.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4908c",
      "incomplete_value": false,
      "site": "00b49090",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4909c",
      "incomplete_value": true,
      "site": "00b490a8",
      "value": [
        "LOAD",
        "8",
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
        "010a06e0",
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
        "011255a0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9300 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9304 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae9308 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b49084 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b49088 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b4908c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae930c ["INT_ADD", "register:40f0:8", ["const:ae930c:8", "const:4:8"]]
+ 00b49090 ["INT_ADD", "register:40f0:8", ["const:b49090:8", "const:4:8"]]
- 00ae9310 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9314 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00b49094 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49098 ["COPY", "tmp:0:8", ["const:5a0:8"]]
~~~


### [`00ae9328`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md) → [`00b490ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

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
      "definition_site": "00b490d8",
      "incomplete_value": true,
      "site": "00b490d8",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b490c0",
      "incomplete_value": true,
      "site": "00b490c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b490cc",
      "incomplete_value": false,
      "site": "00b490d0",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9334 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b490b8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b490bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae933c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b490c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9344 ["COPY", "register:4018:8", ["const:29d000:8"]]
- 00ae9348 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b490c8 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b490cc ["COPY", "tmp:0:8", ["const:f9:8"]]
~~~


### [`00ae9368`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md) → [`00b490ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b49118",
      "incomplete_value": true,
      "site": "00b49118",
      "value": [
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
            "const:6e8:8"
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
      "definition_site": "00b49100",
      "incomplete_value": true,
      "site": "00b49100",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49108",
      "incomplete_value": false,
      "site": "00b49110",
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
            "const:f9:8"
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
            "const:ddf:8"
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9374 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b490f8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b490fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae9380 ["COPY", "register:4018:8", ["const:29d000:8"]]
- 00ae9384 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b49104 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b49108 ["COPY", "tmp:0:8", ["const:f9:8"]]
- 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
+ 00b49110 ["INT_ADD", "register:40f0:8", ["const:b49110:8", "const:4:8"]]
~~~


### [`00ae93a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md) → [`00b4912c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4915c",
      "incomplete_value": true,
      "site": "00b4915c",
      "value": [
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
            "const:6e8:8"
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
      "definition_site": "00b49140",
      "incomplete_value": true,
      "site": "00b49140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
      "definition_site": "00b4914c",
      "incomplete_value": false,
      "site": "00b49154",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae93b4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b49138 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4913c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae93c0 ["COPY", "register:4018:8", ["const:29d000:8"]]
+ 00b49144 ["COPY", "register:4018:8", ["const:2ae000:8"]]
- 00ae93c8 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b4914c ["COPY", "tmp:0:8", ["const:f9:8"]]
~~~


### [`00ae93ec`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md) → [`00b49170`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b491a0",
      "incomplete_value": true,
      "site": "00b491a0",
      "value": [
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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49184",
      "incomplete_value": true,
      "site": "00b49184",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4918c",
      "incomplete_value": false,
      "site": "00b49198",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      16,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae93f8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae93fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b4917c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae9404 ["COPY", "register:4018:8", ["const:29d000:8"]]
- 00ae9408 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b49188 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b4918c ["COPY", "tmp:0:8", ["const:f9:8"]]
- 00ae9414 ["INT_ADD", "register:40f0:8", ["const:ae9414:8", "const:4:8"]]
+ 00b49198 ["INT_ADD", "register:40f0:8", ["const:b49198:8", "const:4:8"]]
~~~


### [`00ae9430`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9430.md) → [`00b491b4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491b4.md) _ZN8firebase4util7context8GetClassEv

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
      "definition_site": "00b491b8",
      "incomplete_value": true,
      "site": "00b491bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a8:8"
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
        "010a06e8",
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
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9430 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9434 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e8:8"]]
+ 00b491b4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b491b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:5a8:8"]]
~~~


### [`00ae943c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md) → [`00b491c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491c0.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49248",
      "incomplete_value": true,
      "site": "00b49248",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00b49200",
      "incomplete_value": true,
      "site": "00b49200",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00ae947c",
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
    "new": {
      "definition_site": "00b491f4",
      "incomplete_value": true,
      "site": "00b49200",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae944c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b491d0 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b491d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
- 00ae9454 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b491d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae945c ["BRANCH", null, ["local:b5:8"]]
+ 00b491e0 ["BRANCH", null, ["local:b7:8"]]
~~~


### [`00ae94d8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md) → [`00b4925c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b49298",
      "incomplete_value": true,
      "site": "00b49298",
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
    "old": {
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b492e8",
      "incomplete_value": true,
      "site": "00b492e8",
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
    "old": {
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49274",
      "incomplete_value": true,
      "site": "00b49274",
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
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae94e8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae94ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b4926c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49270 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae94f0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae94f4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae94f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b49274 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b49278 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4927c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
- 00ae9510 ["INT_ADD", "register:40f0:8", ["const:ae9510:8", "const:4:8"]]
+ 00b49294 ["INT_ADD", "register:40f0:8", ["const:b49294:8", "const:4:8"]]
~~~


### [`00ae9578`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md) → [`00b492fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4933c",
      "incomplete_value": true,
      "site": "00b4933c",
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
    "old": {
      "definition_site": "00ae95b8",
      "incomplete_value": true,
      "site": "00ae95b8",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49318",
      "incomplete_value": true,
      "site": "00b49318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9594",
      "incomplete_value": true,
      "site": "00ae9594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49320",
      "incomplete_value": false,
      "site": "00b49334",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae959c",
      "incomplete_value": false,
      "site": "00ae95b0",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a06e8",
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
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9584 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49308 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae958c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b49310 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae9598 ["COPY", "register:4018:8", ["const:29d000:8"]]
- 00ae959c ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b4931c ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b49320 ["COPY", "tmp:0:8", ["const:f9:8"]]
~~~


### [`00ae95e8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md) → [`00b4936c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde6c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6c0.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b140.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49388",
      "incomplete_value": false,
      "site": "00b4938c",
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
      "definition_site": "00ae9604",
      "incomplete_value": false,
      "site": "00ae9608",
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
      "definition_site": "00b49398",
      "incomplete_value": true,
      "site": "00b493a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9614",
      "incomplete_value": true,
      "site": "00ae9620",
      "value": [
        "LOAD",
        "8",
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
        "010a06f8",
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
        "011255b8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9600 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae9604 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b49384 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b49388 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae9608 ["INT_ADD", "register:40f0:8", ["const:ae9608:8", "const:4:8"]]
+ 00b4938c ["INT_ADD", "register:40f0:8", ["const:b4938c:8", "const:4:8"]]
- 00ae960c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9610 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00b49390 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49394 ["COPY", "tmp:0:8", ["const:5b8:8"]]
~~~


### [`00ae9624`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md) → [`00b493a8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b493e8",
      "incomplete_value": true,
      "site": "00b493e8",
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
    "old": {
      "definition_site": "00ae9664",
      "incomplete_value": true,
      "site": "00ae9664",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b493c4",
      "incomplete_value": true,
      "site": "00b493c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9640",
      "incomplete_value": true,
      "site": "00ae9640",
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
      "definition_site": "00b493d0",
      "incomplete_value": true,
      "site": "00b493e0",
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
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a06e8",
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
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9630 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b493b4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b493bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae9640 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae9644 ["COPY", "register:4018:8", ["const:29d000:8"]]
- 00ae9648 ["COPY", "tmp:0:8", ["const:ddf:8"]]
+ 00b493c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b493c8 ["COPY", "register:4018:8", ["const:2ae000:8"]]
+ 00b493cc ["COPY", "tmp:0:8", ["const:f9:8"]]
~~~


### [`00ae9694`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md) → [`00b49418`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49418.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b49434",
      "incomplete_value": false,
      "site": "00b49438",
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
      "definition_site": "00ae96b0",
      "incomplete_value": false,
      "site": "00ae96b4",
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
      "definition_site": "00b49444",
      "incomplete_value": true,
      "site": "00b49450",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae96c0",
      "incomplete_value": true,
      "site": "00ae96cc",
      "value": [
        "LOAD",
        "8",
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
        "010a0710",
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
        "011255d0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae96ac ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae96b0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b49430 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b49434 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae96b4 ["INT_ADD", "register:40f0:8", ["const:ae96b4:8", "const:4:8"]]
+ 00b49438 ["INT_ADD", "register:40f0:8", ["const:b49438:8", "const:4:8"]]
- 00ae96b8 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae96bc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00b4943c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49440 ["COPY", "tmp:0:8", ["const:5d0:8"]]
~~~


### [`00ae96d0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md) → [`00b49454`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b49480",
      "incomplete_value": true,
      "site": "00b49480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96fc",
      "incomplete_value": true,
      "site": "00ae96fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b49468",
      "incomplete_value": true,
      "site": "00b49468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96e4",
      "incomplete_value": true,
      "site": "00ae96e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49474",
      "incomplete_value": false,
      "site": "00b49478",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96f0",
      "incomplete_value": false,
      "site": "00ae96f4",
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
            "const:1bb:8"
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae96dc ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae96e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00b49460 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00ae96ec ["COPY", "register:4018:8", ["const:294000:8"]]
- 00ae96f0 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b49470 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00b49474 ["COPY", "tmp:0:8", ["const:a4a:8"]]
- 00ae96f4 ["INT_ADD", "register:40f0:8", ["const:ae96f4:8", "const:4:8"]]
+ 00b49478 ["INT_ADD", "register:40f0:8", ["const:b49478:8", "const:4:8"]]
~~~


### [`00ae9710`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md) → [`00b49494`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b494c0",
      "incomplete_value": true,
      "site": "00b494c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae973c",
      "incomplete_value": true,
      "site": "00ae973c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b494a8",
      "incomplete_value": true,
      "site": "00b494a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9724",
      "incomplete_value": true,
      "site": "00ae9724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b494b0",
      "incomplete_value": false,
      "site": "00b494b8",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae972c",
      "incomplete_value": false,
      "site": "00ae9734",
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
            "const:1bb:8"
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae971c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00b494a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b494a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00ae9728 ["COPY", "register:4018:8", ["const:294000:8"]]
- 00ae972c ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b494ac ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00b494b0 ["COPY", "tmp:0:8", ["const:a4a:8"]]
- 00ae9734 ["INT_ADD", "register:40f0:8", ["const:ae9734:8", "const:4:8"]]
+ 00b494b8 ["INT_ADD", "register:40f0:8", ["const:b494b8:8", "const:4:8"]]
~~~


### [`00ae9750`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md) → [`00b494d4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49504",
      "incomplete_value": true,
      "site": "00b49504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9780",
      "incomplete_value": true,
      "site": "00ae9780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b494e8",
      "incomplete_value": true,
      "site": "00b494e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9764",
      "incomplete_value": true,
      "site": "00ae9764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b494f4",
      "incomplete_value": false,
      "site": "00b494fc",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9770",
      "incomplete_value": false,
      "site": "00ae9778",
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
            "const:1bb:8"
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae975c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00b494e0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b494e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00ae9768 ["COPY", "register:4018:8", ["const:294000:8"]]
+ 00b494ec ["COPY", "register:4018:8", ["const:2a3000:8"]]
- 00ae9770 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b494f4 ["COPY", "tmp:0:8", ["const:a4a:8"]]
~~~


### [`00ae9794`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md) → [`00b49518`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49548",
      "incomplete_value": true,
      "site": "00b49548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97c4",
      "incomplete_value": true,
      "site": "00ae97c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b4952c",
      "incomplete_value": true,
      "site": "00b4952c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97a8",
      "incomplete_value": true,
      "site": "00ae97a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49534",
      "incomplete_value": false,
      "site": "00b49540",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97b0",
      "incomplete_value": false,
      "site": "00ae97bc",
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
            "const:1bb:8"
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae97a0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae97a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
+ 00b49524 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
- 00ae97ac ["COPY", "register:4018:8", ["const:294000:8"]]
- 00ae97b0 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b49530 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00b49534 ["COPY", "tmp:0:8", ["const:a4a:8"]]
- 00ae97bc ["INT_ADD", "register:40f0:8", ["const:ae97bc:8", "const:4:8"]]
+ 00b49540 ["INT_ADD", "register:40f0:8", ["const:b49540:8", "const:4:8"]]
~~~


### [`00ae97e4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md) → [`00b49568`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b495f0",
      "incomplete_value": true,
      "site": "00b495f0",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae986c",
      "incomplete_value": true,
      "site": "00ae986c",
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
            "const:720:8"
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
      "definition_site": "00b4959c",
      "incomplete_value": true,
      "site": "00b495a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9818",
      "incomplete_value": true,
      "site": "00ae9824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:718:8"
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
        "010a0720",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0720",
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
        "011255e0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae97f4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae97f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:720:8"]]
+ 00b49578 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4957c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5e0:8"]]
- 00ae980c ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b49590 ["COPY", "register:4048:8", ["const:1125000:8"]]
- 00ae9818 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:718:8"]]
+ 00b4959c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5d8:8"]]
~~~


### [`00ae9880`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md) → [`00b49604`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b49640",
      "incomplete_value": true,
      "site": "00b49640",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae98bc",
      "incomplete_value": true,
      "site": "00ae98bc",
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
            "const:720:8"
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
      "definition_site": "00b49690",
      "incomplete_value": true,
      "site": "00b49690",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae990c",
      "incomplete_value": true,
      "site": "00ae990c",
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
            "const:718:8"
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
      "definition_site": "00b4961c",
      "incomplete_value": true,
      "site": "00b4961c",
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
      "definition_site": "00ae9898",
      "incomplete_value": true,
      "site": "00ae9898",
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0720",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9890 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae9894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00b49614 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49618 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5d8:8"]]
- 00ae9898 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae989c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae98a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:720:8"]]
+ 00b4961c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b49620 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49624 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5e0:8"]]
- 00ae98a8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b4962c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00ae9920`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md) → [`00b496a4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b496e4",
      "incomplete_value": true,
      "site": "00b496e4",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9960",
      "incomplete_value": true,
      "site": "00ae9960",
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
            "const:718:8"
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
      "definition_site": "00b496c0",
      "incomplete_value": true,
      "site": "00b496c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae993c",
      "incomplete_value": true,
      "site": "00ae993c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b496c8",
      "incomplete_value": false,
      "site": "00b496dc",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9944",
      "incomplete_value": false,
      "site": "00ae9958",
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
            "const:1bb:8"
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae992c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b496b0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00b496b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5d8:8"]]
- 00ae993c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9940 ["COPY", "register:4018:8", ["const:294000:8"]]
- 00ae9944 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b496c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b496c4 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00b496c8 ["COPY", "tmp:0:8", ["const:a4a:8"]]
~~~


### [`00ae9990`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md) → [`00b49714`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b49730",
      "incomplete_value": false,
      "site": "00b49734",
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
      "definition_site": "00ae99ac",
      "incomplete_value": false,
      "site": "00ae99b0",
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
      "definition_site": "00b49740",
      "incomplete_value": true,
      "site": "00b4974c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae99bc",
      "incomplete_value": true,
      "site": "00ae99c8",
      "value": [
        "LOAD",
        "8",
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
        "010a0728",
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
        "011255e8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae99a8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae99ac ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4972c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b49730 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae99b0 ["INT_ADD", "register:40f0:8", ["const:ae99b0:8", "const:4:8"]]
+ 00b49734 ["INT_ADD", "register:40f0:8", ["const:b49734:8", "const:4:8"]]
- 00ae99b4 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae99b8 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 00b49738 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4973c ["COPY", "tmp:0:8", ["const:5e8:8"]]
~~~


### [`00ae99cc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md) → [`00b49750`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49790",
      "incomplete_value": true,
      "site": "00b49790",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a0c",
      "incomplete_value": true,
      "site": "00ae9a0c",
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
            "const:718:8"
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
      "definition_site": "00b4976c",
      "incomplete_value": true,
      "site": "00b4976c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae99e8",
      "incomplete_value": true,
      "site": "00ae99e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49778",
      "incomplete_value": true,
      "site": "00b49788",
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
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0718",
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
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae99d8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4975c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae99e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
+ 00b49764 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5d8:8"]]
- 00ae99e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae99ec ["COPY", "register:4018:8", ["const:294000:8"]]
- 00ae99f0 ["COPY", "tmp:0:8", ["const:1bb:8"]]
+ 00b4976c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b49770 ["COPY", "register:4018:8", ["const:2a3000:8"]]
+ 00b49774 ["COPY", "tmp:0:8", ["const:a4a:8"]]
~~~


### [`00ae9a3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md) → [`00b497c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b497dc",
      "incomplete_value": false,
      "site": "00b497e0",
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
      "definition_site": "00ae9a58",
      "incomplete_value": false,
      "site": "00ae9a5c",
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
      "definition_site": "00b497ec",
      "incomplete_value": true,
      "site": "00b497f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9a68",
      "incomplete_value": true,
      "site": "00ae9a74",
      "value": [
        "LOAD",
        "8",
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
        "010a0748",
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
        "01125608",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9a54 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae9a58 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b497d8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b497dc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae9a5c ["INT_ADD", "register:40f0:8", ["const:ae9a5c:8", "const:4:8"]]
+ 00b497e0 ["INT_ADD", "register:40f0:8", ["const:b497e0:8", "const:4:8"]]
- 00ae9a60 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9a64 ["COPY", "tmp:0:8", ["const:748:8"]]
+ 00b497e4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b497e8 ["COPY", "tmp:0:8", ["const:608:8"]]
~~~


### [`00ae9a78`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md) → [`00b497fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49828",
      "incomplete_value": true,
      "site": "00b49828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9aa4",
      "incomplete_value": true,
      "site": "00ae9aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b49810",
      "incomplete_value": true,
      "site": "00b49810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a8c",
      "incomplete_value": true,
      "site": "00ae9a8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4981c",
      "incomplete_value": false,
      "site": "00b49820",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a98",
      "incomplete_value": false,
      "site": "00ae9a9c",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9a84 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b49808 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4980c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00ae9a94 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae9a98 ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b49818 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b4981c ["COPY", "tmp:0:8", ["const:351:8"]]
- 00ae9a9c ["INT_ADD", "register:40f0:8", ["const:ae9a9c:8", "const:4:8"]]
+ 00b49820 ["INT_ADD", "register:40f0:8", ["const:b49820:8", "const:4:8"]]
~~~


### [`00ae9ab8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md) → [`00b4983c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b49868",
      "incomplete_value": true,
      "site": "00b49868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ae4",
      "incomplete_value": true,
      "site": "00ae9ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b49850",
      "incomplete_value": true,
      "site": "00b49850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9acc",
      "incomplete_value": true,
      "site": "00ae9acc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49858",
      "incomplete_value": false,
      "site": "00b49860",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ad4",
      "incomplete_value": false,
      "site": "00ae9adc",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9ac4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9ac8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b49848 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4984c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00ae9ad0 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae9ad4 ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b49854 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b49858 ["COPY", "tmp:0:8", ["const:351:8"]]
- 00ae9adc ["INT_ADD", "register:40f0:8", ["const:ae9adc:8", "const:4:8"]]
+ 00b49860 ["INT_ADD", "register:40f0:8", ["const:b49860:8", "const:4:8"]]
~~~


### [`00ae9af8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9af8.md) → [`00b4987c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4987c.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b498ac",
      "incomplete_value": true,
      "site": "00b498ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b28",
      "incomplete_value": true,
      "site": "00ae9b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b49890",
      "incomplete_value": true,
      "site": "00b49890",
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
      "definition_site": "00ae9b0c",
      "incomplete_value": true,
      "site": "00ae9b0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4989c",
      "incomplete_value": false,
      "site": "00b498a4",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b18",
      "incomplete_value": false,
      "site": "00ae9b20",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9b04 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b49888 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4988c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00ae9b0c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9b10 ["COPY", "register:4018:8", ["const:298000:8"]]
+ 00b49890 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b49894 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 00ae9b18 ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b4989c ["COPY", "tmp:0:8", ["const:351:8"]]
~~~


### [`00ae9b3c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md) → [`00b498c0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b498f0",
      "incomplete_value": true,
      "site": "00b498f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b6c",
      "incomplete_value": true,
      "site": "00ae9b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b498d4",
      "incomplete_value": true,
      "site": "00b498d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b50",
      "incomplete_value": true,
      "site": "00ae9b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b498dc",
      "incomplete_value": false,
      "site": "00b498e8",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b58",
      "incomplete_value": false,
      "site": "00ae9b64",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9b48 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9b4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
+ 00b498cc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b498d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
- 00ae9b54 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae9b58 ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b498d8 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b498dc ["COPY", "tmp:0:8", ["const:351:8"]]
- 00ae9b64 ["INT_ADD", "register:40f0:8", ["const:ae9b64:8", "const:4:8"]]
+ 00b498e8 ["INT_ADD", "register:40f0:8", ["const:b498e8:8", "const:4:8"]]
~~~


### [`00ae9b8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md) → [`00b49910`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49998",
      "incomplete_value": true,
      "site": "00b49998",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9c14",
      "incomplete_value": true,
      "site": "00ae9c14",
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
            "const:758:8"
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
      "definition_site": "00b49944",
      "incomplete_value": true,
      "site": "00b49950",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:610:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9bc0",
      "incomplete_value": true,
      "site": "00ae9bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:750:8"
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
      "definition_site": "00b49964",
      "incomplete_value": true,
      "site": "00b49964",
      "value": [
        "LOAD",
        "8",
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
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9be0",
      "incomplete_value": true,
      "site": "00ae9be0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:720:8"
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
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0758",
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
        "01125618",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9b9c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:758:8"]]
+ 00b49920 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49924 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:618:8"]]
- 00ae9bac ["BRANCH", null, ["local:b6:8"]]
+ 00b49930 ["BRANCH", null, ["local:b5:8"]]
- 00ae9bb4 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b49938 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae9c28`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md) → [`00b499ac`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b499b4",
      "incomplete_value": true,
      "site": "00b499b4",
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
      "definition_site": "00ae9c30",
      "incomplete_value": true,
      "site": "00ae9c30",
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
      "definition_site": "00b499b4",
      "incomplete_value": true,
      "site": "00b499b4",
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
      "definition_site": "00ae9c30",
      "incomplete_value": true,
      "site": "00ae9c30",
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
      "definition_site": "00b499e8",
      "incomplete_value": true,
      "site": "00b499e8",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9c64",
      "incomplete_value": true,
      "site": "00ae9c64",
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
            "const:758:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0758",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9c38 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae9c3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b499bc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b499c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
- 00ae9c44 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9c48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:758:8"]]
+ 00b499c8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b499cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:618:8"]]
- 00ae9c60 ["INT_ADD", "register:40f0:8", ["const:ae9c60:8", "const:4:8"]]
+ 00b499e4 ["INT_ADD", "register:40f0:8", ["const:b499e4:8", "const:4:8"]]
~~~


### [`00ae9cc8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md) → [`00b49a4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49a8c",
      "incomplete_value": true,
      "site": "00b49a8c",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d08",
      "incomplete_value": true,
      "site": "00ae9d08",
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
            "const:750:8"
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
      "definition_site": "00b49a68",
      "incomplete_value": true,
      "site": "00b49a68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ce4",
      "incomplete_value": true,
      "site": "00ae9ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49a70",
      "incomplete_value": false,
      "site": "00b49a84",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9cec",
      "incomplete_value": false,
      "site": "00ae9d00",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9cd4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49a58 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9cdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b49a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
- 00ae9ce4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9ce8 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae9cec ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b49a68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b49a6c ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b49a70 ["COPY", "tmp:0:8", ["const:351:8"]]
~~~


### [`00ae9d38`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d38.md) → [`00b49abc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49abc.md) _ZN8firebase4util4date11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b49ad8",
      "incomplete_value": false,
      "site": "00b49adc",
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
      "definition_site": "00ae9d54",
      "incomplete_value": false,
      "site": "00ae9d58",
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
      "definition_site": "00b49ae8",
      "incomplete_value": true,
      "site": "00b49af4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9d64",
      "incomplete_value": true,
      "site": "00ae9d70",
      "value": [
        "LOAD",
        "8",
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
        "010a0760",
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
        "01125620",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9d4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9d50 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00ae9d54 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b49ad0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b49ad4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b49ad8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00ae9d58 ["INT_ADD", "register:40f0:8", ["const:ae9d58:8", "const:4:8"]]
+ 00b49adc ["INT_ADD", "register:40f0:8", ["const:b49adc:8", "const:4:8"]]
- 00ae9d5c ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9d60 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00b49ae0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49ae4 ["COPY", "tmp:0:8", ["const:620:8"]]
~~~


### [`00ae9d74`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md) → [`00b49af8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49b38",
      "incomplete_value": true,
      "site": "00b49b38",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9db4",
      "incomplete_value": true,
      "site": "00ae9db4",
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
            "const:750:8"
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
      "definition_site": "00b49b14",
      "incomplete_value": true,
      "site": "00b49b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d90",
      "incomplete_value": true,
      "site": "00ae9d90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49b1c",
      "incomplete_value": false,
      "site": "00b49b30",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9d98",
      "incomplete_value": false,
      "site": "00ae9dac",
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
            "const:5fe:8"
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
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0750",
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
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9d80 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49b04 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
+ 00b49b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
- 00ae9d94 ["COPY", "register:4018:8", ["const:298000:8"]]
- 00ae9d98 ["COPY", "tmp:0:8", ["const:5fe:8"]]
+ 00b49b18 ["COPY", "register:4018:8", ["const:2a8000:8"]]
+ 00b49b1c ["COPY", "tmp:0:8", ["const:351:8"]]
~~~


### [`00ae9de4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md) → [`00b49b68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b49b84",
      "incomplete_value": false,
      "site": "00b49b88",
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
      "definition_site": "00ae9e00",
      "incomplete_value": false,
      "site": "00ae9e04",
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
      "definition_site": "00b49b94",
      "incomplete_value": true,
      "site": "00b49ba0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9e10",
      "incomplete_value": true,
      "site": "00ae9e1c",
      "value": [
        "LOAD",
        "8",
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
        "010a0778",
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
        "01125638",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9dfc ["COPY", "register:4000:8", ["const:299000:8"]]
- 00ae9e00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b49b80 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b49b84 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00ae9e04 ["INT_ADD", "register:40f0:8", ["const:ae9e04:8", "const:4:8"]]
+ 00b49b88 ["INT_ADD", "register:40f0:8", ["const:b49b88:8", "const:4:8"]]
- 00ae9e08 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00ae9e0c ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00b49b8c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49b90 ["COPY", "tmp:0:8", ["const:638:8"]]
~~~


### [`00ae9e20`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md) → [`00b49ba4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00b49bd0",
      "incomplete_value": true,
      "site": "00b49bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e4c",
      "incomplete_value": true,
      "site": "00ae9e4c",
      "value": [
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
      "definition_site": "00b49bb8",
      "incomplete_value": true,
      "site": "00b49bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e34",
      "incomplete_value": true,
      "site": "00ae9e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49bc4",
      "incomplete_value": false,
      "site": "00b49bc8",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e40",
      "incomplete_value": false,
      "site": "00ae9e44",
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
            "const:c5:8"
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9e2c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9e30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b49bb0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49bb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00ae9e3c ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae9e40 ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49bc0 ["COPY", "register:4018:8", ["const:2b7000:8"]]
+ 00b49bc4 ["COPY", "tmp:0:8", ["const:c34:8"]]
- 00ae9e44 ["INT_ADD", "register:40f0:8", ["const:ae9e44:8", "const:4:8"]]
+ 00b49bc8 ["INT_ADD", "register:40f0:8", ["const:b49bc8:8", "const:4:8"]]
~~~


### [`00ae9e60`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md) → [`00b49be4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00b49c10",
      "incomplete_value": true,
      "site": "00b49c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e8c",
      "incomplete_value": true,
      "site": "00ae9e8c",
      "value": [
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
      "definition_site": "00b49bf8",
      "incomplete_value": true,
      "site": "00b49bf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e74",
      "incomplete_value": true,
      "site": "00ae9e74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49c00",
      "incomplete_value": false,
      "site": "00b49c08",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9e7c",
      "incomplete_value": false,
      "site": "00ae9e84",
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
            "const:c5:8"
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9e6c ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9e70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b49bf0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00ae9e78 ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae9e7c ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49bfc ["COPY", "register:4018:8", ["const:2b7000:8"]]
+ 00b49c00 ["COPY", "tmp:0:8", ["const:c34:8"]]
- 00ae9e84 ["INT_ADD", "register:40f0:8", ["const:ae9e84:8", "const:4:8"]]
+ 00b49c08 ["INT_ADD", "register:40f0:8", ["const:b49c08:8", "const:4:8"]]
~~~


### [`00ae9ea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ea0.md) → [`00b49c24`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49c54",
      "incomplete_value": true,
      "site": "00b49c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ed0",
      "incomplete_value": true,
      "site": "00ae9ed0",
      "value": [
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
      "definition_site": "00b49c38",
      "incomplete_value": true,
      "site": "00b49c38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9eb4",
      "incomplete_value": true,
      "site": "00ae9eb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00ae9ec4",
      "incomplete_value": false,
      "site": "00ae9ec8",
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9eac ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b49c30 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49c34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00ae9eb8 ["COPY", "register:4018:8", ["const:2a7000:8"]]
+ 00b49c3c ["COPY", "register:4018:8", ["const:2b7000:8"]]
- 00ae9ec0 ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49c44 ["COPY", "tmp:0:8", ["const:c34:8"]]
~~~


### [`00ae9ee4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md) → [`00b49c68`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49c98",
      "incomplete_value": true,
      "site": "00b49c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9f14",
      "incomplete_value": true,
      "site": "00ae9f14",
      "value": [
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
      "definition_site": "00b49c7c",
      "incomplete_value": true,
      "site": "00b49c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ef8",
      "incomplete_value": true,
      "site": "00ae9ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49c84",
      "incomplete_value": false,
      "site": "00b49c90",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9f00",
      "incomplete_value": false,
      "site": "00ae9f0c",
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
            "const:c5:8"
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9ef0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00ae9ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b49c74 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00ae9efc ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00ae9f00 ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49c80 ["COPY", "register:4018:8", ["const:2b7000:8"]]
+ 00b49c84 ["COPY", "tmp:0:8", ["const:c34:8"]]
- 00ae9f0c ["INT_ADD", "register:40f0:8", ["const:ae9f0c:8", "const:4:8"]]
+ 00b49c90 ["INT_ADD", "register:40f0:8", ["const:b49c90:8", "const:4:8"]]
~~~


### [`00ae9f34`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9f34.md) → [`00b49cb8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49d40",
      "incomplete_value": true,
      "site": "00b49d40",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9fbc",
      "incomplete_value": true,
      "site": "00ae9fbc",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49cec",
      "incomplete_value": true,
      "site": "00b49cf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:640:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9f68",
      "incomplete_value": true,
      "site": "00ae9f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a0788",
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
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9f44 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9f48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00b49cc8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49ccc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
- 00ae9f54 ["BRANCH", null, ["local:b7:8"]]
+ 00b49cd8 ["BRANCH", null, ["local:b6:8"]]
- 00ae9f5c ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b49ce0 ["COPY", "register:4048:8", ["const:1125000:8"]]
~~~


### [`00ae9fd0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md) → [`00b49d54`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b49d90",
      "incomplete_value": true,
      "site": "00b49d90",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea00c",
      "incomplete_value": true,
      "site": "00aea00c",
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
      "definition_site": "00b49de0",
      "incomplete_value": true,
      "site": "00b49de0",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea05c",
      "incomplete_value": true,
      "site": "00aea05c",
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
      "definition_site": "00b49d6c",
      "incomplete_value": true,
      "site": "00b49d6c",
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
      "definition_site": "00ae9fe8",
      "incomplete_value": true,
      "site": "00ae9fe8",
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a0788",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00ae9fe0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00ae9fe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b49d64 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49d68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00ae9fe8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae9fec ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00ae9ff0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00b49d6c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b49d70 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49d74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
- 00ae9ff8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b49d7c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
~~~


### [`00aea070`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md) → [`00b49df4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49e34",
      "incomplete_value": true,
      "site": "00b49e34",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea0b0",
      "incomplete_value": true,
      "site": "00aea0b0",
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
      "definition_site": "00b49e10",
      "incomplete_value": true,
      "site": "00b49e10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea08c",
      "incomplete_value": true,
      "site": "00aea08c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49e18",
      "incomplete_value": false,
      "site": "00b49e2c",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea094",
      "incomplete_value": false,
      "site": "00aea0a8",
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
            "const:c5:8"
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea07c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49e00 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b49e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00aea090 ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00aea094 ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49e14 ["COPY", "register:4018:8", ["const:2b7000:8"]]
+ 00b49e18 ["COPY", "tmp:0:8", ["const:c34:8"]]
~~~


### [`00aea0e0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md) → [`00b49e64`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde410`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde410.md) · 呼出先 1件 [`00bde180`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5ae90`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae90.md) · 呼出先 1件 [`00c5ac00`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49e80",
      "incomplete_value": false,
      "site": "00b49e84",
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
      "definition_site": "00aea0fc",
      "incomplete_value": false,
      "site": "00aea100",
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
      "definition_site": "00b49e90",
      "incomplete_value": true,
      "site": "00b49e9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea10c",
      "incomplete_value": true,
      "site": "00aea118",
      "value": [
        "LOAD",
        "8",
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
        "010a0790",
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
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea0f8 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00aea0fc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b49e7c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b49e80 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00aea100 ["INT_ADD", "register:40f0:8", ["const:aea100:8", "const:4:8"]]
+ 00b49e84 ["INT_ADD", "register:40f0:8", ["const:b49e84:8", "const:4:8"]]
- 00aea104 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00aea108 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00b49e88 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49e8c ["COPY", "tmp:0:8", ["const:650:8"]]
~~~


### [`00aea11c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md) → [`00b49ea0`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49ee0",
      "incomplete_value": true,
      "site": "00b49ee0",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea15c",
      "incomplete_value": true,
      "site": "00aea15c",
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
      "definition_site": "00b49ebc",
      "incomplete_value": true,
      "site": "00b49ebc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea138",
      "incomplete_value": true,
      "site": "00aea138",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49ec4",
      "incomplete_value": false,
      "site": "00b49ed8",
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
            "const:c34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea140",
      "incomplete_value": false,
      "site": "00aea154",
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
            "const:c5:8"
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
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a0780",
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
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea128 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49eac ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b49eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00aea13c ["COPY", "register:4018:8", ["const:2a7000:8"]]
- 00aea140 ["COPY", "tmp:0:8", ["const:c5:8"]]
+ 00b49ec0 ["COPY", "register:4018:8", ["const:2b7000:8"]]
+ 00b49ec4 ["COPY", "tmp:0:8", ["const:c34:8"]]
~~~


### [`00aea18c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md) → [`00b49f10`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b49f2c",
      "incomplete_value": false,
      "site": "00b49f30",
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
      "definition_site": "00aea1a8",
      "incomplete_value": false,
      "site": "00aea1ac",
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
      "definition_site": "00b49f3c",
      "incomplete_value": true,
      "site": "00b49f48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea1b8",
      "incomplete_value": true,
      "site": "00aea1c4",
      "value": [
        "LOAD",
        "8",
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
        "010a07a0",
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
        "01125660",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea1a4 ["COPY", "register:4000:8", ["const:299000:8"]]
- 00aea1a8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b49f28 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b49f2c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00aea1ac ["INT_ADD", "register:40f0:8", ["const:aea1ac:8", "const:4:8"]]
+ 00b49f30 ["INT_ADD", "register:40f0:8", ["const:b49f30:8", "const:4:8"]]
- 00aea1b0 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00aea1b4 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00b49f34 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49f38 ["COPY", "tmp:0:8", ["const:660:8"]]
~~~


### [`00aea1c8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md) → [`00b49f4c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b49f78",
      "incomplete_value": true,
      "site": "00b49f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea1f4",
      "incomplete_value": true,
      "site": "00aea1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00b49f60",
      "incomplete_value": true,
      "site": "00b49f60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea1dc",
      "incomplete_value": true,
      "site": "00aea1dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49f6c",
      "incomplete_value": false,
      "site": "00b49f70",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea1e8",
      "incomplete_value": false,
      "site": "00aea1ec",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea1d4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00aea1d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b49f58 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49f5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00aea1e4 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00aea1e8 ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b49f68 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00b49f6c ["COPY", "tmp:0:8", ["const:ad1:8"]]
- 00aea1ec ["INT_ADD", "register:40f0:8", ["const:aea1ec:8", "const:4:8"]]
+ 00b49f70 ["INT_ADD", "register:40f0:8", ["const:b49f70:8", "const:4:8"]]
~~~


### [`00aea208`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md) → [`00b49f8c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b49fb8",
      "incomplete_value": true,
      "site": "00b49fb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea234",
      "incomplete_value": true,
      "site": "00aea234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00b49fa0",
      "incomplete_value": true,
      "site": "00b49fa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea21c",
      "incomplete_value": true,
      "site": "00aea21c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49fa8",
      "incomplete_value": false,
      "site": "00b49fb0",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea224",
      "incomplete_value": false,
      "site": "00aea22c",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea214 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00aea218 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b49f98 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00aea220 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00aea224 ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b49fa4 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00b49fa8 ["COPY", "tmp:0:8", ["const:ad1:8"]]
- 00aea22c ["INT_ADD", "register:40f0:8", ["const:aea22c:8", "const:4:8"]]
+ 00b49fb0 ["INT_ADD", "register:40f0:8", ["const:b49fb0:8", "const:4:8"]]
~~~


### [`00aea248`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md) → [`00b49fcc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49ffc",
      "incomplete_value": true,
      "site": "00b49ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea278",
      "incomplete_value": true,
      "site": "00aea278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00b49fe0",
      "incomplete_value": true,
      "site": "00b49fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea25c",
      "incomplete_value": true,
      "site": "00aea25c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49fec",
      "incomplete_value": false,
      "site": "00b49ff4",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea268",
      "incomplete_value": false,
      "site": "00aea270",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea254 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00aea258 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b49fd8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00aea260 ["COPY", "register:4018:8", ["const:2b0000:8"]]
+ 00b49fe4 ["COPY", "register:4018:8", ["const:2c1000:8"]]
- 00aea268 ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b49fec ["COPY", "tmp:0:8", ["const:ad1:8"]]
~~~


### [`00aea28c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md) → [`00b4a010`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a040",
      "incomplete_value": true,
      "site": "00b4a040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea2bc",
      "incomplete_value": true,
      "site": "00aea2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00b4a024",
      "incomplete_value": true,
      "site": "00b4a024",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea2a0",
      "incomplete_value": true,
      "site": "00aea2a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4a02c",
      "incomplete_value": false,
      "site": "00b4a038",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea2a8",
      "incomplete_value": false,
      "site": "00aea2b4",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea298 ["COPY", "register:4098:8", ["const:10a0000:8"]]
- 00aea29c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
+ 00b4a01c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a020 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00aea2a4 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00aea2a8 ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b4a028 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00b4a02c ["COPY", "tmp:0:8", ["const:ad1:8"]]
- 00aea2b4 ["INT_ADD", "register:40f0:8", ["const:aea2b4:8", "const:4:8"]]
+ 00b4a038 ["INT_ADD", "register:40f0:8", ["const:b4a038:8", "const:4:8"]]
~~~


### [`00aea2dc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md) → [`00b4a060`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4a0e8",
      "incomplete_value": true,
      "site": "00b4a0e8",
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
      "definition_site": "00aea364",
      "incomplete_value": true,
      "site": "00aea364",
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
            "const:7b0:8"
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
      "definition_site": "00b4a094",
      "incomplete_value": true,
      "site": "00b4a0a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:668:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea310",
      "incomplete_value": true,
      "site": "00aea31c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
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
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "010a07b0",
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
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea2ec ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00aea2f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b0:8"]]
+ 00b4a070 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4a074 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:670:8"]]
- 00aea304 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b4a088 ["COPY", "register:4048:8", ["const:1125000:8"]]
- 00aea310 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7a8:8"]]
+ 00b4a094 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:668:8"]]
~~~


### [`00aea378`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md) → [`00b4a0fc`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4a138",
      "incomplete_value": true,
      "site": "00b4a138",
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
      "definition_site": "00aea3b4",
      "incomplete_value": true,
      "site": "00aea3b4",
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
            "const:7b0:8"
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
      "definition_site": "00b4a188",
      "incomplete_value": true,
      "site": "00b4a188",
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
      "definition_site": "00aea404",
      "incomplete_value": true,
      "site": "00aea404",
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
            "const:7a8:8"
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
      "definition_site": "00b4a114",
      "incomplete_value": true,
      "site": "00b4a114",
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
      "definition_site": "00aea390",
      "incomplete_value": true,
      "site": "00aea390",
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "010a07b0",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea388 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
- 00aea38c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b4a10c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a110 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00aea394 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
- 00aea398 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7b0:8"]]
+ 00b4a118 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4a11c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:670:8"]]
- 00aea3b0 ["INT_ADD", "register:40f0:8", ["const:aea3b0:8", "const:4:8"]]
+ 00b4a134 ["INT_ADD", "register:40f0:8", ["const:b4a134:8", "const:4:8"]]
~~~


### [`00aea418`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md) → [`00b4a19c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a1dc",
      "incomplete_value": true,
      "site": "00b4a1dc",
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
      "definition_site": "00aea458",
      "incomplete_value": true,
      "site": "00aea458",
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
            "const:7a8:8"
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
      "definition_site": "00b4a1b8",
      "incomplete_value": true,
      "site": "00b4a1b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea434",
      "incomplete_value": true,
      "site": "00aea434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4a1c0",
      "incomplete_value": false,
      "site": "00b4a1d4",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea43c",
      "incomplete_value": false,
      "site": "00aea450",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea424 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a1a8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea42c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b4a1b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00aea438 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00aea43c ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b4a1bc ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00b4a1c0 ["COPY", "tmp:0:8", ["const:ad1:8"]]
~~~


### [`00aea488`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md) → [`00b4a20c`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4a228",
      "incomplete_value": false,
      "site": "00b4a22c",
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
      "definition_site": "00aea4a4",
      "incomplete_value": false,
      "site": "00aea4a8",
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
      "definition_site": "00b4a238",
      "incomplete_value": true,
      "site": "00b4a244",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea4b4",
      "incomplete_value": true,
      "site": "00aea4c0",
      "value": [
        "LOAD",
        "8",
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
        "010a07b8",
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
        "01125678",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea4a0 ["COPY", "register:4000:8", ["const:298000:8"]]
- 00aea4a4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4a224 ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00b4a228 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00aea4a8 ["INT_ADD", "register:40f0:8", ["const:aea4a8:8", "const:4:8"]]
+ 00b4a22c ["INT_ADD", "register:40f0:8", ["const:b4a22c:8", "const:4:8"]]
- 00aea4ac ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00aea4b0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00b4a230 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a234 ["COPY", "tmp:0:8", ["const:678:8"]]
~~~


### [`00aea4c4`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md) → [`00b4a248`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4a288",
      "incomplete_value": true,
      "site": "00b4a288",
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
      "definition_site": "00aea504",
      "incomplete_value": true,
      "site": "00aea504",
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
            "const:7a8:8"
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
      "definition_site": "00b4a264",
      "incomplete_value": true,
      "site": "00b4a264",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4e0",
      "incomplete_value": true,
      "site": "00aea4e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4a26c",
      "incomplete_value": false,
      "site": "00b4a280",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea4e8",
      "incomplete_value": false,
      "site": "00aea4fc",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea4d0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a254 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea4d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00b4a25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00aea4e4 ["COPY", "register:4018:8", ["const:2b0000:8"]]
- 00aea4e8 ["COPY", "tmp:0:8", ["const:4bb:8"]]
+ 00b4a268 ["COPY", "register:4018:8", ["const:2c1000:8"]]
+ 00b4a26c ["COPY", "tmp:0:8", ["const:ad1:8"]]
~~~


### [`00aea534`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md) → [`00b4a2b8`](https://github.com/sinsuirakv0/KBCS/blob/46968f5ead1722cc1c84c5c58eea80a8dbeac93d/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4a2d4",
      "incomplete_value": false,
      "site": "00b4a2d8",
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
      "definition_site": "00aea550",
      "incomplete_value": false,
      "site": "00aea554",
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
      "definition_site": "00b4a2e4",
      "incomplete_value": true,
      "site": "00b4a2f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea560",
      "incomplete_value": true,
      "site": "00aea56c",
      "value": [
        "LOAD",
        "8",
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
        "010a07c8",
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
        "01125688",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00aea54c ["COPY", "register:4000:8", ["const:299000:8"]]
- 00aea550 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4a2d0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 00b4a2d4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00aea554 ["INT_ADD", "register:40f0:8", ["const:aea554:8", "const:4:8"]]
+ 00b4a2d8 ["INT_ADD", "register:40f0:8", ["const:b4a2d8:8", "const:4:8"]]
- 00aea558 ["COPY", "register:4040:8", ["const:10a0000:8"]]
- 00aea55c ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00b4a2dc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a2e0 ["COPY", "tmp:0:8", ["const:688:8"]]
~~~


