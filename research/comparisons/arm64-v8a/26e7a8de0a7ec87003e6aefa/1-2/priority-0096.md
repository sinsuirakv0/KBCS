# v16.0.2 → v16.0.3 · 最優先の変更候補 (96)

[一覧の目次](README.md)

### [`00bd66d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd66d8.md) → [`00bd76cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd76cc.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd76fc",
      "incomplete_value": true,
      "site": "00bd76fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6708",
      "incomplete_value": true,
      "site": "00bd6708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "definition_site": "00bd76e0",
      "incomplete_value": true,
      "site": "00bd76e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd66ec",
      "incomplete_value": true,
      "site": "00bd66ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd76e8",
      "incomplete_value": false,
      "site": "00bd76f4",
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
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd66f4",
      "incomplete_value": false,
      "site": "00bd6700",
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
            "const:cf4:8"
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
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b9cf4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126c28",
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
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b9dd2",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127be8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd66e4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd66e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c28:8"]]
+ 00bd76d8 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd76dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
- 00bd66f4 ["COPY", "tmp:0:8", ["const:cf4:8"]]
+ 00bd76e8 ["COPY", "tmp:0:8", ["const:dd2:8"]]
- 00bd6700 ["INT_ADD", "register:40f0:8", ["const:bd6700:8", "const:4:8"]]
+ 00bd76f4 ["INT_ADD", "register:40f0:8", ["const:bd76f4:8", "const:4:8"]]
~~~


### [`00bd6728`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6728.md) → [`00bd771c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd771c.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7774",
      "incomplete_value": true,
      "site": "00bd7774",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6780",
      "incomplete_value": true,
      "site": "00bd6780",
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
            "const:c30:8"
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
        "01126c30",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126c30",
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
        "01127bf0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127bf0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6738 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd673c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c30:8"]]
+ 00bd772c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd7730 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bf0:8"]]
- 00bd6750 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd7744 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd675c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c28:8"]]
+ 00bd7750 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be8:8"]]
~~~


### [`00bd6794`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6794.md) → [`00bd7788`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7788.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd77c4",
      "incomplete_value": true,
      "site": "00bd77c4",
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
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd67d0",
      "incomplete_value": true,
      "site": "00bd67d0",
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
            "const:c30:8"
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
      "definition_site": "00bd77e4",
      "incomplete_value": true,
      "site": "00bd77e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd67f0",
      "incomplete_value": true,
      "site": "00bd67f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "definition_site": "00bd77a0",
      "incomplete_value": true,
      "site": "00bd77a0",
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
      "definition_site": "00bd67ac",
      "incomplete_value": true,
      "site": "00bd67ac",
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
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126c30",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126c30",
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
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127bf0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127bf0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd67a4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd67a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
+ 00bd7798 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd779c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00bd67b0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd67b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c30:8"]]
+ 00bd77a4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd77a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bf0:8"]]
- 00bd67cc ["INT_ADD", "register:40f0:8", ["const:bd67cc:8", "const:4:8"]]
+ 00bd77c0 ["INT_ADD", "register:40f0:8", ["const:bd77c0:8", "const:4:8"]]
~~~


### [`00bd6804`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6804.md) → [`00bd77f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd77f8.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7838",
      "incomplete_value": true,
      "site": "00bd7838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6844",
      "incomplete_value": true,
      "site": "00bd6844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9cf4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c28",
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
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9dd2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127be8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6810 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd7804 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd6818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
+ 00bd780c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00bd6828 ["COPY", "tmp:0:8", ["const:cf4:8"]]
+ 00bd781c ["COPY", "tmp:0:8", ["const:dd2:8"]]
~~~


### [`00bd6874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6874.md) → [`00bd7868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7868.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7884",
      "incomplete_value": false,
      "site": "00bd7888",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6890",
      "incomplete_value": false,
      "site": "00bd6894",
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
            "const:30b:8"
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126c38",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127bf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6890 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd7884 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd6894 ["INT_ADD", "register:40f0:8", ["const:bd6894:8", "const:4:8"]]
+ 00bd7888 ["INT_ADD", "register:40f0:8", ["const:bd7888:8", "const:4:8"]]
- 00bd6898 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd689c ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00bd788c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd7890 ["COPY", "tmp:0:8", ["const:bf8:8"]]
~~~


### [`00bd68b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd68b0.md) → [`00bd78a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd78a4.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd78e4",
      "incomplete_value": true,
      "site": "00bd78e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68f0",
      "incomplete_value": true,
      "site": "00bd68f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "definition_site": "00bd78c0",
      "incomplete_value": true,
      "site": "00bd78c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68cc",
      "incomplete_value": true,
      "site": "00bd68cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd78c8",
      "incomplete_value": false,
      "site": "00bd78dc",
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
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68d4",
      "incomplete_value": false,
      "site": "00bd68e8",
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
            "const:cf4:8"
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
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9cf4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c28",
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
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b9dd2",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127be8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd68bc ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd78b0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd68c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
+ 00bd78b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00bd68d4 ["COPY", "tmp:0:8", ["const:cf4:8"]]
+ 00bd78c8 ["COPY", "tmp:0:8", ["const:dd2:8"]]
~~~


### [`00bd6920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6920.md) → [`00bd7914`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7914.md) _ZN8firebase4auth13oauthprovider10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7930",
      "incomplete_value": false,
      "site": "00bd7934",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd693c",
      "incomplete_value": false,
      "site": "00bd6940",
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
            "const:54d:8"
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
      "definition_site": "00bd7940",
      "incomplete_value": true,
      "site": "00bd794c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd694c",
      "incomplete_value": true,
      "site": "00bd6958",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126c50",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127c10",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd693c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd7930 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd6940 ["INT_ADD", "register:40f0:8", ["const:bd6940:8", "const:4:8"]]
+ 00bd7934 ["INT_ADD", "register:40f0:8", ["const:bd7934:8", "const:4:8"]]
- 00bd6944 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd6948 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00bd7938 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd793c ["COPY", "tmp:0:8", ["const:c10:8"]]
~~~


### [`00bd695c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd695c.md) → [`00bd7950`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7950.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd797c",
      "incomplete_value": true,
      "site": "00bd797c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6988",
      "incomplete_value": true,
      "site": "00bd6988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd7964",
      "incomplete_value": true,
      "site": "00bd7964",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6970",
      "incomplete_value": true,
      "site": "00bd6970",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7970",
      "incomplete_value": false,
      "site": "00bd7974",
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
            "const:845:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd697c",
      "incomplete_value": false,
      "site": "00bd6980",
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
            "const:7fb:8"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6968 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd696c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00bd795c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
- 00bd697c ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd7970 ["COPY", "tmp:0:8", ["const:845:8"]]
- 00bd6980 ["INT_ADD", "register:40f0:8", ["const:bd6980:8", "const:4:8"]]
+ 00bd7974 ["INT_ADD", "register:40f0:8", ["const:bd7974:8", "const:4:8"]]
~~~


