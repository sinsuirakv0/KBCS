# v16.0.2 → v16.0.3 · 最優先の変更候補 (102)

[一覧の目次](README.md)

### [`00c3d35c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md) → [`00c3e350`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e350.md) FUN_00c3e350

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e3b4",
      "incomplete_value": false,
      "site": "00c3e3b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3c0",
      "incomplete_value": false,
      "site": "00c3d3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e3d8",
      "incomplete_value": false,
      "site": "00c3e3d8",
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
            "const:94c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3e4",
      "incomplete_value": false,
      "site": "00c3d3e4",
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
            "const:875:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b1875",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b194c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d390 ["INT_ADD", "register:40f0:8", ["const:c3d390:8", "const:4:8"]]
+ 00c3e384 ["INT_ADD", "register:40f0:8", ["const:c3e384:8", "const:4:8"]]
- 00c3d3b0 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d3b4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e3a4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e3a8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d3dc ["COPY", "tmp:0:8", ["const:875:8"]]
+ 00c3e3d0 ["COPY", "tmp:0:8", ["const:94c:8"]]
~~~


### [`00c3d40c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md) → [`00c3e400`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e400.md) FUN_00c3e400

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e464",
      "incomplete_value": false,
      "site": "00c3e464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d470",
      "incomplete_value": false,
      "site": "00c3d470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e488",
      "incomplete_value": false,
      "site": "00c3e488",
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
            "const:e5e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d494",
      "incomplete_value": false,
      "site": "00c3d494",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "0029fe1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "0029fe5e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d440 ["INT_ADD", "register:40f0:8", ["const:c3d440:8", "const:4:8"]]
+ 00c3e434 ["INT_ADD", "register:40f0:8", ["const:c3e434:8", "const:4:8"]]
- 00c3d460 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d464 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e454 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e458 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d48c ["COPY", "tmp:0:8", ["const:e1e:8"]]
+ 00c3e480 ["COPY", "tmp:0:8", ["const:e5e:8"]]
~~~


### [`00c3d4bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md) → [`00c3e4b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e4b0.md) FUN_00c3e4b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e514",
      "incomplete_value": false,
      "site": "00c3e514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d520",
      "incomplete_value": false,
      "site": "00c3d520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e538",
      "incomplete_value": false,
      "site": "00c3e538",
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
            "const:903:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d544",
      "incomplete_value": false,
      "site": "00c3d544",
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
            "const:8b9:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b28b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b2903",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d4f0 ["INT_ADD", "register:40f0:8", ["const:c3d4f0:8", "const:4:8"]]
+ 00c3e4e4 ["INT_ADD", "register:40f0:8", ["const:c3e4e4:8", "const:4:8"]]
- 00c3d510 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d514 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e504 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e508 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d53c ["COPY", "tmp:0:8", ["const:8b9:8"]]
+ 00c3e530 ["COPY", "tmp:0:8", ["const:903:8"]]
~~~


### [`00c3d56c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md) → [`00c3e560`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e560.md) FUN_00c3e560

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e5c4",
      "incomplete_value": false,
      "site": "00c3e5c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d5d0",
      "incomplete_value": false,
      "site": "00c3d5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e5e8",
      "incomplete_value": false,
      "site": "00c3e5e8",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d5f4",
      "incomplete_value": false,
      "site": "00c3d5f4",
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
            "const:9db:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a99db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a9aa8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d5a0 ["INT_ADD", "register:40f0:8", ["const:c3d5a0:8", "const:4:8"]]
+ 00c3e594 ["INT_ADD", "register:40f0:8", ["const:c3e594:8", "const:4:8"]]
- 00c3d5c0 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d5c4 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e5b4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e5b8 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d5ec ["COPY", "tmp:0:8", ["const:9db:8"]]
+ 00c3e5e0 ["COPY", "tmp:0:8", ["const:aa8:8"]]
~~~


### [`00c3d7cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md) → [`00c3e7c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e7c0.md) FUN_00c3e7c0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e824",
      "incomplete_value": false,
      "site": "00c3e824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d830",
      "incomplete_value": false,
      "site": "00c3d830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e848",
      "incomplete_value": false,
      "site": "00c3e848",
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
            "const:eff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d854",
      "incomplete_value": false,
      "site": "00c3d854",
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
            "const:e21:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b9e21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b9eff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d800 ["INT_ADD", "register:40f0:8", ["const:c3d800:8", "const:4:8"]]
+ 00c3e7f4 ["INT_ADD", "register:40f0:8", ["const:c3e7f4:8", "const:4:8"]]
- 00c3d820 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d824 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e814 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e818 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d84c ["COPY", "tmp:0:8", ["const:e21:8"]]
+ 00c3e840 ["COPY", "tmp:0:8", ["const:eff:8"]]
~~~


### [`00c3d87c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md) → [`00c3e870`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e870.md) FUN_00c3e870

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e8d8",
      "incomplete_value": false,
      "site": "00c3e8d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:670:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d8e4",
      "incomplete_value": false,
      "site": "00c3d8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c976a0",
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
        "00c98670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d8b4 ["INT_ADD", "register:40f0:8", ["const:c3d8b4:8", "const:4:8"]]
+ 00c3e8a8 ["INT_ADD", "register:40f0:8", ["const:c3e8a8:8", "const:4:8"]]
- 00c3d8d4 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d8d8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00c3e8c8 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e8cc ["COPY", "tmp:0:8", ["const:670:8"]]
- 00c3d920 ["INT_ADD", "register:40f0:8", ["const:c3d920:8", "const:4:8"]]
+ 00c3e914 ["INT_ADD", "register:40f0:8", ["const:c3e914:8", "const:4:8"]]
~~~


### [`00c3d924`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md) → [`00c3e918`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e918.md) FUN_00c3e918

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e97c",
      "incomplete_value": false,
      "site": "00c3e97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d988",
      "incomplete_value": false,
      "site": "00c3d988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3e9a0",
      "incomplete_value": false,
      "site": "00c3e9a0",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d9ac",
      "incomplete_value": false,
      "site": "00c3d9ac",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b0889",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b0960",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
+ 00c3e94c ["INT_ADD", "register:40f0:8", ["const:c3e94c:8", "const:4:8"]]
- 00c3d978 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3d97c ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3e96c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3e970 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3d9a4 ["COPY", "tmp:0:8", ["const:889:8"]]
+ 00c3e998 ["COPY", "tmp:0:8", ["const:960:8"]]
~~~


### [`00c3d9d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md) → [`00c3e9c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3e9c8.md) FUN_00c3e9c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ea2c",
      "incomplete_value": false,
      "site": "00c3ea2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da38",
      "incomplete_value": false,
      "site": "00c3da38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3ea50",
      "incomplete_value": false,
      "site": "00c3ea50",
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
            "const:e9e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da5c",
      "incomplete_value": false,
      "site": "00c3da5c",
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
            "const:e54:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c0e54",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c0e9e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3da08 ["INT_ADD", "register:40f0:8", ["const:c3da08:8", "const:4:8"]]
+ 00c3e9fc ["INT_ADD", "register:40f0:8", ["const:c3e9fc:8", "const:4:8"]]
- 00c3da28 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3da2c ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3ea1c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3ea20 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3da54 ["COPY", "tmp:0:8", ["const:e54:8"]]
+ 00c3ea48 ["COPY", "tmp:0:8", ["const:e9e:8"]]
~~~


### [`00c3da84`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md) → [`00c3ea78`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ea78.md) FUN_00c3ea78

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eadc",
      "incomplete_value": false,
      "site": "00c3eadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3dae8",
      "incomplete_value": false,
      "site": "00c3dae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3eb00",
      "incomplete_value": false,
      "site": "00c3eb00",
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
            "const:a97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3db0c",
      "incomplete_value": false,
      "site": "00c3db0c",
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
            "const:93f:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a893f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a8a97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3dab8 ["INT_ADD", "register:40f0:8", ["const:c3dab8:8", "const:4:8"]]
+ 00c3eaac ["INT_ADD", "register:40f0:8", ["const:c3eaac:8", "const:4:8"]]
- 00c3dad8 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3dadc ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3eacc ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3ead0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3dafc ["COPY", "tmp:0:8", ["const:93f:8"]]
+ 00c3eaf0 ["COPY", "tmp:0:8", ["const:a97:8"]]
~~~


### [`00c3db30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md) → [`00c3eb24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eb24.md) FUN_00c3eb24

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eb88",
      "incomplete_value": false,
      "site": "00c3eb88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3db94",
      "incomplete_value": false,
      "site": "00c3db94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00c3ebac",
      "incomplete_value": false,
      "site": "00c3ebac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c2000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3dbb8",
      "incomplete_value": false,
      "site": "00c3dbb8",
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
            "const:fe6:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
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
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c1fe6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c985f0",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c2030",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3db64 ["INT_ADD", "register:40f0:8", ["const:c3db64:8", "const:4:8"]]
+ 00c3eb58 ["INT_ADD", "register:40f0:8", ["const:c3eb58:8", "const:4:8"]]
- 00c3db84 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3db88 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 00c3eb78 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3eb7c ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00c3dbac ["COPY", "register:4040:8", ["const:2c1000:8"]]
- 00c3dbb0 ["COPY", "tmp:0:8", ["const:fe6:8"]]
+ 00c3eba0 ["COPY", "register:4040:8", ["const:2c2000:8"]]
+ 00c3eba4 ["COPY", "tmp:0:8", ["const:30:8"]]
~~~


