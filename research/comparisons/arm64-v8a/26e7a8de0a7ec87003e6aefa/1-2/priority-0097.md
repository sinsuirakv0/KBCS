# v16.0.2 → v16.0.3 · 最優先の変更候補 (97)

[一覧の目次](README.md)

### [`00bd935c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd935c.md) → [`00bda350`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda350.md) _ZN8firebase4auth10CredentialaSERKS1_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de30.md) · 呼出先 4件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b180`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 1件 [`00c5ee00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee00.md) · 呼出先 4件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda388",
      "incomplete_value": false,
      "site": "00bda38c",
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
      "definition_site": "00bd9394",
      "incomplete_value": false,
      "site": "00bd9398",
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
      56,
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
      56,
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
- 00bd9384 ["INT_ADD", "register:40f0:8", ["const:bd9384:8", "const:4:8"]]
+ 00bda378 ["INT_ADD", "register:40f0:8", ["const:bda378:8", "const:4:8"]]
- 00bd9394 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda388 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bd9398 ["INT_ADD", "register:40f0:8", ["const:bd9398:8", "const:4:8"]]
+ 00bda38c ["INT_ADD", "register:40f0:8", ["const:bda38c:8", "const:4:8"]]
~~~


### [`00bd942c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd942c.md) → [`00bda420`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda420.md) _ZNK8firebase4auth10Credential8providerEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md) [`00c5b460`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md) [`00c5c430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda448",
      "incomplete_value": false,
      "site": "00bda44c",
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
      "definition_site": "00bd9454",
      "incomplete_value": false,
      "site": "00bd9458",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda464",
      "incomplete_value": true,
      "site": "00bda46c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9470",
      "incomplete_value": true,
      "site": "00bd9478",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
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
      40,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined8"
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
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127b18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9444 ["INT_ADD", "register:40f0:8", ["const:bd9444:8", "const:4:8"]]
+ 00bda438 ["INT_ADD", "register:40f0:8", ["const:bda438:8", "const:4:8"]]
- 00bd9454 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda448 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bd9458 ["INT_ADD", "register:40f0:8", ["const:bd9458:8", "const:4:8"]]
+ 00bda44c ["INT_ADD", "register:40f0:8", ["const:bda44c:8", "const:4:8"]]
~~~