### [`00bd699c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd699c.md) → [`00bd7990`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7990.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd79bc",
      "incomplete_value": true,
      "site": "00bd79bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69c8",
      "incomplete_value": true,
      "site": "00bd69c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd79a4",
      "incomplete_value": true,
      "site": "00bd79a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69b0",
      "incomplete_value": true,
      "site": "00bd69b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00bd69b0"
      ],
      [
        "FALL_THROUGH",
        "00bd79a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bd79a4",
      "incomplete_value": true,
      "site": "00bd79bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69b0",
      "incomplete_value": true,
      "site": "00bd69c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd69a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd69ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00bd799c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd79a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
- 00bd69b8 ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd79ac ["COPY", "tmp:0:8", ["const:845:8"]]
- 00bd69c0 ["INT_ADD", "register:40f0:8", ["const:bd69c0:8", "const:4:8"]]
+ 00bd79b4 ["INT_ADD", "register:40f0:8", ["const:bd79b4:8", "const:4:8"]]
~~~


### [`00bd69dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd69dc.md) → [`00bd79d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd79d0.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7a00",
      "incomplete_value": true,
      "site": "00bd7a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6a0c",
      "incomplete_value": true,
      "site": "00bd6a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd79e4",
      "incomplete_value": true,
      "site": "00bd79e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69f0",
      "incomplete_value": true,
      "site": "00bd69f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd79f0",
      "incomplete_value": false,
      "site": "00bd79f8",
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
            "const:845:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd69fc",
      "incomplete_value": false,
      "site": "00bd6a04",
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
            "const:7fb:8"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd69e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd69ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00bd79dc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd79e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
- 00bd69fc ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd79f0 ["COPY", "tmp:0:8", ["const:845:8"]]
- 00bd6a04 ["INT_ADD", "register:40f0:8", ["const:bd6a04:8", "const:4:8"]]
+ 00bd79f8 ["INT_ADD", "register:40f0:8", ["const:bd79f8:8", "const:4:8"]]
~~~


### [`00bd6a20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6a20.md) → [`00bd7a14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7a14.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7a44",
      "incomplete_value": true,
      "site": "00bd7a44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6a50",
      "incomplete_value": true,
      "site": "00bd6a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6a2c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00bd7a20 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
- 00bd6a3c ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd7a30 ["COPY", "tmp:0:8", ["const:845:8"]]
- 00bd6a48 ["INT_ADD", "register:40f0:8", ["const:bd6a48:8", "const:4:8"]]
+ 00bd7a3c ["INT_ADD", "register:40f0:8", ["const:bd7a3c:8", "const:4:8"]]
~~~


### [`00bd6a70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6a70.md) → [`00bd7a64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7a64.md) _ZN8firebase4auth8timeunit15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7abc",
      "incomplete_value": true,
      "site": "00bd7abc",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6ac8",
      "incomplete_value": true,
      "site": "00bd6ac8",
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
            "const:c60:8"
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
      "definition_site": "00bd7a98",
      "incomplete_value": true,
      "site": "00bd7aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:c18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6aa4",
      "incomplete_value": true,
      "site": "00bd6ab0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
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
        "01126c60",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126c60",
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
        "01127c20",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127c20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6a80 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd6a84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c60:8"]]
+ 00bd7a74 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd7a78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c20:8"]]
- 00bd6a98 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd7a8c ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd6aa4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c58:8"]]
+ 00bd7a98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c18:8"]]
~~~


### [`00bd6adc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6adc.md) → [`00bd7ad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7ad0.md) _ZN8firebase4auth8timeunit12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7b0c",
      "incomplete_value": true,
      "site": "00bd7b0c",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6b18",
      "incomplete_value": true,
      "site": "00bd6b18",
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
            "const:c60:8"
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
      "definition_site": "00bd7b2c",
      "incomplete_value": true,
      "site": "00bd7b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6b38",
      "incomplete_value": true,
      "site": "00bd6b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd7ae8",
      "incomplete_value": true,
      "site": "00bd7ae8",
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
      "definition_site": "00bd6af4",
      "incomplete_value": true,
      "site": "00bd6af4",
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126c60",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126c60",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127c20",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127c20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6aec ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd6af0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00bd7ae0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd7ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
- 00bd6af8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd6afc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c60:8"]]
+ 00bd7aec ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd7af0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c20:8"]]
- 00bd6b14 ["INT_ADD", "register:40f0:8", ["const:bd6b14:8", "const:4:8"]]
+ 00bd7b08 ["INT_ADD", "register:40f0:8", ["const:bd7b08:8", "const:4:8"]]
~~~


### [`00bd6b4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6b4c.md) → [`00bd7b40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7b40.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7b80",
      "incomplete_value": true,
      "site": "00bd7b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6b8c",
      "incomplete_value": true,
      "site": "00bd6b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd7b5c",
      "incomplete_value": true,
      "site": "00bd7b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6b68",
      "incomplete_value": true,
      "site": "00bd6b68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7b64",
      "incomplete_value": false,
      "site": "00bd7b78",
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
            "const:845:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6b70",
      "incomplete_value": false,
      "site": "00bd6b84",
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
            "const:7fb:8"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6b58 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd7b4c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd6b60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00bd7b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
- 00bd6b70 ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd7b64 ["COPY", "tmp:0:8", ["const:845:8"]]
~~~


### [`00bd6bbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6bbc.md) → [`00bd7bb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7bb0.md) _ZN8firebase4auth8timeunit11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7bcc",
      "incomplete_value": false,
      "site": "00bd7bd0",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6bd8",
      "incomplete_value": false,
      "site": "00bd6bdc",
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
            "const:30b:8"
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
      "definition_site": "00bd7bdc",
      "incomplete_value": true,
      "site": "00bd7be8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd6be8",
      "incomplete_value": true,
      "site": "00bd6bf4",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126c68",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127c28",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6bd8 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd7bcc ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd6bdc ["INT_ADD", "register:40f0:8", ["const:bd6bdc:8", "const:4:8"]]
+ 00bd7bd0 ["INT_ADD", "register:40f0:8", ["const:bd7bd0:8", "const:4:8"]]
- 00bd6be0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd6be4 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00bd7bd4 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd7bd8 ["COPY", "tmp:0:8", ["const:c28:8"]]
~~~


### [`00bd6bf8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6bf8.md) → [`00bd7bec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7bec.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7c2c",
      "incomplete_value": true,
      "site": "00bd7c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c38",
      "incomplete_value": true,
      "site": "00bd6c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bd7c08",
      "incomplete_value": true,
      "site": "00bd7c08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c14",
      "incomplete_value": true,
      "site": "00bd6c14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7c10",
      "incomplete_value": false,
      "site": "00bd7c24",
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
            "const:845:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c1c",
      "incomplete_value": false,
      "site": "00bd6c30",
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
            "const:7fb:8"
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
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b37fb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c58",
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
        "01127c18",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b3845",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6c04 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd7bf8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd6c0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00bd7c00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
- 00bd6c1c ["COPY", "tmp:0:8", ["const:7fb:8"]]
+ 00bd7c10 ["COPY", "tmp:0:8", ["const:845:8"]]
~~~


### [`00bd6c68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6c68.md) → [`00bd7c5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7c5c.md) _ZN8firebase4auth8timeunit10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7c78",
      "incomplete_value": false,
      "site": "00bd7c7c",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c84",
      "incomplete_value": false,
      "site": "00bd6c88",
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
            "const:54d:8"
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
      "definition_site": "00bd7c88",
      "incomplete_value": true,
      "site": "00bd7c94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd6c94",
      "incomplete_value": true,
      "site": "00bd6ca0",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126c70",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127c30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6c84 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd7c78 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd6c88 ["INT_ADD", "register:40f0:8", ["const:bd6c88:8", "const:4:8"]]
+ 00bd7c7c ["INT_ADD", "register:40f0:8", ["const:bd7c7c:8", "const:4:8"]]
- 00bd6c8c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd6c90 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00bd7c80 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd7c84 ["COPY", "tmp:0:8", ["const:c30:8"]]
~~~


### [`00bd6ca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6ca4.md) → [`00bd7c98`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7c98.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7cc4",
      "incomplete_value": true,
      "site": "00bd7cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cd0",
      "incomplete_value": true,
      "site": "00bd6cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7cac",
      "incomplete_value": true,
      "site": "00bd7cac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cb8",
      "incomplete_value": true,
      "site": "00bd6cb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7cb8",
      "incomplete_value": false,
      "site": "00bd7cbc",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cc4",
      "incomplete_value": false,
      "site": "00bd6cc8",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6cb0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6cb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00bd7ca4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7ca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00bd6cc4 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7cb8 ["COPY", "tmp:0:8", ["const:d24:8"]]
- 00bd6cc8 ["INT_ADD", "register:40f0:8", ["const:bd6cc8:8", "const:4:8"]]
+ 00bd7cbc ["INT_ADD", "register:40f0:8", ["const:bd7cbc:8", "const:4:8"]]
~~~


### [`00bd6ce4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6ce4.md) → [`00bd7cd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7cd8.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7d04",
      "incomplete_value": true,
      "site": "00bd7d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d10",
      "incomplete_value": true,
      "site": "00bd6d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7cec",
      "incomplete_value": true,
      "site": "00bd7cec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cf8",
      "incomplete_value": true,
      "site": "00bd6cf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7cf4",
      "incomplete_value": false,
      "site": "00bd7cfc",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d00",
      "incomplete_value": false,
      "site": "00bd6d08",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6cf0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6cf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00bd7ce4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7ce8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00bd6d00 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7cf4 ["COPY", "tmp:0:8", ["const:d24:8"]]
- 00bd6d08 ["INT_ADD", "register:40f0:8", ["const:bd6d08:8", "const:4:8"]]
+ 00bd7cfc ["INT_ADD", "register:40f0:8", ["const:bd7cfc:8", "const:4:8"]]
~~~


### [`00bd6d24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6d24.md) → [`00bd7d18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7d18.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7d48",
      "incomplete_value": true,
      "site": "00bd7d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d54",
      "incomplete_value": true,
      "site": "00bd6d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7d2c",
      "incomplete_value": true,
      "site": "00bd7d2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d38",
      "incomplete_value": true,
      "site": "00bd6d38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7d38",
      "incomplete_value": false,
      "site": "00bd7d40",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d44",
      "incomplete_value": false,
      "site": "00bd6d4c",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6d30 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6d34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00bd7d24 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7d28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00bd6d44 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7d38 ["COPY", "tmp:0:8", ["const:d24:8"]]
- 00bd6d4c ["INT_ADD", "register:40f0:8", ["const:bd6d4c:8", "const:4:8"]]
+ 00bd7d40 ["INT_ADD", "register:40f0:8", ["const:bd7d40:8", "const:4:8"]]
~~~


### [`00bd6d68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6d68.md) → [`00bd7d5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7d5c.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7d8c",
      "incomplete_value": true,
      "site": "00bd7d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d98",
      "incomplete_value": true,
      "site": "00bd6d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7d70",
      "incomplete_value": true,
      "site": "00bd7d70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d7c",
      "incomplete_value": true,
      "site": "00bd6d7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7d78",
      "incomplete_value": false,
      "site": "00bd7d84",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d84",
      "incomplete_value": false,
      "site": "00bd6d90",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6d74 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6d78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00bd7d68 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7d6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
- 00bd6d84 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7d78 ["COPY", "tmp:0:8", ["const:d24:8"]]
- 00bd6d90 ["INT_ADD", "register:40f0:8", ["const:bd6d90:8", "const:4:8"]]
+ 00bd7d84 ["INT_ADD", "register:40f0:8", ["const:bd7d84:8", "const:4:8"]]
~~~


### [`00bd6db8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6db8.md) → [`00bd7dac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7dac.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7e04",
      "incomplete_value": true,
      "site": "00bd7e04",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6e10",
      "incomplete_value": true,
      "site": "00bd6e10",
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
            "const:c80:8"
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
      "definition_site": "00bd7de0",
      "incomplete_value": true,
      "site": "00bd7dec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6dec",
      "incomplete_value": true,
      "site": "00bd6df8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
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
        "01126c80",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126c80",
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
        "01127c40",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127c40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6dc8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd6dcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c80:8"]]
+ 00bd7dbc ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd7dc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c40:8"]]
- 00bd6de0 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd7dd4 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd6dec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
+ 00bd7de0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c38:8"]]
~~~


### [`00bd6e24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6e24.md) → [`00bd7e18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7e18.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7e54",
      "incomplete_value": true,
      "site": "00bd7e54",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6e60",
      "incomplete_value": true,
      "site": "00bd6e60",
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
            "const:c80:8"
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
      "definition_site": "00bd7e74",
      "incomplete_value": true,
      "site": "00bd7e74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6e80",
      "incomplete_value": true,
      "site": "00bd6e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7e30",
      "incomplete_value": true,
      "site": "00bd7e30",
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
      "definition_site": "00bd6e3c",
      "incomplete_value": true,
      "site": "00bd6e3c",
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126c80",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126c80",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127c40",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127c40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6e34 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd6e38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00bd7e28 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd7e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00bd6e40 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd6e44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c80:8"]]
+ 00bd7e34 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd7e38 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c40:8"]]
- 00bd6e5c ["INT_ADD", "register:40f0:8", ["const:bd6e5c:8", "const:4:8"]]
+ 00bd7e50 ["INT_ADD", "register:40f0:8", ["const:bd7e50:8", "const:4:8"]]
~~~


### [`00bd6e94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6e94.md) → [`00bd7e88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7e88.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7ec8",
      "incomplete_value": true,
      "site": "00bd7ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6ed4",
      "incomplete_value": true,
      "site": "00bd6ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7ea4",
      "incomplete_value": true,
      "site": "00bd7ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6eb0",
      "incomplete_value": true,
      "site": "00bd6eb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7eac",
      "incomplete_value": false,
      "site": "00bd7ec0",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6eb8",
      "incomplete_value": false,
      "site": "00bd6ecc",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6ea0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd7e94 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd6ea8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00bd7e9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00bd6eb8 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7eac ["COPY", "tmp:0:8", ["const:d24:8"]]
~~~


### [`00bd6f04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6f04.md) → [`00bd7ef8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7ef8.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7f14",
      "incomplete_value": false,
      "site": "00bd7f18",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6f20",
      "incomplete_value": false,
      "site": "00bd6f24",
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
            "const:30b:8"
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
      "definition_site": "00bd7f24",
      "incomplete_value": true,
      "site": "00bd7f30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd6f30",
      "incomplete_value": true,
      "site": "00bd6f3c",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126c88",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127c48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6f20 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd7f14 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd6f24 ["INT_ADD", "register:40f0:8", ["const:bd6f24:8", "const:4:8"]]
+ 00bd7f18 ["INT_ADD", "register:40f0:8", ["const:bd7f18:8", "const:4:8"]]
- 00bd6f28 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd6f2c ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00bd7f1c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd7f20 ["COPY", "tmp:0:8", ["const:c48:8"]]
~~~