### [`00c3decc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md) → [`00c3eec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3eec0.md) FUN_00c3eec0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ef28",
      "incomplete_value": true,
      "site": "00c3ef34",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:1e6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3df34",
      "incomplete_value": true,
      "site": "00c3df40",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:108:8"
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
      "definition_site": "00c3ef2c",
      "incomplete_value": true,
      "site": "00c3ef38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c3df38",
      "incomplete_value": true,
      "site": "00c3df44",
      "value": [
        "LOAD",
        "8",
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
      "READ",
      [
        "storage",
        "002bb108",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002bb118",
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
        "002bb1e6",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002bb1f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3df14 ["INT_ADD", "register:40f0:8", ["const:c3df14:8", "const:4:8"]]
+ 00c3ef08 ["INT_ADD", "register:40f0:8", ["const:c3ef08:8", "const:4:8"]]
- 00c3df2c ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00c3ef20 ["COPY", "tmp:0:8", ["const:1e6:8"]]
- 00c3df64 ["INT_ADD", "register:40f0:8", ["const:c3df64:8", "const:4:8"]]
+ 00c3ef58 ["INT_ADD", "register:40f0:8", ["const:c3ef58:8", "const:4:8"]]
~~~


### [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) → [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) FUN_00c3f040

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3dbe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 7件 [`00c3ebd4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ebd4.md) [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) [`00c446fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f160",
      "incomplete_value": false,
      "site": "00c3f160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e16c",
      "incomplete_value": false,
      "site": "00c3e16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      288,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002af708",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      288,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002af7df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e13c ["INT_ADD", "register:40f0:8", ["const:c3e13c:8", "const:4:8"]]
+ 00c3f130 ["INT_ADD", "register:40f0:8", ["const:c3f130:8", "const:4:8"]]
- 00c3e15c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3e160 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3f150 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3f154 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c3e1c4 ["INT_ADD", "register:40f0:8", ["const:c3e1c4:8", "const:4:8"]]
+ 00c3f1b8 ["INT_ADD", "register:40f0:8", ["const:c3f1b8:8", "const:4:8"]]
~~~


### [`00c3e278`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md) → [`00c3f26c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f26c.md) FUN_00c3f26c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f2d0",
      "incomplete_value": false,
      "site": "00c3f2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e2dc",
      "incomplete_value": false,
      "site": "00c3e2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e2ac ["INT_ADD", "register:40f0:8", ["const:c3e2ac:8", "const:4:8"]]
+ 00c3f2a0 ["INT_ADD", "register:40f0:8", ["const:c3f2a0:8", "const:4:8"]]
- 00c3e2cc ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3e2d0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3f2c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3f2c4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c3e314 ["INT_ADD", "register:40f0:8", ["const:c3e314:8", "const:4:8"]]
+ 00c3f308 ["INT_ADD", "register:40f0:8", ["const:c3f308:8", "const:4:8"]]
~~~


### [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) → [`00c3f4e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) FUN_00c3f4e4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 4件 [`00c3f0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 4件 [`00c400c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md) [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f5e8",
      "incomplete_value": false,
      "site": "00c3f5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:dff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e5f4",
      "incomplete_value": false,
      "site": "00c3e600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      232,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b8d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      232,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b8dff",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e548 ["INT_ADD", "register:40f0:8", ["const:c3e548:8", "const:4:8"]]
+ 00c3f53c ["INT_ADD", "register:40f0:8", ["const:c3f53c:8", "const:4:8"]]
- 00c3e598 ["INT_ADD", "register:40f0:8", ["const:c3e598:8", "const:4:8"]]
+ 00c3f58c ["INT_ADD", "register:40f0:8", ["const:c3f58c:8", "const:4:8"]]
- 00c3e5c8 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c3e5cc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3f5bc ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c3f5c0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) → [`00c3f654`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) FUN_00c3f654

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 8件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 5件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c446fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) [`00c4c83c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) [`00c4f678`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) · 呼出先 8件 [`00c3d9d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fad4",
      "incomplete_value": false,
      "site": "00c3fad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eae0",
      "incomplete_value": false,
      "site": "00c3eae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      532,
      "DATA",
      [
        "storage",
        "00c99530",
        null,
        "undefined *"
      ]
    ],
    [
      1152,
      "DATA",
      [
        "storage",
        "00c995a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      532,
      "DATA",
      [
        "storage",
        "00c9a500",
        null,
        "undefined *"
      ]
    ],
    [
      1152,
      "DATA",
      [
        "storage",
        "00c9a570",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e6d4 ["INT_ADD", "register:40f0:8", ["const:c3e6d4:8", "const:4:8"]]
+ 00c3f6c8 ["INT_ADD", "register:40f0:8", ["const:c3f6c8:8", "const:4:8"]]
- 00c3e6e0 ["INT_ADD", "register:40f0:8", ["const:c3e6e0:8", "const:4:8"]]
+ 00c3f6d4 ["INT_ADD", "register:40f0:8", ["const:c3f6d4:8", "const:4:8"]]
- 00c3e6e8 ["INT_ADD", "register:40f0:8", ["const:c3e6e8:8", "const:4:8"]]
+ 00c3f6dc ["INT_ADD", "register:40f0:8", ["const:c3f6dc:8", "const:4:8"]]
~~~


### [`00c3eb30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) → [`00c3fb24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md) FUN_00c3fb24

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c446fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fb8c",
      "incomplete_value": false,
      "site": "00c3fb8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eb98",
      "incomplete_value": false,
      "site": "00c3eb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99610",
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
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3eb68 ["INT_ADD", "register:40f0:8", ["const:c3eb68:8", "const:4:8"]]
+ 00c3fb5c ["INT_ADD", "register:40f0:8", ["const:c3fb5c:8", "const:4:8"]]
- 00c3eb88 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c3eb8c ["COPY", "tmp:0:8", ["const:610:8"]]
+ 00c3fb7c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c3fb80 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00c3ebd4 ["INT_ADD", "register:40f0:8", ["const:c3ebd4:8", "const:4:8"]]
+ 00c3fbc8 ["INT_ADD", "register:40f0:8", ["const:c3fbc8:8", "const:4:8"]]
~~~


### [`00c3ebd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) → [`00c3fbcc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) FUN_00c3fbcc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 7件 [`00c3fa0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) [`00c3fae4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 4件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4c6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 7件 [`00c40a00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40a00.md) [`00c40ad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md) [`00c58fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fe38",
      "incomplete_value": false,
      "site": "00c3fe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ee44",
      "incomplete_value": false,
      "site": "00c3ee44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
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
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00c977f0",
        null,
        "undefined *"
      ]
    ],
    [
      844,
      "PARAM",
      [
        "storage",
        "002a1d4c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      340,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00c987c0",
        null,
        "undefined *"
      ]
    ],
    [
      844,
      "PARAM",
      [
        "storage",
        "002a1d8c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3ecfc ["INT_ADD", "register:40f0:8", ["const:c3ecfc:8", "const:4:8"]]
+ 00c3fcf0 ["INT_ADD", "register:40f0:8", ["const:c3fcf0:8", "const:4:8"]]
- 00c3ed1c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3ed20 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c3fd10 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c3fd14 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c3ee0c ["INT_ADD", "register:40f0:8", ["const:c3ee0c:8", "const:4:8"]]
+ 00c3fe00 ["INT_ADD", "register:40f0:8", ["const:c3fe00:8", "const:4:8"]]
~~~


### [`00c3ef9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) → [`00c3ff90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md) FUN_00c3ff90

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 3件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 3件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c4c6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 3件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4006c",
      "incomplete_value": false,
      "site": "00c4006c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f078",
      "incomplete_value": false,
      "site": "00c3f078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4008c",
      "incomplete_value": false,
      "site": "00c4008c",
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
            "const:5fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f098",
      "incomplete_value": false,
      "site": "00c3f098",
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
            "const:530:8"
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
      220,
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "002ae530",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      220,
      "DATA",
      [
        "storage",
        "00c990e0",
        null,
        "undefined *"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "002ae5fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3effc ["INT_ADD", "register:40f0:8", ["const:c3effc:8", "const:4:8"]]
+ 00c3fff0 ["INT_ADD", "register:40f0:8", ["const:c3fff0:8", "const:4:8"]]
- 00c3f044 ["INT_ADD", "register:40f0:8", ["const:c3f044:8", "const:4:8"]]
+ 00c40038 ["INT_ADD", "register:40f0:8", ["const:c40038:8", "const:4:8"]]
- 00c3f068 ["COPY", "register:4050:8", ["const:c98000:8"]]
- 00c3f06c ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00c4005c ["COPY", "register:4050:8", ["const:c99000:8"]]
+ 00c40060 ["COPY", "tmp:0:8", ["const:e0:8"]]
~~~


### [`00c3f0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) → [`00c400c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c400c4.md) FUN_00c400c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 6件 [`00c4c2c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)
- 新版 呼出元 3件 [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3f4e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) [`00c4c6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) · 呼出先 6件 [`00c4d2b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d2b8.md) [`00c58fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c402e8",
      "incomplete_value": false,
      "site": "00c402ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f2f4",
      "incomplete_value": false,
      "site": "00c3f2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      552,
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      552,
      "DATA",
      [
        "storage",
        "00c9a110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f29c ["INT_ADD", "register:40f0:8", ["const:c3f29c:8", "const:4:8"]]
+ 00c40290 ["INT_ADD", "register:40f0:8", ["const:c40290:8", "const:4:8"]]
- 00c3f2f0 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c3f2f4 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00c402e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c402e8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00c3f2fc ["INT_ADD", "register:40f0:8", ["const:c3f2fc:8", "const:4:8"]]
+ 00c402f0 ["INT_ADD", "register:40f0:8", ["const:c402f0:8", "const:4:8"]]
~~~


### [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) → [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) FUN_00c403a0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) · 呼出先 13件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3dbe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md)
- 新版 呼出元 2件 [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3f4e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f4e4.md) · 呼出先 13件 [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c3ebd4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3e/00c3ebd4.md) [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c475b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c405e8",
      "incomplete_value": false,
      "site": "00c405e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f5f4",
      "incomplete_value": false,
      "site": "00c3f5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40850",
      "incomplete_value": false,
      "site": "00c40850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f85c",
      "incomplete_value": false,
      "site": "00c3f85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      396,
      "DATA",
      [
        "storage",
        "00c991c8",
        null,
        "undefined *"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00c99370",
        null,
        "undefined *"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c99450",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      396,
      "DATA",
      [
        "storage",
        "00c9a198",
        null,
        "undefined *"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00c9a340",
        null,
        "undefined *"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c9a420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f3e0 ["INT_ADD", "register:40f0:8", ["const:c3f3e0:8", "const:4:8"]]
+ 00c403d4 ["INT_ADD", "register:40f0:8", ["const:c403d4:8", "const:4:8"]]
- 00c3f464 ["INT_ADD", "register:40f0:8", ["const:c3f464:8", "const:4:8"]]
+ 00c40458 ["INT_ADD", "register:40f0:8", ["const:c40458:8", "const:4:8"]]
- 00c3f484 ["INT_ADD", "register:40f0:8", ["const:c3f484:8", "const:4:8"]]
+ 00c40478 ["INT_ADD", "register:40f0:8", ["const:c40478:8", "const:4:8"]]
~~~


### [`00c3f96c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md) → [`00c40960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40960.md) FUN_00c40960

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c409c4",
      "incomplete_value": false,
      "site": "00c409c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f9d0",
      "incomplete_value": false,
      "site": "00c3f9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f9a0 ["INT_ADD", "register:40f0:8", ["const:c3f9a0:8", "const:4:8"]]
+ 00c40994 ["INT_ADD", "register:40f0:8", ["const:c40994:8", "const:4:8"]]
- 00c3f9c0 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c3f9c4 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c409b4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c409b8 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c3fa08 ["INT_ADD", "register:40f0:8", ["const:c3fa08:8", "const:4:8"]]
+ 00c409fc ["INT_ADD", "register:40f0:8", ["const:c409fc:8", "const:4:8"]]
~~~


### [`00c3fae4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) → [`00c40ad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40ad8.md) FUN_00c40ad8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ebd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3fbcc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fbcc.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c40b44",
      "incomplete_value": false,
      "site": "00c40b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3fb50",
      "incomplete_value": false,
      "site": "00c3fb50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3fb18 ["INT_ADD", "register:40f0:8", ["const:c3fb18:8", "const:4:8"]]
+ 00c40b0c ["INT_ADD", "register:40f0:8", ["const:c40b0c:8", "const:4:8"]]
- 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
+ 00c40b34 ["INT_ADD", "register:40f0:8", ["const:c40b34:8", "const:4:8"]]
- 00c3fb44 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c3fb48 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c40b38 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c40b3c ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) → [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) FUN_00c40e0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3ef9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) · 呼出先 42件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3cd04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md)
- 新版 呼出元 14件 [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3f654`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c3ff90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3ff90.md) · 呼出先 42件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3b1a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md) [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d9d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c3dcf8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3dcf8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c415a0",
      "incomplete_value": false,
      "site": "00c415a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c405ac",
      "incomplete_value": false,
      "site": "00c405ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c419e0",
      "incomplete_value": false,
      "site": "00c419e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c409ec",
      "incomplete_value": false,
      "site": "00c409ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4208c",
      "incomplete_value": false,
      "site": "00c4208c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41098",
      "incomplete_value": false,
      "site": "00c41098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "ordinal": 164,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      212,
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      212,
      "READ",
      [
        "storage",
        "00c98a00",
        null,
        "undefined1"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00c98a01",
        null,
        "undefined1"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c98a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3fecc ["COPY", "register:4040:8", ["const:c97850:8"]]
- 00c3fed0 ["BRANCH", null, ["local:b10:8"]]
- 00c3fed4 ["COPY", "tmp:0:8", ["const:1:8"]]
- 00c3fed4 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
+ 00c40ec0 ["COPY", "register:4040:8", ["const:c98820:8"]]
+ 00c40ec4 ["BRANCH", null, ["local:b10:8"]]
+ 00c40ec8 ["COPY", "tmp:0:8", ["const:1:8"]]
+ 00c40ec8 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
~~~


### [`00c411a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md) → [`00c4219c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4219c.md) FUN_00c4219c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4220c",
      "incomplete_value": false,
      "site": "00c4220c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41218",
      "incomplete_value": false,
      "site": "00c41218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c98cf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c411e8 ["INT_ADD", "register:40f0:8", ["const:c411e8:8", "const:4:8"]]
+ 00c421dc ["INT_ADD", "register:40f0:8", ["const:c421dc:8", "const:4:8"]]
- 00c41208 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c4120c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00c421fc ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c42200 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 00c41264 ["INT_ADD", "register:40f0:8", ["const:c41264:8", "const:4:8"]]
+ 00c42258 ["INT_ADD", "register:40f0:8", ["const:c42258:8", "const:4:8"]]
~~~


### [`00c41268`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md) → [`00c4225c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c4225c.md) FUN_00c4225c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c422cc",
      "incomplete_value": false,
      "site": "00c422cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c412d8",
      "incomplete_value": false,
      "site": "00c412d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c98d60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c412a8 ["INT_ADD", "register:40f0:8", ["const:c412a8:8", "const:4:8"]]
+ 00c4229c ["INT_ADD", "register:40f0:8", ["const:c4229c:8", "const:4:8"]]
- 00c412c8 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c412cc ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 00c422bc ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c422c0 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00c41320 ["INT_ADD", "register:40f0:8", ["const:c41320:8", "const:4:8"]]
+ 00c42314 ["INT_ADD", "register:40f0:8", ["const:c42314:8", "const:4:8"]]
~~~


### [`00c41324`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md) → [`00c42318`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42318.md) FUN_00c42318

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4238c",
      "incomplete_value": false,
      "site": "00c4238c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41398",
      "incomplete_value": false,
      "site": "00c41398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c98dd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41368 ["INT_ADD", "register:40f0:8", ["const:c41368:8", "const:4:8"]]
+ 00c4235c ["INT_ADD", "register:40f0:8", ["const:c4235c:8", "const:4:8"]]
- 00c41388 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c4138c ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00c4237c ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c42380 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00c413ec ["INT_ADD", "register:40f0:8", ["const:c413ec:8", "const:4:8"]]
+ 00c423e0 ["INT_ADD", "register:40f0:8", ["const:c423e0:8", "const:4:8"]]
~~~


### [`00c413f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md) → [`00c423e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c423e4.md) FUN_00c423e4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42464",
      "incomplete_value": false,
      "site": "00c42464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41470",
      "incomplete_value": false,
      "site": "00c41470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      128,
      "DATA",
      [
        "storage",
        "00c97e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      128,
      "DATA",
      [
        "storage",
        "00c98e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41440 ["INT_ADD", "register:40f0:8", ["const:c41440:8", "const:4:8"]]
+ 00c42434 ["INT_ADD", "register:40f0:8", ["const:c42434:8", "const:4:8"]]
- 00c41460 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c41464 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00c42454 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c42458 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00c414d8 ["INT_ADD", "register:40f0:8", ["const:c414d8:8", "const:4:8"]]
+ 00c424cc ["INT_ADD", "register:40f0:8", ["const:c424cc:8", "const:4:8"]]
~~~


### [`00c414dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md) → [`00c424d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c424d0.md) FUN_00c424d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42540",
      "incomplete_value": false,
      "site": "00c42540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4154c",
      "incomplete_value": false,
      "site": "00c4154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c98f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4151c ["INT_ADD", "register:40f0:8", ["const:c4151c:8", "const:4:8"]]
+ 00c42510 ["INT_ADD", "register:40f0:8", ["const:c42510:8", "const:4:8"]]
- 00c4153c ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c41540 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00c42530 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c42534 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00c41598 ["INT_ADD", "register:40f0:8", ["const:c41598:8", "const:4:8"]]
+ 00c4258c ["INT_ADD", "register:40f0:8", ["const:c4258c:8", "const:4:8"]]
~~~


### [`00c4159c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md) → [`00c42590`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42590.md) FUN_00c42590

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42600",
      "incomplete_value": false,
      "site": "00c42600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4160c",
      "incomplete_value": false,
      "site": "00c4160c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c98f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c415dc ["INT_ADD", "register:40f0:8", ["const:c415dc:8", "const:4:8"]]
+ 00c425d0 ["INT_ADD", "register:40f0:8", ["const:c425d0:8", "const:4:8"]]
- 00c415fc ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c41600 ["COPY", "tmp:0:8", ["const:fc0:8"]]
+ 00c425f0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c425f4 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00c41658 ["INT_ADD", "register:40f0:8", ["const:c41658:8", "const:4:8"]]
+ 00c4264c ["INT_ADD", "register:40f0:8", ["const:c4264c:8", "const:4:8"]]
~~~


### [`00c4165c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md) → [`00c42650`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42650.md) FUN_00c42650

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c426c4",
      "incomplete_value": false,
      "site": "00c426c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c416d0",
      "incomplete_value": false,
      "site": "00c416d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:30:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c98030",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c99000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c416a0 ["INT_ADD", "register:40f0:8", ["const:c416a0:8", "const:4:8"]]
+ 00c42694 ["INT_ADD", "register:40f0:8", ["const:c42694:8", "const:4:8"]]
- 00c416c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c416c4 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00c426b4 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c426b8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00c41720 ["INT_ADD", "register:40f0:8", ["const:c41720:8", "const:4:8"]]
+ 00c42714 ["INT_ADD", "register:40f0:8", ["const:c42714:8", "const:4:8"]]
~~~


### [`00c41724`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md) → [`00c42718`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c42718.md) FUN_00c42718

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4278c",
      "incomplete_value": false,
      "site": "00c4278c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41798",
      "incomplete_value": false,
      "site": "00c41798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c980a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c99070",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41768 ["INT_ADD", "register:40f0:8", ["const:c41768:8", "const:4:8"]]
+ 00c4275c ["INT_ADD", "register:40f0:8", ["const:c4275c:8", "const:4:8"]]
- 00c41788 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c4178c ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00c4277c ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c42780 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00c417e8 ["INT_ADD", "register:40f0:8", ["const:c417e8:8", "const:4:8"]]
+ 00c427dc ["INT_ADD", "register:40f0:8", ["const:c427dc:8", "const:4:8"]]
~~~


### [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) → [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) FUN_00c427e0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 12件 [`00c3a1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c462d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) [`00c463c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md)
- 新版 呼出元 2件 [`00c3d9d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 12件 [`00c3b1a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b1a8.md) [`00c3b208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3b208.md) [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c472c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md) [`00c473bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42b24",
      "incomplete_value": false,
      "site": "00c42b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41b30",
      "incomplete_value": false,
      "site": "00c41b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42e40",
      "incomplete_value": false,
      "site": "00c42e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41e4c",
      "incomplete_value": false,
      "site": "00c41e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c430bc",
      "incomplete_value": false,
      "site": "00c430bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c420c8",
      "incomplete_value": false,
      "site": "00c420c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      96,
      "DATA",
      [
        "storage",
        "00312b1c",
        "switchD_00c41854::switchdataD_00312b1c",
        "ushort"
      ]
    ],
    [
      408,
      "PARAM",
      [
        "storage",
        "002ad191",
        null,
        "string"
      ]
    ],
    [
      432,
      "PARAM",
      [
        "storage",
        "002ac46c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      96,
      "DATA",
      [
        "storage",
        "00312b5c",
        "switchD_00c42848::switchdataD_00312b5c",
        "ushort"
      ]
    ],
    [
      408,
      "PARAM",
      [
        "storage",
        "002ad25e",
        null,
        "string"
      ]
    ],
    [
      432,
      "PARAM",
      [
        "storage",
        "002ac539",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41840 ["COPY", "tmp:0:8", ["const:b1c:8"]]
+ 00c42834 ["COPY", "tmp:0:8", ["const:b5c:8"]]
- 00c41848 ["COPY", "register:4078:8", ["const:c41858:8"]]
+ 00c4283c ["COPY", "register:4078:8", ["const:c4284c:8"]]
- 00c41860 ["INT_ADD", "register:40f0:8", ["const:c41860:8", "const:4:8"]]
+ 00c42854 ["INT_ADD", "register:40f0:8", ["const:c42854:8", "const:4:8"]]
~~~


### [`00c4216c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) → [`00c43160`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md) FUN_00c43160

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 3件 [`00c495f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 3件 [`00c4a5ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4338c",
      "incomplete_value": false,
      "site": "00c4338c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42398",
      "incomplete_value": false,
      "site": "00c42398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00c433b4",
      "incomplete_value": false,
      "site": "00c433b4",
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
            "const:ee5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c423c0",
      "incomplete_value": false,
      "site": "00c423c0",
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
            "const:e9b:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43464",
      "incomplete_value": false,
      "site": "00c43464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42470",
      "incomplete_value": false,
      "site": "00c42470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      556,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "DATA",
      [
        "storage",
        "002c0e9b",
        null,
        null
      ]
    ],
    [
      772,
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      556,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "DATA",
      [
        "storage",
        "002c0ee5",
        null,
        null
      ]
    ],
    [
      772,
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42368 ["INT_ADD", "register:40f0:8", ["const:c42368:8", "const:4:8"]]
+ 00c4335c ["INT_ADD", "register:40f0:8", ["const:c4335c:8", "const:4:8"]]
- 00c42388 ["COPY", "register:4050:8", ["const:c97000:8"]]
- 00c4238c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4337c ["COPY", "register:4050:8", ["const:c98000:8"]]
+ 00c43380 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c423b0 ["COPY", "tmp:0:8", ["const:e9b:8"]]
+ 00c433a4 ["COPY", "tmp:0:8", ["const:ee5:8"]]
~~~


### [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) → [`00c4351c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) FUN_00c4351c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) · 呼出先 5件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) · 呼出先 5件 [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c4351c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c4351c.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c435e4",
      "incomplete_value": false,
      "site": "00c435e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c425f0",
      "incomplete_value": false,
      "site": "00c425f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      200,
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      552,
      "DATA",
      [
        "storage",
        "00c98a40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      200,
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ],
    [
      552,
      "DATA",
      [
        "storage",
        "00c99a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42588 ["INT_ADD", "register:40f0:8", ["const:c42588:8", "const:4:8"]]
+ 00c4357c ["INT_ADD", "register:40f0:8", ["const:c4357c:8", "const:4:8"]]
- 00c42598 ["INT_ADD", "register:40f0:8", ["const:c42598:8", "const:4:8"]]
+ 00c4358c ["INT_ADD", "register:40f0:8", ["const:c4358c:8", "const:4:8"]]
- 00c425c0 ["INT_ADD", "register:40f0:8", ["const:c425c0:8", "const:4:8"]]
+ 00c435b4 ["INT_ADD", "register:40f0:8", ["const:c435b4:8", "const:4:8"]]
~~~


### [`00c42790`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md) → [`00c43784`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43784.md) FUN_00c43784

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c437e8",
      "incomplete_value": true,
      "site": "00c437e8",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c427f4",
      "incomplete_value": true,
      "site": "00c427f4",
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
            "const:ab0:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
+ 00c437b8 ["INT_ADD", "register:40f0:8", ["const:c437b8:8", "const:4:8"]]
- 00c427e4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c427e8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00c437d8 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c437dc ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00c42830 ["INT_ADD", "register:40f0:8", ["const:c42830:8", "const:4:8"]]
+ 00c43824 ["INT_ADD", "register:40f0:8", ["const:c43824:8", "const:4:8"]]
~~~


### [`00c42834`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md) → [`00c43828`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43828.md) FUN_00c43828

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 4件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43944",
      "incomplete_value": false,
      "site": "00c43944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42950",
      "incomplete_value": false,
      "site": "00c42950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      284,
      "DATA",
      [
        "storage",
        "00c98b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c99af0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42850 ["INT_ADD", "register:40f0:8", ["const:c42850:8", "const:4:8"]]
+ 00c43844 ["INT_ADD", "register:40f0:8", ["const:c43844:8", "const:4:8"]]
- 00c42860 ["INT_ADD", "register:40f0:8", ["const:c42860:8", "const:4:8"]]
+ 00c43854 ["INT_ADD", "register:40f0:8", ["const:c43854:8", "const:4:8"]]
- 00c4291c ["INT_ADD", "register:40f0:8", ["const:c4291c:8", "const:4:8"]]
+ 00c43910 ["INT_ADD", "register:40f0:8", ["const:c43910:8", "const:4:8"]]
~~~


### [`00c4299c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md) → [`00c43990`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43990.md) FUN_00c43990

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c439f8",
      "incomplete_value": false,
      "site": "00c439f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42a04",
      "incomplete_value": false,
      "site": "00c42a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43a24",
      "incomplete_value": false,
      "site": "00c43a24",
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
            "const:f99:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42a30",
      "incomplete_value": false,
      "site": "00c42a30",
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
            "const:eca:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
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
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "DATA",
      [
        "storage",
        "002b7eca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c990e0",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "DATA",
      [
        "storage",
        "002b7f99",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c429d4 ["INT_ADD", "register:40f0:8", ["const:c429d4:8", "const:4:8"]]
+ 00c439c8 ["INT_ADD", "register:40f0:8", ["const:c439c8:8", "const:4:8"]]
- 00c429f4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c429f8 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00c439e8 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c439ec ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00c42a18 ["COPY", "tmp:0:8", ["const:eca:8"]]
+ 00c43a0c ["COPY", "tmp:0:8", ["const:f99:8"]]
~~~


### [`00c42a5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) → [`00c43a50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43a50.md) FUN_00c43a50

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 9件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 9件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43ee0",
      "incomplete_value": false,
      "site": "00c43ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42eec",
      "incomplete_value": false,
      "site": "00c42eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      748,
      "DATA",
      [
        "storage",
        "00c98b90",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98c00",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98c70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      748,
      "DATA",
      [
        "storage",
        "00c99b60",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c99bd0",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42af8 ["INT_ADD", "register:40f0:8", ["const:c42af8:8", "const:4:8"]]
+ 00c43aec ["INT_ADD", "register:40f0:8", ["const:c43aec:8", "const:4:8"]]
- 00c42b40 ["INT_ADD", "register:40f0:8", ["const:c42b40:8", "const:4:8"]]
+ 00c43b34 ["INT_ADD", "register:40f0:8", ["const:c43b34:8", "const:4:8"]]
- 00c42b70 ["INT_ADD", "register:40f0:8", ["const:c42b70:8", "const:4:8"]]
+ 00c43b64 ["INT_ADD", "register:40f0:8", ["const:c43b64:8", "const:4:8"]]
~~~


### [`00c42f2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md) → [`00c43f20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43f20.md) FUN_00c43f20

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 8件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 8件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44204",
      "incomplete_value": true,
      "site": "00c44204",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43210",
      "incomplete_value": true,
      "site": "00c43210",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      740,
      "DATA",
      [
        "storage",
        "00c98d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      740,
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42f54 ["INT_ADD", "register:40f0:8", ["const:c42f54:8", "const:4:8"]]
+ 00c43f48 ["INT_ADD", "register:40f0:8", ["const:c43f48:8", "const:4:8"]]
- 00c42f64 ["INT_ADD", "register:40f0:8", ["const:c42f64:8", "const:4:8"]]
+ 00c43f58 ["INT_ADD", "register:40f0:8", ["const:c43f58:8", "const:4:8"]]
- 00c42ff8 ["COPY", "register:40e0:8", ["const:c97000:8"]]
- 00c42ffc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c43fec ["COPY", "register:40e0:8", ["const:c98000:8"]]
+ 00c43ff0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c43474`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md) → [`00c44468`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44468.md) FUN_00c44468

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c444cc",
      "incomplete_value": false,
      "site": "00c444cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c434d8",
      "incomplete_value": false,
      "site": "00c434d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c434a8 ["INT_ADD", "register:40f0:8", ["const:c434a8:8", "const:4:8"]]
+ 00c4449c ["INT_ADD", "register:40f0:8", ["const:c4449c:8", "const:4:8"]]
- 00c434c8 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c434cc ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 00c444bc ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c444c0 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00c4350c ["INT_ADD", "register:40f0:8", ["const:c4350c:8", "const:4:8"]]
+ 00c44500 ["INT_ADD", "register:40f0:8", ["const:c44500:8", "const:4:8"]]
~~~


### [`00c43510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md) → [`00c44504`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44504.md) FUN_00c44504

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4456c",
      "incomplete_value": false,
      "site": "00c4456c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43578",
      "incomplete_value": false,
      "site": "00c43578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c98ab0",
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
        "00c99a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c43548 ["INT_ADD", "register:40f0:8", ["const:c43548:8", "const:4:8"]]
+ 00c4453c ["INT_ADD", "register:40f0:8", ["const:c4453c:8", "const:4:8"]]
- 00c43568 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c4356c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00c4455c ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c44560 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00c435b8 ["INT_ADD", "register:40f0:8", ["const:c435b8:8", "const:4:8"]]
+ 00c445ac ["INT_ADD", "register:40f0:8", ["const:c445ac:8", "const:4:8"]]
~~~


### [`00c43668`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md) → [`00c4465c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c4465c.md) FUN_00c4465c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c446c0",
      "incomplete_value": true,
      "site": "00c446c0",
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
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c436cc",
      "incomplete_value": true,
      "site": "00c436cc",
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
            "const:ea0:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c98ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4369c ["INT_ADD", "register:40f0:8", ["const:c4369c:8", "const:4:8"]]
+ 00c44690 ["INT_ADD", "register:40f0:8", ["const:c44690:8", "const:4:8"]]
- 00c436bc ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c436c0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00c446b0 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c446b4 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00c43704 ["INT_ADD", "register:40f0:8", ["const:c43704:8", "const:4:8"]]
+ 00c446f8 ["INT_ADD", "register:40f0:8", ["const:c446f8:8", "const:4:8"]]
~~~


### [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) → [`00c446fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) FUN_00c446fc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 7件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3eb30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 7件 [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c3f654`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c3fb24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3fb24.md) [`00c4c6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) [`00c4c83c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c447d0",
      "incomplete_value": false,
      "site": "00c447d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c437dc",
      "incomplete_value": false,
      "site": "00c437dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44ad0",
      "incomplete_value": false,
      "site": "00c44ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43adc",
      "incomplete_value": false,
      "site": "00c43adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44ba0",
      "incomplete_value": false,
      "site": "00c44ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43bac",
      "incomplete_value": false,
      "site": "00c43bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d0:8"
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
      212,
      "DATA",
      [
        "storage",
        "00c990d0",
        null,
        "undefined *"
      ]
    ],
    [
      520,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      588,
      "DATA",
      [
        "storage",
        "00c98f10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      212,
      "DATA",
      [
        "storage",
        "00c9a0a0",
        null,
        "undefined *"
      ]
    ],
    [
      520,
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ],
    [
      588,
      "DATA",
      [
        "storage",
        "00c99ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c43780 ["INT_ADD", "register:40f0:8", ["const:c43780:8", "const:4:8"]]
+ 00c44774 ["INT_ADD", "register:40f0:8", ["const:c44774:8", "const:4:8"]]
- 00c437a8 ["INT_ADD", "register:40f0:8", ["const:c437a8:8", "const:4:8"]]
+ 00c4479c ["INT_ADD", "register:40f0:8", ["const:c4479c:8", "const:4:8"]]
- 00c437cc ["COPY", "register:4050:8", ["const:c99000:8"]]
- 00c437d0 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 00c447c0 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00c447c4 ["COPY", "tmp:0:8", ["const:a0:8"]]
~~~


### [`00c43d7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md) → [`00c44d70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c44d70.md) FUN_00c44d70

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c44de4",
      "incomplete_value": false,
      "site": "00c44de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43df0",
      "incomplete_value": false,
      "site": "00c43df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c98c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c43dc0 ["INT_ADD", "register:40f0:8", ["const:c43dc0:8", "const:4:8"]]
+ 00c44db4 ["INT_ADD", "register:40f0:8", ["const:c44db4:8", "const:4:8"]]
- 00c43de0 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c43de4 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c44dd4 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c44dd8 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00c43e44 ["INT_ADD", "register:40f0:8", ["const:c43e44:8", "const:4:8"]]
+ 00c44e38 ["INT_ADD", "register:40f0:8", ["const:c44e38:8", "const:4:8"]]
~~~


### [`00c4435c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md) → [`00c45350`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c45/00c45350.md) FUN_00c45350

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c453c0",
      "incomplete_value": false,
      "site": "00c453c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c443cc",
      "incomplete_value": false,
      "site": "00c443cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c98c80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4439c ["INT_ADD", "register:40f0:8", ["const:c4439c:8", "const:4:8"]]
+ 00c45390 ["INT_ADD", "register:40f0:8", ["const:c45390:8", "const:4:8"]]
- 00c443bc ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c443c0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
+ 00c453b0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c453b4 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 00c44418 ["INT_ADD", "register:40f0:8", ["const:c44418:8", "const:4:8"]]
+ 00c4540c ["INT_ADD", "register:40f0:8", ["const:c4540c:8", "const:4:8"]]
~~~


### [`00c462d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) → [`00c472c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c472c8.md) FUN_00c472c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c3ac28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 3件 [`00c3bc1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bc1c.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47370",
      "incomplete_value": false,
      "site": "00c47370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4637c",
      "incomplete_value": false,
      "site": "00c4637c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
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
        "00c98180",
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
        "00c99150",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c462fc ["INT_ADD", "register:40f0:8", ["const:c462fc:8", "const:4:8"]]
+ 00c472f0 ["INT_ADD", "register:40f0:8", ["const:c472f0:8", "const:4:8"]]
- 00c46344 ["INT_ADD", "register:40f0:8", ["const:c46344:8", "const:4:8"]]
+ 00c47338 ["INT_ADD", "register:40f0:8", ["const:c47338:8", "const:4:8"]]
- 00c46374 ["COPY", "register:4048:8", ["const:c98000:8"]]
- 00c46378 ["COPY", "tmp:0:8", ["const:180:8"]]
+ 00c47368 ["COPY", "register:4048:8", ["const:c99000:8"]]
+ 00c4736c ["COPY", "tmp:0:8", ["const:150:8"]]
~~~


### [`00c463c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md) → [`00c473bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c473bc.md) FUN_00c473bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4742c",
      "incomplete_value": false,
      "site": "00c47438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
      124,
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c991c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c463fc ["INT_ADD", "register:40f0:8", ["const:c463fc:8", "const:4:8"]]
+ 00c473f0 ["INT_ADD", "register:40f0:8", ["const:c473f0:8", "const:4:8"]]
- 00c46434 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c46438 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00c47428 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4742c ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 00c4646c ["INT_ADD", "register:40f0:8", ["const:c4646c:8", "const:4:8"]]
+ 00c47460 ["INT_ADD", "register:40f0:8", ["const:c47460:8", "const:4:8"]]
~~~


### [`00c46470`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md) → [`00c47464`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47464.md) FUN_00c47464

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c474c8",
      "incomplete_value": false,
      "site": "00c474c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c464d4",
      "incomplete_value": false,
      "site": "00c464d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c464a4 ["INT_ADD", "register:40f0:8", ["const:c464a4:8", "const:4:8"]]
+ 00c47498 ["INT_ADD", "register:40f0:8", ["const:c47498:8", "const:4:8"]]
- 00c464c4 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c464c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 00c474b8 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c474bc ["COPY", "tmp:0:8", ["const:380:8"]]
- 00c4650c ["INT_ADD", "register:40f0:8", ["const:c4650c:8", "const:4:8"]]
+ 00c47500 ["INT_ADD", "register:40f0:8", ["const:c47500:8", "const:4:8"]]
~~~


### [`00c46510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md) → [`00c47504`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47504.md) FUN_00c47504

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47570",
      "incomplete_value": false,
      "site": "00c47570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4657c",
      "incomplete_value": false,
      "site": "00c4657c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46544 ["INT_ADD", "register:40f0:8", ["const:c46544:8", "const:4:8"]]
+ 00c47538 ["INT_ADD", "register:40f0:8", ["const:c47538:8", "const:4:8"]]
- 00c4656c ["INT_ADD", "register:40f0:8", ["const:c4656c:8", "const:4:8"]]
+ 00c47560 ["INT_ADD", "register:40f0:8", ["const:c47560:8", "const:4:8"]]
- 00c46570 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c46574 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c47564 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c47568 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) → [`00c475b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) FUN_00c475b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 14件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md)
- 新版 呼出元 2件 [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 14件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c488c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c476d0",
      "incomplete_value": false,
      "site": "00c476d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c466dc",
      "incomplete_value": false,
      "site": "00c466dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c476f8",
      "incomplete_value": false,
      "site": "00c476f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:e03:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46704",
      "incomplete_value": false,
      "site": "00c46704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d34:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47884",
      "incomplete_value": false,
      "site": "00c47884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46890",
      "incomplete_value": false,
      "site": "00c46890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:420:8"
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
      288,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "002b8d34",
        null,
        "string"
      ]
    ],
    [
      724,
      "DATA",
      [
        "storage",
        "00c98420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      288,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "002b8e03",
        null,
        "string"
      ]
    ],
    [
      724,
      "DATA",
      [
        "storage",
        "00c993f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c466ac ["INT_ADD", "register:40f0:8", ["const:c466ac:8", "const:4:8"]]
+ 00c476a0 ["INT_ADD", "register:40f0:8", ["const:c476a0:8", "const:4:8"]]
- 00c466cc ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c466d0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c476c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c476c4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c466f4 ["COPY", "tmp:0:8", ["const:d34:8"]]
+ 00c476e8 ["COPY", "tmp:0:8", ["const:e03:8"]]
~~~


### [`00c46d3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md) → [`00c47d30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47d30.md) FUN_00c47d30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47d94",
      "incomplete_value": false,
      "site": "00c47d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46da0",
      "incomplete_value": false,
      "site": "00c46da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c987a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99770",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46d70 ["INT_ADD", "register:40f0:8", ["const:c46d70:8", "const:4:8"]]
+ 00c47d64 ["INT_ADD", "register:40f0:8", ["const:c47d64:8", "const:4:8"]]
- 00c46d90 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c46d94 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00c47d84 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c47d88 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00c46dd8 ["INT_ADD", "register:40f0:8", ["const:c46dd8:8", "const:4:8"]]
+ 00c47dcc ["INT_ADD", "register:40f0:8", ["const:c47dcc:8", "const:4:8"]]
~~~


### [`00c46ddc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md) → [`00c47dd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c47dd0.md) FUN_00c47dd0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c427e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c42/00c427e0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47e38",
      "incomplete_value": false,
      "site": "00c47e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46e44",
      "incomplete_value": false,
      "site": "00c46e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c98810",
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
        "00c997e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46e14 ["INT_ADD", "register:40f0:8", ["const:c46e14:8", "const:4:8"]]
+ 00c47e08 ["INT_ADD", "register:40f0:8", ["const:c47e08:8", "const:4:8"]]
- 00c46e34 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c46e38 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 00c47e28 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c47e2c ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 00c46e84 ["INT_ADD", "register:40f0:8", ["const:c46e84:8", "const:4:8"]]
+ 00c47e78 ["INT_ADD", "register:40f0:8", ["const:c47e78:8", "const:4:8"]]
~~~


### [`00c4722c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md) → [`00c48220`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48220.md) FUN_00c48220

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c48344",
      "incomplete_value": false,
      "site": "00c4835c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:dfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47350",
      "incomplete_value": false,
      "site": "00c47368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d2c:8"
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
      292,
      "PARAM",
      [
        "storage",
        "002b8d2c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      292,
      "PARAM",
      [
        "storage",
        "002b8dfb",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c47350 ["COPY", "tmp:0:8", ["const:d2c:8"]]
+ 00c48344 ["COPY", "tmp:0:8", ["const:dfb:8"]]
- 00c47368 ["INT_ADD", "register:40f0:8", ["const:c47368:8", "const:4:8"]]
+ 00c4835c ["INT_ADD", "register:40f0:8", ["const:c4835c:8", "const:4:8"]]
- 00c4739c ["INT_ADD", "register:40f0:8", ["const:c4739c:8", "const:4:8"]]
+ 00c48390 ["INT_ADD", "register:40f0:8", ["const:c48390:8", "const:4:8"]]
~~~


### [`00c473e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md) → [`00c483dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c483dc.md) FUN_00c483dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c48518",
      "incomplete_value": false,
      "site": "00c48528",
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
            "const:58e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47524",
      "incomplete_value": false,
      "site": "00c47534",
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
            "const:4c1:8"
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
      316,
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      316,
      "PARAM",
      [
        "storage",
        "002ac58e",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c47524 ["COPY", "tmp:0:8", ["const:4c1:8"]]
+ 00c48518 ["COPY", "tmp:0:8", ["const:58e:8"]]
- 00c47534 ["INT_ADD", "register:40f0:8", ["const:c47534:8", "const:4:8"]]
+ 00c48528 ["INT_ADD", "register:40f0:8", ["const:c48528:8", "const:4:8"]]
- 00c47568 ["INT_ADD", "register:40f0:8", ["const:c47568:8", "const:4:8"]]
+ 00c4855c ["INT_ADD", "register:40f0:8", ["const:c4855c:8", "const:4:8"]]
~~~


### [`00c475b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md) → [`00c485a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c485a8.md) FUN_00c485a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5f1a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4871c",
      "incomplete_value": false,
      "site": "00c48730",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47728",
      "incomplete_value": false,
      "site": "00c4773c",
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
            "const:dfa:8"
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
      372,
      "PARAM",
      [
        "storage",
        "002b9dfa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      372,
      "PARAM",
      [
        "storage",
        "002b9ed8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c47728 ["COPY", "tmp:0:8", ["const:dfa:8"]]
+ 00c4871c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00c4773c ["INT_ADD", "register:40f0:8", ["const:c4773c:8", "const:4:8"]]
+ 00c48730 ["INT_ADD", "register:40f0:8", ["const:c48730:8", "const:4:8"]]
- 00c47770 ["INT_ADD", "register:40f0:8", ["const:c47770:8", "const:4:8"]]
+ 00c48764 ["INT_ADD", "register:40f0:8", ["const:c48764:8", "const:4:8"]]
~~~


### [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) → [`00c488c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) FUN_00c488c4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 14件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)
- 新版 呼出元 3件 [`00c3d9d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d9d0.md) [`00c475b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) [`00c488c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) · 呼出先 14件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c489e0",
      "incomplete_value": false,
      "site": "00c489e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c479ec",
      "incomplete_value": false,
      "site": "00c479ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48ab8",
      "incomplete_value": false,
      "site": "00c48ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47ac4",
      "incomplete_value": false,
      "site": "00c47ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48b78",
      "incomplete_value": false,
      "site": "00c48b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47b84",
      "incomplete_value": false,
      "site": "00c47b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      500,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      692,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      500,
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      692,
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4796c ["INT_ADD", "register:40f0:8", ["const:c4796c:8", "const:4:8"]]
+ 00c48960 ["INT_ADD", "register:40f0:8", ["const:c48960:8", "const:4:8"]]
- 00c47980 ["INT_ADD", "register:40f0:8", ["const:c47980:8", "const:4:8"]]
+ 00c48974 ["INT_ADD", "register:40f0:8", ["const:c48974:8", "const:4:8"]]
- 00c479b8 ["INT_ADD", "register:40f0:8", ["const:c479b8:8", "const:4:8"]]
+ 00c489ac ["INT_ADD", "register:40f0:8", ["const:c489ac:8", "const:4:8"]]
~~~


### [`00c4823c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md) → [`00c49230`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49230.md) FUN_00c49230

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c475b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c47/00c475b0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c492ac",
      "incomplete_value": false,
      "site": "00c492ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c482b8",
      "incomplete_value": false,
      "site": "00c482b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c98730",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c99700",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48288 ["INT_ADD", "register:40f0:8", ["const:c48288:8", "const:4:8"]]
+ 00c4927c ["INT_ADD", "register:40f0:8", ["const:c4927c:8", "const:4:8"]]
- 00c482a8 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c482ac ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00c4929c ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c492a0 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00c48318 ["INT_ADD", "register:40f0:8", ["const:c48318:8", "const:4:8"]]
+ 00c4930c ["INT_ADD", "register:40f0:8", ["const:c4930c:8", "const:4:8"]]
~~~


### [`00c4831c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md) → [`00c49310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49310.md) FUN_00c49310

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c59700`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4936c",
      "incomplete_value": false,
      "site": "00c49384",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48378",
      "incomplete_value": false,
      "site": "00c48390",
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
            "const:e95:8"
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
      "definition_site": "00c49374",
      "incomplete_value": false,
      "site": "00c49384",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48380",
      "incomplete_value": false,
      "site": "00c48390",
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
            "const:8c7:8"
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
      "definition_site": "00c4937c",
      "incomplete_value": false,
      "site": "00c49384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48388",
      "incomplete_value": false,
      "site": "00c48390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:38e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      92,
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      92,
      "PARAM",
      [
        "storage",
        "002a0ed5",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "002b2911",
        null,
        "string"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48378 ["COPY", "tmp:0:8", ["const:e95:8"]]
+ 00c4936c ["COPY", "tmp:0:8", ["const:ed5:8"]]
- 00c48380 ["COPY", "tmp:0:8", ["const:8c7:8"]]
+ 00c49374 ["COPY", "tmp:0:8", ["const:911:8"]]
- 00c48388 ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 00c4937c ["COPY", "tmp:0:8", ["const:4e6:8"]]
~~~


### [`00c484e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md) → [`00c494dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c494dc.md) FUN_00c494dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c488c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c488c4.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49540",
      "incomplete_value": false,
      "site": "00c49540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4854c",
      "incomplete_value": false,
      "site": "00c4854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c986c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99690",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4851c ["INT_ADD", "register:40f0:8", ["const:c4851c:8", "const:4:8"]]
+ 00c49510 ["INT_ADD", "register:40f0:8", ["const:c49510:8", "const:4:8"]]
- 00c4853c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c48540 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c49530 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c49534 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00c48584 ["INT_ADD", "register:40f0:8", ["const:c48584:8", "const:4:8"]]
+ 00c49578 ["INT_ADD", "register:40f0:8", ["const:c49578:8", "const:4:8"]]
~~~


### [`00c487bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md) → [`00c497b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c497b0.md) FUN_00c497b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49808",
      "incomplete_value": true,
      "site": "00c49814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48814",
      "incomplete_value": true,
      "site": "00c48820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d51:8"
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
      88,
      "READ",
      [
        "storage",
        "002a1d51",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "002a1d91",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c487f8 ["INT_ADD", "register:40f0:8", ["const:c487f8:8", "const:4:8"]]
+ 00c497ec ["INT_ADD", "register:40f0:8", ["const:c497ec:8", "const:4:8"]]
- 00c4880c ["COPY", "tmp:0:8", ["const:d51:8"]]
+ 00c49800 ["COPY", "tmp:0:8", ["const:d91:8"]]
- 00c48840 ["INT_ADD", "register:40f0:8", ["const:c48840:8", "const:4:8"]]
+ 00c49834 ["INT_ADD", "register:40f0:8", ["const:c49834:8", "const:4:8"]]
~~~


### [`00c48b0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) → [`00c49b00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49b00.md) FUN_00c49b00

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49b68",
      "incomplete_value": true,
      "site": "00c49b74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48b74",
      "incomplete_value": true,
      "site": "00c48b80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:afc:8"
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
      "definition_site": "00c49bd4",
      "incomplete_value": true,
      "site": "00c49be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9be:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48be0",
      "incomplete_value": true,
      "site": "00c48bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 13,
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
        "002bfafc",
        null,
        "string"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "002b08e7",
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
        "002bfbda",
        null,
        "string"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "002b09be",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48b58 ["INT_ADD", "register:40f0:8", ["const:c48b58:8", "const:4:8"]]
+ 00c49b4c ["INT_ADD", "register:40f0:8", ["const:c49b4c:8", "const:4:8"]]
- 00c48b6c ["COPY", "tmp:0:8", ["const:afc:8"]]
+ 00c49b60 ["COPY", "tmp:0:8", ["const:bda:8"]]
- 00c48b98 ["INT_ADD", "register:40f0:8", ["const:c48b98:8", "const:4:8"]]
+ 00c49b8c ["INT_ADD", "register:40f0:8", ["const:c49b8c:8", "const:4:8"]]
~~~


### [`00c48c28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md) → [`00c49c1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c49/00c49c1c.md) FUN_00c49c1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49cbc",
      "incomplete_value": true,
      "site": "00c49ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48cc8",
      "incomplete_value": true,
      "site": "00c48cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
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
      160,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      160,
      "READ",
      [
        "storage",
        "002c0eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48c54 ["INT_ADD", "register:40f0:8", ["const:c48c54:8", "const:4:8"]]
+ 00c49c48 ["INT_ADD", "register:40f0:8", ["const:c49c48:8", "const:4:8"]]
- 00c48c78 ["INT_ADD", "register:40f0:8", ["const:c48c78:8", "const:4:8"]]
+ 00c49c6c ["INT_ADD", "register:40f0:8", ["const:c49c6c:8", "const:4:8"]]
- 00c48cac ["INT_ADD", "register:40f0:8", ["const:c48cac:8", "const:4:8"]]
+ 00c49ca0 ["INT_ADD", "register:40f0:8", ["const:c49ca0:8", "const:4:8"]]
~~~


### [`00c495f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) → [`00c4a5ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a5ec.md) FUN_00c4a5ec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4216c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c43160`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c43/00c43160.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a650",
      "incomplete_value": false,
      "site": "00c4a650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4965c",
      "incomplete_value": false,
      "site": "00c4965c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4962c ["INT_ADD", "register:40f0:8", ["const:c4962c:8", "const:4:8"]]
+ 00c4a620 ["INT_ADD", "register:40f0:8", ["const:c4a620:8", "const:4:8"]]
- 00c4964c ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00c49650 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00c4a640 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c4a644 ["COPY", "tmp:0:8", ["const:850:8"]]
- 00c49694 ["INT_ADD", "register:40f0:8", ["const:c49694:8", "const:4:8"]]
+ 00c4a688 ["INT_ADD", "register:40f0:8", ["const:c4a688:8", "const:4:8"]]
~~~


### [`00c4978c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) → [`00c4a780`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4a780.md) FUN_00c4a780

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c49f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c4af04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a960",
      "incomplete_value": false,
      "site": "00c4a964",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4996c",
      "incomplete_value": false,
      "site": "00c49970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00c4ac98",
      "incomplete_value": false,
      "site": "00c4ac9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c49ca4",
      "incomplete_value": false,
      "site": "00c49ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      484,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ],
    [
      1308,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      484,
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ],
    [
      1308,
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c497e0 ["INT_ADD", "register:40f0:8", ["const:c497e0:8", "const:4:8"]]
+ 00c4a7d4 ["INT_ADD", "register:40f0:8", ["const:c4a7d4:8", "const:4:8"]]
- 00c4985c ["INT_ADD", "register:40f0:8", ["const:c4985c:8", "const:4:8"]]
+ 00c4a850 ["INT_ADD", "register:40f0:8", ["const:c4a850:8", "const:4:8"]]
- 00c4988c ["INT_ADD", "register:40f0:8", ["const:c4988c:8", "const:4:8"]]
+ 00c4a880 ["INT_ADD", "register:40f0:8", ["const:c4a880:8", "const:4:8"]]
~~~


### [`00c4a8b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md) → [`00c4b8a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4b8a8.md) FUN_00c4b8a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ba68",
      "incomplete_value": true,
      "site": "00c4ba74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:96b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4aa74",
      "incomplete_value": true,
      "site": "00c4aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:894:8"
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
      448,
      "READ",
      [
        "storage",
        "002b1894",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      448,
      "READ",
      [
        "storage",
        "002b196b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4a8fc ["INT_ADD", "register:40f0:8", ["const:c4a8fc:8", "const:4:8"]]
+ 00c4b8f0 ["INT_ADD", "register:40f0:8", ["const:c4b8f0:8", "const:4:8"]]
- 00c4a968 ["INT_ADD", "register:40f0:8", ["const:c4a968:8", "const:4:8"]]
+ 00c4b95c ["INT_ADD", "register:40f0:8", ["const:c4b95c:8", "const:4:8"]]
- 00c4a99c ["INT_ADD", "register:40f0:8", ["const:c4a99c:8", "const:4:8"]]
+ 00c4b990 ["INT_ADD", "register:40f0:8", ["const:c4b990:8", "const:4:8"]]
~~~


### [`00c4aba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md) → [`00c4bb94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bb94.md) FUN_00c4bb94

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bbf8",
      "incomplete_value": true,
      "site": "00c4bc08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:38c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ac04",
      "incomplete_value": true,
      "site": "00c4ac14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ae:8"
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
      100,
      "READ",
      [
        "storage",
        "002bc2ae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bc38c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4abe4 ["INT_ADD", "register:40f0:8", ["const:c4abe4:8", "const:4:8"]]
+ 00c4bbd8 ["INT_ADD", "register:40f0:8", ["const:c4bbd8:8", "const:4:8"]]
- 00c4abfc ["COPY", "tmp:0:8", ["const:2ae:8"]]
+ 00c4bbf0 ["COPY", "tmp:0:8", ["const:38c:8"]]
- 00c4ac34 ["INT_ADD", "register:40f0:8", ["const:c4ac34:8", "const:4:8"]]
+ 00c4bc28 ["INT_ADD", "register:40f0:8", ["const:c4bc28:8", "const:4:8"]]
~~~


### [`00c4acc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md) → [`00c4bcb8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4b/00c4bcb8.md) FUN_00c4bcb8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bd1c",
      "incomplete_value": true,
      "site": "00c4bd2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ad28",
      "incomplete_value": true,
      "site": "00c4ad38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
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
      100,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002c0eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ad08 ["INT_ADD", "register:40f0:8", ["const:c4ad08:8", "const:4:8"]]
+ 00c4bcfc ["INT_ADD", "register:40f0:8", ["const:c4bcfc:8", "const:4:8"]]
- 00c4ad20 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00c4bd14 ["COPY", "tmp:0:8", ["const:eda:8"]]
- 00c4ad58 ["INT_ADD", "register:40f0:8", ["const:c4ad58:8", "const:4:8"]]
+ 00c4bd4c ["INT_ADD", "register:40f0:8", ["const:c4bd4c:8", "const:4:8"]]
~~~


### [`00c4b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md) → [`00c4c134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c134.md) FUN_00c4c134

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c254",
      "incomplete_value": true,
      "site": "00c4c260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b260",
      "incomplete_value": true,
      "site": "00c4b26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee4:8"
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
      288,
      "READ",
      [
        "storage",
        "002b7ee4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      288,
      "READ",
      [
        "storage",
        "002b7fb3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b16c ["INT_ADD", "register:40f0:8", ["const:c4b16c:8", "const:4:8"]]
+ 00c4c160 ["INT_ADD", "register:40f0:8", ["const:c4c160:8", "const:4:8"]]
- 00c4b190 ["INT_ADD", "register:40f0:8", ["const:c4b190:8", "const:4:8"]]
+ 00c4c184 ["INT_ADD", "register:40f0:8", ["const:c4c184:8", "const:4:8"]]
- 00c4b1bc ["INT_ADD", "register:40f0:8", ["const:c4b1bc:8", "const:4:8"]]
+ 00c4c1b0 ["INT_ADD", "register:40f0:8", ["const:c4c1b0:8", "const:4:8"]]
~~~


### [`00c4b450`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) → [`00c4c444`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c444.md) FUN_00c4c444

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c49f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c4af04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4a/00c4af04.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c4ac",
      "incomplete_value": true,
      "site": "00c4c4b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b4b8",
      "incomplete_value": true,
      "site": "00c4b4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:524:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c538",
      "incomplete_value": false,
      "site": "00c4c53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b544",
      "incomplete_value": false,
      "site": "00c4b548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      104,
      "READ",
      [
        "storage",
        "002ac524",
        null,
        "string"
      ]
    ],
    [
      248,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "READ",
      [
        "storage",
        "002ac5f1",
        null,
        "string"
      ]
    ],
    [
      248,
      "DATA",
      [
        "storage",
        "00c99930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b498 ["INT_ADD", "register:40f0:8", ["const:c4b498:8", "const:4:8"]]
+ 00c4c48c ["INT_ADD", "register:40f0:8", ["const:c4c48c:8", "const:4:8"]]
- 00c4b4b0 ["COPY", "tmp:0:8", ["const:524:8"]]
+ 00c4c4a4 ["COPY", "tmp:0:8", ["const:5f1:8"]]
- 00c4b504 ["INT_ADD", "register:40f0:8", ["const:c4b504:8", "const:4:8"]]
+ 00c4c4f8 ["INT_ADD", "register:40f0:8", ["const:c4c4f8:8", "const:4:8"]]
~~~


### [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) → [`00c4c83c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) FUN_00c4c83c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 6件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4bbf8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c446fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c44/00c446fc.md) · 呼出先 6件 [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c3f654`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c4c6b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c6b8.md) [`00c4cbec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c93c",
      "incomplete_value": false,
      "site": "00c4c93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b948",
      "incomplete_value": false,
      "site": "00c4b948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c9e4",
      "incomplete_value": false,
      "site": "00c4c9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b9f0",
      "incomplete_value": false,
      "site": "00c4b9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "definition_site": "00c4caa4",
      "incomplete_value": false,
      "site": "00c4caa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bab0",
      "incomplete_value": false,
      "site": "00c4bab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      256,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      424,
      "DATA",
      [
        "storage",
        "00c98f80",
        null,
        "undefined *"
      ]
    ],
    [
      616,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      256,
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ],
    [
      424,
      "DATA",
      [
        "storage",
        "00c99f50",
        null,
        "undefined *"
      ]
    ],
    [
      616,
      "DATA",
      [
        "storage",
        "00c9a5e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b8b4 ["INT_ADD", "register:40f0:8", ["const:c4b8b4:8", "const:4:8"]]
+ 00c4c8a8 ["INT_ADD", "register:40f0:8", ["const:c4c8a8:8", "const:4:8"]]
- 00c4b8c4 ["INT_ADD", "register:40f0:8", ["const:c4b8c4:8", "const:4:8"]]
+ 00c4c8b8 ["INT_ADD", "register:40f0:8", ["const:c4c8b8:8", "const:4:8"]]
- 00c4b8f0 ["INT_ADD", "register:40f0:8", ["const:c4b8f0:8", "const:4:8"]]
+ 00c4c8e4 ["INT_ADD", "register:40f0:8", ["const:c4c8e4:8", "const:4:8"]]
~~~


### [`00c4bbf8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) → [`00c4cbec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4cbec.md) FUN_00c4cbec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) [`00c4c83c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4c/00c4c83c.md) · 呼出先 5件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3f040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f040.md) [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cd38",
      "incomplete_value": false,
      "site": "00c4cd38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bd44",
      "incomplete_value": false,
      "site": "00c4bd44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cf24",
      "incomplete_value": false,
      "site": "00c4cf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bf30",
      "incomplete_value": false,
      "site": "00c4bf30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      88,
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00c98a00",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c98a01",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c98a10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4bc30 ["COPY", "register:4060:8", ["const:c97850:8"]]
+ 00c4cc24 ["COPY", "register:4060:8", ["const:c98820:8"]]
- 00c4bcdc ["INT_ADD", "register:40f0:8", ["const:c4bcdc:8", "const:4:8"]]
+ 00c4ccd0 ["INT_ADD", "register:40f0:8", ["const:c4ccd0:8", "const:4:8"]]
- 00c4bd10 ["INT_ADD", "register:40f0:8", ["const:c4bd10:8", "const:4:8"]]
+ 00c4cd04 ["INT_ADD", "register:40f0:8", ["const:c4cd04:8", "const:4:8"]]
~~~


### [`00c4c014`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md) → [`00c4d008`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d008.md) FUN_00c4d008

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d06c",
      "incomplete_value": true,
      "site": "00c4d07c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:71f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c078",
      "incomplete_value": true,
      "site": "00c4c088",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:641:8"
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
      100,
      "READ",
      [
        "storage",
        "002bd641",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bd71f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c058 ["INT_ADD", "register:40f0:8", ["const:c4c058:8", "const:4:8"]]
+ 00c4d04c ["INT_ADD", "register:40f0:8", ["const:c4d04c:8", "const:4:8"]]
- 00c4c070 ["COPY", "tmp:0:8", ["const:641:8"]]
+ 00c4d064 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 00c4c0a8 ["INT_ADD", "register:40f0:8", ["const:c4c0a8:8", "const:4:8"]]
+ 00c4d09c ["INT_ADD", "register:40f0:8", ["const:c4d09c:8", "const:4:8"]]
~~~


### [`00c4c0f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md) → [`00c4d0ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d0ec.md) FUN_00c4d0ec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d150",
      "incomplete_value": true,
      "site": "00c4d160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:397:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c15c",
      "incomplete_value": true,
      "site": "00c4c16c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b9:8"
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
      100,
      "READ",
      [
        "storage",
        "002bc2b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bc397",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c13c ["INT_ADD", "register:40f0:8", ["const:c4c13c:8", "const:4:8"]]
+ 00c4d130 ["INT_ADD", "register:40f0:8", ["const:c4d130:8", "const:4:8"]]
- 00c4c154 ["COPY", "tmp:0:8", ["const:2b9:8"]]
+ 00c4d148 ["COPY", "tmp:0:8", ["const:397:8"]]
- 00c4c190 ["INT_ADD", "register:40f0:8", ["const:c4c190:8", "const:4:8"]]
+ 00c4d184 ["INT_ADD", "register:40f0:8", ["const:c4d184:8", "const:4:8"]]
~~~


### [`00c4c3d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md) → [`00c4d3c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d3c8.md) FUN_00c4d3c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d55c",
      "incomplete_value": false,
      "site": "00c4d574",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c568",
      "incomplete_value": false,
      "site": "00c4c580",
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
            "const:e95:8"
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
      "definition_site": "00c4d564",
      "incomplete_value": false,
      "site": "00c4d574",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c570",
      "incomplete_value": false,
      "site": "00c4c580",
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
            "const:8c7:8"
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
      "definition_site": "00c4d56c",
      "incomplete_value": false,
      "site": "00c4d574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c578",
      "incomplete_value": false,
      "site": "00c4c580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:38e:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
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
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002bd64b",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002b8d44",
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
        "002b9fad",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002bd729",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002b8e13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c41c ["INT_ADD", "register:40f0:8", ["const:c4c41c:8", "const:4:8"]]
+ 00c4d410 ["INT_ADD", "register:40f0:8", ["const:c4d410:8", "const:4:8"]]
- 00c4c470 ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00c4d464 ["COPY", "tmp:0:8", ["const:fad:8"]]
- 00c4c490 ["COPY", "tmp:0:8", ["const:64b:8"]]
+ 00c4d484 ["COPY", "tmp:0:8", ["const:729:8"]]
~~~


### [`00c4c58c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md) → [`00c4d580`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d580.md) FUN_00c4d580

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c3909c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c39/00c3909c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4d640",
      "incomplete_value": false,
      "site": "00c4d658",
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
            "const:ed5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c64c",
      "incomplete_value": false,
      "site": "00c4c664",
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
            "const:e95:8"
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
      "definition_site": "00c4d648",
      "incomplete_value": false,
      "site": "00c4d658",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c654",
      "incomplete_value": false,
      "site": "00c4c664",
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
            "const:8c7:8"
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
      "definition_site": "00c4d650",
      "incomplete_value": false,
      "site": "00c4d658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:4e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c65c",
      "incomplete_value": false,
      "site": "00c4c664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:38e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "002b7ef0",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      32,
      "DATA",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "002b7fbf",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "002b9fad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c5ac ["COPY", "tmp:0:8", ["const:ecf:8"]]
+ 00c4d5a0 ["COPY", "tmp:0:8", ["const:fad:8"]]
- 00c4c5cc ["COPY", "tmp:0:8", ["const:64b:8"]]
+ 00c4d5c0 ["COPY", "tmp:0:8", ["const:729:8"]]
- 00c4c5dc ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00c4d5d0 ["COPY", "tmp:0:8", ["const:fbf:8"]]
~~~


### [`00c4c670`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md) → [`00c4d664`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d664.md) FUN_00c4d664

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d7a4",
      "incomplete_value": true,
      "site": "00c4d7ac",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:bbf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c7b0",
      "incomplete_value": true,
      "site": "00c4c7b8",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:ae1:8"
              ]
            ]
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
      "definition_site": "00c4d7a8",
      "incomplete_value": true,
      "site": "00c4d7b0",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c7b4",
      "incomplete_value": true,
      "site": "00c4c7bc",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d810",
      "incomplete_value": true,
      "site": "00c4d818",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:220:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c81c",
      "incomplete_value": true,
      "site": "00c4c824",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:142:8"
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
      320,
      "READ",
      [
        "storage",
        "002b4ae1",
        null,
        "string"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "002b4aee",
        null,
        "string"
      ]
    ],
    [
      428,
      "READ",
      [
        "storage",
        "002bb142",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      320,
      "READ",
      [
        "storage",
        "002b4bbf",
        null,
        "string"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "002b4bcc",
        null,
        "string"
      ]
    ],
    [
      428,
      "READ",
      [
        "storage",
        "002bb220",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c6b8 ["INT_ADD", "register:40f0:8", ["const:c4c6b8:8", "const:4:8"]]
+ 00c4d6ac ["INT_ADD", "register:40f0:8", ["const:c4d6ac:8", "const:4:8"]]
- 00c4c6fc ["INT_ADD", "register:40f0:8", ["const:c4c6fc:8", "const:4:8"]]
+ 00c4d6f0 ["INT_ADD", "register:40f0:8", ["const:c4d6f0:8", "const:4:8"]]
- 00c4c734 ["INT_ADD", "register:40f0:8", ["const:c4c734:8", "const:4:8"]]
+ 00c4d728 ["INT_ADD", "register:40f0:8", ["const:c4d728:8", "const:4:8"]]
~~~


### [`00c4c8ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md) → [`00c4d8a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4d8a0.md) FUN_00c4d8a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c4d8c0",
      "incomplete_value": true,
      "site": "00c4d8c4",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:e08:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c8cc",
      "incomplete_value": true,
      "site": "00c4c8d0",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:dc8:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
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
      16,
      "DATA",
      [
        "storage",
        "00313d98",
        null,
        null
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00313dc8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00313dd8",
        null,
        null
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00313e08",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c8b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00c4d8ac ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00c4c8c4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00c4d8b8 ["COPY", "tmp:0:8", ["const:e08:8"]]
~~~


### [`00c4cba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md) → [`00c4db94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4db94.md) FUN_00c4db94

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c403a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c403a0.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4dc04",
      "incomplete_value": false,
      "site": "00c4dc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4cc10",
      "incomplete_value": false,
      "site": "00c4cc10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c99300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c9a2d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4cbe0 ["INT_ADD", "register:40f0:8", ["const:c4cbe0:8", "const:4:8"]]
+ 00c4dbd4 ["INT_ADD", "register:40f0:8", ["const:c4dbd4:8", "const:4:8"]]
- 00c4cc08 ["COPY", "register:4048:8", ["const:c99000:8"]]
- 00c4cc0c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00c4dbfc ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00c4dc00 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00c4cc5c ["INT_ADD", "register:40f0:8", ["const:c4cc5c:8", "const:4:8"]]
+ 00c4dc50 ["INT_ADD", "register:40f0:8", ["const:c4dc50:8", "const:4:8"]]
~~~


### [`00c4ce88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md) → [`00c4de7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4d/00c4de7c.md) FUN_00c4de7c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4df14",
      "incomplete_value": true,
      "site": "00c4df24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:303:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4cf20",
      "incomplete_value": true,
      "site": "00c4cf30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
            ]
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
      152,
      "READ",
      [
        "storage",
        "002a5238",
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
        "002a5303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ceb4 ["INT_ADD", "register:40f0:8", ["const:c4ceb4:8", "const:4:8"]]
+ 00c4dea8 ["INT_ADD", "register:40f0:8", ["const:c4dea8:8", "const:4:8"]]
- 00c4ced8 ["INT_ADD", "register:40f0:8", ["const:c4ced8:8", "const:4:8"]]
+ 00c4decc ["INT_ADD", "register:40f0:8", ["const:c4decc:8", "const:4:8"]]
- 00c4cf04 ["INT_ADD", "register:40f0:8", ["const:c4cf04:8", "const:4:8"]]
+ 00c4def8 ["INT_ADD", "register:40f0:8", ["const:c4def8:8", "const:4:8"]]
~~~


### [`00c4d18c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md) → [`00c4e180`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e180.md) FUN_00c4e180

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e1ec",
      "incomplete_value": false,
      "site": "00c4e1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d1f8",
      "incomplete_value": false,
      "site": "00c4d1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d1c0 ["INT_ADD", "register:40f0:8", ["const:c4d1c0:8", "const:4:8"]]
+ 00c4e1b4 ["INT_ADD", "register:40f0:8", ["const:c4e1b4:8", "const:4:8"]]
- 00c4d1e8 ["INT_ADD", "register:40f0:8", ["const:c4d1e8:8", "const:4:8"]]
+ 00c4e1dc ["INT_ADD", "register:40f0:8", ["const:c4e1dc:8", "const:4:8"]]
- 00c4d1ec ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c4d1f0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4e1e0 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c4e1e4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c4d238`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md) → [`00c4e22c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e22c.md) FUN_00c4e22c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e294",
      "incomplete_value": false,
      "site": "00c4e294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d2a0",
      "incomplete_value": false,
      "site": "00c4d2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c994c0",
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
        "00c9a490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
+ 00c4e264 ["INT_ADD", "register:40f0:8", ["const:c4e264:8", "const:4:8"]]
- 00c4d290 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4d294 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00c4e284 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c4e288 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00c4d2dc ["INT_ADD", "register:40f0:8", ["const:c4d2dc:8", "const:4:8"]]
+ 00c4e2d0 ["INT_ADD", "register:40f0:8", ["const:c4e2d0:8", "const:4:8"]]
~~~


### [`00c4d868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md) → [`00c4e85c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4e85c.md) FUN_00c4e85c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e8c0",
      "incomplete_value": true,
      "site": "00c4e8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:efa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d8cc",
      "incomplete_value": true,
      "site": "00c4d8e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e2f:8"
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
      100,
      "READ",
      [
        "storage",
        "002a3e2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002a3efa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d8ac ["INT_ADD", "register:40f0:8", ["const:c4d8ac:8", "const:4:8"]]
+ 00c4e8a0 ["INT_ADD", "register:40f0:8", ["const:c4e8a0:8", "const:4:8"]]
- 00c4d8c4 ["COPY", "tmp:0:8", ["const:e2f:8"]]
+ 00c4e8b8 ["COPY", "tmp:0:8", ["const:efa:8"]]
- 00c4d8f4 ["INT_ADD", "register:40f0:8", ["const:c4d8f4:8", "const:4:8"]]
+ 00c4e8e8 ["INT_ADD", "register:40f0:8", ["const:c4e8e8:8", "const:4:8"]]
~~~


### [`00c4db64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md) → [`00c4eb58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4e/00c4eb58.md) FUN_00c4eb58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ecf0",
      "incomplete_value": true,
      "site": "00c4ecfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dcfc",
      "incomplete_value": true,
      "site": "00c4dd08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
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
      "definition_site": "00c4ed58",
      "incomplete_value": true,
      "site": "00c4ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dd64",
      "incomplete_value": true,
      "site": "00c4dd70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eeb8",
      "incomplete_value": true,
      "site": "00c4eec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dec4",
      "incomplete_value": true,
      "site": "00c4ded4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      408,
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      408,
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "002c0eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4dbb4 ["INT_ADD", "register:40f0:8", ["const:c4dbb4:8", "const:4:8"]]
+ 00c4eba8 ["INT_ADD", "register:40f0:8", ["const:c4eba8:8", "const:4:8"]]
- 00c4dbdc ["INT_ADD", "register:40f0:8", ["const:c4dbdc:8", "const:4:8"]]
+ 00c4ebd0 ["INT_ADD", "register:40f0:8", ["const:c4ebd0:8", "const:4:8"]]
- 00c4dc14 ["INT_ADD", "register:40f0:8", ["const:c4dc14:8", "const:4:8"]]
+ 00c4ec08 ["INT_ADD", "register:40f0:8", ["const:c4ec08:8", "const:4:8"]]
~~~


### [`00c4e0dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md) → [`00c4f0d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f0d0.md) FUN_00c4f0d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 8件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 8件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3de70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3de70.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c590a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f2c8",
      "incomplete_value": false,
      "site": "00c4f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e2d4",
      "incomplete_value": false,
      "site": "00c4e2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      "definition_site": "00c4f2ec",
      "incomplete_value": false,
      "site": "00c4f2ec",
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
            "const:aeb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e2f8",
      "incomplete_value": false,
      "site": "00c4e2f8",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e384",
      "incomplete_value": false,
      "site": "00c4e384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      540,
      "DATA",
      [
        "storage",
        "002a8993",
        null,
        "string"
      ]
    ],
    [
      680,
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      540,
      "DATA",
      [
        "storage",
        "002a8aeb",
        null,
        "string"
      ]
    ],
    [
      680,
      "DATA",
      [
        "storage",
        "00c9a8f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4e1e0 ["INT_ADD", "register:40f0:8", ["const:c4e1e0:8", "const:4:8"]]
+ 00c4f1d4 ["INT_ADD", "register:40f0:8", ["const:c4f1d4:8", "const:4:8"]]
- 00c4e228 ["INT_ADD", "register:40f0:8", ["const:c4e228:8", "const:4:8"]]
+ 00c4f21c ["INT_ADD", "register:40f0:8", ["const:c4f21c:8", "const:4:8"]]
- 00c4e258 ["INT_ADD", "register:40f0:8", ["const:c4e258:8", "const:4:8"]]
+ 00c4f24c ["INT_ADD", "register:40f0:8", ["const:c4f24c:8", "const:4:8"]]
~~~


### [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) → [`00c4f678`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) FUN_00c4f678

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 2件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c4f678`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) · 呼出先 5件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c3f654`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3f/00c3f654.md) [`00c4f678`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4f678.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f870",
      "incomplete_value": false,
      "site": "00c4f870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e87c",
      "incomplete_value": false,
      "site": "00c4e87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f8f8",
      "incomplete_value": false,
      "site": "00c4f8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e904",
      "incomplete_value": false,
      "site": "00c4e904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fa08",
      "incomplete_value": false,
      "site": "00c4fa08",
      "value": [
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
    },
    "old": {
      "definition_site": "00c4ea14",
      "incomplete_value": false,
      "site": "00c4ea14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      504,
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ],
    [
      640,
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ],
    [
      912,
      "DATA",
      [
        "storage",
        "00c99a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c9ab20",
        null,
        "undefined *"
      ]
    ],
    [
      640,
      "DATA",
      [
        "storage",
        "00c9aab0",
        null,
        "undefined *"
      ]
    ],
    [
      912,
      "DATA",
      [
        "storage",
        "00c9aa40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4e7a0 ["INT_ADD", "register:40f0:8", ["const:c4e7a0:8", "const:4:8"]]
+ 00c4f794 ["INT_ADD", "register:40f0:8", ["const:c4f794:8", "const:4:8"]]
- 00c4e81c ["INT_ADD", "register:40f0:8", ["const:c4e81c:8", "const:4:8"]]
+ 00c4f810 ["INT_ADD", "register:40f0:8", ["const:c4f810:8", "const:4:8"]]
- 00c4e844 ["INT_ADD", "register:40f0:8", ["const:c4e844:8", "const:4:8"]]
+ 00c4f838 ["INT_ADD", "register:40f0:8", ["const:c4f838:8", "const:4:8"]]
~~~


### [`00c4ea5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md) → [`00c4fa50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fa50.md) FUN_00c4fa50

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fabc",
      "incomplete_value": false,
      "site": "00c4fabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eac8",
      "incomplete_value": false,
      "site": "00c4eac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ea90 ["INT_ADD", "register:40f0:8", ["const:c4ea90:8", "const:4:8"]]
+ 00c4fa84 ["INT_ADD", "register:40f0:8", ["const:c4fa84:8", "const:4:8"]]
- 00c4eab8 ["INT_ADD", "register:40f0:8", ["const:c4eab8:8", "const:4:8"]]
+ 00c4faac ["INT_ADD", "register:40f0:8", ["const:c4faac:8", "const:4:8"]]
- 00c4eabc ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c4eac0 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4fab0 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c4fab4 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c4eb08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md) → [`00c4fafc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fafc.md) FUN_00c4fafc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fb68",
      "incomplete_value": false,
      "site": "00c4fb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eb74",
      "incomplete_value": false,
      "site": "00c4eb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4eb3c ["INT_ADD", "register:40f0:8", ["const:c4eb3c:8", "const:4:8"]]
+ 00c4fb30 ["INT_ADD", "register:40f0:8", ["const:c4fb30:8", "const:4:8"]]
- 00c4eb64 ["INT_ADD", "register:40f0:8", ["const:c4eb64:8", "const:4:8"]]
+ 00c4fb58 ["INT_ADD", "register:40f0:8", ["const:c4fb58:8", "const:4:8"]]
- 00c4eb68 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c4eb6c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4fb5c ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c4fb60 ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c4ebb4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md) → [`00c4fba8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fba8.md) FUN_00c4fba8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c59080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fc14",
      "incomplete_value": false,
      "site": "00c4fc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ec20",
      "incomplete_value": false,
      "site": "00c4ec20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
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
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ebe8 ["INT_ADD", "register:40f0:8", ["const:c4ebe8:8", "const:4:8"]]
+ 00c4fbdc ["INT_ADD", "register:40f0:8", ["const:c4fbdc:8", "const:4:8"]]
- 00c4ec10 ["INT_ADD", "register:40f0:8", ["const:c4ec10:8", "const:4:8"]]
+ 00c4fc04 ["INT_ADD", "register:40f0:8", ["const:c4fc04:8", "const:4:8"]]
- 00c4ec14 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00c4ec18 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4fc08 ["COPY", "register:4048:8", ["const:c98000:8"]]
+ 00c4fc0c ["COPY", "tmp:0:8", ["const:6e0:8"]]
~~~


### [`00c4ec60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md) → [`00c4fc54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fc54.md) FUN_00c4fc54

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fcbc",
      "incomplete_value": false,
      "site": "00c4fcbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ecc8",
      "incomplete_value": false,
      "site": "00c4ecc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99bc0",
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
        "00c9ab90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ec98 ["INT_ADD", "register:40f0:8", ["const:c4ec98:8", "const:4:8"]]
+ 00c4fc8c ["INT_ADD", "register:40f0:8", ["const:c4fc8c:8", "const:4:8"]]
- 00c4ecb8 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4ecbc ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00c4fcac ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c4fcb0 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00c4ed08 ["INT_ADD", "register:40f0:8", ["const:c4ed08:8", "const:4:8"]]
+ 00c4fcfc ["INT_ADD", "register:40f0:8", ["const:c4fcfc:8", "const:4:8"]]
~~~


### [`00c4ed0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md) → [`00c4fd00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fd00.md) FUN_00c4fd00

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fd64",
      "incomplete_value": false,
      "site": "00c4fd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ed70",
      "incomplete_value": false,
      "site": "00c4ed70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c99c30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c9ac00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ed40 ["INT_ADD", "register:40f0:8", ["const:c4ed40:8", "const:4:8"]]
+ 00c4fd34 ["INT_ADD", "register:40f0:8", ["const:c4fd34:8", "const:4:8"]]
- 00c4ed60 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4ed64 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 00c4fd54 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c4fd58 ["COPY", "tmp:0:8", ["const:c00:8"]]
- 00c4eda8 ["INT_ADD", "register:40f0:8", ["const:c4eda8:8", "const:4:8"]]
+ 00c4fd9c ["INT_ADD", "register:40f0:8", ["const:c4fd9c:8", "const:4:8"]]
~~~


### [`00c4edac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md) → [`00c4fda0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fda0.md) FUN_00c4fda0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fe08",
      "incomplete_value": false,
      "site": "00c4fe08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ee14",
      "incomplete_value": false,
      "site": "00c4ee14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99ca0",
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
        "00c9ac70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ede4 ["INT_ADD", "register:40f0:8", ["const:c4ede4:8", "const:4:8"]]
+ 00c4fdd8 ["INT_ADD", "register:40f0:8", ["const:c4fdd8:8", "const:4:8"]]
- 00c4ee04 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4ee08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c4fdf8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c4fdfc ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00c4ee54 ["INT_ADD", "register:40f0:8", ["const:c4ee54:8", "const:4:8"]]
+ 00c4fe48 ["INT_ADD", "register:40f0:8", ["const:c4fe48:8", "const:4:8"]]
~~~


### [`00c4ee58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md) → [`00c4fe4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fe4c.md) FUN_00c4fe4c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4feb4",
      "incomplete_value": false,
      "site": "00c4feb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eec0",
      "incomplete_value": false,
      "site": "00c4eec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99d10",
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
        "00c9ace0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ee90 ["INT_ADD", "register:40f0:8", ["const:c4ee90:8", "const:4:8"]]
+ 00c4fe84 ["INT_ADD", "register:40f0:8", ["const:c4fe84:8", "const:4:8"]]
- 00c4eeb0 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4eeb4 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c4fea4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c4fea8 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00c4ef00 ["INT_ADD", "register:40f0:8", ["const:c4ef00:8", "const:4:8"]]
+ 00c4fef4 ["INT_ADD", "register:40f0:8", ["const:c4fef4:8", "const:4:8"]]
~~~


### [`00c4ef04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) → [`00c4fef8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c4f/00c4fef8.md) FUN_00c4fef8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 6件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c508cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) [`00c5096c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 6件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) [`00c40e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c40/00c40e0c.md) [`00c518c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c518c0.md) [`00c51960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51960.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fff4",
      "incomplete_value": false,
      "site": "00c4fff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f000",
      "incomplete_value": false,
      "site": "00c4f000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c500d0",
      "incomplete_value": false,
      "site": "00c500d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "definition_site": "00c5016c",
      "incomplete_value": false,
      "site": "00c5016c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f178",
      "incomplete_value": false,
      "site": "00c4f178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      252,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      472,
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ],
    [
      628,
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      252,
      "DATA",
      [
        "storage",
        "00c986e0",
        null,
        "undefined *"
      ]
    ],
    [
      472,
      "DATA",
      [
        "storage",
        "00c9adc0",
        null,
        "undefined *"
      ]
    ],
    [
      628,
      "DATA",
      [
        "storage",
        "00c9adc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4efc8 ["INT_ADD", "register:40f0:8", ["const:c4efc8:8", "const:4:8"]]
+ 00c4ffbc ["INT_ADD", "register:40f0:8", ["const:c4ffbc:8", "const:4:8"]]
- 00c4eff8 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c4effc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4ffec ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4fff0 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00c4f06c ["INT_ADD", "register:40f0:8", ["const:c4f06c:8", "const:4:8"]]
+ 00c50060 ["INT_ADD", "register:40f0:8", ["const:c50060:8", "const:4:8"]]
~~~


### [`00c4f1c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md) → [`00c501b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c501b4.md) FUN_00c501b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 3件 [`00c3d29c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3d/00c3d29c.md) [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c502c0",
      "incomplete_value": false,
      "site": "00c502c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f2cc",
      "incomplete_value": false,
      "site": "00c4f2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      268,
      "DATA",
      [
        "storage",
        "00c99f40",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002b367d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c9af10",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002b36c7",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f238 ["COPY", "tmp:0:8", ["const:67d:8"]]
+ 00c5022c ["COPY", "tmp:0:8", ["const:6c7:8"]]
- 00c4f248 ["COPY", "tmp:0:8", ["const:c5e:8"]]
+ 00c5023c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00c4f258 ["COPY", "tmp:0:8", ["const:7eb:8"]]
+ 00c5024c ["COPY", "tmp:0:8", ["const:8b8:8"]]
~~~


### [`00c4f310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md) → [`00c50304`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50304.md) FUN_00c50304

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5036c",
      "incomplete_value": false,
      "site": "00c5036c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99fb0",
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
        "00c9af80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f344 ["INT_ADD", "register:40f0:8", ["const:c4f344:8", "const:4:8"]]
+ 00c50338 ["INT_ADD", "register:40f0:8", ["const:c50338:8", "const:4:8"]]
- 00c4f36c ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4f370 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00c50360 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c50364 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 00c4f3b8 ["INT_ADD", "register:40f0:8", ["const:c4f3b8:8", "const:4:8"]]
+ 00c503ac ["INT_ADD", "register:40f0:8", ["const:c503ac:8", "const:4:8"]]
~~~


### [`00c4f3bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md) → [`00c503b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c503b0.md) FUN_00c503b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50424",
      "incomplete_value": false,
      "site": "00c50424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f430",
      "incomplete_value": false,
      "site": "00c4f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c9a020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c9aff0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f3f4 ["INT_ADD", "register:40f0:8", ["const:c4f3f4:8", "const:4:8"]]
+ 00c503e8 ["INT_ADD", "register:40f0:8", ["const:c503e8:8", "const:4:8"]]
- 00c4f420 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00c50414 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00c4f474 ["INT_ADD", "register:40f0:8", ["const:c4f474:8", "const:4:8"]]
+ 00c50468 ["INT_ADD", "register:40f0:8", ["const:c50468:8", "const:4:8"]]
~~~


### [`00c4f478`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md) → [`00c5046c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5046c.md) FUN_00c5046c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c504d0",
      "incomplete_value": false,
      "site": "00c504d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f4dc",
      "incomplete_value": false,
      "site": "00c4f4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00c504f0",
      "incomplete_value": false,
      "site": "00c504f0",
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
            "const:667:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f4fc",
      "incomplete_value": false,
      "site": "00c4f4fc",
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
            "const:50f:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "002a750f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c9ace0",
        null,
        "undefined *"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "002a7667",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f4ac ["INT_ADD", "register:40f0:8", ["const:c4f4ac:8", "const:4:8"]]
+ 00c504a0 ["INT_ADD", "register:40f0:8", ["const:c504a0:8", "const:4:8"]]
- 00c4f4cc ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4f4d0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c504c0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c504c4 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00c4f4f4 ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 00c504e8 ["COPY", "tmp:0:8", ["const:667:8"]]
~~~


### [`00c4f528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md) → [`00c5051c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c5051c.md) FUN_00c5051c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)
- 新版 呼出元 1件 [`00c3bd5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c3b/00c3bd5c.md) · 呼出先 2件 [`00c590c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5b0c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0c0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50580",
      "incomplete_value": false,
      "site": "00c50580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f58c",
      "incomplete_value": false,
      "site": "00c4f58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00c505a0",
      "incomplete_value": false,
      "site": "00c505a0",
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
            "const:ef9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f5ac",
      "incomplete_value": false,
      "site": "00c4f5ac",
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
            "const:eb9:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "002a0eb9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c9ace0",
        null,
        "undefined *"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "002a0ef9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f55c ["INT_ADD", "register:40f0:8", ["const:c4f55c:8", "const:4:8"]]
+ 00c50550 ["INT_ADD", "register:40f0:8", ["const:c50550:8", "const:4:8"]]
- 00c4f57c ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00c4f580 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c50570 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c50574 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00c4f5a4 ["COPY", "tmp:0:8", ["const:eb9:8"]]
+ 00c50598 ["COPY", "tmp:0:8", ["const:ef9:8"]]
~~~


### [`00c4fa3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md) → [`00c50a30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c50/00c50a30.md) FUN_00c50a30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c461d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c46/00c461d4.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50bc0",
      "incomplete_value": true,
      "site": "00c50bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fbcc",
      "incomplete_value": true,
      "site": "00c4fbd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
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
      "definition_site": "00c50c28",
      "incomplete_value": true,
      "site": "00c50c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fc34",
      "incomplete_value": true,
      "site": "00c4fc40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      400,
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      504,
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      400,
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      504,
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4fa88 ["INT_ADD", "register:40f0:8", ["const:c4fa88:8", "const:4:8"]]
+ 00c50a7c ["INT_ADD", "register:40f0:8", ["const:c50a7c:8", "const:4:8"]]
- 00c4fab0 ["INT_ADD", "register:40f0:8", ["const:c4fab0:8", "const:4:8"]]
+ 00c50aa4 ["INT_ADD", "register:40f0:8", ["const:c50aa4:8", "const:4:8"]]
- 00c4fae8 ["INT_ADD", "register:40f0:8", ["const:c4fae8:8", "const:4:8"]]
+ 00c50adc ["INT_ADD", "register:40f0:8", ["const:c50adc:8", "const:4:8"]]
~~~


### [`00c50150`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md) → [`00c51144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c51/00c51144.md) FUN_00c51144

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5121c",
      "incomplete_value": true,
      "site": "00c51228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:737:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50228",
      "incomplete_value": true,
      "site": "00c50234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
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
      "definition_site": "00c51284",
      "incomplete_value": true,
      "site": "00c51290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50290",
      "incomplete_value": true,
      "site": "00c5029c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
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
      216,
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      216,
      "READ",
      [
        "storage",
        "002bd737",
        null,
        "string"
      ]
    ],
    [
      320,
      "READ",
      [
        "storage",
        "002beb8d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c50174 ["INT_ADD", "register:40f0:8", ["const:c50174:8", "const:4:8"]]
+ 00c51168 ["INT_ADD", "register:40f0:8", ["const:c51168:8", "const:4:8"]]
- 00c501a8 ["INT_ADD", "register:40f0:8", ["const:c501a8:8", "const:4:8"]]
+ 00c5119c ["INT_ADD", "register:40f0:8", ["const:c5119c:8", "const:4:8"]]
- 00c5020c ["INT_ADD", "register:40f0:8", ["const:c5020c:8", "const:4:8"]]
+ 00c51200 ["INT_ADD", "register:40f0:8", ["const:c51200:8", "const:4:8"]]
~~~