### [`00bd94c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd94c0.md) → [`00bda4b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda4b4.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda50c",
      "incomplete_value": false,
      "site": "00bda510",
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
      "definition_site": "00bd9518",
      "incomplete_value": false,
      "site": "00bd951c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda550",
      "incomplete_value": true,
      "site": "00bda568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd955c",
      "incomplete_value": true,
      "site": "00bd9574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
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
      "definition_site": "00bda554",
      "incomplete_value": true,
      "site": "00bda568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9560",
      "incomplete_value": true,
      "site": "00bd9574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
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
      60,
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "01126b68",
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
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      88,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "01127b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd94f8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd94fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bda4ec ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bda4f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bd9508 ["INT_ADD", "register:40f0:8", ["const:bd9508:8", "const:4:8"]]
+ 00bda4fc ["INT_ADD", "register:40f0:8", ["const:bda4fc:8", "const:4:8"]]
- 00bd9518 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda50c ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bd9804`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9804.md) → [`00bda7f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda7f8.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md) [`00c5b460`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md) [`00c5c430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda828",
      "incomplete_value": false,
      "site": "00bda82c",
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
      "definition_site": "00bd9834",
      "incomplete_value": false,
      "site": "00bd9838",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda840",
      "incomplete_value": true,
      "site": "00bda848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd984c",
      "incomplete_value": true,
      "site": "00bd9854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
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
      48,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      72,
      "READ",
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
      48,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      72,
      "READ",
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
- 00bd9824 ["INT_ADD", "register:40f0:8", ["const:bd9824:8", "const:4:8"]]
+ 00bda818 ["INT_ADD", "register:40f0:8", ["const:bda818:8", "const:4:8"]]
- 00bd9834 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda828 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bd9838 ["INT_ADD", "register:40f0:8", ["const:bd9838:8", "const:4:8"]]
+ 00bda82c ["INT_ADD", "register:40f0:8", ["const:bda82c:8", "const:4:8"]]
~~~


### [`00bd988c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd988c.md) → [`00bda880`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda880.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de70.md) · 呼出先 3件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 1件 [`00c5ee40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee40.md) · 呼出先 3件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda8ac",
      "incomplete_value": false,
      "site": "00bda8b0",
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
      "definition_site": "00bd98b8",
      "incomplete_value": false,
      "site": "00bd98bc",
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
      44,
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
      44,
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
- 00bd98a8 ["INT_ADD", "register:40f0:8", ["const:bd98a8:8", "const:4:8"]]
+ 00bda89c ["INT_ADD", "register:40f0:8", ["const:bda89c:8", "const:4:8"]]
- 00bd98b8 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda8ac ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bd98bc ["INT_ADD", "register:40f0:8", ["const:bd98bc:8", "const:4:8"]]
+ 00bda8b0 ["INT_ADD", "register:40f0:8", ["const:bda8b0:8", "const:4:8"]]
~~~


### [`00bd991c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd991c.md) → [`00bda910`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bda910.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda94c",
      "incomplete_value": false,
      "site": "00bda950",
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
      "definition_site": "00bd9958",
      "incomplete_value": false,
      "site": "00bd995c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda978",
      "incomplete_value": true,
      "site": "00bda98c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9984",
      "incomplete_value": true,
      "site": "00bd9998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b88:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda97c",
      "incomplete_value": true,
      "site": "00bda98c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9988",
      "incomplete_value": true,
      "site": "00bd9998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01126b88",
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
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01127b48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9938 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd993c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bda92c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bda930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bd9948 ["INT_ADD", "register:40f0:8", ["const:bd9948:8", "const:4:8"]]
+ 00bda93c ["INT_ADD", "register:40f0:8", ["const:bda93c:8", "const:4:8"]]
- 00bd9958 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bda94c ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bd9a68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md) → [`00bdaa5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bdaa5c.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaa98",
      "incomplete_value": false,
      "site": "00bdaa9c",
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
      "definition_site": "00bd9aa4",
      "incomplete_value": false,
      "site": "00bd9aa8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaac4",
      "incomplete_value": true,
      "site": "00bdaad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9ad0",
      "incomplete_value": true,
      "site": "00bd9ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaac8",
      "incomplete_value": true,
      "site": "00bdaad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9ad4",
      "incomplete_value": true,
      "site": "00bd9ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01126ba8",
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
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01127b68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9a84 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd9a88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdaa78 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdaa7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bd9a94 ["INT_ADD", "register:40f0:8", ["const:bd9a94:8", "const:4:8"]]
+ 00bdaa88 ["INT_ADD", "register:40f0:8", ["const:bdaa88:8", "const:4:8"]]
- 00bd9aa4 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdaa98 ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bd9bb4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9bb4.md) → [`00bdaba8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bdaba8.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aaa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aaa0.md) · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 1件 [`00c5ba70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5ba70.md) · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdabe4",
      "incomplete_value": false,
      "site": "00bdabe8",
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
      "definition_site": "00bd9bf0",
      "incomplete_value": false,
      "site": "00bd9bf4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdac48",
      "incomplete_value": false,
      "site": "00bdac4c",
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
            "const:f1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9c54",
      "incomplete_value": false,
      "site": "00bd9c58",
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
            "const:e50:8"
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
      "definition_site": "00bdac54",
      "incomplete_value": true,
      "site": "00bdac58",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9c60",
      "incomplete_value": true,
      "site": "00bd9c64",
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
            "const:130:8"
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "002b7e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "002b7f1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9bc8 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bd9bcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:df8:8"]]
+ 00bdabbc ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00bdabc0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:db8:8"]]
- 00bd9be0 ["INT_ADD", "register:40f0:8", ["const:bd9be0:8", "const:4:8"]]
+ 00bdabd4 ["INT_ADD", "register:40f0:8", ["const:bdabd4:8", "const:4:8"]]
- 00bd9bf0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdabe4 ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bd9d58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md) → [`00bdad4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bdad4c.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdad88",
      "incomplete_value": false,
      "site": "00bdad8c",
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
      "definition_site": "00bd9d94",
      "incomplete_value": false,
      "site": "00bd9d98",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdadb4",
      "incomplete_value": true,
      "site": "00bdadc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9dc0",
      "incomplete_value": true,
      "site": "00bd9dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdadb8",
      "incomplete_value": true,
      "site": "00bdadc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9dc4",
      "incomplete_value": true,
      "site": "00bd9dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01126be8",
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
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01127ba8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9d74 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd9d78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdad68 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdad6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bd9d84 ["INT_ADD", "register:40f0:8", ["const:bd9d84:8", "const:4:8"]]
+ 00bdad78 ["INT_ADD", "register:40f0:8", ["const:bdad78:8", "const:4:8"]]
- 00bd9d94 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdad88 ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bd9ea4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9ea4.md) → [`00bdae98`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bda/00bdae98.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaedc",
      "incomplete_value": false,
      "site": "00bdaee0",
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
      "definition_site": "00bd9ee8",
      "incomplete_value": false,
      "site": "00bd9eec",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaf20",
      "incomplete_value": true,
      "site": "00bdaf38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9f2c",
      "incomplete_value": true,
      "site": "00bd9f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
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
      "definition_site": "00bdaf24",
      "incomplete_value": true,
      "site": "00bdaf38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9f30",
      "incomplete_value": true,
      "site": "00bd9f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
              ]
            ]
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
      40,
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01126c08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01127bc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bd9ec8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bd9ecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdaebc ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdaec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bd9ed8 ["INT_ADD", "register:40f0:8", ["const:bd9ed8:8", "const:4:8"]]
+ 00bdaecc ["INT_ADD", "register:40f0:8", ["const:bdaecc:8", "const:4:8"]]
- 00bd9ee8 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdaedc ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bda028`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda028.md) → [`00bdb01c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb01c.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb06c",
      "incomplete_value": false,
      "site": "00bdb070",
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
      "definition_site": "00bda078",
      "incomplete_value": false,
      "site": "00bda07c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb0c8",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda0d4",
      "incomplete_value": true,
      "site": "00bda0f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb0cc",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda0d8",
      "incomplete_value": true,
      "site": "00bda0f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      172,
      "READ",
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
      52,
      "READ",
      [
        "storage",
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      172,
      "READ",
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
- 00bda058 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bda05c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdb04c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdb050 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bda068 ["INT_ADD", "register:40f0:8", ["const:bda068:8", "const:4:8"]]
+ 00bdb05c ["INT_ADD", "register:40f0:8", ["const:bdb05c:8", "const:4:8"]]
- 00bda078 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb06c ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bda1ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda1ec.md) → [`00bdb1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb1e0.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb234",
      "incomplete_value": false,
      "site": "00bdb238",
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
      "definition_site": "00bda240",
      "incomplete_value": false,
      "site": "00bda244",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb290",
      "incomplete_value": true,
      "site": "00bdb2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda29c",
      "incomplete_value": true,
      "site": "00bda2b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb294",
      "incomplete_value": true,
      "site": "00bdb2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda2a0",
      "incomplete_value": true,
      "site": "00bda2b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
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
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      176,
      "READ",
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
      52,
      "READ",
      [
        "storage",
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      176,
      "READ",
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
- 00bda21c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bda220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdb210 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdb214 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bda230 ["INT_ADD", "register:40f0:8", ["const:bda230:8", "const:4:8"]]
+ 00bdb224 ["INT_ADD", "register:40f0:8", ["const:bdb224:8", "const:4:8"]]
- 00bda240 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb234 ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bda4ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda4ac.md) → [`00bdb4a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb4a0.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdc4c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4c4.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5aed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdd4b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd4b8.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bea0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb4e8",
      "incomplete_value": true,
      "site": "00bdb4fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda4f4",
      "incomplete_value": true,
      "site": "00bda508",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:b00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb524",
      "incomplete_value": true,
      "site": "00bdb538",
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
            "const:d7a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda530",
      "incomplete_value": true,
      "site": "00bda544",
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
            "const:c9c:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb548",
      "incomplete_value": false,
      "site": "00bdb54c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:a36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda554",
      "incomplete_value": false,
      "site": "00bda558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      72,
      "READ",
      [
        "storage",
        "00c9bb00",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00bdc4c4",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002b9c9c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      72,
      "READ",
      [
        "storage",
        "00c9cad0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00bdd4b8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002b9d7a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bda4d0 ["INT_ADD", "register:40f0:8", ["const:bda4d0:8", "const:4:8"]]
+ 00bdb4c4 ["INT_ADD", "register:40f0:8", ["const:bdb4c4:8", "const:4:8"]]
- 00bda4dc ["INT_ADD", "register:40f0:8", ["const:bda4dc:8", "const:4:8"]]
+ 00bdb4d0 ["INT_ADD", "register:40f0:8", ["const:bdb4d0:8", "const:4:8"]]
- 00bda4f0 ["COPY", "register:4018:8", ["const:c9b000:8"]]
- 00bda4f4 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b00:8"]]
+ 00bdb4e4 ["COPY", "register:4018:8", ["const:c9c000:8"]]
+ 00bdb4e8 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:ad0:8"]]
~~~


### [`00bda6f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda6f4.md) → [`00bdb6e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb6e8.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

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
      "definition_site": "00bdb6f4",
      "incomplete_value": false,
      "site": "00bdb6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:a36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda700",
      "incomplete_value": false,
      "site": "00bda704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
        "002b4958",
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
        "002b4a36",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bda700 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bdb6f4 ["COPY", "tmp:0:8", ["const:a36:8"]]
- 00bda704 ["INT_ADD", "register:40f0:8", ["const:bda704:8", "const:4:8"]]
+ 00bdb6f8 ["INT_ADD", "register:40f0:8", ["const:bdb6f8:8", "const:4:8"]]
~~~


### [`00bda740`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda740.md) → [`00bdb734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb734.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb760",
      "incomplete_value": false,
      "site": "00bdb764",
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
      "definition_site": "00bda76c",
      "incomplete_value": false,
      "site": "00bda770",
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
      44,
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
      44,
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
- 00bda75c ["INT_ADD", "register:40f0:8", ["const:bda75c:8", "const:4:8"]]
+ 00bdb750 ["INT_ADD", "register:40f0:8", ["const:bdb750:8", "const:4:8"]]
- 00bda76c ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb760 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bda770 ["INT_ADD", "register:40f0:8", ["const:bda770:8", "const:4:8"]]
+ 00bdb764 ["INT_ADD", "register:40f0:8", ["const:bdb764:8", "const:4:8"]]
~~~


### [`00bda7e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda7e4.md) → [`00bdb7d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb7d8.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df10.md) · 呼出先 3件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 1件 [`00c5eee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eee0.md) · 呼出先 3件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb808",
      "incomplete_value": false,
      "site": "00bdb80c",
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
      "definition_site": "00bda814",
      "incomplete_value": false,
      "site": "00bda818",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb83c",
      "incomplete_value": false,
      "site": "00bdb840",
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
      "definition_site": "00bda848",
      "incomplete_value": false,
      "site": "00bda84c",
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
      48,
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ],
    [
      100,
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
      48,
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ],
    [
      100,
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
- 00bda804 ["INT_ADD", "register:40f0:8", ["const:bda804:8", "const:4:8"]]
+ 00bdb7f8 ["INT_ADD", "register:40f0:8", ["const:bdb7f8:8", "const:4:8"]]
- 00bda814 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb808 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bda818 ["INT_ADD", "register:40f0:8", ["const:bda818:8", "const:4:8"]]
+ 00bdb80c ["INT_ADD", "register:40f0:8", ["const:bdb80c:8", "const:4:8"]]
~~~


### [`00bda8b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda8b8.md) → [`00bdb8ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb8ac.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb8d4",
      "incomplete_value": false,
      "site": "00bdb8d8",
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
      "definition_site": "00bda8e0",
      "incomplete_value": false,
      "site": "00bda8e4",
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
- 00bda8d0 ["INT_ADD", "register:40f0:8", ["const:bda8d0:8", "const:4:8"]]
+ 00bdb8c4 ["INT_ADD", "register:40f0:8", ["const:bdb8c4:8", "const:4:8"]]
- 00bda8e0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb8d4 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bda8e4 ["INT_ADD", "register:40f0:8", ["const:bda8e4:8", "const:4:8"]]
+ 00bdb8d8 ["INT_ADD", "register:40f0:8", ["const:bdb8d8:8", "const:4:8"]]
~~~


### [`00bda924`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda924.md) → [`00bdb918`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb918.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb940",
      "incomplete_value": false,
      "site": "00bdb944",
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
      "definition_site": "00bda94c",
      "incomplete_value": false,
      "site": "00bda950",
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
- 00bda93c ["INT_ADD", "register:40f0:8", ["const:bda93c:8", "const:4:8"]]
+ 00bdb930 ["INT_ADD", "register:40f0:8", ["const:bdb930:8", "const:4:8"]]
- 00bda94c ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb940 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bda950 ["INT_ADD", "register:40f0:8", ["const:bda950:8", "const:4:8"]]
+ 00bdb944 ["INT_ADD", "register:40f0:8", ["const:bdb944:8", "const:4:8"]]
~~~


### [`00bda998`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda998.md) → [`00bdb98c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb98c.md) _ZN8firebase4auth17PhoneAuthProviderD1Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5da90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5da90.md) · 呼出先 4件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 1件 [`00c5ea60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ea60.md) · 呼出先 4件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdb9b4",
      "incomplete_value": false,
      "site": "00bdb9b8",
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
      "definition_site": "00bda9c0",
      "incomplete_value": false,
      "site": "00bda9c4",
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
- 00bda9b0 ["INT_ADD", "register:40f0:8", ["const:bda9b0:8", "const:4:8"]]
+ 00bdb9a4 ["INT_ADD", "register:40f0:8", ["const:bdb9a4:8", "const:4:8"]]
- 00bda9c0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdb9b4 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bda9c4 ["INT_ADD", "register:40f0:8", ["const:bda9c4:8", "const:4:8"]]
+ 00bdb9b8 ["INT_ADD", "register:40f0:8", ["const:bdb9b8:8", "const:4:8"]]
~~~


### [`00bdaa08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa08.md) → [`00bdb9fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb9fc.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00589734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00589a54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdba14",
      "incomplete_value": true,
      "site": "00bdba18",
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
      "definition_site": "00bdaa20",
      "incomplete_value": true,
      "site": "00bdaa24",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdba3c",
      "incomplete_value": false,
      "site": "00bdba40",
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
      "definition_site": "00bdaa48",
      "incomplete_value": false,
      "site": "00bdaa4c",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdba54",
      "incomplete_value": true,
      "site": "00bdba64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdaa60",
      "incomplete_value": true,
      "site": "00bdaa70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
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
      16,
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c92610",
        null,
        "undefined1[64]"
      ]
    ],
    [
      64,
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
      16,
      "READ",
      [
        "storage",
        "00c9cae0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c935e0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      64,
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
- 00bdaa14 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bdaa18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00bdba08 ["COPY", "register:4040:8", ["const:c9c000:8"]]
+ 00bdba0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ae0:8"]]
- 00bdaa2c ["INT_ADD", "register:40f0:8", ["const:bdaa2c:8", "const:4:8"]]
+ 00bdba20 ["INT_ADD", "register:40f0:8", ["const:bdba20:8", "const:4:8"]]
- 00bdaa38 ["INT_ADD", "register:40f0:8", ["const:bdaa38:8", "const:4:8"]]
+ 00bdba2c ["INT_ADD", "register:40f0:8", ["const:bdba2c:8", "const:4:8"]]
~~~


### [`00bdaa9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdaa9c.md) → [`00bdba90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdba90.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00574d2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0057504c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bdbaa8",
      "incomplete_value": true,
      "site": "00bdbaac",
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
      "definition_site": "00bdaab4",
      "incomplete_value": true,
      "site": "00bdaab8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbac0",
      "incomplete_value": false,
      "site": "00bdbac4",
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
      "definition_site": "00bdaacc",
      "incomplete_value": false,
      "site": "00bdaad0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbad8",
      "incomplete_value": true,
      "site": "00bdbae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdaae4",
      "incomplete_value": true,
      "site": "00bdaaf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
          ]
        ]
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
      16,
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c92610",
        null,
        "undefined1[64]"
      ]
    ],
    [
      48,
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
      16,
      "READ",
      [
        "storage",
        "00c9cae0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c935e0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      48,
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
- 00bdaaa8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bdaaac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00bdba9c ["COPY", "register:4040:8", ["const:c9c000:8"]]
+ 00bdbaa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ae0:8"]]
- 00bdaabc ["INT_ADD", "register:40f0:8", ["const:bdaabc:8", "const:4:8"]]
+ 00bdbab0 ["INT_ADD", "register:40f0:8", ["const:bdbab0:8", "const:4:8"]]
- 00bdaacc ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdbac0 ["COPY", "tmp:0:8", ["const:653:8"]]
~~~


### [`00bdab34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bdab34.md) → [`00bdbb28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdbb28.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00589a54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 13件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbb94",
      "incomplete_value": true,
      "site": "00bdbbac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bdaba0",
      "incomplete_value": true,
      "site": "00bdabb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbba0",
      "incomplete_value": true,
      "site": "00bdbbac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdabac",
      "incomplete_value": true,
      "site": "00bdabb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdbbc4",
      "incomplete_value": false,
      "site": "00bdbbcc",
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
            "const:9a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdabd0",
      "incomplete_value": false,
      "site": "00bdabd8",
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
            "const:8c9:8"
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
      108,
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "002be8c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      108,
      "READ",
      [
        "storage",
        "01127c38",
        null,
        "undefined8"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "01127c48",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "002be9a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdab94 ["INT_ADD", "register:40f0:8", ["const:bdab94:8", "const:4:8"]]
+ 00bdbb88 ["INT_ADD", "register:40f0:8", ["const:bdbb88:8", "const:4:8"]]
- 00bdab9c ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bdaba0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
+ 00bdbb90 ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00bdbb94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c38:8"]]
- 00bdaba4 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bdbb98 ["COPY", "register:4048:8", ["const:1127000:8"]]
~~~


### [`00bdb054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md) → [`00bdc048`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc048.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5ad70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5bd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc0c0",
      "incomplete_value": true,
      "site": "00bdc0d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00bdb0cc",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc0c4",
      "incomplete_value": true,
      "site": "00bdc0d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdb0d0",
      "incomplete_value": true,
      "site": "00bdb0e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc130",
      "incomplete_value": false,
      "site": "00bdc134",
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
      "definition_site": "00bdb13c",
      "incomplete_value": false,
      "site": "00bdb140",
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
      40,
      "READ",
      [
        "storage",
        "01126df8",
        null,
        "undefined1"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "01126ce8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      40,
      "READ",
      [
        "storage",
        "01127db8",
        null,
        "undefined1"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "01127c90",
        null,
        "undefined8"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "01127ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdb078 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdb07c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df8:8"]]
+ 00bdc06c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdc070 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 00bdb094 ["INT_ADD", "register:40f0:8", ["const:bdb094:8", "const:4:8"]]
+ 00bdc088 ["INT_ADD", "register:40f0:8", ["const:bdc088:8", "const:4:8"]]
- 00bdb0a8 ["INT_ADD", "register:40f0:8", ["const:bdb0a8:8", "const:4:8"]]
+ 00bdc09c ["INT_ADD", "register:40f0:8", ["const:bdc09c:8", "const:4:8"]]
~~~


### [`00bdb270`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb270.md) → [`00bdc264`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc264.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b330`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b330.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc2a4",
      "incomplete_value": false,
      "site": "00bdc2a8",
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
      "definition_site": "00bdb2b0",
      "incomplete_value": false,
      "site": "00bdb2b4",
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
      64,
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
      64,
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
- 00bdb2a0 ["INT_ADD", "register:40f0:8", ["const:bdb2a0:8", "const:4:8"]]
+ 00bdc294 ["INT_ADD", "register:40f0:8", ["const:bdc294:8", "const:4:8"]]
- 00bdb2b0 ["COPY", "tmp:0:8", ["const:609:8"]]
+ 00bdc2a4 ["COPY", "tmp:0:8", ["const:653:8"]]
- 00bdb2b4 ["INT_ADD", "register:40f0:8", ["const:bdb2b4:8", "const:4:8"]]
+ 00bdc2a8 ["INT_ADD", "register:40f0:8", ["const:bdc2a8:8", "const:4:8"]]
~~~


### [`00bdb40c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb40c.md) → [`00bdc400`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc400.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdc4a8",
      "incomplete_value": false,
      "site": "00bdc4ac",
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
      "definition_site": "00bdb4b4",
      "incomplete_value": false,
      "site": "00bdb4b8",
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
      168,
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
      168,
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
- 00bdb444 ["INT_ADD", "register:40f0:8", ["const:bdb444:8", "const:4:8"]]
+ 00bdc438 ["INT_ADD", "register:40f0:8", ["const:bdc438:8", "const:4:8"]]
- 00bdb458 ["INT_ADD", "register:40f0:8", ["const:bdb458:8", "const:4:8"]]
+ 00bdc44c ["INT_ADD", "register:40f0:8", ["const:bdc44c:8", "const:4:8"]]
- 00bdb468 ["INT_ADD", "register:40f0:8", ["const:bdb468:8", "const:4:8"]]
+ 00bdc45c ["INT_ADD", "register:40f0:8", ["const:bdc45c:8", "const:4:8"]]
~~~


### [`00bdbcd4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md) → [`00bdccc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdccc8.md) FUN_00bdccc8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bdb930`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb930.md) [`00bdbf14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbf14.md) [`00bdc1ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc1ec.md) · 呼出先 9件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ac70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac70.md) [`00c5b080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b080.md)
- 新版 呼出元 3件 [`00bdc924`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdc924.md) [`00bdcf08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdcf08.md) [`00bdd1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd1e0.md) · 呼出先 9件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00589a54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc40.md) [`00c5c050`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdcd24",
      "incomplete_value": true,
      "site": "00bdcd3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbd30",
      "incomplete_value": true,
      "site": "00bdbd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
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
      "definition_site": "00bdcd28",
      "incomplete_value": true,
      "site": "00bdcd3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbd34",
      "incomplete_value": true,
      "site": "00bdbd48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdcd9c",
      "incomplete_value": true,
      "site": "00bdcdac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdbda8",
      "incomplete_value": true,
      "site": "00bdbdb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      92,
      "READ",
      [
        "storage",
        "01126c28",
        null,
        "undefined8"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "01126c40",
        null,
        "undefined8"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "01126d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      92,
      "READ",
      [
        "storage",
        "01127be8",
        null,
        "undefined8"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "01127c00",
        null,
        "undefined8"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "01127cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdbd04 ["INT_ADD", "register:40f0:8", ["const:bdbd04:8", "const:4:8"]]
+ 00bdccf8 ["INT_ADD", "register:40f0:8", ["const:bdccf8:8", "const:4:8"]]
- 00bdbd24 ["INT_ADD", "register:40f0:8", ["const:bdbd24:8", "const:4:8"]]
+ 00bdcd18 ["INT_ADD", "register:40f0:8", ["const:bdcd18:8", "const:4:8"]]
- 00bdbd28 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdbd2c ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bdbd30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c28:8"]]
+ 00bdcd1c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdcd20 ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00bdcd24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:be8:8"]]
~~~


### [`00bdc4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdc4f0.md) → [`00bdd4e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd4e4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dea0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dea0.md) · 呼出先 10件 [`00c5aad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ee70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee70.md) · 呼出先 10件 [`00c5baa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdd548",
      "incomplete_value": false,
      "site": "00bdd54c",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdc554",
      "incomplete_value": false,
      "site": "00bdc558",
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
            "const:88:8"
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
      100,
      "PARAM",
      [
        "storage",
        "002a7088",
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
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdc51c ["INT_ADD", "register:40f0:8", ["const:bdc51c:8", "const:4:8"]]
+ 00bdd510 ["INT_ADD", "register:40f0:8", ["const:bdd510:8", "const:4:8"]]
- 00bdc528 ["INT_ADD", "register:40f0:8", ["const:bdc528:8", "const:4:8"]]
+ 00bdd51c ["INT_ADD", "register:40f0:8", ["const:bdd51c:8", "const:4:8"]]
- 00bdc544 ["INT_ADD", "register:40f0:8", ["const:bdc544:8", "const:4:8"]]
+ 00bdd538 ["INT_ADD", "register:40f0:8", ["const:bdd538:8", "const:4:8"]]
~~~


### [`00bdccf4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdccf4.md) → [`00bddce8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddce8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5de90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5de90.md) · 呼出先 10件 [`00c5aad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ee60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ee60.md) · 呼出先 10件 [`00c5baa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddd54",
      "incomplete_value": false,
      "site": "00bddd58",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcd60",
      "incomplete_value": false,
      "site": "00bdcd64",
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
            "const:88:8"
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
      108,
      "PARAM",
      [
        "storage",
        "002a7088",
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
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcd28 ["INT_ADD", "register:40f0:8", ["const:bdcd28:8", "const:4:8"]]
+ 00bddd1c ["INT_ADD", "register:40f0:8", ["const:bddd1c:8", "const:4:8"]]
- 00bdcd34 ["INT_ADD", "register:40f0:8", ["const:bdcd34:8", "const:4:8"]]
+ 00bddd28 ["INT_ADD", "register:40f0:8", ["const:bddd28:8", "const:4:8"]]
- 00bdcd50 ["INT_ADD", "register:40f0:8", ["const:bdcd50:8", "const:4:8"]]
+ 00bddd44 ["INT_ADD", "register:40f0:8", ["const:bddd44:8", "const:4:8"]]
~~~


### [`00bdceb4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdceb4.md) → [`00bddea8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddea8.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bdded4",
      "incomplete_value": true,
      "site": "00bdded4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcee0",
      "incomplete_value": true,
      "site": "00bdcee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bddebc",
      "incomplete_value": true,
      "site": "00bddebc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcec8",
      "incomplete_value": true,
      "site": "00bdcec8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddec8",
      "incomplete_value": false,
      "site": "00bddecc",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdced4",
      "incomplete_value": false,
      "site": "00bdced8",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcec0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdcec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bddeb4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bddeb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dc0:8"]]
- 00bdced4 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bddec8 ["COPY", "tmp:0:8", ["const:2da:8"]]
- 00bdced8 ["INT_ADD", "register:40f0:8", ["const:bdced8:8", "const:4:8"]]
+ 00bddecc ["INT_ADD", "register:40f0:8", ["const:bddecc:8", "const:4:8"]]
~~~


### [`00bdcef4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md) → [`00bddee8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddee8.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bddf14",
      "incomplete_value": true,
      "site": "00bddf14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf20",
      "incomplete_value": true,
      "site": "00bdcf20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bddefc",
      "incomplete_value": true,
      "site": "00bddefc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf08",
      "incomplete_value": true,
      "site": "00bdcf08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddf04",
      "incomplete_value": false,
      "site": "00bddf0c",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf10",
      "incomplete_value": false,
      "site": "00bdcf18",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcf00 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdcf04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bddef4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bddef8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dc0:8"]]
- 00bdcf10 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bddf04 ["COPY", "tmp:0:8", ["const:2da:8"]]
- 00bdcf18 ["INT_ADD", "register:40f0:8", ["const:bdcf18:8", "const:4:8"]]
+ 00bddf0c ["INT_ADD", "register:40f0:8", ["const:bddf0c:8", "const:4:8"]]
~~~


### [`00bdcf34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf34.md) → [`00bddf28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddf28.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bddf58",
      "incomplete_value": true,
      "site": "00bddf58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf64",
      "incomplete_value": true,
      "site": "00bdcf64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bddf3c",
      "incomplete_value": true,
      "site": "00bddf3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf48",
      "incomplete_value": true,
      "site": "00bdcf48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddf48",
      "incomplete_value": false,
      "site": "00bddf50",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf54",
      "incomplete_value": false,
      "site": "00bdcf5c",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcf40 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdcf44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bddf34 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bddf38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dc0:8"]]
- 00bdcf54 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bddf48 ["COPY", "tmp:0:8", ["const:2da:8"]]
- 00bdcf5c ["INT_ADD", "register:40f0:8", ["const:bdcf5c:8", "const:4:8"]]
+ 00bddf50 ["INT_ADD", "register:40f0:8", ["const:bddf50:8", "const:4:8"]]
~~~


### [`00bdcf78`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcf78.md) → [`00bddf6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddf6c.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bddf9c",
      "incomplete_value": true,
      "site": "00bddf9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcfa8",
      "incomplete_value": true,
      "site": "00bdcfa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bddf80",
      "incomplete_value": true,
      "site": "00bddf80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf8c",
      "incomplete_value": true,
      "site": "00bdcf8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bddf88",
      "incomplete_value": false,
      "site": "00bddf94",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcf94",
      "incomplete_value": false,
      "site": "00bdcfa0",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcf84 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdcf88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e00:8"]]
+ 00bddf78 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bddf7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:dc0:8"]]
- 00bdcf94 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bddf88 ["COPY", "tmp:0:8", ["const:2da:8"]]
- 00bdcfa0 ["INT_ADD", "register:40f0:8", ["const:bdcfa0:8", "const:4:8"]]
+ 00bddf94 ["INT_ADD", "register:40f0:8", ["const:bddf94:8", "const:4:8"]]
~~~


### [`00bdcfc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcfc8.md) → [`00bddfbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddfbc.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bde014",
      "incomplete_value": true,
      "site": "00bde014",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd020",
      "incomplete_value": true,
      "site": "00bdd020",
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
            "const:e08:8"
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
      "definition_site": "00bddff0",
      "incomplete_value": true,
      "site": "00bddffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdcffc",
      "incomplete_value": true,
      "site": "00bdd008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126e08",
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
        "01127dc8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdcfd8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdcfdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e08:8"]]
+ 00bddfcc ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bddfd0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
- 00bdcff0 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bddfe4 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bdcffc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
+ 00bddff0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc0:8"]]
~~~


### [`00bdd034`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd034.md) → [`00bde028`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde028.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bde064",
      "incomplete_value": true,
      "site": "00bde064",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd070",
      "incomplete_value": true,
      "site": "00bdd070",
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
            "const:e08:8"
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
      "definition_site": "00bde084",
      "incomplete_value": true,
      "site": "00bde084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd090",
      "incomplete_value": true,
      "site": "00bdd090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bde040",
      "incomplete_value": true,
      "site": "00bde040",
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
      "definition_site": "00bdd04c",
      "incomplete_value": true,
      "site": "00bdd04c",
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126e08",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd044 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bdd048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bde038 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bde03c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00bdd050 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd054 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e08:8"]]
+ 00bde044 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde048 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
- 00bdd06c ["INT_ADD", "register:40f0:8", ["const:bdd06c:8", "const:4:8"]]
+ 00bde060 ["INT_ADD", "register:40f0:8", ["const:bde060:8", "const:4:8"]]
~~~


### [`00bdd0a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd0a4.md) → [`00bde098`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde098.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde0d8",
      "incomplete_value": true,
      "site": "00bde0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd0e4",
      "incomplete_value": true,
      "site": "00bdd0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bde0b4",
      "incomplete_value": true,
      "site": "00bde0b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd0c0",
      "incomplete_value": true,
      "site": "00bdd0c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde0bc",
      "incomplete_value": false,
      "site": "00bde0d0",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd0c8",
      "incomplete_value": false,
      "site": "00bdd0dc",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd0b0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde0a4 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd0b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bde0ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00bdd0c8 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bde0bc ["COPY", "tmp:0:8", ["const:2da:8"]]
~~~


### [`00bdd114`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd114.md) → [`00bde108`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde108.md) _ZN8firebase4auth11tokenresult11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bde124",
      "incomplete_value": false,
      "site": "00bde128",
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
      "definition_site": "00bdd130",
      "incomplete_value": false,
      "site": "00bdd134",
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
      "definition_site": "00bde134",
      "incomplete_value": true,
      "site": "00bde140",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd140",
      "incomplete_value": true,
      "site": "00bdd14c",
      "value": [
        "LOAD",
        "8",
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
        "01126e10",
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
        "01127dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd130 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bde124 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bdd134 ["INT_ADD", "register:40f0:8", ["const:bdd134:8", "const:4:8"]]
+ 00bde128 ["INT_ADD", "register:40f0:8", ["const:bde128:8", "const:4:8"]]
- 00bdd138 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd13c ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00bde12c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde130 ["COPY", "tmp:0:8", ["const:dd0:8"]]
~~~


### [`00bdd150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd150.md) → [`00bde144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde144.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde184",
      "incomplete_value": true,
      "site": "00bde184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd190",
      "incomplete_value": true,
      "site": "00bdd190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bde160",
      "incomplete_value": true,
      "site": "00bde160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd16c",
      "incomplete_value": true,
      "site": "00bdd16c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde168",
      "incomplete_value": false,
      "site": "00bde17c",
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
            "const:2da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd174",
      "incomplete_value": false,
      "site": "00bdd188",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd15c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde150 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bde158 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00bdd174 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bde168 ["COPY", "tmp:0:8", ["const:2da:8"]]
~~~


### [`00bdd1c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1c0.md) → [`00bde1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde1b4.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bde1d0",
      "incomplete_value": false,
      "site": "00bde1d4",
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
      "definition_site": "00bdd1dc",
      "incomplete_value": false,
      "site": "00bdd1e0",
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
      "definition_site": "00bde1e0",
      "incomplete_value": true,
      "site": "00bde1ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd1ec",
      "incomplete_value": true,
      "site": "00bdd1f8",
      "value": [
        "LOAD",
        "8",
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
        "01126e18",
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
        "01127dd8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd1dc ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bde1d0 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bdd1e0 ["INT_ADD", "register:40f0:8", ["const:bdd1e0:8", "const:4:8"]]
+ 00bde1d4 ["INT_ADD", "register:40f0:8", ["const:bde1d4:8", "const:4:8"]]
- 00bdd1e4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd1e8 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00bde1d8 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde1dc ["COPY", "tmp:0:8", ["const:dd8:8"]]
~~~


### [`00bdd1fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd1fc.md) → [`00bde1f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde1f0.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00bde21c",
      "incomplete_value": true,
      "site": "00bde21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd228",
      "incomplete_value": true,
      "site": "00bdd228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde204",
      "incomplete_value": true,
      "site": "00bde204",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd210",
      "incomplete_value": true,
      "site": "00bdd210",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde210",
      "incomplete_value": false,
      "site": "00bde214",
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
      "definition_site": "00bdd21c",
      "incomplete_value": false,
      "site": "00bdd220",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd208 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd20c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bde1fc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
- 00bdd21c ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde210 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bdd220 ["INT_ADD", "register:40f0:8", ["const:bdd220:8", "const:4:8"]]
+ 00bde214 ["INT_ADD", "register:40f0:8", ["const:bde214:8", "const:4:8"]]
~~~


### [`00bdd23c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd23c.md) → [`00bde230`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde230.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bde25c",
      "incomplete_value": true,
      "site": "00bde25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd268",
      "incomplete_value": true,
      "site": "00bdd268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde244",
      "incomplete_value": true,
      "site": "00bde244",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd250",
      "incomplete_value": true,
      "site": "00bdd250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde24c",
      "incomplete_value": false,
      "site": "00bde254",
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
      "definition_site": "00bdd258",
      "incomplete_value": false,
      "site": "00bdd260",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd248 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd24c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bde23c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde240 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
- 00bdd258 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde24c ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bdd260 ["INT_ADD", "register:40f0:8", ["const:bdd260:8", "const:4:8"]]
+ 00bde254 ["INT_ADD", "register:40f0:8", ["const:bde254:8", "const:4:8"]]
~~~


### [`00bdd27c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd27c.md) → [`00bde270`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde270.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bde2a0",
      "incomplete_value": true,
      "site": "00bde2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd2ac",
      "incomplete_value": true,
      "site": "00bdd2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde284",
      "incomplete_value": true,
      "site": "00bde284",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd290",
      "incomplete_value": true,
      "site": "00bdd290",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde290",
      "incomplete_value": false,
      "site": "00bde298",
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
      "definition_site": "00bdd29c",
      "incomplete_value": false,
      "site": "00bdd2a4",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd288 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd28c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bde27c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde280 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
- 00bdd29c ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde290 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bdd2a4 ["INT_ADD", "register:40f0:8", ["const:bdd2a4:8", "const:4:8"]]
+ 00bde298 ["INT_ADD", "register:40f0:8", ["const:bde298:8", "const:4:8"]]
~~~


### [`00bdd2c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd2c0.md) → [`00bde2b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde2b4.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde2e4",
      "incomplete_value": true,
      "site": "00bde2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd2f0",
      "incomplete_value": true,
      "site": "00bdd2f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde2c8",
      "incomplete_value": true,
      "site": "00bde2c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd2d4",
      "incomplete_value": true,
      "site": "00bdd2d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde2d0",
      "incomplete_value": false,
      "site": "00bde2dc",
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
      "definition_site": "00bdd2dc",
      "incomplete_value": false,
      "site": "00bdd2e8",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd2cc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd2d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e20:8"]]
+ 00bde2c0 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde2c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
- 00bdd2dc ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde2d0 ["COPY", "tmp:0:8", ["const:983:8"]]
- 00bdd2e8 ["INT_ADD", "register:40f0:8", ["const:bdd2e8:8", "const:4:8"]]
+ 00bde2dc ["INT_ADD", "register:40f0:8", ["const:bde2dc:8", "const:4:8"]]
~~~


### [`00bdd310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd310.md) → [`00bde304`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde304.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bde35c",
      "incomplete_value": true,
      "site": "00bde35c",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd368",
      "incomplete_value": true,
      "site": "00bdd368",
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
            "const:e28:8"
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
      "definition_site": "00bde338",
      "incomplete_value": true,
      "site": "00bde344",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd344",
      "incomplete_value": true,
      "site": "00bdd350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
        "01126e28",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126e28",
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
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127de0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd320 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd324 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e28:8"]]
+ 00bde314 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde318 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:de8:8"]]
- 00bdd338 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bde32c ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bdd344 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e20:8"]]
+ 00bde338 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
~~~


### [`00bdd37c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd37c.md) → [`00bde370`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde370.md) _ZN8firebase4auth4user12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bde3ac",
      "incomplete_value": true,
      "site": "00bde3ac",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd3b8",
      "incomplete_value": true,
      "site": "00bdd3b8",
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
            "const:e28:8"
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
      "definition_site": "00bde3cc",
      "incomplete_value": true,
      "site": "00bde3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd3d8",
      "incomplete_value": true,
      "site": "00bdd3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde388",
      "incomplete_value": true,
      "site": "00bde388",
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
      "definition_site": "00bdd394",
      "incomplete_value": true,
      "site": "00bdd394",
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
        "01126e20",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126e28",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126e28",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd38c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bdd390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bde380 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bde384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00bdd398 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd39c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e28:8"]]
+ 00bde38c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde390 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:de8:8"]]
- 00bdd3b4 ["INT_ADD", "register:40f0:8", ["const:bdd3b4:8", "const:4:8"]]
+ 00bde3a8 ["INT_ADD", "register:40f0:8", ["const:bde3a8:8", "const:4:8"]]
~~~


### [`00bdd3ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd3ec.md) → [`00bde3e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde3e0.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde420",
      "incomplete_value": true,
      "site": "00bde420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd42c",
      "incomplete_value": true,
      "site": "00bdd42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde3fc",
      "incomplete_value": true,
      "site": "00bde3fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd408",
      "incomplete_value": true,
      "site": "00bdd408",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde404",
      "incomplete_value": false,
      "site": "00bde418",
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
      "definition_site": "00bdd410",
      "incomplete_value": false,
      "site": "00bdd424",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd3f8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde3ec ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd400 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bde3f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00bdd410 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde404 ["COPY", "tmp:0:8", ["const:983:8"]]
~~~


### [`00bdd45c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd45c.md) → [`00bde450`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde450.md) _ZN8firebase4auth4user11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bde46c",
      "incomplete_value": false,
      "site": "00bde470",
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
      "definition_site": "00bdd478",
      "incomplete_value": false,
      "site": "00bdd47c",
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
      "definition_site": "00bde47c",
      "incomplete_value": true,
      "site": "00bde488",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd488",
      "incomplete_value": true,
      "site": "00bdd494",
      "value": [
        "LOAD",
        "8",
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
        "01126e30",
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
        "01127df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd478 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bde46c ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bdd47c ["INT_ADD", "register:40f0:8", ["const:bdd47c:8", "const:4:8"]]
+ 00bde470 ["INT_ADD", "register:40f0:8", ["const:bde470:8", "const:4:8"]]
- 00bdd480 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd484 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00bde474 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde478 ["COPY", "tmp:0:8", ["const:df0:8"]]
~~~


### [`00bdd498`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd498.md) → [`00bde48c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde48c.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde4cc",
      "incomplete_value": true,
      "site": "00bde4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd4d8",
      "incomplete_value": true,
      "site": "00bdd4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00bde4a8",
      "incomplete_value": true,
      "site": "00bde4a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd4b4",
      "incomplete_value": true,
      "site": "00bdd4b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde4b0",
      "incomplete_value": false,
      "site": "00bde4c4",
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
      "definition_site": "00bdd4bc",
      "incomplete_value": false,
      "site": "00bdd4d0",
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
        "01126e20",
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
        "01126e20",
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
        "01127de0",
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
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd4a4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde498 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd4ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e20:8"]]
+ 00bde4a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:de0:8"]]
- 00bdd4bc ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00bde4b0 ["COPY", "tmp:0:8", ["const:983:8"]]
~~~


### [`00bdd508`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd508.md) → [`00bde4fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde4fc.md) _ZN8firebase4auth4user10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bde518",
      "incomplete_value": false,
      "site": "00bde51c",
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
      "definition_site": "00bdd524",
      "incomplete_value": false,
      "site": "00bdd528",
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
      "definition_site": "00bde528",
      "incomplete_value": true,
      "site": "00bde534",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd534",
      "incomplete_value": true,
      "site": "00bdd540",
      "value": [
        "LOAD",
        "8",
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
        "01126ea8",
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
        "01127e68",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd524 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bde518 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bdd528 ["INT_ADD", "register:40f0:8", ["const:bdd528:8", "const:4:8"]]
+ 00bde51c ["INT_ADD", "register:40f0:8", ["const:bde51c:8", "const:4:8"]]
- 00bdd52c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd530 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00bde520 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde524 ["COPY", "tmp:0:8", ["const:e68:8"]]
~~~


### [`00bdd544`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd544.md) → [`00bde538`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde538.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bde564",
      "incomplete_value": true,
      "site": "00bde564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd570",
      "incomplete_value": true,
      "site": "00bdd570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde54c",
      "incomplete_value": true,
      "site": "00bde54c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd558",
      "incomplete_value": true,
      "site": "00bdd558",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde558",
      "incomplete_value": false,
      "site": "00bde55c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd564",
      "incomplete_value": false,
      "site": "00bdd568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd550 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd554 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bde544 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00bdd564 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde558 ["COPY", "tmp:0:8", ["const:7f7:8"]]
- 00bdd568 ["INT_ADD", "register:40f0:8", ["const:bdd568:8", "const:4:8"]]
+ 00bde55c ["INT_ADD", "register:40f0:8", ["const:bde55c:8", "const:4:8"]]
~~~


### [`00bdd584`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd584.md) → [`00bde578`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde578.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bde5a4",
      "incomplete_value": true,
      "site": "00bde5a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5b0",
      "incomplete_value": true,
      "site": "00bdd5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde58c",
      "incomplete_value": true,
      "site": "00bde58c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd598",
      "incomplete_value": true,
      "site": "00bdd598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde594",
      "incomplete_value": false,
      "site": "00bde59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5a0",
      "incomplete_value": false,
      "site": "00bdd5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd590 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bde584 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00bdd5a0 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde594 ["COPY", "tmp:0:8", ["const:7f7:8"]]
- 00bdd5a8 ["INT_ADD", "register:40f0:8", ["const:bdd5a8:8", "const:4:8"]]
+ 00bde59c ["INT_ADD", "register:40f0:8", ["const:bde59c:8", "const:4:8"]]
~~~


### [`00bdd5c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd5c4.md) → [`00bde5b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde5b8.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bde5e8",
      "incomplete_value": true,
      "site": "00bde5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5f4",
      "incomplete_value": true,
      "site": "00bdd5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde5cc",
      "incomplete_value": true,
      "site": "00bde5cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5d8",
      "incomplete_value": true,
      "site": "00bdd5d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde5d8",
      "incomplete_value": false,
      "site": "00bde5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd5e4",
      "incomplete_value": false,
      "site": "00bdd5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd5d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd5d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bde5c4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde5c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00bdd5e4 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde5d8 ["COPY", "tmp:0:8", ["const:7f7:8"]]
- 00bdd5ec ["INT_ADD", "register:40f0:8", ["const:bdd5ec:8", "const:4:8"]]
+ 00bde5e0 ["INT_ADD", "register:40f0:8", ["const:bde5e0:8", "const:4:8"]]
~~~


### [`00bdd608`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd608.md) → [`00bde5fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde5fc.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde62c",
      "incomplete_value": true,
      "site": "00bde62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd638",
      "incomplete_value": true,
      "site": "00bdd638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde610",
      "incomplete_value": true,
      "site": "00bde610",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd61c",
      "incomplete_value": true,
      "site": "00bdd61c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde618",
      "incomplete_value": false,
      "site": "00bde624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd624",
      "incomplete_value": false,
      "site": "00bdd630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd614 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd618 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:eb0:8"]]
+ 00bde608 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde60c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e70:8"]]
- 00bdd624 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde618 ["COPY", "tmp:0:8", ["const:7f7:8"]]
- 00bdd630 ["INT_ADD", "register:40f0:8", ["const:bdd630:8", "const:4:8"]]
+ 00bde624 ["INT_ADD", "register:40f0:8", ["const:bde624:8", "const:4:8"]]
~~~


### [`00bdd658`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md) → [`00bde64c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde64c.md) _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bde6a4",
      "incomplete_value": true,
      "site": "00bde6a4",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd6b0",
      "incomplete_value": true,
      "site": "00bdd6b0",
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
            "const:eb8:8"
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
      "definition_site": "00bde680",
      "incomplete_value": true,
      "site": "00bde68c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd68c",
      "incomplete_value": true,
      "site": "00bdd698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
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
        "01126eb8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126eb8",
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
        "01127e78",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127e78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd668 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd66c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:eb8:8"]]
+ 00bde65c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde660 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e78:8"]]
- 00bdd680 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bde674 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bdd68c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:eb0:8"]]
+ 00bde680 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
~~~


### [`00bdd6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd6c4.md) → [`00bde6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde6b8.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bde6f4",
      "incomplete_value": true,
      "site": "00bde6f4",
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
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd700",
      "incomplete_value": true,
      "site": "00bdd700",
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
            "const:eb8:8"
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
      "definition_site": "00bde714",
      "incomplete_value": true,
      "site": "00bde714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd720",
      "incomplete_value": true,
      "site": "00bdd720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde6d0",
      "incomplete_value": true,
      "site": "00bde6d0",
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
      "definition_site": "00bdd6dc",
      "incomplete_value": true,
      "site": "00bdd6dc",
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126eb8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126eb8",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127e78",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127e78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd6d4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bdd6d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bde6c8 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bde6cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
- 00bdd6e0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd6e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:eb8:8"]]
+ 00bde6d4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde6d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e78:8"]]
- 00bdd6fc ["INT_ADD", "register:40f0:8", ["const:bdd6fc:8", "const:4:8"]]
+ 00bde6f0 ["INT_ADD", "register:40f0:8", ["const:bde6f0:8", "const:4:8"]]
~~~


### [`00bdd734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd734.md) → [`00bde728`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde728.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bde768",
      "incomplete_value": true,
      "site": "00bde768",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd774",
      "incomplete_value": true,
      "site": "00bdd774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde744",
      "incomplete_value": true,
      "site": "00bde744",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd750",
      "incomplete_value": true,
      "site": "00bdd750",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00bdd750"
      ],
      [
        "FALL_THROUGH",
        "00bde744"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bde744",
      "incomplete_value": true,
      "site": "00bde768",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd750",
      "incomplete_value": true,
      "site": "00bdd774",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd740 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde734 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bde73c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
- 00bdd758 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde74c ["COPY", "tmp:0:8", ["const:7f7:8"]]
~~~


### [`00bdd7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7a4.md) → [`00bde798`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde798.md) _ZN8firebase4auth8userinfo11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bde7b4",
      "incomplete_value": false,
      "site": "00bde7b8",
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
      "definition_site": "00bdd7c0",
      "incomplete_value": false,
      "site": "00bdd7c4",
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
      "definition_site": "00bde7c4",
      "incomplete_value": true,
      "site": "00bde7d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd7d0",
      "incomplete_value": true,
      "site": "00bdd7dc",
      "value": [
        "LOAD",
        "8",
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
        "01126ec0",
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
        "01127e80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd7c0 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bde7b4 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bdd7c4 ["INT_ADD", "register:40f0:8", ["const:bdd7c4:8", "const:4:8"]]
+ 00bde7b8 ["INT_ADD", "register:40f0:8", ["const:bde7b8:8", "const:4:8"]]
- 00bdd7c8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd7cc ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 00bde7bc ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde7c0 ["COPY", "tmp:0:8", ["const:e80:8"]]
~~~


### [`00bdd7e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd7e0.md) → [`00bde7d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde7d4.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde814",
      "incomplete_value": true,
      "site": "00bde814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd820",
      "incomplete_value": true,
      "site": "00bdd820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00bde7f0",
      "incomplete_value": true,
      "site": "00bde7f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd7fc",
      "incomplete_value": true,
      "site": "00bdd7fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde7f8",
      "incomplete_value": false,
      "site": "00bde80c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd804",
      "incomplete_value": false,
      "site": "00bdd818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126eb0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b1720",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126eb0",
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
        "01127e70",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002b17f7",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127e70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd7ec ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bde7e0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdd7f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
+ 00bde7e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
- 00bdd804 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 00bde7f8 ["COPY", "tmp:0:8", ["const:7f7:8"]]
~~~


### [`00bdd850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd850.md) → [`00bde844`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde844.md) _ZN8firebase4auth8userinfo10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bde860",
      "incomplete_value": false,
      "site": "00bde864",
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
      "definition_site": "00bdd86c",
      "incomplete_value": false,
      "site": "00bdd870",
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
      "definition_site": "00bde870",
      "incomplete_value": true,
      "site": "00bde87c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdd87c",
      "incomplete_value": true,
      "site": "00bdd888",
      "value": [
        "LOAD",
        "8",
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
        "01126ef8",
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
        "01127eb8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd86c ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bde860 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bdd870 ["INT_ADD", "register:40f0:8", ["const:bdd870:8", "const:4:8"]]
+ 00bde864 ["INT_ADD", "register:40f0:8", ["const:bde864:8", "const:4:8"]]
- 00bdd874 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdd878 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00bde868 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bde86c ["COPY", "tmp:0:8", ["const:eb8:8"]]
~~~


### [`00bdd88c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd88c.md) → [`00bde880`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde880.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00bde8ac",
      "incomplete_value": true,
      "site": "00bde8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8b8",
      "incomplete_value": true,
      "site": "00bdd8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bde894",
      "incomplete_value": true,
      "site": "00bde894",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8a0",
      "incomplete_value": true,
      "site": "00bdd8a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde8a0",
      "incomplete_value": false,
      "site": "00bde8a4",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8ac",
      "incomplete_value": false,
      "site": "00bdd8b0",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd898 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd89c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bde88c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ec0:8"]]
- 00bdd8ac ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bde8a0 ["COPY", "tmp:0:8", ["const:a37:8"]]
- 00bdd8b0 ["INT_ADD", "register:40f0:8", ["const:bdd8b0:8", "const:4:8"]]
+ 00bde8a4 ["INT_ADD", "register:40f0:8", ["const:bde8a4:8", "const:4:8"]]
~~~


### [`00bdd8cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd8cc.md) → [`00bde8c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde8c0.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00bde8ec",
      "incomplete_value": true,
      "site": "00bde8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8f8",
      "incomplete_value": true,
      "site": "00bdd8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bde8d4",
      "incomplete_value": true,
      "site": "00bde8d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8e0",
      "incomplete_value": true,
      "site": "00bdd8e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde8dc",
      "incomplete_value": false,
      "site": "00bde8e4",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd8e8",
      "incomplete_value": false,
      "site": "00bdd8f0",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd8d8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd8dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bde8cc ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde8d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ec0:8"]]
- 00bdd8e8 ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bde8dc ["COPY", "tmp:0:8", ["const:a37:8"]]
- 00bdd8f0 ["INT_ADD", "register:40f0:8", ["const:bdd8f0:8", "const:4:8"]]
+ 00bde8e4 ["INT_ADD", "register:40f0:8", ["const:bde8e4:8", "const:4:8"]]
~~~


### [`00bdd90c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd90c.md) → [`00bde900`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde900.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bde930",
      "incomplete_value": true,
      "site": "00bde930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd93c",
      "incomplete_value": true,
      "site": "00bdd93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bde914",
      "incomplete_value": true,
      "site": "00bde914",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd920",
      "incomplete_value": true,
      "site": "00bdd920",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde920",
      "incomplete_value": false,
      "site": "00bde928",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd92c",
      "incomplete_value": false,
      "site": "00bdd934",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd918 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd91c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bde90c ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde910 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ec0:8"]]
- 00bdd92c ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bde920 ["COPY", "tmp:0:8", ["const:a37:8"]]
- 00bdd934 ["INT_ADD", "register:40f0:8", ["const:bdd934:8", "const:4:8"]]
+ 00bde928 ["INT_ADD", "register:40f0:8", ["const:bde928:8", "const:4:8"]]
~~~


### [`00bdd950`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd950.md) → [`00bde944`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde944.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bde974",
      "incomplete_value": true,
      "site": "00bde974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd980",
      "incomplete_value": true,
      "site": "00bdd980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bde958",
      "incomplete_value": true,
      "site": "00bde958",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd964",
      "incomplete_value": true,
      "site": "00bdd964",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bde960",
      "incomplete_value": false,
      "site": "00bde96c",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd96c",
      "incomplete_value": false,
      "site": "00bdd978",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd95c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bdd960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f00:8"]]
+ 00bde950 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bde954 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ec0:8"]]
- 00bdd96c ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bde960 ["COPY", "tmp:0:8", ["const:a37:8"]]
- 00bdd978 ["INT_ADD", "register:40f0:8", ["const:bdd978:8", "const:4:8"]]
+ 00bde96c ["INT_ADD", "register:40f0:8", ["const:bde96c:8", "const:4:8"]]
~~~


### [`00bdd9a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd9a0.md) → [`00bde994`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bde994.md) _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bde9ec",
      "incomplete_value": true,
      "site": "00bde9ec",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdd9f8",
      "incomplete_value": true,
      "site": "00bdd9f8",
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
            "const:f08:8"
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
        "01126f08",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126f08",
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
        "01127ec8",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127ec8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdd9b0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdd9b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f08:8"]]
+ 00bde9a4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bde9a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ec8:8"]]
- 00bdd9c8 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bde9bc ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bdd9d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f00:8"]]
+ 00bde9c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
~~~


### [`00bdda0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda0c.md) → [`00bdea00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdea00.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bdea3c",
      "incomplete_value": true,
      "site": "00bdea3c",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdda48",
      "incomplete_value": true,
      "site": "00bdda48",
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
            "const:f08:8"
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
      "definition_site": "00bdea5c",
      "incomplete_value": true,
      "site": "00bdea5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdda68",
      "incomplete_value": true,
      "site": "00bdda68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bdea18",
      "incomplete_value": true,
      "site": "00bdea18",
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
      "definition_site": "00bdda24",
      "incomplete_value": true,
      "site": "00bdda24",
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126f08",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126f08",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127ec8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127ec8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdda1c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bdda20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bdea10 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bdea14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec0:8"]]
- 00bdda28 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bdda2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f08:8"]]
+ 00bdea1c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bdea20 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ec8:8"]]
- 00bdda44 ["INT_ADD", "register:40f0:8", ["const:bdda44:8", "const:4:8"]]
+ 00bdea38 ["INT_ADD", "register:40f0:8", ["const:bdea38:8", "const:4:8"]]
~~~


### [`00bdda7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdda7c.md) → [`00bdea70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdea70.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdeab0",
      "incomplete_value": true,
      "site": "00bdeab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddabc",
      "incomplete_value": true,
      "site": "00bddabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bdea8c",
      "incomplete_value": true,
      "site": "00bdea8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdda98",
      "incomplete_value": true,
      "site": "00bdda98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdea94",
      "incomplete_value": false,
      "site": "00bdeaa8",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddaa0",
      "incomplete_value": false,
      "site": "00bddab4",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdda88 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdea7c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdda90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bdea84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec0:8"]]
- 00bddaa0 ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bdea94 ["COPY", "tmp:0:8", ["const:a37:8"]]
~~~


### [`00bddaec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddaec.md) → [`00bdeae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeae0.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdeafc",
      "incomplete_value": false,
      "site": "00bdeb00",
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
      "definition_site": "00bddb08",
      "incomplete_value": false,
      "site": "00bddb0c",
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
      "definition_site": "00bdeb0c",
      "incomplete_value": true,
      "site": "00bdeb18",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bddb18",
      "incomplete_value": true,
      "site": "00bddb24",
      "value": [
        "LOAD",
        "8",
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
        "01126f10",
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
        "01127ed0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddb08 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bdeafc ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bddb0c ["INT_ADD", "register:40f0:8", ["const:bddb0c:8", "const:4:8"]]
+ 00bdeb00 ["INT_ADD", "register:40f0:8", ["const:bdeb00:8", "const:4:8"]]
- 00bddb10 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bddb14 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 00bdeb04 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdeb08 ["COPY", "tmp:0:8", ["const:ed0:8"]]
~~~


### [`00bddb28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb28.md) → [`00bdeb1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeb1c.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdeb5c",
      "incomplete_value": true,
      "site": "00bdeb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb68",
      "incomplete_value": true,
      "site": "00bddb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f00:8"
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
      "definition_site": "00bdeb38",
      "incomplete_value": true,
      "site": "00bdeb38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb44",
      "incomplete_value": true,
      "site": "00bddb44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdeb40",
      "incomplete_value": false,
      "site": "00bdeb54",
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
            "const:a37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddb4c",
      "incomplete_value": false,
      "site": "00bddb60",
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
            "const:959:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002be959",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126f00",
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
        "01127ec0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002bea37",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127ec0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddb34 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdeb28 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bddb3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00bdeb30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec0:8"]]
- 00bddb4c ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00bdeb40 ["COPY", "tmp:0:8", ["const:a37:8"]]
~~~


### [`00bddb98`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddb98.md) → [`00bdeb8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeb8c.md) _ZN8firebase4auth8metadata10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdeba8",
      "incomplete_value": false,
      "site": "00bdebac",
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
      "definition_site": "00bddbb4",
      "incomplete_value": false,
      "site": "00bddbb8",
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
      "definition_site": "00bdebb8",
      "incomplete_value": true,
      "site": "00bdebc4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bddbc4",
      "incomplete_value": true,
      "site": "00bddbd0",
      "value": [
        "LOAD",
        "8",
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
        "01126f20",
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
        "01127ee0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddbb4 ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bdeba8 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bddbb8 ["INT_ADD", "register:40f0:8", ["const:bddbb8:8", "const:4:8"]]
+ 00bdebac ["INT_ADD", "register:40f0:8", ["const:bdebac:8", "const:4:8"]]
- 00bddbbc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bddbc0 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00bdebb0 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdebb4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
~~~


### [`00bddbd4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddbd4.md) → [`00bdebc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdebc8.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bdebf4",
      "incomplete_value": true,
      "site": "00bdebf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc00",
      "incomplete_value": true,
      "site": "00bddc00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdebdc",
      "incomplete_value": true,
      "site": "00bdebdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddbe8",
      "incomplete_value": true,
      "site": "00bddbe8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdebe8",
      "incomplete_value": false,
      "site": "00bdebec",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddbf4",
      "incomplete_value": false,
      "site": "00bddbf8",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddbe0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bddbe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bdebd4 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bdebd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ee8:8"]]
- 00bddbf4 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdebe8 ["COPY", "tmp:0:8", ["const:4f9:8"]]
- 00bddbf8 ["INT_ADD", "register:40f0:8", ["const:bddbf8:8", "const:4:8"]]
+ 00bdebec ["INT_ADD", "register:40f0:8", ["const:bdebec:8", "const:4:8"]]
~~~


### [`00bddc14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc14.md) → [`00bdec08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec08.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00bdec34",
      "incomplete_value": true,
      "site": "00bdec34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc40",
      "incomplete_value": true,
      "site": "00bddc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdec1c",
      "incomplete_value": true,
      "site": "00bdec1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc28",
      "incomplete_value": true,
      "site": "00bddc28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdec24",
      "incomplete_value": false,
      "site": "00bdec2c",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc30",
      "incomplete_value": false,
      "site": "00bddc38",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      44,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddc20 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bddc24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bdec14 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bdec18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ee8:8"]]
- 00bddc30 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdec24 ["COPY", "tmp:0:8", ["const:4f9:8"]]
- 00bddc38 ["INT_ADD", "register:40f0:8", ["const:bddc38:8", "const:4:8"]]
+ 00bdec2c ["INT_ADD", "register:40f0:8", ["const:bdec2c:8", "const:4:8"]]
~~~


### [`00bddc54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc54.md) → [`00bdec48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec48.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bdec78",
      "incomplete_value": true,
      "site": "00bdec78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc84",
      "incomplete_value": true,
      "site": "00bddc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdec5c",
      "incomplete_value": true,
      "site": "00bdec5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc68",
      "incomplete_value": true,
      "site": "00bddc68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdec68",
      "incomplete_value": false,
      "site": "00bdec70",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddc74",
      "incomplete_value": false,
      "site": "00bddc7c",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddc60 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bddc64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bdec54 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bdec58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ee8:8"]]
- 00bddc74 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdec68 ["COPY", "tmp:0:8", ["const:4f9:8"]]
- 00bddc7c ["INT_ADD", "register:40f0:8", ["const:bddc7c:8", "const:4:8"]]
+ 00bdec70 ["INT_ADD", "register:40f0:8", ["const:bdec70:8", "const:4:8"]]
~~~


### [`00bddc98`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddc98.md) → [`00bdec8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdec8c.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdecbc",
      "incomplete_value": true,
      "site": "00bdecbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcc8",
      "incomplete_value": true,
      "site": "00bddcc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdeca0",
      "incomplete_value": true,
      "site": "00bdeca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcac",
      "incomplete_value": true,
      "site": "00bddcac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdeca8",
      "incomplete_value": false,
      "site": "00bdecb4",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddcb4",
      "incomplete_value": false,
      "site": "00bddcc0",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddca4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00bddca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f28:8"]]
+ 00bdec98 ["COPY", "register:4098:8", ["const:1127000:8"]]
+ 00bdec9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ee8:8"]]
- 00bddcb4 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdeca8 ["COPY", "tmp:0:8", ["const:4f9:8"]]
- 00bddcc0 ["INT_ADD", "register:40f0:8", ["const:bddcc0:8", "const:4:8"]]
+ 00bdecb4 ["INT_ADD", "register:40f0:8", ["const:bdecb4:8", "const:4:8"]]
~~~


### [`00bddce8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddce8.md) → [`00bdecdc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdecdc.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bded34",
      "incomplete_value": true,
      "site": "00bded34",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd40",
      "incomplete_value": true,
      "site": "00bddd40",
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
            "const:f30:8"
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
      "definition_site": "00bded10",
      "incomplete_value": true,
      "site": "00bded1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd1c",
      "incomplete_value": true,
      "site": "00bddd28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f28:8"
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
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01126f30",
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
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      88,
      "WRITE",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddcf8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bddcfc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f30:8"]]
+ 00bdecec ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bdecf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ef0:8"]]
- 00bddd10 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bded04 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bddd1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f28:8"]]
+ 00bded10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ee8:8"]]
~~~


### [`00bddd54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddd54.md) → [`00bded48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bded48.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bded84",
      "incomplete_value": true,
      "site": "00bded84",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddd90",
      "incomplete_value": true,
      "site": "00bddd90",
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
            "const:f30:8"
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
      "definition_site": "00bdeda4",
      "incomplete_value": true,
      "site": "00bdeda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdddb0",
      "incomplete_value": true,
      "site": "00bdddb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bded60",
      "incomplete_value": true,
      "site": "00bded60",
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
      "definition_site": "00bddd6c",
      "incomplete_value": true,
      "site": "00bddd6c",
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01126f30",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126f30",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127ef0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddd64 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bddd68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bded58 ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bded5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
- 00bddd70 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bddd74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f30:8"]]
+ 00bded64 ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bded68 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ef0:8"]]
- 00bddd8c ["INT_ADD", "register:40f0:8", ["const:bddd8c:8", "const:4:8"]]
+ 00bded80 ["INT_ADD", "register:40f0:8", ["const:bded80:8", "const:4:8"]]
~~~


### [`00bdddc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdddc4.md) → [`00bdedb8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdedb8.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdedf8",
      "incomplete_value": true,
      "site": "00bdedf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde04",
      "incomplete_value": true,
      "site": "00bdde04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdedd4",
      "incomplete_value": true,
      "site": "00bdedd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddde0",
      "incomplete_value": true,
      "site": "00bddde0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdeddc",
      "incomplete_value": false,
      "site": "00bdedf0",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddde8",
      "incomplete_value": false,
      "site": "00bdddfc",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdddd0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdedc4 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdddd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bdedcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
- 00bddde8 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdeddc ["COPY", "tmp:0:8", ["const:4f9:8"]]
~~~


### [`00bdde34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde34.md) → [`00bdee28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee28.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bdee44",
      "incomplete_value": false,
      "site": "00bdee48",
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
      "definition_site": "00bdde50",
      "incomplete_value": false,
      "site": "00bdde54",
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
      "definition_site": "00bdee54",
      "incomplete_value": true,
      "site": "00bdee60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bdde60",
      "incomplete_value": true,
      "site": "00bdde6c",
      "value": [
        "LOAD",
        "8",
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
        "01126f38",
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
        "01127ef8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdde50 ["COPY", "tmp:0:8", ["const:30b:8"]]
+ 00bdee44 ["COPY", "tmp:0:8", ["const:463:8"]]
- 00bdde54 ["INT_ADD", "register:40f0:8", ["const:bdde54:8", "const:4:8"]]
+ 00bdee48 ["INT_ADD", "register:40f0:8", ["const:bdee48:8", "const:4:8"]]
- 00bdde58 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdde5c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00bdee4c ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdee50 ["COPY", "tmp:0:8", ["const:ef8:8"]]
~~~


### [`00bdde70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdde70.md) → [`00bdee64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdee64.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bdeea4",
      "incomplete_value": true,
      "site": "00bdeea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddeb0",
      "incomplete_value": true,
      "site": "00bddeb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00bdee80",
      "incomplete_value": true,
      "site": "00bdee80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde8c",
      "incomplete_value": true,
      "site": "00bdde8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdee88",
      "incomplete_value": false,
      "site": "00bdee9c",
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
            "const:4f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdde94",
      "incomplete_value": false,
      "site": "00bddea8",
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
            "const:42c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
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
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad42c",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01126f28",
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
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "PARAM",
      [
        "storage",
        "002ad4f9",
        null,
        "string"
      ]
    ],
    [
      64,
      "WRITE",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdde7c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bdee70 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bdde84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f28:8"]]
+ 00bdee78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee8:8"]]
- 00bdde94 ["COPY", "tmp:0:8", ["const:42c:8"]]
+ 00bdee88 ["COPY", "tmp:0:8", ["const:4f9:8"]]
~~~


### [`00bddee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddee0.md) → [`00bdeed4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeed4.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bdeef0",
      "incomplete_value": false,
      "site": "00bdeef4",
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
      "definition_site": "00bddefc",
      "incomplete_value": false,
      "site": "00bddf00",
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
      "definition_site": "00bdef00",
      "incomplete_value": true,
      "site": "00bdef0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bddf0c",
      "incomplete_value": true,
      "site": "00bddf18",
      "value": [
        "LOAD",
        "8",
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
        "01126f58",
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
        "01127f18",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddefc ["COPY", "tmp:0:8", ["const:54d:8"]]
+ 00bdeef0 ["COPY", "tmp:0:8", ["const:61a:8"]]
- 00bddf00 ["INT_ADD", "register:40f0:8", ["const:bddf00:8", "const:4:8"]]
+ 00bdeef4 ["INT_ADD", "register:40f0:8", ["const:bdeef4:8", "const:4:8"]]
- 00bddf04 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bddf08 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00bdeef8 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00bdeefc ["COPY", "tmp:0:8", ["const:f18:8"]]
~~~


### [`00bddf1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bddf1c.md) → [`00bdef10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dd20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd20.md) · 呼出先 2件 [`00c5afe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 1件 [`00c5ecf0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ecf0.md) · 呼出先 2件 [`00c5bfb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 17件, `store_condition` 1件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bdef54",
      "incomplete_value": true,
      "site": "00bdef54",
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
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bddf60",
      "incomplete_value": true,
      "site": "00bddf60",
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
            "const:e00:8"
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
      "definition_site": "00bdefac",
      "incomplete_value": true,
      "site": "00bdefac",
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
    "old": {
      "definition_site": "00bddfb8",
      "incomplete_value": true,
      "site": "00bddfb8",
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
            "const:e20:8"
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
      "definition_site": "00bdf004",
      "incomplete_value": true,
      "site": "00bdf004",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde010",
      "incomplete_value": true,
      "site": "00bde010",
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
            "const:eb0:8"
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
      24,
      "READ",
      [
        "storage",
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "002bc1fc",
        null,
        "string"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "01126e00",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "002bc2da",
        null,
        "string"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "01127dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bddf2c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bdef20 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bddf34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e00:8"]]
+ 00bdef28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc0:8"]]
- 00bddf44 ["COPY", "tmp:0:8", ["const:1fc:8"]]
+ 00bdef38 ["COPY", "tmp:0:8", ["const:2da:8"]]
~~~


### [`00bde108`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde108.md) → [`00bdf0fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf0fc.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dd40.md) · 呼出先 1件 [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5ed10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ed10.md) · 呼出先 1件 [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bdf138",
      "incomplete_value": true,
      "site": "00bdf138",
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
            "const:dc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde144",
      "incomplete_value": true,
      "site": "00bde144",
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
            "const:e08:8"
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
      "definition_site": "00bdf158",
      "incomplete_value": true,
      "site": "00bdf158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde164",
      "incomplete_value": true,
      "site": "00bde164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "definition_site": "00bdf184",
      "incomplete_value": true,
      "site": "00bdf184",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde190",
      "incomplete_value": true,
      "site": "00bde190",
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
            "const:e28:8"
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
        "01126e00",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01126e08",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01126e08",
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
        "01127dc0",
        null,
        "undefined8"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ],
    [
      60,
      "WRITE",
      [
        "storage",
        "01127dc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bde118 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00bde11c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e00:8"]]
+ 00bdf10c ["COPY", "register:40a0:8", ["const:1127000:8"]]
+ 00bdf110 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
- 00bde128 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00bde12c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e08:8"]]
+ 00bdf11c ["COPY", "register:40a8:8", ["const:1127000:8"]]
+ 00bdf120 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
- 00bde140 ["INT_ADD", "register:40f0:8", ["const:bde140:8", "const:4:8"]]
+ 00bdf134 ["INT_ADD", "register:40f0:8", ["const:bdf134:8", "const:4:8"]]
~~~


### [`00bde740`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde740.md) → [`00bdf734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf734.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde8b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde8b4.md) · 呼出先 9件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00bdf8a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdf8a8.md) · 呼出先 9件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdf7b8",
      "incomplete_value": false,
      "site": "00bdf7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:ffe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde7c4",
      "incomplete_value": false,
      "site": "00bde7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:f2f:8"
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
      "definition_site": "00bdf7c4",
      "incomplete_value": true,
      "site": "00bdf7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bde7d0",
      "incomplete_value": true,
      "site": "00bde7dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e10:8"
              ]
            ]
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
      132,
      "PARAM",
      [
        "storage",
        "002b6f2f",
        null,
        "string"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "01126e10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      132,
      "PARAM",
      [
        "storage",
        "002b6ffe",
        null,
        "string"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "01127dd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bde784 ["INT_ADD", "register:40f0:8", ["const:bde784:8", "const:4:8"]]
+ 00bdf778 ["INT_ADD", "register:40f0:8", ["const:bdf778:8", "const:4:8"]]
- 00bde79c ["INT_ADD", "register:40f0:8", ["const:bde79c:8", "const:4:8"]]
+ 00bdf790 ["INT_ADD", "register:40f0:8", ["const:bdf790:8", "const:4:8"]]
- 00bde7ac ["INT_ADD", "register:40f0:8", ["const:bde7ac:8", "const:4:8"]]
+ 00bdf7a0 ["INT_ADD", "register:40f0:8", ["const:bdf7a0:8", "const:4:8"]]
~~~


### [`00bdec18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bdec18.md) → [`00bdfc0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdf/00bdfc0c.md) _ZNK8firebase4auth4User13provider_dataEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5ab80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab80.md) · 呼出先 14件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`005762f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5bb50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb50.md) · 呼出先 14件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00576618`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00576/00576618.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be01a8",
      "incomplete_value": true,
      "site": "00be01ac",
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
      "definition_site": "00bdf1b4",
      "incomplete_value": true,
      "site": "00bdf1b8",
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
    "ordinal": 102,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdfc6c",
      "incomplete_value": true,
      "site": "00bdfc7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdec78",
      "incomplete_value": true,
      "site": "00bdec88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdfe58",
      "incomplete_value": true,
      "site": "00bdfe64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdee64",
      "incomplete_value": true,
      "site": "00bdee70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      96,
      "READ",
      [
        "storage",
        "01126e40",
        null,
        "undefined8"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      96,
      "READ",
      [
        "storage",
        "01127e00",
        null,
        "undefined8"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00c9ca68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdec6c ["INT_ADD", "register:40f0:8", ["const:bdec6c:8", "const:4:8"]]
+ 00bdfc60 ["INT_ADD", "register:40f0:8", ["const:bdfc60:8", "const:4:8"]]
- 00bdec74 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00bdec78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e40:8"]]
+ 00bdfc68 ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00bdfc6c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
- 00bdec88 ["INT_ADD", "register:40f0:8", ["const:bdec88:8", "const:4:8"]]
+ 00bdfc7c ["INT_ADD", "register:40f0:8", ["const:bdfc7c:8", "const:4:8"]]
~~~


### [`00bdf324`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf324.md) → [`00be0318`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0318.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dfa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfa0.md) · 呼出先 4件 [`00b4035c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5df70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df70.md)
- 新版 呼出元 1件 [`00c5ef70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef70.md) · 呼出先 4件 [`00b41350`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ef40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0428",
      "incomplete_value": false,
      "site": "00be042c",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf434",
      "incomplete_value": false,
      "site": "00bdf438",
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
            "const:61f:8"
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
      272,
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      272,
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdf394 ["INT_ADD", "register:40f0:8", ["const:bdf394:8", "const:4:8"]]
+ 00be0388 ["INT_ADD", "register:40f0:8", ["const:be0388:8", "const:4:8"]]
- 00bdf3b8 ["INT_ADD", "register:40f0:8", ["const:bdf3b8:8", "const:4:8"]]
+ 00be03ac ["INT_ADD", "register:40f0:8", ["const:be03ac:8", "const:4:8"]]
- 00bdf3ec ["INT_ADD", "register:40f0:8", ["const:bdf3ec:8", "const:4:8"]]
+ 00be03e0 ["INT_ADD", "register:40f0:8", ["const:be03e0:8", "const:4:8"]]
~~~


### [`00bdf578`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf578.md) → [`00be056c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be056c.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b460`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0598",
      "incomplete_value": true,
      "site": "00be05a4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf5a4",
      "incomplete_value": true,
      "site": "00bdf5b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ed0:8"
              ]
            ]
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
      44,
      "READ",
      [
        "storage",
        "01126ed0",
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
        "01127e90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdf594 ["INT_ADD", "register:40f0:8", ["const:bdf594:8", "const:4:8"]]
+ 00be0588 ["INT_ADD", "register:40f0:8", ["const:be0588:8", "const:4:8"]]
- 00bdf5a0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdf5a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 00be0594 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00be0598 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00bdf5b0 ["INT_ADD", "register:40f0:8", ["const:bdf5b0:8", "const:4:8"]]
+ 00be05a4 ["INT_ADD", "register:40f0:8", ["const:be05a4:8", "const:4:8"]]
~~~


### [`00bdf5fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf5fc.md) → [`00be05f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be05f0.md) _ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5b3c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b3c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5c390`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be061c",
      "incomplete_value": true,
      "site": "00be0628",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdf628",
      "incomplete_value": true,
      "site": "00bdf634",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ee0:8"
              ]
            ]
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
      44,
      "READ",
      [
        "storage",
        "01126ee0",
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
        "01127ea0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdf618 ["INT_ADD", "register:40f0:8", ["const:bdf618:8", "const:4:8"]]
+ 00be060c ["INT_ADD", "register:40f0:8", ["const:be060c:8", "const:4:8"]]
- 00bdf624 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00bdf628 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 00be0618 ["COPY", "register:4040:8", ["const:1127000:8"]]
+ 00be061c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00bdf634 ["INT_ADD", "register:40f0:8", ["const:bdf634:8", "const:4:8"]]
+ 00be0628 ["INT_ADD", "register:40f0:8", ["const:be0628:8", "const:4:8"]]
~~~


### [`00bdf788`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdf788.md) → [`00be077c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be077c.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5ec20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be0798",
      "incomplete_value": true,
      "site": "00be079c",
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
      "definition_site": "00bdf7a4",
      "incomplete_value": true,
      "site": "00bdf7a8",
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
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c939b0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdf794 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be0788 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bdf79c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
+ 00be0790 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b00:8"]]
- 00bdf7b0 ["INT_ADD", "register:40f0:8", ["const:bdf7b0:8", "const:4:8"]]
+ 00be07a4 ["INT_ADD", "register:40f0:8", ["const:be07a4:8", "const:4:8"]]
~~~


### [`00bdfa14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdf/00bdfa14.md) → [`00be0a08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be0/00be0a08.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00589734`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589734.md) [`00bd055c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd055c.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00589a54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00589/00589a54.md) [`00bd1550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd1550.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0a98",
      "incomplete_value": true,
      "site": "00be0aa8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdfaa4",
      "incomplete_value": true,
      "site": "00bdfab4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be0d50",
      "incomplete_value": true,
      "site": "00be0d60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdfd5c",
      "incomplete_value": true,
      "site": "00bdfd6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "READ",
      [
        "storage",
        "01126f28",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "01126f38",
        null,
        "undefined8"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01126f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      140,
      "READ",
      [
        "storage",
        "01127ee8",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "READ",
      [
        "storage",
        "01127ef8",
        null,
        "undefined8"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00bdfa74 ["INT_ADD", "register:40f0:8", ["const:bdfa74:8", "const:4:8"]]
+ 00be0a68 ["INT_ADD", "register:40f0:8", ["const:be0a68:8", "const:4:8"]]
- 00bdfa80 ["INT_ADD", "register:40f0:8", ["const:bdfa80:8", "const:4:8"]]
+ 00be0a74 ["INT_ADD", "register:40f0:8", ["const:be0a74:8", "const:4:8"]]
- 00bdfa88 ["INT_ADD", "register:40f0:8", ["const:bdfa88:8", "const:4:8"]]
+ 00be0a7c ["INT_ADD", "register:40f0:8", ["const:be0a7c:8", "const:4:8"]]
~~~


### [`00be0014`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0014.md) → [`00be1008`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1008.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5bc80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be1044",
      "incomplete_value": false,
      "site": "00be1048",
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
            "const:cd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0050",
      "incomplete_value": false,
      "site": "00be0054",
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
            "const:c02:8"
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
      60,
      "PARAM",
      [
        "storage",
        "002b5c02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "PARAM",
      [
        "storage",
        "002b5cd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be0050 ["COPY", "tmp:0:8", ["const:c02:8"]]
+ 00be1044 ["COPY", "tmp:0:8", ["const:cd1:8"]]
- 00be0054 ["INT_ADD", "register:40f0:8", ["const:be0054:8", "const:4:8"]]
+ 00be1048 ["INT_ADD", "register:40f0:8", ["const:be1048:8", "const:4:8"]]
- 00be0060 ["INT_ADD", "register:40f0:8", ["const:be0060:8", "const:4:8"]]
+ 00be1054 ["INT_ADD", "register:40f0:8", ["const:be1054:8", "const:4:8"]]
~~~


### [`00be02a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be02a0.md) → [`00be1294`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1294.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bd01a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd0/00bd01a8.md) [`00bd4cd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4cd8.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bd119c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd1/00bd119c.md) [`00bd5ccc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd5/00bd5ccc.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be1390",
      "incomplete_value": true,
      "site": "00be1390",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9c000:8"
              ],
              [
                "leaf",
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be039c",
      "incomplete_value": true,
      "site": "00be039c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:af8:8"
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
      "definition_site": "00be132c",
      "incomplete_value": true,
      "site": "00be133c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0338",
      "incomplete_value": true,
      "site": "00be0348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be13dc",
      "incomplete_value": false,
      "site": "00be13f0",
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
            "const:903:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be03e8",
      "incomplete_value": false,
      "site": "00be03fc",
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
            "const:82c:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 4
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
        "01126e70",
        null,
        "undefined8"
      ]
    ],
    [
      248,
      "READ",
      [
        "storage",
        "00c9baf8",
        null,
        "pointer"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "00bd4cd8",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      152,
      "READ",
      [
        "storage",
        "01127e30",
        null,
        "undefined8"
      ]
    ],
    [
      248,
      "READ",
      [
        "storage",
        "00c9cac8",
        null,
        "pointer"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "00bd5ccc",
        "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00be02f4 ["INT_ADD", "register:40f0:8", ["const:be02f4:8", "const:4:8"]]
+ 00be12e8 ["INT_ADD", "register:40f0:8", ["const:be12e8:8", "const:4:8"]]
- 00be0300 ["INT_ADD", "register:40f0:8", ["const:be0300:8", "const:4:8"]]
+ 00be12f4 ["INT_ADD", "register:40f0:8", ["const:be12f4:8", "const:4:8"]]
- 00be030c ["INT_ADD", "register:40f0:8", ["const:be030c:8", "const:4:8"]]
+ 00be1300 ["INT_ADD", "register:40f0:8", ["const:be1300:8", "const:4:8"]]
~~~


### [`00be0aac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0aac.md) → [`00be1aa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be1/00be1aa0.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5acb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5b0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5bc80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5c0a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be1adc",
      "incomplete_value": false,
      "site": "00be1ae0",
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
            "const:cd1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be0ae8",
      "incomplete_value": false,
      "site": "00be0aec",
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
            "const:c02:8"
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
      60,
      "PARAM",
      [
        "storage",
        "002b5c02",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "PARAM",
      [
        "storage",
        "002b5cd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be0ae8 ["COPY", "tmp:0:8", ["const:c02:8"]]
+ 00be1adc ["COPY", "tmp:0:8", ["const:cd1:8"]]
- 00be0aec ["INT_ADD", "register:40f0:8", ["const:be0aec:8", "const:4:8"]]
+ 00be1ae0 ["INT_ADD", "register:40f0:8", ["const:be1ae0:8", "const:4:8"]]
- 00be0af8 ["INT_ADD", "register:40f0:8", ["const:be0af8:8", "const:4:8"]]
+ 00be1aec ["INT_ADD", "register:40f0:8", ["const:be1aec:8", "const:4:8"]]
~~~


### [`00be1140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1140.md) → [`00be2134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2134.md) _ZNK8firebase4auth4User8metadataEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497874`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`0058f5dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058f/0058f5dc.md) [`00c5b030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`0058f8fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0058f/0058f8fc.md) [`00c5c000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be2168",
      "incomplete_value": true,
      "site": "00be2174",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be1174",
      "incomplete_value": true,
      "site": "00be1180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be2190",
      "incomplete_value": true,
      "site": "00be219c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be119c",
      "incomplete_value": true,
      "site": "00be11a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
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
      52,
      "READ",
      [
        "storage",
        "01126ea0",
        null,
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01126f10",
        null,
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01126f18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "01127e60",
        null,
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127ed0",
        null,
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01127ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be1168 ["INT_ADD", "register:40f0:8", ["const:be1168:8", "const:4:8"]]
+ 00be215c ["INT_ADD", "register:40f0:8", ["const:be215c:8", "const:4:8"]]
- 00be1170 ["COPY", "register:4048:8", ["const:1126000:8"]]
- 00be1174 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ea0:8"]]
+ 00be2164 ["COPY", "register:4048:8", ["const:1127000:8"]]
+ 00be2168 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e60:8"]]
- 00be1180 ["INT_ADD", "register:40f0:8", ["const:be1180:8", "const:4:8"]]
+ 00be2174 ["INT_ADD", "register:40f0:8", ["const:be2174:8", "const:4:8"]]
~~~


### [`00be12cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be12cc.md) → [`00be22c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be22c0.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md) [`00c5dc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md) [`00c5ec20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be22dc",
      "incomplete_value": true,
      "site": "00be22e0",
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
      "definition_site": "00be12e8",
      "incomplete_value": true,
      "site": "00be12ec",
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
        "00c9bb30",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c929e0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9cb00",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c939b0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be12d8 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be22cc ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00be12e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
+ 00be22d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b00:8"]]
- 00be12f4 ["INT_ADD", "register:40f0:8", ["const:be12f4:8", "const:4:8"]]
+ 00be22e8 ["INT_ADD", "register:40f0:8", ["const:be22e8:8", "const:4:8"]]
~~~


### [`00be1348`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1348.md) → [`00be233c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be233c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df60.md) · 呼出先 10件 [`00c5aad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ef30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef30.md) · 呼出先 10件 [`00c5baa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be23a0",
      "incomplete_value": false,
      "site": "00be23a4",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be13ac",
      "incomplete_value": false,
      "site": "00be13b0",
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
            "const:88:8"
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
      100,
      "PARAM",
      [
        "storage",
        "002a7088",
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
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be1374 ["INT_ADD", "register:40f0:8", ["const:be1374:8", "const:4:8"]]
+ 00be2368 ["INT_ADD", "register:40f0:8", ["const:be2368:8", "const:4:8"]]
- 00be1380 ["INT_ADD", "register:40f0:8", ["const:be1380:8", "const:4:8"]]
+ 00be2374 ["INT_ADD", "register:40f0:8", ["const:be2374:8", "const:4:8"]]
- 00be139c ["INT_ADD", "register:40f0:8", ["const:be139c:8", "const:4:8"]]
+ 00be2390 ["INT_ADD", "register:40f0:8", ["const:be2390:8", "const:4:8"]]
~~~


### [`00be1524`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1524.md) → [`00be2518`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be2/00be2518.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5df50.md) · 呼出先 10件 [`00c5aad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af00.md) [`00c5af20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af20.md) [`00c5af30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af30.md)
- 新版 呼出元 1件 [`00c5ef20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ef20.md) · 呼出先 10件 [`00c5baa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bed0.md) [`00c5bef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bef0.md) [`00c5bf00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00be2584",
      "incomplete_value": false,
      "site": "00be2588",
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
            "const:1e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00be1590",
      "incomplete_value": false,
      "site": "00be1594",
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
            "const:88:8"
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
      108,
      "PARAM",
      [
        "storage",
        "002a7088",
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
        "002a71e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be1558 ["INT_ADD", "register:40f0:8", ["const:be1558:8", "const:4:8"]]
+ 00be254c ["INT_ADD", "register:40f0:8", ["const:be254c:8", "const:4:8"]]
- 00be1564 ["INT_ADD", "register:40f0:8", ["const:be1564:8", "const:4:8"]]
+ 00be2558 ["INT_ADD", "register:40f0:8", ["const:be2558:8", "const:4:8"]]
- 00be1580 ["INT_ADD", "register:40f0:8", ["const:be1580:8", "const:4:8"]]
+ 00be2574 ["INT_ADD", "register:40f0:8", ["const:be2574:8", "const:4:8"]]
~~~


### [`00be21c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be21c0.md) → [`00be31b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be31b4.md) _ZN8firebase4auth17UserInfoInterfaceD2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5dc40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc40.md) [`00c5dc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md) · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`00c5ec10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec10.md) [`00c5ec20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md) · 呼出先 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00be31d0",
      "incomplete_value": true,
      "site": "00be31d4",
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
      "definition_site": "00be21dc",
      "incomplete_value": true,
      "site": "00be21e0",
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
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c92a48",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9ca68",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "DATA",
      [
        "storage",
        "00c93a18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be21cc ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00be31c0 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00be21d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a98:8"]]
+ 00be31c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a68:8"]]
- 00be2220 ["INT_ADD", "register:40f0:8", ["const:be2220:8", "const:4:8"]]
+ 00be3214 ["INT_ADD", "register:40f0:8", ["const:be3214:8", "const:4:8"]]
~~~


### [`00be3150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) → [`00be4144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) FUN_00be4144

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3134.md) [`00be3150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) · 呼出先 4件 [`00be3150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3150.md) [`00be9e64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be9/00be9e64.md) [`00bea124`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea124.md) [`00bea24c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00bea24c.md)
- 新版 呼出元 2件 [`00be4128`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4128.md) [`00be4144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) · 呼出先 4件 [`00be4144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4144.md) [`00beae58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bea/00beae58.md) [`00beb118`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb118.md) [`00beb240`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00beb240.md)

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
      "site": "00be44d0",
      "value": [
        "leaf",
        "ram:beae58:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be34dc",
      "value": [
        "leaf",
        "ram:be9e64:8"
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
      "site": "00be44e4",
      "value": [
        "leaf",
        "ram:beae58:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be34f0",
      "value": [
        "leaf",
        "ram:be9e64:8"
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
      908,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ],
    [
      928,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be9e64"
      ]
    ]
  ],
  "added": [
    [
      908,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae58"
      ]
    ],
    [
      928,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae58"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be34dc ["INT_ADD", "register:40f0:8", ["const:be34dc:8", "const:4:8"]]
- 00be34dc ["CALL", null, ["ram:be9e64:8"]]
+ 00be44d0 ["INT_ADD", "register:40f0:8", ["const:be44d0:8", "const:4:8"]]
+ 00be44d0 ["CALL", null, ["ram:beae58:8"]]
- 00be34f0 ["INT_ADD", "register:40f0:8", ["const:be34f0:8", "const:4:8"]]
- 00be34f0 ["CALL", null, ["ram:be9e64:8"]]
+ 00be44e4 ["INT_ADD", "register:40f0:8", ["const:be44e4:8", "const:4:8"]]
+ 00be44e4 ["CALL", null, ["ram:beae58:8"]]
- 00be350c ["INT_ADD", "register:40f0:8", ["const:be350c:8", "const:4:8"]]
+ 00be4500 ["INT_ADD", "register:40f0:8", ["const:be4500:8", "const:4:8"]]
~~~


### [`00be3fbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) → [`00be4fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) FUN_00be4fb0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3f9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3f9c.md) [`00be3fbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) · 呼出先 4件 [`00be3fbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be3/00be3fbc.md) [`00beac1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beac1c.md) [`00beaedc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bea/00beaedc.md) [`00beb004`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb004.md)
- 新版 呼出元 2件 [`00be4f90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4f90.md) [`00be4fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) · 呼出先 4件 [`00be4fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be4/00be4fb0.md) [`00bebc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebc10.md) [`00bebed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebed0.md) [`00bebff8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebff8.md)

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
      "site": "00be5340",
      "value": [
        "leaf",
        "ram:bebc10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be434c",
      "value": [
        "leaf",
        "ram:beac1c:8"
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
      "site": "00be5354",
      "value": [
        "leaf",
        "ram:bebc10:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4360",
      "value": [
        "leaf",
        "ram:beac1c:8"
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
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beac1c"
      ]
    ]
  ],
  "added": [
    [
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bebc10"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bebc10"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be434c ["INT_ADD", "register:40f0:8", ["const:be434c:8", "const:4:8"]]
- 00be434c ["CALL", null, ["ram:beac1c:8"]]
+ 00be5340 ["INT_ADD", "register:40f0:8", ["const:be5340:8", "const:4:8"]]
+ 00be5340 ["CALL", null, ["ram:bebc10:8"]]
- 00be4360 ["INT_ADD", "register:40f0:8", ["const:be4360:8", "const:4:8"]]
- 00be4360 ["CALL", null, ["ram:beac1c:8"]]
+ 00be5354 ["INT_ADD", "register:40f0:8", ["const:be5354:8", "const:4:8"]]
+ 00be5354 ["CALL", null, ["ram:bebc10:8"]]
- 00be437c ["INT_ADD", "register:40f0:8", ["const:be437c:8", "const:4:8"]]
+ 00be5370 ["INT_ADD", "register:40f0:8", ["const:be5370:8", "const:4:8"]]
~~~


### [`00be46f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) → [`00be56ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) FUN_00be56ec

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be46d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46d8.md) [`00be46f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) · 呼出先 4件 [`00be46f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be46f8.md) [`00beb300`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb300.md) [`00beb5c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb5c0.md) [`00beb6e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb6e8.md)
- 新版 呼出元 2件 [`00be56cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56cc.md) [`00be56ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) · 呼出先 4件 [`00be56ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be56ec.md) [`00bec2f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec2f4.md) [`00bec5b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec5b4.md) [`00bec6dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec6dc.md)

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
      "site": "00be5a7c",
      "value": [
        "leaf",
        "ram:bec2f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a88",
      "value": [
        "leaf",
        "ram:beb300:8"
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
      "site": "00be5a90",
      "value": [
        "leaf",
        "ram:bec2f4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4a9c",
      "value": [
        "leaf",
        "ram:beb300:8"
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
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb300"
      ]
    ]
  ],
  "added": [
    [
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec2f4"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec2f4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be4a88 ["INT_ADD", "register:40f0:8", ["const:be4a88:8", "const:4:8"]]
- 00be4a88 ["CALL", null, ["ram:beb300:8"]]
+ 00be5a7c ["INT_ADD", "register:40f0:8", ["const:be5a7c:8", "const:4:8"]]
+ 00be5a7c ["CALL", null, ["ram:bec2f4:8"]]
- 00be4a9c ["INT_ADD", "register:40f0:8", ["const:be4a9c:8", "const:4:8"]]
- 00be4a9c ["CALL", null, ["ram:beb300:8"]]
+ 00be5a90 ["INT_ADD", "register:40f0:8", ["const:be5a90:8", "const:4:8"]]
+ 00be5a90 ["CALL", null, ["ram:bec2f4:8"]]
- 00be4ab8 ["INT_ADD", "register:40f0:8", ["const:be4ab8:8", "const:4:8"]]
+ 00be5aac ["INT_ADD", "register:40f0:8", ["const:be5aac:8", "const:4:8"]]
~~~


### [`00be4e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) → [`00be5e28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) FUN_00be5e28

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be4e14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e14.md) [`00be4e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) · 呼出先 4件 [`00be4e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be4/00be4e34.md) [`00beb9e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00beb9e4.md) [`00bebc84`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebc84.md) [`00bebdac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00beb/00bebdac.md)
- 新版 呼出元 2件 [`00be5e08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e08.md) [`00be5e28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) · 呼出先 4件 [`00be5e28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be5/00be5e28.md) [`00bec9d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00bec9d8.md) [`00becc78`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becc78.md) [`00becda0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bec/00becda0.md)

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
      "site": "00be61b8",
      "value": [
        "leaf",
        "ram:bec9d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be51c4",
      "value": [
        "leaf",
        "ram:beb9e4:8"
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
      "site": "00be61cc",
      "value": [
        "leaf",
        "ram:bec9d8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be51d8",
      "value": [
        "leaf",
        "ram:beb9e4:8"
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
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb9e4"
      ]
    ]
  ],
  "added": [
    [
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec9d8"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bec9d8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be51c4 ["INT_ADD", "register:40f0:8", ["const:be51c4:8", "const:4:8"]]
- 00be51c4 ["CALL", null, ["ram:beb9e4:8"]]
+ 00be61b8 ["INT_ADD", "register:40f0:8", ["const:be61b8:8", "const:4:8"]]
+ 00be61b8 ["CALL", null, ["ram:bec9d8:8"]]
- 00be51d8 ["INT_ADD", "register:40f0:8", ["const:be51d8:8", "const:4:8"]]
- 00be51d8 ["CALL", null, ["ram:beb9e4:8"]]
+ 00be61cc ["INT_ADD", "register:40f0:8", ["const:be61cc:8", "const:4:8"]]
+ 00be61cc ["CALL", null, ["ram:bec9d8:8"]]
- 00be51f4 ["INT_ADD", "register:40f0:8", ["const:be51f4:8", "const:4:8"]]
+ 00be61e8 ["INT_ADD", "register:40f0:8", ["const:be61e8:8", "const:4:8"]]
~~~


### [`00be78c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) → [`00be88b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) FUN_00be88b8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be78a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78a4.md) [`00be78c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) · 呼出先 4件 [`00be78c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be7/00be78c4.md) [`00bee27c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee27c.md) [`00bee51c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee51c.md) [`00bee644`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00bee644.md)
- 新版 呼出元 2件 [`00be8898`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be8898.md) [`00be88b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) · 呼出先 4件 [`00be88b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be8/00be88b8.md) [`00bef270`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef270.md) [`00bef510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef510.md) [`00bef638`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00bef638.md)

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
      "site": "00be8c48",
      "value": [
        "leaf",
        "ram:bef270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7c54",
      "value": [
        "leaf",
        "ram:bee27c:8"
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
      "site": "00be8c5c",
      "value": [
        "leaf",
        "ram:bef270:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7c68",
      "value": [
        "leaf",
        "ram:bee27c:8"
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
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee27c"
      ]
    ]
  ],
  "added": [
    [
      912,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef270"
      ]
    ],
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bef270"
      ]
    ]
  ]
}
~~~


~~~diff
- 00be7c54 ["INT_ADD", "register:40f0:8", ["const:be7c54:8", "const:4:8"]]
- 00be7c54 ["CALL", null, ["ram:bee27c:8"]]
+ 00be8c48 ["INT_ADD", "register:40f0:8", ["const:be8c48:8", "const:4:8"]]
+ 00be8c48 ["CALL", null, ["ram:bef270:8"]]
- 00be7c68 ["INT_ADD", "register:40f0:8", ["const:be7c68:8", "const:4:8"]]
- 00be7c68 ["CALL", null, ["ram:bee27c:8"]]
+ 00be8c5c ["INT_ADD", "register:40f0:8", ["const:be8c5c:8", "const:4:8"]]
+ 00be8c5c ["CALL", null, ["ram:bef270:8"]]
- 00be7c84 ["INT_ADD", "register:40f0:8", ["const:be7c84:8", "const:4:8"]]
+ 00be8c78 ["INT_ADD", "register:40f0:8", ["const:be8c78:8", "const:4:8"]]
~~~