### [`00bd6f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6f40.md) → [`00bd7f34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7f34.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd7f74",
      "incomplete_value": true,
      "site": "00bd7f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6f80",
      "incomplete_value": true,
      "site": "00bd6f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "00bd7f50",
      "incomplete_value": true,
      "site": "00bd7f50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6f5c",
      "incomplete_value": true,
      "site": "00bd6f5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd7f58",
      "incomplete_value": false,
      "site": "00bd7f6c",
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
            "const:d24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6f64",
      "incomplete_value": false,
      "site": "00bd6f78",
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
            "const:ce4:8"
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
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fce4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126c78",
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
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "0029fd24",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6f4c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd7f40 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd6f54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00bd7f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00bd6f64 ["COPY", "tmp:0:8", ["const:ce4:8"]]
+ 00bd7f58 ["COPY", "tmp:0:8", ["const:d24:8"]]
~~~


### [`00bd6fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6fb0.md) → [`00bd7fa4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7fa4.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7fc0",
      "incomplete_value": false,
      "site": "00bd7fc4",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6fcc",
      "incomplete_value": false,
      "site": "00bd6fd0",
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
            "const:54d:8"
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
      "definition_site": "00bd7fd0",
      "incomplete_value": true,
      "site": "00bd7fdc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd6fdc",
      "incomplete_value": true,
      "site": "00bd6fe8",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126cc8",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127c88",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6fcc ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd7fc0 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd6fd0 ["INT_ADD", "register:40f0:8", ["const:bd6fd0:8", "const:4:8"]]
+ 00bd7fc4 ["INT_ADD", "register:40f0:8", ["const:bd7fc4:8", "const:4:8"]]
- 00bd6fd4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd6fd8 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00bd7fc8 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd7fcc ["COPY", "tmp:0:8", ["const:c88:8"]]
~~~


### [`00bd6fec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd6/00bd6fec.md) → [`00bd7fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd7/00bd7fe0.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd800c",
      "incomplete_value": true,
      "site": "00bd800c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7018",
      "incomplete_value": true,
      "site": "00bd7018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd7ff4",
      "incomplete_value": true,
      "site": "00bd7ff4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7000",
      "incomplete_value": true,
      "site": "00bd7000",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8000",
      "incomplete_value": false,
      "site": "00bd8004",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd700c",
      "incomplete_value": false,
      "site": "00bd7010",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd6ff8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd6ffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00bd7fec ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd7ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00bd700c ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd8000 ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00bd7010 ["INT_ADD", "register:40f0:8", ["const:bd7010:8", "const:4:8"]]
+ 00bd8004 ["INT_ADD", "register:40f0:8", ["const:bd8004:8", "const:4:8"]]
~~~


### [`00bd702c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd702c.md) → [`00bd8020`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8020.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd804c",
      "incomplete_value": true,
      "site": "00bd804c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7058",
      "incomplete_value": true,
      "site": "00bd7058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd8034",
      "incomplete_value": true,
      "site": "00bd8034",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7040",
      "incomplete_value": true,
      "site": "00bd7040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd803c",
      "incomplete_value": false,
      "site": "00bd8044",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7048",
      "incomplete_value": false,
      "site": "00bd7050",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7038 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd703c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00bd802c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00bd7048 ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd803c ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00bd7050 ["INT_ADD", "register:40f0:8", ["const:bd7050:8", "const:4:8"]]
+ 00bd8044 ["INT_ADD", "register:40f0:8", ["const:bd8044:8", "const:4:8"]]
~~~


### [`00bd706c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd706c.md) → [`00bd8060`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8060.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8090",
      "incomplete_value": true,
      "site": "00bd8090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd709c",
      "incomplete_value": true,
      "site": "00bd709c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd8074",
      "incomplete_value": true,
      "site": "00bd8074",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7080",
      "incomplete_value": true,
      "site": "00bd7080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8080",
      "incomplete_value": false,
      "site": "00bd8088",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd708c",
      "incomplete_value": false,
      "site": "00bd7094",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7078 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd707c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00bd806c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00bd708c ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd8080 ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00bd7094 ["INT_ADD", "register:40f0:8", ["const:bd7094:8", "const:4:8"]]
+ 00bd8088 ["INT_ADD", "register:40f0:8", ["const:bd8088:8", "const:4:8"]]
~~~


### [`00bd70b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd70b0.md) → [`00bd80a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd80a4.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd80d4",
      "incomplete_value": true,
      "site": "00bd80d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd70e0",
      "incomplete_value": true,
      "site": "00bd70e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd80b8",
      "incomplete_value": true,
      "site": "00bd80b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd70c4",
      "incomplete_value": true,
      "site": "00bd70c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd80c0",
      "incomplete_value": false,
      "site": "00bd80cc",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd70cc",
      "incomplete_value": false,
      "site": "00bd70d8",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd70bc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd70c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00bd80b0 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd80b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00bd70cc ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd80c0 ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00bd70d8 ["INT_ADD", "register:40f0:8", ["const:bd70d8:8", "const:4:8"]]
+ 00bd80cc ["INT_ADD", "register:40f0:8", ["const:bd80cc:8", "const:4:8"]]
~~~


### [`00bd7100`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7100.md) → [`00bd80f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd80f4.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd814c",
      "incomplete_value": true,
      "site": "00bd814c",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7158",
      "incomplete_value": true,
      "site": "00bd7158",
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
            "const:cd8:8"
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
      "definition_site": "00bd8128",
      "incomplete_value": true,
      "site": "00bd8134",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:c90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7134",
      "incomplete_value": true,
      "site": "00bd7140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
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
        "01126cd8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126cd8",
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
        "01127c98",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127c98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7110 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd7114 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cd8:8"]]
+ 00bd8104 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8108 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
- 00bd7128 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd811c ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd7134 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cd0:8"]]
+ 00bd8128 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
~~~


### [`00bd716c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd716c.md) → [`00bd8160`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8160.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd819c",
      "incomplete_value": true,
      "site": "00bd819c",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd71a8",
      "incomplete_value": true,
      "site": "00bd71a8",
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
            "const:cd8:8"
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
      "definition_site": "00bd81bc",
      "incomplete_value": true,
      "site": "00bd81bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd71c8",
      "incomplete_value": true,
      "site": "00bd71c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd8178",
      "incomplete_value": true,
      "site": "00bd8178",
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
      "definition_site": "00bd7184",
      "incomplete_value": true,
      "site": "00bd7184",
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126cd8",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127c98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd717c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd7180 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00bd8170 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd8174 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00bd7188 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd718c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cd8:8"]]
+ 00bd817c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8180 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c98:8"]]
- 00bd71a4 ["INT_ADD", "register:40f0:8", ["const:bd71a4:8", "const:4:8"]]
+ 00bd8198 ["INT_ADD", "register:40f0:8", ["const:bd8198:8", "const:4:8"]]
~~~


### [`00bd71dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd71dc.md) → [`00bd81d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd81d0.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8210",
      "incomplete_value": true,
      "site": "00bd8210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd721c",
      "incomplete_value": true,
      "site": "00bd721c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd81ec",
      "incomplete_value": true,
      "site": "00bd81ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd71f8",
      "incomplete_value": true,
      "site": "00bd71f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd81f4",
      "incomplete_value": false,
      "site": "00bd8208",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7200",
      "incomplete_value": false,
      "site": "00bd7214",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd71e8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd81dc ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd71f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00bd81e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00bd7200 ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd81f4 ["COPY", "tmp:0:8", ["const:d3c:8"]]
~~~


### [`00bd724c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd724c.md) → [`00bd8240`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8240.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd825c",
      "incomplete_value": false,
      "site": "00bd8260",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7268",
      "incomplete_value": false,
      "site": "00bd726c",
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
            "const:30b:8"
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
      "definition_site": "00bd826c",
      "incomplete_value": true,
      "site": "00bd8278",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7278",
      "incomplete_value": true,
      "site": "00bd7284",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126ce0",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7268 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd825c ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd726c ["INT_ADD", "register:40f0:8", ["const:bd726c:8", "const:4:8"]]
+ 00bd8260 ["INT_ADD", "register:40f0:8", ["const:bd8260:8", "const:4:8"]]
- 00bd7270 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7274 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00bd8264 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd8268 ["COPY", "tmp:0:8", ["const:ca0:8"]]
~~~


### [`00bd7288`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7288.md) → [`00bd827c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd827c.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd82bc",
      "incomplete_value": true,
      "site": "00bd82bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd72c8",
      "incomplete_value": true,
      "site": "00bd72c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
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
      "definition_site": "00bd8298",
      "incomplete_value": true,
      "site": "00bd8298",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd72a4",
      "incomplete_value": true,
      "site": "00bd72a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd82a0",
      "incomplete_value": false,
      "site": "00bd82b4",
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
            "const:d3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd72ac",
      "incomplete_value": false,
      "site": "00bd72c0",
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
            "const:cfc:8"
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
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1cfc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126cd0",
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
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a1d3c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7294 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8288 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd729c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00bd8290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00bd72ac ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 00bd82a0 ["COPY", "tmp:0:8", ["const:d3c:8"]]
~~~


### [`00bd72f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd72f8.md) → [`00bd82ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd82ec.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8308",
      "incomplete_value": false,
      "site": "00bd830c",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7314",
      "incomplete_value": false,
      "site": "00bd7318",
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
            "const:54d:8"
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
      "definition_site": "00bd8318",
      "incomplete_value": true,
      "site": "00bd8324",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7324",
      "incomplete_value": true,
      "site": "00bd7330",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126cf8",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127cb8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7314 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd8308 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd7318 ["INT_ADD", "register:40f0:8", ["const:bd7318:8", "const:4:8"]]
+ 00bd830c ["INT_ADD", "register:40f0:8", ["const:bd830c:8", "const:4:8"]]
- 00bd731c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7320 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00bd8310 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd8314 ["COPY", "tmp:0:8", ["const:cb8:8"]]
~~~


### [`00bd7334`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7334.md) → [`00bd8328`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8328.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8354",
      "incomplete_value": true,
      "site": "00bd8354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7360",
      "incomplete_value": true,
      "site": "00bd7360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd833c",
      "incomplete_value": true,
      "site": "00bd833c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7348",
      "incomplete_value": true,
      "site": "00bd7348",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8348",
      "incomplete_value": false,
      "site": "00bd834c",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7354",
      "incomplete_value": false,
      "site": "00bd7358",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7340 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7344 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bd8334 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cc0:8"]]
- 00bd7354 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd8348 ["COPY", "tmp:0:8", ["const:da4:8"]]
- 00bd7358 ["INT_ADD", "register:40f0:8", ["const:bd7358:8", "const:4:8"]]
+ 00bd834c ["INT_ADD", "register:40f0:8", ["const:bd834c:8", "const:4:8"]]
~~~


### [`00bd7374`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7374.md) → [`00bd8368`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8368.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8394",
      "incomplete_value": true,
      "site": "00bd8394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd73a0",
      "incomplete_value": true,
      "site": "00bd73a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd837c",
      "incomplete_value": true,
      "site": "00bd837c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7388",
      "incomplete_value": true,
      "site": "00bd7388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8384",
      "incomplete_value": false,
      "site": "00bd838c",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7390",
      "incomplete_value": false,
      "site": "00bd7398",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7380 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bd8374 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cc0:8"]]
- 00bd7390 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd8384 ["COPY", "tmp:0:8", ["const:da4:8"]]
- 00bd7398 ["INT_ADD", "register:40f0:8", ["const:bd7398:8", "const:4:8"]]
+ 00bd838c ["INT_ADD", "register:40f0:8", ["const:bd838c:8", "const:4:8"]]
~~~


### [`00bd73b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd73b4.md) → [`00bd83a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd83a8.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd83d8",
      "incomplete_value": true,
      "site": "00bd83d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd73e4",
      "incomplete_value": true,
      "site": "00bd73e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd83bc",
      "incomplete_value": true,
      "site": "00bd83bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd73c8",
      "incomplete_value": true,
      "site": "00bd73c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd83c8",
      "incomplete_value": false,
      "site": "00bd83d0",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd73d4",
      "incomplete_value": false,
      "site": "00bd73dc",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd73c0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd73c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bd83b4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd83b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cc0:8"]]
- 00bd73d4 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd83c8 ["COPY", "tmp:0:8", ["const:da4:8"]]
- 00bd73dc ["INT_ADD", "register:40f0:8", ["const:bd73dc:8", "const:4:8"]]
+ 00bd83d0 ["INT_ADD", "register:40f0:8", ["const:bd83d0:8", "const:4:8"]]
~~~


### [`00bd73f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd73f8.md) → [`00bd83ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd83ec.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd841c",
      "incomplete_value": true,
      "site": "00bd841c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7428",
      "incomplete_value": true,
      "site": "00bd7428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd8400",
      "incomplete_value": true,
      "site": "00bd8400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd740c",
      "incomplete_value": true,
      "site": "00bd740c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8408",
      "incomplete_value": false,
      "site": "00bd8414",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7414",
      "incomplete_value": false,
      "site": "00bd7420",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7404 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d00:8"]]
+ 00bd83f8 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd83fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cc0:8"]]
- 00bd7414 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd8408 ["COPY", "tmp:0:8", ["const:da4:8"]]
- 00bd7420 ["INT_ADD", "register:40f0:8", ["const:bd7420:8", "const:4:8"]]
+ 00bd8414 ["INT_ADD", "register:40f0:8", ["const:bd8414:8", "const:4:8"]]
~~~


### [`00bd7448`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7448.md) → [`00bd843c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd843c.md) _ZN8firebase4auth21oauthprovider_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8494",
      "incomplete_value": true,
      "site": "00bd8494",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd74a0",
      "incomplete_value": true,
      "site": "00bd74a0",
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
            "const:d08:8"
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
      "definition_site": "00bd8470",
      "incomplete_value": true,
      "site": "00bd847c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd747c",
      "incomplete_value": true,
      "site": "00bd7488",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
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
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126d08",
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
        "01127cc8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127cc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7458 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd745c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d08:8"]]
+ 00bd844c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
- 00bd7470 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd8464 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd747c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d00:8"]]
+ 00bd8470 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
~~~


### [`00bd74b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd74b4.md) → [`00bd84a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd84a8.md) _ZN8firebase4auth21oauthprovider_builder12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd84e4",
      "incomplete_value": true,
      "site": "00bd84e4",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd74f0",
      "incomplete_value": true,
      "site": "00bd74f0",
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
            "const:d08:8"
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
      "definition_site": "00bd8504",
      "incomplete_value": true,
      "site": "00bd8504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7510",
      "incomplete_value": true,
      "site": "00bd7510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd84c0",
      "incomplete_value": true,
      "site": "00bd84c0",
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
      "definition_site": "00bd74cc",
      "incomplete_value": true,
      "site": "00bd74cc",
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126d08",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126d08",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127cc8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127cc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd74c4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd74c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bd84b8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd84bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00bd74d0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd74d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d08:8"]]
+ 00bd84c4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd84c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
- 00bd74ec ["INT_ADD", "register:40f0:8", ["const:bd74ec:8", "const:4:8"]]
+ 00bd84e0 ["INT_ADD", "register:40f0:8", ["const:bd84e0:8", "const:4:8"]]
~~~


### [`00bd7524`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7524.md) → [`00bd8518`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8518.md) _ZN8firebase4auth21oauthprovider_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8558",
      "incomplete_value": true,
      "site": "00bd8558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7564",
      "incomplete_value": true,
      "site": "00bd7564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd8534",
      "incomplete_value": true,
      "site": "00bd8534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7540",
      "incomplete_value": true,
      "site": "00bd7540",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd853c",
      "incomplete_value": false,
      "site": "00bd8550",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7548",
      "incomplete_value": false,
      "site": "00bd755c",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7530 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8524 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bd852c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00bd7548 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd853c ["COPY", "tmp:0:8", ["const:da4:8"]]
~~~


### [`00bd7594`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7594.md) → [`00bd8588`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8588.md) _ZN8firebase4auth21oauthprovider_builder11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd85a4",
      "incomplete_value": false,
      "site": "00bd85a8",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd75b0",
      "incomplete_value": false,
      "site": "00bd75b4",
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
            "const:30b:8"
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
      "definition_site": "00bd85b4",
      "incomplete_value": true,
      "site": "00bd85c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd75c0",
      "incomplete_value": true,
      "site": "00bd75cc",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d10",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd75b0 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd85a4 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd75b4 ["INT_ADD", "register:40f0:8", ["const:bd75b4:8", "const:4:8"]]
+ 00bd85a8 ["INT_ADD", "register:40f0:8", ["const:bd85a8:8", "const:4:8"]]
- 00bd75b8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd75bc ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00bd85ac ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd85b0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
~~~


### [`00bd75d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd75d0.md) → [`00bd85c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd85c4.md) _ZN8firebase4auth21oauthprovider_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8604",
      "incomplete_value": true,
      "site": "00bd8604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7610",
      "incomplete_value": true,
      "site": "00bd7610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d00:8"
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
      "definition_site": "00bd85e0",
      "incomplete_value": true,
      "site": "00bd85e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd75ec",
      "incomplete_value": true,
      "site": "00bd75ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd85e8",
      "incomplete_value": false,
      "site": "00bd85fc",
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
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd75f4",
      "incomplete_value": false,
      "site": "00bd7608",
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
            "const:d5a:8"
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
        "01126d00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c0d5a",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d00",
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
        "01127cc0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002c0da4",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd75dc ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd85d0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd75e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d00:8"]]
+ 00bd85d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00bd75f4 ["COPY", "tmp:0:8", ["const:d5a:8"]]
+ 00bd85e8 ["COPY", "tmp:0:8", ["const:da4:8"]]
~~~


### [`00bd7640`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7640.md) → [`00bd8634`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8634.md) _ZN8firebase4auth21oauthprovider_builder10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8650",
      "incomplete_value": false,
      "site": "00bd8654",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd765c",
      "incomplete_value": false,
      "site": "00bd7660",
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
            "const:54d:8"
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
      "definition_site": "00bd8660",
      "incomplete_value": true,
      "site": "00bd866c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd766c",
      "incomplete_value": true,
      "site": "00bd7678",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d28",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127ce8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd765c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd8650 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd7660 ["INT_ADD", "register:40f0:8", ["const:bd7660:8", "const:4:8"]]
+ 00bd8654 ["INT_ADD", "register:40f0:8", ["const:bd8654:8", "const:4:8"]]
- 00bd7664 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7668 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00bd8658 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd865c ["COPY", "tmp:0:8", ["const:ce8:8"]]
~~~


### [`00bd767c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd767c.md) → [`00bd8670`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8670.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd869c",
      "incomplete_value": true,
      "site": "00bd869c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd76a8",
      "incomplete_value": true,
      "site": "00bd76a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "definition_site": "00bd8684",
      "incomplete_value": true,
      "site": "00bd8684",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7690",
      "incomplete_value": true,
      "site": "00bd7690",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8690",
      "incomplete_value": false,
      "site": "00bd8694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd769c",
      "incomplete_value": false,
      "site": "00bd76a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7688 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd768c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d30:8"]]
+ 00bd867c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00bd769c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd8690 ["COPY", "tmp:0:8", ["const:29d:8"]]
- 00bd76a0 ["INT_ADD", "register:40f0:8", ["const:bd76a0:8", "const:4:8"]]
+ 00bd8694 ["INT_ADD", "register:40f0:8", ["const:bd8694:8", "const:4:8"]]
~~~


### [`00bd76bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd76bc.md) → [`00bd86b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd86b0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd86dc",
      "incomplete_value": true,
      "site": "00bd86dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd76e8",
      "incomplete_value": true,
      "site": "00bd76e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "definition_site": "00bd86c4",
      "incomplete_value": true,
      "site": "00bd86c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd76d0",
      "incomplete_value": true,
      "site": "00bd76d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd86cc",
      "incomplete_value": false,
      "site": "00bd86d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd76d8",
      "incomplete_value": false,
      "site": "00bd76e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd76c8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd76cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d30:8"]]
+ 00bd86bc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd86c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00bd76d8 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd86cc ["COPY", "tmp:0:8", ["const:29d:8"]]
- 00bd76e0 ["INT_ADD", "register:40f0:8", ["const:bd76e0:8", "const:4:8"]]
+ 00bd86d4 ["INT_ADD", "register:40f0:8", ["const:bd86d4:8", "const:4:8"]]
~~~


### [`00bd76fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd76fc.md) → [`00bd86f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd86f0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8720",
      "incomplete_value": true,
      "site": "00bd8720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd772c",
      "incomplete_value": true,
      "site": "00bd772c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "definition_site": "00bd8704",
      "incomplete_value": true,
      "site": "00bd8704",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7710",
      "incomplete_value": true,
      "site": "00bd7710",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8710",
      "incomplete_value": false,
      "site": "00bd8718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd771c",
      "incomplete_value": false,
      "site": "00bd7724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7708 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd770c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d30:8"]]
+ 00bd86fc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8700 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00bd771c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd8710 ["COPY", "tmp:0:8", ["const:29d:8"]]
- 00bd7724 ["INT_ADD", "register:40f0:8", ["const:bd7724:8", "const:4:8"]]
+ 00bd8718 ["INT_ADD", "register:40f0:8", ["const:bd8718:8", "const:4:8"]]
~~~


### [`00bd7740`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7740.md) → [`00bd8734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8734.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8764",
      "incomplete_value": true,
      "site": "00bd8764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7770",
      "incomplete_value": true,
      "site": "00bd7770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "definition_site": "00bd8748",
      "incomplete_value": true,
      "site": "00bd8748",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7754",
      "incomplete_value": true,
      "site": "00bd7754",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8750",
      "incomplete_value": false,
      "site": "00bd875c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd775c",
      "incomplete_value": false,
      "site": "00bd7768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd774c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d30:8"]]
+ 00bd8740 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8744 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00bd775c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd8750 ["COPY", "tmp:0:8", ["const:29d:8"]]
- 00bd7768 ["INT_ADD", "register:40f0:8", ["const:bd7768:8", "const:4:8"]]
+ 00bd875c ["INT_ADD", "register:40f0:8", ["const:bd875c:8", "const:4:8"]]
~~~


### [`00bd7790`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7790.md) → [`00bd8784`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8784.md) _ZN8firebase4auth31oauthprovider_credentialbuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd87dc",
      "incomplete_value": true,
      "site": "00bd87dc",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd77e8",
      "incomplete_value": true,
      "site": "00bd77e8",
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
            "const:d38:8"
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
      "definition_site": "00bd87b8",
      "incomplete_value": true,
      "site": "00bd87c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd77c4",
      "incomplete_value": true,
      "site": "00bd77d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
        "01126d38",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126d38",
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
        "01127cf8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127cf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd77a0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd77a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d38:8"]]
+ 00bd8794 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8798 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf8:8"]]
- 00bd77b8 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd87ac ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd77c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
+ 00bd87b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
~~~


### [`00bd77fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd77fc.md) → [`00bd87f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd87f0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd882c",
      "incomplete_value": true,
      "site": "00bd882c",
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
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7838",
      "incomplete_value": true,
      "site": "00bd7838",
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
            "const:d38:8"
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
      "definition_site": "00bd884c",
      "incomplete_value": true,
      "site": "00bd884c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7858",
      "incomplete_value": true,
      "site": "00bd7858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      "definition_site": "00bd8808",
      "incomplete_value": true,
      "site": "00bd8808",
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
      "definition_site": "00bd7814",
      "incomplete_value": true,
      "site": "00bd7814",
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126d38",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126d38",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127cf8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127cf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd780c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd7810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
+ 00bd8800 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd8804 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00bd7818 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd781c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d38:8"]]
+ 00bd880c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8810 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf8:8"]]
- 00bd7834 ["INT_ADD", "register:40f0:8", ["const:bd7834:8", "const:4:8"]]
+ 00bd8828 ["INT_ADD", "register:40f0:8", ["const:bd8828:8", "const:4:8"]]
~~~


### [`00bd786c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd786c.md) → [`00bd8860`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8860.md) _ZN8firebase4auth31oauthprovider_credentialbuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd88a0",
      "incomplete_value": true,
      "site": "00bd88a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd78ac",
      "incomplete_value": true,
      "site": "00bd78ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8884",
      "incomplete_value": false,
      "site": "00bd8898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7890",
      "incomplete_value": false,
      "site": "00bd78a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7878 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd886c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7880 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
+ 00bd8874 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00bd7890 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd8884 ["COPY", "tmp:0:8", ["const:29d:8"]]
~~~


### [`00bd78dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd78dc.md) → [`00bd88d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd88d0.md) _ZN8firebase4auth31oauthprovider_credentialbuilder11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd88ec",
      "incomplete_value": false,
      "site": "00bd88f0",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd78f8",
      "incomplete_value": false,
      "site": "00bd78fc",
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
            "const:30b:8"
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
      "definition_site": "00bd88fc",
      "incomplete_value": true,
      "site": "00bd8908",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7908",
      "incomplete_value": true,
      "site": "00bd7914",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d40",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd78f8 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd88ec ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd78fc ["INT_ADD", "register:40f0:8", ["const:bd78fc:8", "const:4:8"]]
+ 00bd88f0 ["INT_ADD", "register:40f0:8", ["const:bd88f0:8", "const:4:8"]]
- 00bd7900 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7904 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00bd88f4 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd88f8 ["COPY", "tmp:0:8", ["const:d00:8"]]
~~~


### [`00bd7918`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7918.md) → [`00bd890c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd890c.md) _ZN8firebase4auth31oauthprovider_credentialbuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd894c",
      "incomplete_value": true,
      "site": "00bd894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7958",
      "incomplete_value": true,
      "site": "00bd7958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8930",
      "incomplete_value": false,
      "site": "00bd8944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd793c",
      "incomplete_value": false,
      "site": "00bd7950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:1bf:8"
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
        "01126d30",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc1bf",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d30",
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
        "01127cf0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc29d",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7924 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8918 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd792c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
+ 00bd8920 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00bd793c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 00bd8930 ["COPY", "tmp:0:8", ["const:29d:8"]]
~~~


### [`00bd7988`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7988.md) → [`00bd897c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd897c.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8998",
      "incomplete_value": false,
      "site": "00bd899c",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd79a4",
      "incomplete_value": false,
      "site": "00bd79a8",
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
            "const:54d:8"
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
      "definition_site": "00bd89a8",
      "incomplete_value": true,
      "site": "00bd89b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd79b4",
      "incomplete_value": true,
      "site": "00bd79c0",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d60",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d20",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd79a4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd8998 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd79a8 ["INT_ADD", "register:40f0:8", ["const:bd79a8:8", "const:4:8"]]
+ 00bd899c ["INT_ADD", "register:40f0:8", ["const:bd899c:8", "const:4:8"]]
- 00bd79ac ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd79b0 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00bd89a0 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd89a4 ["COPY", "tmp:0:8", ["const:d20:8"]]
~~~


### [`00bd79c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd79c4.md) → [`00bd89b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd89b8.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd89e4",
      "incomplete_value": true,
      "site": "00bd89e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd79f0",
      "incomplete_value": true,
      "site": "00bd79f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd89cc",
      "incomplete_value": true,
      "site": "00bd89cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd79d8",
      "incomplete_value": true,
      "site": "00bd79d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd89d8",
      "incomplete_value": true,
      "site": "00bd89dc",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd79e4",
      "incomplete_value": true,
      "site": "00bd79e8",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd79d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd79d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00bd89c4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd89c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
- 00bd79e4 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd89d8 ["COPY", "tmp:0:8", ["const:2ad:8"]]
- 00bd79e8 ["INT_ADD", "register:40f0:8", ["const:bd79e8:8", "const:4:8"]]
+ 00bd89dc ["INT_ADD", "register:40f0:8", ["const:bd89dc:8", "const:4:8"]]
~~~


### [`00bd7a04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7a04.md) → [`00bd89f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd89f8.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8a24",
      "incomplete_value": true,
      "site": "00bd8a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a30",
      "incomplete_value": true,
      "site": "00bd7a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8a0c",
      "incomplete_value": true,
      "site": "00bd8a0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a18",
      "incomplete_value": true,
      "site": "00bd7a18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8a14",
      "incomplete_value": false,
      "site": "00bd8a1c",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a20",
      "incomplete_value": false,
      "site": "00bd7a28",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7a10 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7a14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00bd8a04 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8a08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
- 00bd7a20 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd8a14 ["COPY", "tmp:0:8", ["const:2ad:8"]]
- 00bd7a28 ["INT_ADD", "register:40f0:8", ["const:bd7a28:8", "const:4:8"]]
+ 00bd8a1c ["INT_ADD", "register:40f0:8", ["const:bd8a1c:8", "const:4:8"]]
~~~


### [`00bd7a44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7a44.md) → [`00bd8a38`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8a38.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8a68",
      "incomplete_value": true,
      "site": "00bd8a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a74",
      "incomplete_value": true,
      "site": "00bd7a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8a4c",
      "incomplete_value": true,
      "site": "00bd8a4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a58",
      "incomplete_value": true,
      "site": "00bd7a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8a58",
      "incomplete_value": false,
      "site": "00bd8a60",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a64",
      "incomplete_value": false,
      "site": "00bd7a6c",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7a50 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7a54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00bd8a44 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8a48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
- 00bd7a64 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd8a58 ["COPY", "tmp:0:8", ["const:2ad:8"]]
- 00bd7a6c ["INT_ADD", "register:40f0:8", ["const:bd7a6c:8", "const:4:8"]]
+ 00bd8a60 ["INT_ADD", "register:40f0:8", ["const:bd8a60:8", "const:4:8"]]
~~~


### [`00bd7a88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7a88.md) → [`00bd8a7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8a7c.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8aac",
      "incomplete_value": true,
      "site": "00bd8aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ab8",
      "incomplete_value": true,
      "site": "00bd7ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8a90",
      "incomplete_value": true,
      "site": "00bd8a90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7a9c",
      "incomplete_value": true,
      "site": "00bd7a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8a98",
      "incomplete_value": false,
      "site": "00bd8aa4",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7aa4",
      "incomplete_value": false,
      "site": "00bd7ab0",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7a94 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7a98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
+ 00bd8a88 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8a8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
- 00bd7aa4 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd8a98 ["COPY", "tmp:0:8", ["const:2ad:8"]]
- 00bd7ab0 ["INT_ADD", "register:40f0:8", ["const:bd7ab0:8", "const:4:8"]]
+ 00bd8aa4 ["INT_ADD", "register:40f0:8", ["const:bd8aa4:8", "const:4:8"]]
~~~


### [`00bd7ad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7ad8.md) → [`00bd8acc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8acc.md) _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8b24",
      "incomplete_value": true,
      "site": "00bd8b24",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7b30",
      "incomplete_value": true,
      "site": "00bd7b30",
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
            "const:d70:8"
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
      "definition_site": "00bd8b00",
      "incomplete_value": true,
      "site": "00bd8b0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7b0c",
      "incomplete_value": true,
      "site": "00bd7b18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
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
        "01126d70",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126d70",
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
        "01127d30",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127d30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7ae8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd7aec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
+ 00bd8adc ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8ae0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d30:8"]]
- 00bd7b00 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd8af4 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd7b0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d68:8"]]
+ 00bd8b00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
~~~


### [`00bd7b44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7b44.md) → [`00bd8b38`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8b38.md) _ZN8firebase4auth8auth_idp12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8b74",
      "incomplete_value": true,
      "site": "00bd8b74",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7b80",
      "incomplete_value": true,
      "site": "00bd7b80",
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
            "const:d70:8"
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
      "definition_site": "00bd8b94",
      "incomplete_value": true,
      "site": "00bd8b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ba0",
      "incomplete_value": true,
      "site": "00bd7ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8b50",
      "incomplete_value": true,
      "site": "00bd8b50",
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
      "definition_site": "00bd7b5c",
      "incomplete_value": true,
      "site": "00bd7b5c",
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126d70",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126d70",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127d30",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127d30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7b54 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd7b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00bd8b48 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd8b4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00bd7b60 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd7b64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
+ 00bd8b54 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8b58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d30:8"]]
- 00bd7b7c ["INT_ADD", "register:40f0:8", ["const:bd7b7c:8", "const:4:8"]]
+ 00bd8b70 ["INT_ADD", "register:40f0:8", ["const:bd8b70:8", "const:4:8"]]
~~~


### [`00bd7bb4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7bb4.md) → [`00bd8ba8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8ba8.md) _ZN8firebase4auth8auth_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8be8",
      "incomplete_value": true,
      "site": "00bd8be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bf4",
      "incomplete_value": true,
      "site": "00bd7bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8bc4",
      "incomplete_value": true,
      "site": "00bd8bc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bd0",
      "incomplete_value": true,
      "site": "00bd7bd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8bcc",
      "incomplete_value": false,
      "site": "00bd8be0",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7bd8",
      "incomplete_value": false,
      "site": "00bd7bec",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7bc0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8bb4 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7bc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00bd8bbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00bd7bd8 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd8bcc ["COPY", "tmp:0:8", ["const:2ad:8"]]
~~~


### [`00bd7c24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7c24.md) → [`00bd8c18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8c18.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8c34",
      "incomplete_value": false,
      "site": "00bd8c38",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c40",
      "incomplete_value": false,
      "site": "00bd7c44",
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
            "const:30b:8"
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
      "definition_site": "00bd8c44",
      "incomplete_value": true,
      "site": "00bd8c50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7c50",
      "incomplete_value": true,
      "site": "00bd7c5c",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d78",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7c40 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd8c34 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd7c44 ["INT_ADD", "register:40f0:8", ["const:bd7c44:8", "const:4:8"]]
+ 00bd8c38 ["INT_ADD", "register:40f0:8", ["const:bd8c38:8", "const:4:8"]]
- 00bd7c48 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7c4c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00bd8c3c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd8c40 ["COPY", "tmp:0:8", ["const:d38:8"]]
~~~


### [`00bd7c60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7c60.md) → [`00bd8c54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8c54.md) _ZN8firebase4auth8auth_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8c94",
      "incomplete_value": true,
      "site": "00bd8c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ca0",
      "incomplete_value": true,
      "site": "00bd7ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd8c70",
      "incomplete_value": true,
      "site": "00bd8c70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c7c",
      "incomplete_value": true,
      "site": "00bd7c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8c78",
      "incomplete_value": false,
      "site": "00bd8c8c",
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
            "const:2ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c84",
      "incomplete_value": false,
      "site": "00bd7c98",
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
            "const:1e0:8"
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
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac1e0",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d68",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ac2ad",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7c6c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8c60 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7c74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00bd8c68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00bd7c84 ["COPY", "tmp:0:8", ["const:1e0:8"]]
+ 00bd8c78 ["COPY", "tmp:0:8", ["const:2ad:8"]]
~~~


### [`00bd7cd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7cd0.md) → [`00bd8cc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8cc4.md) _ZN8firebase4auth8auth_idp10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8ce0",
      "incomplete_value": false,
      "site": "00bd8ce4",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7cec",
      "incomplete_value": false,
      "site": "00bd7cf0",
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
            "const:54d:8"
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
      "definition_site": "00bd8cf0",
      "incomplete_value": true,
      "site": "00bd8cfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7cfc",
      "incomplete_value": true,
      "site": "00bd7d08",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d80",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d40",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7cec ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd8ce0 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd7cf0 ["INT_ADD", "register:40f0:8", ["const:bd7cf0:8", "const:4:8"]]
+ 00bd8ce4 ["INT_ADD", "register:40f0:8", ["const:bd8ce4:8", "const:4:8"]]
- 00bd7cf4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7cf8 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00bd8ce8 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd8cec ["COPY", "tmp:0:8", ["const:d40:8"]]
~~~


### [`00bd7d0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7d0c.md) → [`00bd8d00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8d00.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8d2c",
      "incomplete_value": true,
      "site": "00bd8d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d38",
      "incomplete_value": true,
      "site": "00bd7d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8d14",
      "incomplete_value": true,
      "site": "00bd8d14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d20",
      "incomplete_value": true,
      "site": "00bd7d20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8d20",
      "incomplete_value": false,
      "site": "00bd8d24",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d2c",
      "incomplete_value": false,
      "site": "00bd7d30",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7d18 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00bd8d0c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00bd7d2c ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8d20 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bd7d30 ["INT_ADD", "register:40f0:8", ["const:bd7d30:8", "const:4:8"]]
+ 00bd8d24 ["INT_ADD", "register:40f0:8", ["const:bd8d24:8", "const:4:8"]]
~~~


### [`00bd7d4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7d4c.md) → [`00bd8d40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8d40.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8d6c",
      "incomplete_value": true,
      "site": "00bd8d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d78",
      "incomplete_value": true,
      "site": "00bd7d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8d54",
      "incomplete_value": true,
      "site": "00bd8d54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d60",
      "incomplete_value": true,
      "site": "00bd7d60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8d5c",
      "incomplete_value": false,
      "site": "00bd8d64",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7d68",
      "incomplete_value": false,
      "site": "00bd7d70",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7d58 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7d5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00bd8d4c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8d50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00bd7d68 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8d5c ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bd7d70 ["INT_ADD", "register:40f0:8", ["const:bd7d70:8", "const:4:8"]]
+ 00bd8d64 ["INT_ADD", "register:40f0:8", ["const:bd8d64:8", "const:4:8"]]
~~~


### [`00bd7d8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7d8c.md) → [`00bd8d80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8d80.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8db0",
      "incomplete_value": true,
      "site": "00bd8db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7dbc",
      "incomplete_value": true,
      "site": "00bd7dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8d94",
      "incomplete_value": true,
      "site": "00bd8d94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7da0",
      "incomplete_value": true,
      "site": "00bd7da0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8da0",
      "incomplete_value": false,
      "site": "00bd8da8",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7dac",
      "incomplete_value": false,
      "site": "00bd7db4",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7d98 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7d9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00bd8d8c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00bd7dac ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8da0 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bd7db4 ["INT_ADD", "register:40f0:8", ["const:bd7db4:8", "const:4:8"]]
+ 00bd8da8 ["INT_ADD", "register:40f0:8", ["const:bd8da8:8", "const:4:8"]]
~~~


### [`00bd7dd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7dd0.md) → [`00bd8dc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8dc4.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8df4",
      "incomplete_value": true,
      "site": "00bd8df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e00",
      "incomplete_value": true,
      "site": "00bd7e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8dd8",
      "incomplete_value": true,
      "site": "00bd8dd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7de4",
      "incomplete_value": true,
      "site": "00bd7de4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8de0",
      "incomplete_value": false,
      "site": "00bd8dec",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7dec",
      "incomplete_value": false,
      "site": "00bd7df8",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7ddc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd7de0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
+ 00bd8dd0 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd8dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00bd7dec ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8de0 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bd7df8 ["INT_ADD", "register:40f0:8", ["const:bd7df8:8", "const:4:8"]]
+ 00bd8dec ["INT_ADD", "register:40f0:8", ["const:bd8dec:8", "const:4:8"]]
~~~


### [`00bd7e20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7e20.md) → [`00bd8e14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8e14.md) _ZN8firebase4auth8user_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8e6c",
      "incomplete_value": true,
      "site": "00bd8e6c",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e78",
      "incomplete_value": true,
      "site": "00bd7e78",
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
            "const:d90:8"
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
      "definition_site": "00bd8e48",
      "incomplete_value": true,
      "site": "00bd8e54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e54",
      "incomplete_value": true,
      "site": "00bd7e60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
        "01126d90",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126d90",
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
        "01127d50",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127d50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7e30 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd7e34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d90:8"]]
+ 00bd8e24 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8e28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d50:8"]]
- 00bd7e48 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd8e3c ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd7e54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d88:8"]]
+ 00bd8e48 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d48:8"]]
~~~


### [`00bd7e8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7e8c.md) → [`00bd8e80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8e80.md) _ZN8firebase4auth8user_idp12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8ebc",
      "incomplete_value": true,
      "site": "00bd8ebc",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ec8",
      "incomplete_value": true,
      "site": "00bd7ec8",
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
            "const:d90:8"
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
      "definition_site": "00bd8edc",
      "incomplete_value": true,
      "site": "00bd8edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ee8",
      "incomplete_value": true,
      "site": "00bd7ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8e98",
      "incomplete_value": true,
      "site": "00bd8e98",
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
      "definition_site": "00bd7ea4",
      "incomplete_value": true,
      "site": "00bd7ea4",
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126d90",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126d90",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127d50",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127d50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7e9c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd7ea0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00bd8e90 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd8e94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00bd7ea8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd7eac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d90:8"]]
+ 00bd8e9c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd8ea0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d50:8"]]
- 00bd7ec4 ["INT_ADD", "register:40f0:8", ["const:bd7ec4:8", "const:4:8"]]
+ 00bd8eb8 ["INT_ADD", "register:40f0:8", ["const:bd8eb8:8", "const:4:8"]]
~~~


### [`00bd7efc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7efc.md) → [`00bd8ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8ef0.md) _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8f30",
      "incomplete_value": true,
      "site": "00bd8f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7f3c",
      "incomplete_value": true,
      "site": "00bd7f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8f0c",
      "incomplete_value": true,
      "site": "00bd8f0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7f18",
      "incomplete_value": true,
      "site": "00bd7f18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8f14",
      "incomplete_value": false,
      "site": "00bd8f28",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7f20",
      "incomplete_value": false,
      "site": "00bd7f34",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7f08 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8efc ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7f10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00bd8f04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00bd7f20 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8f14 ["COPY", "tmp:0:8", ["const:983:8"]]
~~~


### [`00bd7f6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7f6c.md) → [`00bd8f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8f60.md) _ZN8firebase4auth8user_idp11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd8f7c",
      "incomplete_value": false,
      "site": "00bd8f80",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7f88",
      "incomplete_value": false,
      "site": "00bd7f8c",
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
            "const:30b:8"
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
      "definition_site": "00bd8f8c",
      "incomplete_value": true,
      "site": "00bd8f98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd7f98",
      "incomplete_value": true,
      "site": "00bd7fa4",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126d98",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7f88 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd8f7c ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd7f8c ["INT_ADD", "register:40f0:8", ["const:bd7f8c:8", "const:4:8"]]
+ 00bd8f80 ["INT_ADD", "register:40f0:8", ["const:bd8f80:8", "const:4:8"]]
- 00bd7f90 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd7f94 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00bd8f84 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd8f88 ["COPY", "tmp:0:8", ["const:d58:8"]]
~~~


### [`00bd7fa8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd7/00bd7fa8.md) → [`00bd8f9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8f9c.md) _ZN8firebase4auth8user_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd8fdc",
      "incomplete_value": true,
      "site": "00bd8fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7fe8",
      "incomplete_value": true,
      "site": "00bd7fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "00bd8fb8",
      "incomplete_value": true,
      "site": "00bd8fb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7fc4",
      "incomplete_value": true,
      "site": "00bd7fc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd8fc0",
      "incomplete_value": false,
      "site": "00bd8fd4",
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
            "const:983:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7fcc",
      "incomplete_value": false,
      "site": "00bd7fe0",
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
            "const:8b6:8"
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
        "01126d88",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a98b6",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126d88",
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
        "01127d48",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002a9983",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd7fb4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd8fa8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd7fbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00bd8fb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00bd7fcc ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bd8fc0 ["COPY", "tmp:0:8", ["const:983:8"]]
~~~


### [`00bd8018`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8018.md) → [`00bd900c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd900c.md) _ZN8firebase4auth8user_idp10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9028",
      "incomplete_value": false,
      "site": "00bd902c",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8034",
      "incomplete_value": false,
      "site": "00bd8038",
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
            "const:54d:8"
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
      "definition_site": "00bd9038",
      "incomplete_value": true,
      "site": "00bd9044",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd8044",
      "incomplete_value": true,
      "site": "00bd8050",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126da8",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d68",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8034 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd9028 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd8038 ["INT_ADD", "register:40f0:8", ["const:bd8038:8", "const:4:8"]]
+ 00bd902c ["INT_ADD", "register:40f0:8", ["const:bd902c:8", "const:4:8"]]
- 00bd803c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd8040 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00bd9030 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd9034 ["COPY", "tmp:0:8", ["const:d68:8"]]
~~~


### [`00bd8054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8054.md) → [`00bd9048`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9048.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9074",
      "incomplete_value": true,
      "site": "00bd9074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8080",
      "incomplete_value": true,
      "site": "00bd8080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd905c",
      "incomplete_value": true,
      "site": "00bd905c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8068",
      "incomplete_value": true,
      "site": "00bd8068",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd9068",
      "incomplete_value": false,
      "site": "00bd906c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8074",
      "incomplete_value": false,
      "site": "00bd8078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8060 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd8064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bd9054 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd9058 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d70:8"]]
- 00bd8074 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd9068 ["COPY", "tmp:0:8", ["const:832:8"]]
- 00bd8078 ["INT_ADD", "register:40f0:8", ["const:bd8078:8", "const:4:8"]]
+ 00bd906c ["INT_ADD", "register:40f0:8", ["const:bd906c:8", "const:4:8"]]
~~~


### [`00bd8094`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8094.md) → [`00bd9088`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9088.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd90b4",
      "incomplete_value": true,
      "site": "00bd90b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd80c0",
      "incomplete_value": true,
      "site": "00bd80c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd909c",
      "incomplete_value": true,
      "site": "00bd909c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd80a8",
      "incomplete_value": true,
      "site": "00bd80a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd90a4",
      "incomplete_value": false,
      "site": "00bd90ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd80b0",
      "incomplete_value": false,
      "site": "00bd80b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd80a0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd80a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bd9094 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd9098 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d70:8"]]
- 00bd80b0 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd90a4 ["COPY", "tmp:0:8", ["const:832:8"]]
- 00bd80b8 ["INT_ADD", "register:40f0:8", ["const:bd80b8:8", "const:4:8"]]
+ 00bd90ac ["INT_ADD", "register:40f0:8", ["const:bd90ac:8", "const:4:8"]]
~~~


### [`00bd80d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd80d4.md) → [`00bd90c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd90c8.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd90f8",
      "incomplete_value": true,
      "site": "00bd90f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8104",
      "incomplete_value": true,
      "site": "00bd8104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd90dc",
      "incomplete_value": true,
      "site": "00bd90dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd80e8",
      "incomplete_value": true,
      "site": "00bd80e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd90e8",
      "incomplete_value": false,
      "site": "00bd90f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd80f4",
      "incomplete_value": false,
      "site": "00bd80fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd80e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd80e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bd90d4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd90d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d70:8"]]
- 00bd80f4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd90e8 ["COPY", "tmp:0:8", ["const:832:8"]]
- 00bd80fc ["INT_ADD", "register:40f0:8", ["const:bd80fc:8", "const:4:8"]]
+ 00bd90f0 ["INT_ADD", "register:40f0:8", ["const:bd90f0:8", "const:4:8"]]
~~~


### [`00bd8118`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8118.md) → [`00bd910c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd910c.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd913c",
      "incomplete_value": true,
      "site": "00bd913c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8148",
      "incomplete_value": true,
      "site": "00bd8148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd9120",
      "incomplete_value": true,
      "site": "00bd9120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd812c",
      "incomplete_value": true,
      "site": "00bd812c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00bd812c"
      ],
      [
        "FALL_THROUGH",
        "00bd9120"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bd9120",
      "incomplete_value": true,
      "site": "00bd913c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd812c",
      "incomplete_value": true,
      "site": "00bd8148",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8124 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd8128 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 00bd9118 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd911c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d70:8"]]
- 00bd8134 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd9128 ["COPY", "tmp:0:8", ["const:832:8"]]
- 00bd8140 ["INT_ADD", "register:40f0:8", ["const:bd8140:8", "const:4:8"]]
+ 00bd9134 ["INT_ADD", "register:40f0:8", ["const:bd9134:8", "const:4:8"]]
~~~


### [`00bd8168`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8168.md) → [`00bd915c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd915c.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 constant, operands_and_dependencies, store_destination

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd91b4",
      "incomplete_value": true,
      "site": "00bd91b4",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd81c0",
      "incomplete_value": true,
      "site": "00bd81c0",
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
            "const:db8:8"
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
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126db8",
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
        "01127d78",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127d78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8178 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd817c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
+ 00bd916c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd9170 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00bd8190 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd9184 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd819c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db0:8"]]
+ 00bd9190 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d70:8"]]
~~~


### [`00bd81d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd81d4.md) → [`00bd91c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd91c8.md) _ZN8firebase4auth8jniphone12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9204",
      "incomplete_value": true,
      "site": "00bd9204",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8210",
      "incomplete_value": true,
      "site": "00bd8210",
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
            "const:db8:8"
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
      "definition_site": "00bd9224",
      "incomplete_value": true,
      "site": "00bd9224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8230",
      "incomplete_value": true,
      "site": "00bd8230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd91e0",
      "incomplete_value": true,
      "site": "00bd91e0",
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
      "definition_site": "00bd81ec",
      "incomplete_value": true,
      "site": "00bd81ec",
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126db8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126db8",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127d78",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127d78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd81e4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd81e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bd91d8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd91dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
- 00bd81f0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd81f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
+ 00bd91e4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd91e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00bd820c ["INT_ADD", "register:40f0:8", ["const:bd820c:8", "const:4:8"]]
+ 00bd9200 ["INT_ADD", "register:40f0:8", ["const:bd9200:8", "const:4:8"]]
~~~


### [`00bd8244`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8244.md) → [`00bd9238`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9238.md) _ZN8firebase4auth8jniphone14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9278",
      "incomplete_value": true,
      "site": "00bd9278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8284",
      "incomplete_value": true,
      "site": "00bd8284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd9254",
      "incomplete_value": true,
      "site": "00bd9254",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8260",
      "incomplete_value": true,
      "site": "00bd8260",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd925c",
      "incomplete_value": false,
      "site": "00bd9270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8268",
      "incomplete_value": false,
      "site": "00bd827c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8250 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd9244 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd8258 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bd924c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
- 00bd8268 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd925c ["COPY", "tmp:0:8", ["const:832:8"]]
~~~


### [`00bd82b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd82b4.md) → [`00bd92a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd92a8.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd92c4",
      "incomplete_value": false,
      "site": "00bd92c8",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd82d0",
      "incomplete_value": false,
      "site": "00bd82d4",
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
            "const:30b:8"
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
      "definition_site": "00bd92d4",
      "incomplete_value": true,
      "site": "00bd92e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd82e0",
      "incomplete_value": true,
      "site": "00bd82ec",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126dc0",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd82d0 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd92c4 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd82d4 ["INT_ADD", "register:40f0:8", ["const:bd82d4:8", "const:4:8"]]
+ 00bd92c8 ["INT_ADD", "register:40f0:8", ["const:bd92c8:8", "const:4:8"]]
- 00bd82d8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd82dc ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00bd92cc ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd92d0 ["COPY", "tmp:0:8", ["const:d80:8"]]
~~~


### [`00bd82f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd82f0.md) → [`00bd92e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd92e4.md) _ZN8firebase4auth8jniphone13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9324",
      "incomplete_value": true,
      "site": "00bd9324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8330",
      "incomplete_value": true,
      "site": "00bd8330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:db0:8"
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
      "definition_site": "00bd9300",
      "incomplete_value": true,
      "site": "00bd9300",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd830c",
      "incomplete_value": true,
      "site": "00bd830c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd9308",
      "incomplete_value": false,
      "site": "00bd931c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:832:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8314",
      "incomplete_value": false,
      "site": "00bd8328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd82fc ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd92f0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd8304 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00bd92f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
- 00bd8314 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd9308 ["COPY", "tmp:0:8", ["const:832:8"]]
~~~


### [`00bd8360`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8360.md) → [`00bd9354`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9354.md) _ZN8firebase4auth8jniphone10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9370",
      "incomplete_value": false,
      "site": "00bd9374",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd837c",
      "incomplete_value": false,
      "site": "00bd8380",
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
            "const:54d:8"
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
      "definition_site": "00bd9380",
      "incomplete_value": true,
      "site": "00bd938c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd838c",
      "incomplete_value": true,
      "site": "00bd8398",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126dd0",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127d90",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd837c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd9370 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd8380 ["INT_ADD", "register:40f0:8", ["const:bd8380:8", "const:4:8"]]
+ 00bd9374 ["INT_ADD", "register:40f0:8", ["const:bd9374:8", "const:4:8"]]
- 00bd8384 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd8388 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00bd9378 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd937c ["COPY", "tmp:0:8", ["const:d90:8"]]
~~~


### [`00bd839c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd839c.md) → [`00bd9390`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9390.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd93bc",
      "incomplete_value": true,
      "site": "00bd93bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd83c8",
      "incomplete_value": true,
      "site": "00bd83c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd93a4",
      "incomplete_value": true,
      "site": "00bd93a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd83b0",
      "incomplete_value": true,
      "site": "00bd83b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd93b0",
      "incomplete_value": false,
      "site": "00bd93b4",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd83bc",
      "incomplete_value": false,
      "site": "00bd83c0",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd83a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd83ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd8:8"]]
+ 00bd939c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd93a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00bd83bc ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd93b0 ["COPY", "tmp:0:8", ["const:dfb:8"]]
- 00bd83c0 ["INT_ADD", "register:40f0:8", ["const:bd83c0:8", "const:4:8"]]
+ 00bd93b4 ["INT_ADD", "register:40f0:8", ["const:bd93b4:8", "const:4:8"]]
~~~


### [`00bd83dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd83dc.md) → [`00bd93d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd93d0.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd93fc",
      "incomplete_value": true,
      "site": "00bd93fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8408",
      "incomplete_value": true,
      "site": "00bd8408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd93e4",
      "incomplete_value": true,
      "site": "00bd93e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd83f0",
      "incomplete_value": true,
      "site": "00bd83f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd93ec",
      "incomplete_value": false,
      "site": "00bd93f4",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd83f8",
      "incomplete_value": false,
      "site": "00bd8400",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd83e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd83ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd8:8"]]
+ 00bd93dc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd93e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00bd83f8 ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd93ec ["COPY", "tmp:0:8", ["const:dfb:8"]]
- 00bd8400 ["INT_ADD", "register:40f0:8", ["const:bd8400:8", "const:4:8"]]
+ 00bd93f4 ["INT_ADD", "register:40f0:8", ["const:bd93f4:8", "const:4:8"]]
~~~


### [`00bd841c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd841c.md) → [`00bd9410`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9410.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9440",
      "incomplete_value": true,
      "site": "00bd9440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd844c",
      "incomplete_value": true,
      "site": "00bd844c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd9424",
      "incomplete_value": true,
      "site": "00bd9424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8430",
      "incomplete_value": true,
      "site": "00bd8430",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd9430",
      "incomplete_value": false,
      "site": "00bd9438",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd843c",
      "incomplete_value": false,
      "site": "00bd8444",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8428 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd842c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd8:8"]]
+ 00bd941c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd9420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00bd843c ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd9430 ["COPY", "tmp:0:8", ["const:dfb:8"]]
- 00bd8444 ["INT_ADD", "register:40f0:8", ["const:bd8444:8", "const:4:8"]]
+ 00bd9438 ["INT_ADD", "register:40f0:8", ["const:bd9438:8", "const:4:8"]]
~~~


### [`00bd8460`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8460.md) → [`00bd9454`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9454.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9484",
      "incomplete_value": true,
      "site": "00bd9484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8490",
      "incomplete_value": true,
      "site": "00bd8490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd9468",
      "incomplete_value": true,
      "site": "00bd9468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8474",
      "incomplete_value": true,
      "site": "00bd8474",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd9470",
      "incomplete_value": false,
      "site": "00bd947c",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd847c",
      "incomplete_value": false,
      "site": "00bd8488",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd846c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bd8470 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dd8:8"]]
+ 00bd9460 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bd9464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00bd847c ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd9470 ["COPY", "tmp:0:8", ["const:dfb:8"]]
- 00bd8488 ["INT_ADD", "register:40f0:8", ["const:bd8488:8", "const:4:8"]]
+ 00bd947c ["INT_ADD", "register:40f0:8", ["const:bd947c:8", "const:4:8"]]
~~~


### [`00bd84b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd84b0.md) → [`00bd94a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd94a4.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd94fc",
      "incomplete_value": true,
      "site": "00bd94fc",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8508",
      "incomplete_value": true,
      "site": "00bd8508",
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
            "const:de0:8"
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
      "definition_site": "00bd94d8",
      "incomplete_value": true,
      "site": "00bd94e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
    "old": {
      "definition_site": "00bd84e4",
      "incomplete_value": true,
      "site": "00bd84f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
        "01126de0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126de0",
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
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd84c0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd84c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:de0:8"]]
+ 00bd94b4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd94b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:da0:8"]]
- 00bd84d8 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bd94cc ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bd84e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
+ 00bd94d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
~~~


### [`00bd851c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd851c.md) → [`00bd9510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9510.md) _ZN8firebase4auth15phonecredential12ReleaseClassEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd954c",
      "incomplete_value": true,
      "site": "00bd954c",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8558",
      "incomplete_value": true,
      "site": "00bd8558",
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
            "const:de0:8"
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
      "definition_site": "00bd956c",
      "incomplete_value": true,
      "site": "00bd956c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8578",
      "incomplete_value": true,
      "site": "00bd8578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd9528",
      "incomplete_value": true,
      "site": "00bd9528",
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
      "definition_site": "00bd8534",
      "incomplete_value": true,
      "site": "00bd8534",
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126de0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126de0",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd852c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd8530 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00bd9520 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd9524 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00bd8538 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd853c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:de0:8"]]
+ 00bd952c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd9530 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:da0:8"]]
- 00bd8554 ["INT_ADD", "register:40f0:8", ["const:bd8554:8", "const:4:8"]]
+ 00bd9548 ["INT_ADD", "register:40f0:8", ["const:bd9548:8", "const:4:8"]]
~~~


### [`00bd858c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd858c.md) → [`00bd9580`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9580.md) _ZN8firebase4auth15phonecredential14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd95c0",
      "incomplete_value": true,
      "site": "00bd95c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd85cc",
      "incomplete_value": true,
      "site": "00bd85cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd959c",
      "incomplete_value": true,
      "site": "00bd959c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd85a8",
      "incomplete_value": true,
      "site": "00bd85a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd95a4",
      "incomplete_value": false,
      "site": "00bd95b8",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd85b0",
      "incomplete_value": false,
      "site": "00bd85c4",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8598 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd958c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd85a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00bd9594 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00bd85b0 ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd95a4 ["COPY", "tmp:0:8", ["const:dfb:8"]]
~~~


### [`00bd85fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd85fc.md) → [`00bd95f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd95f0.md) _ZN8firebase4auth15phonecredential11GetMethodIdENS1_6MethodE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd960c",
      "incomplete_value": false,
      "site": "00bd9610",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8618",
      "incomplete_value": false,
      "site": "00bd861c",
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
            "const:30b:8"
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
      "definition_site": "00bd961c",
      "incomplete_value": true,
      "site": "00bd9628",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd8628",
      "incomplete_value": true,
      "site": "00bd8634",
      "value": [
        "LOAD",
        "8",
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
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126de8",
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
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127da8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8618 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bd960c ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bd861c ["INT_ADD", "register:40f0:8", ["const:bd861c:8", "const:4:8"]]
+ 00bd9610 ["INT_ADD", "register:40f0:8", ["const:bd9610:8", "const:4:8"]]
- 00bd8620 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd8624 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00bd9614 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd9618 ["COPY", "tmp:0:8", ["const:da8:8"]]
~~~


### [`00bd8638`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8638.md) → [`00bd962c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd962c.md) _ZN8firebase4auth15phonecredential13CacheFieldIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd966c",
      "incomplete_value": true,
      "site": "00bd966c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8678",
      "incomplete_value": true,
      "site": "00bd8678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "definition_site": "00bd9648",
      "incomplete_value": true,
      "site": "00bd9648",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8654",
      "incomplete_value": true,
      "site": "00bd8654",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
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
      "definition_site": "00bd9650",
      "incomplete_value": false,
      "site": "00bd9664",
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
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd865c",
      "incomplete_value": false,
      "site": "00bd8670",
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
            "const:d2c:8"
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
        "01126dd8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5d2c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126dd8",
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
        "01127d98",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b5dfb",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8644 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bd9638 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bd864c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00bd9640 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00bd865c ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00bd9650 ["COPY", "tmp:0:8", ["const:dfb:8"]]
~~~


### [`00bd86a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd86a8.md) → [`00bd969c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd969c.md) _ZN8firebase4auth15phonecredential10GetFieldIdENS1_5FieldE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd96b8",
      "incomplete_value": false,
      "site": "00bd96bc",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd86c4",
      "incomplete_value": false,
      "site": "00bd86c8",
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
            "const:54d:8"
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
      "definition_site": "00bd96c8",
      "incomplete_value": true,
      "site": "00bd96d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bd86d4",
      "incomplete_value": true,
      "site": "00bd86e0",
      "value": [
        "LOAD",
        "8",
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
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01126df0",
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
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      44,
      "DATA",
      [
        "storage",
        "01127db0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd86c4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bd96b8 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bd86c8 ["INT_ADD", "register:40f0:8", ["const:bd86c8:8", "const:4:8"]]
+ 00bd96bc ["INT_ADD", "register:40f0:8", ["const:bd96bc:8", "const:4:8"]]
- 00bd86cc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd86d0 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00bd96c0 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bd96c4 ["COPY", "tmp:0:8", ["const:db0:8"]]
~~~


### [`00bd86e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd86e4.md) → [`00bd96d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd96d8.md) _ZN8firebase4auth24CacheCredentialMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd80.md) · 呼出先 4件 [`00c5afc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5ed50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed50.md) · 呼出先 4件 [`00c5bf90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 57件, `store_condition` 2件, `store_destination` 18件

アドレスに依存する影響 `branch_value` 14件, `call_argument_candidate` 1件, `store_condition` 14件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9718",
      "incomplete_value": true,
      "site": "00bd9718",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8724",
      "incomplete_value": true,
      "site": "00bd8724",
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
            "const:db0:8"
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
      "definition_site": "00bd9790",
      "incomplete_value": true,
      "site": "00bd9790",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd879c",
      "incomplete_value": true,
      "site": "00bd879c",
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
            "const:db8:8"
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
      "definition_site": "00bd97cc",
      "incomplete_value": true,
      "site": "00bd97cc",
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
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd87d8",
      "incomplete_value": true,
      "site": "00bd87d8",
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
            "const:b48:8"
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
      24,
      "READ",
      [
        "storage",
        "01126db0",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "002b27e8",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126db0",
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
        "01127d70",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd86f4 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bd96e8 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bd86fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db0:8"]]
+ 00bd96f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
- 00bd870c ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00bd9700 ["COPY", "tmp:0:8", ["const:832:8"]]
~~~


### [`00bd8d50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd8/00bd8d50.md) → [`00bd9d44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd9/00bd9d44.md) _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd90.md) · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5ed60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed60.md) · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 34件

アドレスに依存する影響 `branch_value` 17件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd9d80",
      "incomplete_value": true,
      "site": "00bd9d80",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8d8c",
      "incomplete_value": true,
      "site": "00bd8d8c",
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
            "const:d70:8"
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
      "definition_site": "00bd9da0",
      "incomplete_value": true,
      "site": "00bd9da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8dac",
      "incomplete_value": true,
      "site": "00bd8dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00bd9dcc",
      "incomplete_value": true,
      "site": "00bd9dcc",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd8dd8",
      "incomplete_value": true,
      "site": "00bd8dd8",
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
            "const:b50:8"
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
      20,
      "READ",
      [
        "storage",
        "01126d68",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01126d70",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126d70",
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
        "01127d28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01127d30",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127d30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd8d60 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bd8d64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
+ 00bd9d54 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bd9d58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00bd8d70 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bd8d74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
+ 00bd9d64 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bd9d68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d30:8"]]
- 00bd8d88 ["INT_ADD", "register:40f0:8", ["const:bd8d88:8", "const:4:8"]]
+ 00bd9d7c ["INT_ADD", "register:40f0:8", ["const:bd9d7c:8", "const:4:8"]]
~~~


### [`00bd9288`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9288.md) → [`00bda27c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda27c.md) _ZN8firebase4auth10CredentialD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5aac0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aac0.md) [`00c5ded0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5ded0.md) · 呼出先 4件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 2件 [`00c5ba90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba90.md) [`00c5eea0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eea0.md) · 呼出先 4件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda2a4",
      "incomplete_value": false,
      "site": "00bda2a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:653:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd92b0",
      "incomplete_value": false,
      "site": "00bd92b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b2000:8"
          ],
          [
            "leaf",
            "const:609:8"
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
      40,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      40,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd92a0 ["INT_ADD", "register:40f0:8", ["const:bd92a0:8", "const:4:8"]]
+ 00bda294 ["INT_ADD", "register:40f0:8", ["const:bda294:8", "const:4:8"]]
- 00bd92b0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda2a4 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bd92b4 ["INT_ADD", "register:40f0:8", ["const:bd92b4:8", "const:4:8"]]
+ 00bda2a8 ["INT_ADD", "register:40f0:8", ["const:bda2a8:8", "const:4:8"]]
~~~


