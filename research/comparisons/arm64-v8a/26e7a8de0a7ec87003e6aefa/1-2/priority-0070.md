# v16.0.2 → v16.0.3 · 最優先の変更候補 (70)

[一覧の目次](README.md)

### [`009fdbb8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdbb8.md) → [`009feb64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009feb64.md) FUN_009feb64

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
      "definition_site": "009feb70",
      "incomplete_value": true,
      "site": "009feb70",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdbc4",
      "incomplete_value": true,
      "site": "009fdbc4",
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
            "const:770:8"
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
        "00c8a770",
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
        "00c8b740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fdbbc ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009fdbc0 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 009feb68 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 009feb6c ["COPY", "tmp:0:8", ["const:740:8"]]
~~~


### [`009fdbd4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdbd4.md) → [`009feb80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009feb80.md) FUN_009feb80

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "009feba0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdbf4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "009febac",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdc00",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
        "0047ad34"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fdbf4 ["INT_ADD", "register:40f0:8", ["const:9fdbf4:8", "const:4:8"]]
- 009fdbf4 ["CALL", null, ["ram:47ad34:8"]]
+ 009feba0 ["INT_ADD", "register:40f0:8", ["const:9feba0:8", "const:4:8"]]
+ 009feba0 ["CALL", null, ["ram:47b054:8"]]
- 009fdc00 ["INT_ADD", "register:40f0:8", ["const:9fdc00:8", "const:4:8"]]
- 009fdc00 ["CALL", null, ["ram:47ad34:8"]]
+ 009febac ["INT_ADD", "register:40f0:8", ["const:9febac:8", "const:4:8"]]
+ 009febac ["CALL", null, ["ram:47b054:8"]]
~~~


### [`009fdc54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdc54.md) → [`009fec00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009fec00.md) FUN_009fec00

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009fec24",
      "incomplete_value": false,
      "site": "009fec24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdc78",
      "incomplete_value": false,
      "site": "009fdc78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
        "00c8a7f0",
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
        "00c8b7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fdc68 ["INT_ADD", "register:40f0:8", ["const:9fdc68:8", "const:4:8"]]
+ 009fec14 ["INT_ADD", "register:40f0:8", ["const:9fec14:8", "const:4:8"]]
- 009fdc70 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009fdc74 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 009fec1c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 009fec20 ["COPY", "tmp:0:8", ["const:7c0:8"]]
~~~


### [`009fdc88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdc88.md) → [`009fec34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009fec34.md) FUN_009fec34

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
      "definition_site": "009fec40",
      "incomplete_value": false,
      "site": "009fec40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fdc94",
      "incomplete_value": false,
      "site": "009fdc94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
        "00c8a7f0",
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
        "00c8b7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fdc8c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 009fdc90 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 009fec38 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 009fec3c ["COPY", "tmp:0:8", ["const:7c0:8"]]
~~~


### [`009fdca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdca4.md) → [`009fec50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fe/009fec50.md) FUN_009fec50

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`009fbbcc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fb/009fbbcc.md)

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
      "site": "009fec70",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdcc4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "009fec7c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "009fdcd0",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
        "0047ad34"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fdcc4 ["INT_ADD", "register:40f0:8", ["const:9fdcc4:8", "const:4:8"]]
- 009fdcc4 ["CALL", null, ["ram:47ad34:8"]]
+ 009fec70 ["INT_ADD", "register:40f0:8", ["const:9fec70:8", "const:4:8"]]
+ 009fec70 ["CALL", null, ["ram:47b054:8"]]
- 009fdcd0 ["INT_ADD", "register:40f0:8", ["const:9fdcd0:8", "const:4:8"]]
- 009fdcd0 ["CALL", null, ["ram:47ad34:8"]]
+ 009fec7c ["INT_ADD", "register:40f0:8", ["const:9fec7c:8", "const:4:8"]]
+ 009fec7c ["CALL", null, ["ram:47b054:8"]]
~~~


### [`009ff20c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff20c.md) → [`00a001b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a001b8.md) FUN_00a001b8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a001c4",
      "incomplete_value": false,
      "site": "00a001d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff218",
      "incomplete_value": false,
      "site": "009ff224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      24,
      "DATA",
      [
        "storage",
        "00c8a870",
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
        "00c8b840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ff214 ["COPY", "register:4050:8", ["const:c8a000:8"]]
- 009ff218 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00a001c0 ["COPY", "register:4050:8", ["const:c8b000:8"]]
+ 00a001c4 ["COPY", "tmp:0:8", ["const:840:8"]]
~~~


### [`009ff250`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff250.md) → [`00a001fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a001fc.md) FUN_00a001fc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a00214",
      "incomplete_value": false,
      "site": "00a00220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff268",
      "incomplete_value": false,
      "site": "009ff274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
        "00c8a870",
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
        "00c8b840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ff264 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ff268 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00a00210 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a00214 ["COPY", "tmp:0:8", ["const:840:8"]]
- 009ff298 ["INT_ADD", "register:40f0:8", ["const:9ff298:8", "const:4:8"]]
+ 00a00244 ["INT_ADD", "register:40f0:8", ["const:a00244:8", "const:4:8"]]
~~~


### [`009ff2ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff2ac.md) → [`00a00258`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00258.md) FUN_00a00258

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a00274",
      "incomplete_value": false,
      "site": "00a00284",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff2c8",
      "incomplete_value": false,
      "site": "009ff2d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      44,
      "DATA",
      [
        "storage",
        "00c8a870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "00c8b840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ff2c0 ["INT_ADD", "register:40f0:8", ["const:9ff2c0:8", "const:4:8"]]
+ 00a0026c ["INT_ADD", "register:40f0:8", ["const:a0026c:8", "const:4:8"]]
- 009ff2c4 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ff2c8 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00a00270 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a00274 ["COPY", "tmp:0:8", ["const:840:8"]]
- 009ff300 ["INT_ADD", "register:40f0:8", ["const:9ff300:8", "const:4:8"]]
+ 00a002ac ["INT_ADD", "register:40f0:8", ["const:a002ac:8", "const:4:8"]]
~~~


### [`009ff34c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff34c.md) → [`00a002f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a002f8.md) FUN_00a002f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a00308",
      "incomplete_value": false,
      "site": "00a00310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff35c",
      "incomplete_value": false,
      "site": "009ff364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      24,
      "DATA",
      [
        "storage",
        "00c8a870",
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
        "00c8b840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ff358 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ff35c ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00a00304 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a00308 ["COPY", "tmp:0:8", ["const:840:8"]]
- 009ff398 ["INT_ADD", "register:40f0:8", ["const:9ff398:8", "const:4:8"]]
+ 00a00344 ["INT_ADD", "register:40f0:8", ["const:a00344:8", "const:4:8"]]
- 009ff3c0 ["INT_ADD", "register:40f0:8", ["const:9ff3c0:8", "const:4:8"]]
+ 00a0036c ["INT_ADD", "register:40f0:8", ["const:a0036c:8", "const:4:8"]]
~~~


### [`009ff460`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff460.md) → [`00a0040c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a0040c.md) FUN_00a0040c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 27件 [`0046d4d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046db34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 27件 [`0046d7f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0046de54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046de54.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 4件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a00588",
      "incomplete_value": true,
      "site": "00a00598",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:fa2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff5dc",
      "incomplete_value": true,
      "site": "009ff5ec",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:ec4:8"
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
      "definition_site": "00a0059c",
      "incomplete_value": true,
      "site": "00a0059c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009ff5f0",
      "incomplete_value": true,
      "site": "009ff5f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a00590",
      "incomplete_value": true,
      "site": "00a005a0",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ff5e4",
      "incomplete_value": true,
      "site": "009ff5f4",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      120,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      380,
      "READ",
      [
        "storage",
        "002bcec4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      120,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      380,
      "READ",
      [
        "storage",
        "002bcfa2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ff4b0 ["INT_ADD", "register:40f0:8", ["const:9ff4b0:8", "const:4:8"]]
- 009ff4b0 ["CALL", null, ["ram:47ad34:8"]]
+ 00a0045c ["INT_ADD", "register:40f0:8", ["const:a0045c:8", "const:4:8"]]
+ 00a0045c ["CALL", null, ["ram:47b054:8"]]
- 009ff4d8 ["INT_ADD", "register:40f0:8", ["const:9ff4d8:8", "const:4:8"]]
- 009ff4d8 ["CALL", null, ["ram:47ad34:8"]]
+ 00a00484 ["INT_ADD", "register:40f0:8", ["const:a00484:8", "const:4:8"]]
+ 00a00484 ["CALL", null, ["ram:47b054:8"]]
- 009ff52c ["INT_ADD", "register:40f0:8", ["const:9ff52c:8", "const:4:8"]]
+ 00a004d8 ["INT_ADD", "register:40f0:8", ["const:a004d8:8", "const:4:8"]]
~~~


### [`009ffe08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffe08.md) → [`00a00db4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00db4.md) FUN_00a00db4

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
      "definition_site": "00a00dc0",
      "incomplete_value": false,
      "site": "00a00dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ffe14",
      "incomplete_value": false,
      "site": "009ffe20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      24,
      "DATA",
      [
        "storage",
        "00c8a8e0",
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
        "00c8b8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ffe10 ["COPY", "register:4050:8", ["const:c8a000:8"]]
- 009ffe14 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00a00dbc ["COPY", "register:4050:8", ["const:c8b000:8"]]
+ 00a00dc0 ["COPY", "tmp:0:8", ["const:8b0:8"]]
~~~


### [`009ffea8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffea8.md) → [`00a00e54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00e54.md) FUN_00a00e54

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a00e80",
      "incomplete_value": false,
      "site": "00a00e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009ffed4",
      "incomplete_value": false,
      "site": "009ffed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      44,
      "DATA",
      [
        "storage",
        "00c8a8e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "00c8b8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009ffebc ["INT_ADD", "register:40f0:8", ["const:9ffebc:8", "const:4:8"]]
+ 00a00e68 ["INT_ADD", "register:40f0:8", ["const:a00e68:8", "const:4:8"]]
- 009ffec8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009ffecc ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00a00e74 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a00e78 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 009ffef0 ["INT_ADD", "register:40f0:8", ["const:9ffef0:8", "const:4:8"]]
+ 00a00e9c ["INT_ADD", "register:40f0:8", ["const:a00e9c:8", "const:4:8"]]
~~~


### [`009fff40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009fff40.md) → [`00a00eec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00eec.md) FUN_00a00eec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a00f0c",
      "incomplete_value": false,
      "site": "00a00f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009fff60",
      "incomplete_value": false,
      "site": "009fff60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
        "00c8a8e0",
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
        "00c8b8b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009fff58 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 009fff5c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00a00f04 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a00f08 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 009fff7c ["INT_ADD", "register:40f0:8", ["const:9fff7c:8", "const:4:8"]]
+ 00a00f28 ["INT_ADD", "register:40f0:8", ["const:a00f28:8", "const:4:8"]]
- 009fffa0 ["INT_ADD", "register:40f0:8", ["const:9fffa0:8", "const:4:8"]]
+ 00a00f4c ["INT_ADD", "register:40f0:8", ["const:a00f4c:8", "const:4:8"]]
~~~


### [`00a00048`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00048.md) → [`00a00ff4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a00/00a00ff4.md) FUN_00a00ff4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459db4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0045a0d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00a01034",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00088",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00088 ["INT_ADD", "register:40f0:8", ["const:a00088:8", "const:4:8"]]
- 00a00088 ["CALL", null, ["ram:47ad34:8"]]
+ 00a01034 ["INT_ADD", "register:40f0:8", ["const:a01034:8", "const:4:8"]]
+ 00a01034 ["CALL", null, ["ram:47b054:8"]]
- 00a00094 ["INT_ADD", "register:40f0:8", ["const:a00094:8", "const:4:8"]]
+ 00a01040 ["INT_ADD", "register:40f0:8", ["const:a01040:8", "const:4:8"]]
- 00a000f0 ["INT_ADD", "register:40f0:8", ["const:a000f0:8", "const:4:8"]]
+ 00a0109c ["INT_ADD", "register:40f0:8", ["const:a0109c:8", "const:4:8"]]
~~~


### [`00a00190`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00190.md) → [`00a0113c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0113c.md) FUN_00a0113c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01164",
      "incomplete_value": false,
      "site": "00a01164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a001b8",
      "incomplete_value": false,
      "site": "00a001b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      40,
      "DATA",
      [
        "storage",
        "00c8a960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c8b930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a001a4 ["INT_ADD", "register:40f0:8", ["const:a001a4:8", "const:4:8"]]
+ 00a01150 ["INT_ADD", "register:40f0:8", ["const:a01150:8", "const:4:8"]]
- 00a001b0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a001b4 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00a0115c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a01160 ["COPY", "tmp:0:8", ["const:930:8"]]
~~~


### [`00a001cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001cc.md) → [`00a01178`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a01178.md) FUN_00a01178

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
      "definition_site": "00a0117c",
      "incomplete_value": false,
      "site": "00a01180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a001d0",
      "incomplete_value": false,
      "site": "00a001d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
        "00c8a960",
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
        "00c8b930",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a001cc ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a001d0 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00a01178 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a0117c ["COPY", "tmp:0:8", ["const:930:8"]]
~~~


### [`00a00390`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00390.md) → [`00a0133c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0133c.md) FUN_00a0133c

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
      "definition_site": "00a01340",
      "incomplete_value": false,
      "site": "00a01344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00394",
      "incomplete_value": false,
      "site": "00a00398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
        "00c8a9f0",
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
        "00c8b9c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00390 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a00394 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 00a0133c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a01340 ["COPY", "tmp:0:8", ["const:9c0:8"]]
~~~


### [`00a003b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a003b0.md) → [`00a0135c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0135c.md) FUN_00a0135c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0046ca04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`006648e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00859ba4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ba4.md) [`008b6ab4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0046cd24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00664c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c90.md) [`008524fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`0085ab50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0085a/0085ab50.md) [`008b7a60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7a60.md)

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
      "site": "00a014f8",
      "value": [
        "leaf",
        "ram:664c90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0054c",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      412,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ]
  ],
  "added": [
    [
      412,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664c90"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a003e8 ["INT_ADD", "register:40f0:8", ["const:a003e8:8", "const:4:8"]]
+ 00a01394 ["INT_ADD", "register:40f0:8", ["const:a01394:8", "const:4:8"]]
- 00a00414 ["INT_ADD", "register:40f0:8", ["const:a00414:8", "const:4:8"]]
+ 00a013c0 ["INT_ADD", "register:40f0:8", ["const:a013c0:8", "const:4:8"]]
- 00a00420 ["INT_ADD", "register:40f0:8", ["const:a00420:8", "const:4:8"]]
+ 00a013cc ["INT_ADD", "register:40f0:8", ["const:a013cc:8", "const:4:8"]]
~~~


### [`00a00778`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00778.md) → [`00a01724`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a01724.md) FUN_00a01724

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01744",
      "incomplete_value": false,
      "site": "00a01748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00798",
      "incomplete_value": false,
      "site": "00a0079c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
        "00c8aa70",
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
        "00c8ba40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0078c ["INT_ADD", "register:40f0:8", ["const:a0078c:8", "const:4:8"]]
+ 00a01738 ["INT_ADD", "register:40f0:8", ["const:a01738:8", "const:4:8"]]
- 00a00794 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a00798 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a01740 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a01744 ["COPY", "tmp:0:8", ["const:a40:8"]]
~~~


### [`00a007b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a007b0.md) → [`00a0175c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0175c.md) FUN_00a0175c

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
      "definition_site": "00a01760",
      "incomplete_value": false,
      "site": "00a01764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a007b4",
      "incomplete_value": false,
      "site": "00a007b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
        "00c8aa70",
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
        "00c8ba40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a007b0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a007b4 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00a0175c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a01760 ["COPY", "tmp:0:8", ["const:a40:8"]]
~~~


### [`00a007d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a007d0.md) → [`00a0177c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a0177c.md) FUN_00a0177c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00467ba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00468fc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md) [`00469c44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046af58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046a/0046af58.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00467ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`004692e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`004699bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004699bc.md) [`00469f64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046b278`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046b/0046b278.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a017e0",
      "incomplete_value": true,
      "site": "00a017e0",
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
      "definition_site": "00a00834",
      "incomplete_value": true,
      "site": "00a00834",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a01820",
      "incomplete_value": true,
      "site": "00a01820",
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
      "definition_site": "00a00874",
      "incomplete_value": true,
      "site": "00a00874",
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a017e8",
      "incomplete_value": false,
      "site": "00a017f8",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0083c",
      "incomplete_value": false,
      "site": "00a0084c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      96,
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      96,
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "00c72a30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00810 ["INT_ADD", "register:40f0:8", ["const:a00810:8", "const:4:8"]]
+ 00a017bc ["INT_ADD", "register:40f0:8", ["const:a017bc:8", "const:4:8"]]
- 00a00820 ["INT_ADD", "register:40f0:8", ["const:a00820:8", "const:4:8"]]
+ 00a017cc ["INT_ADD", "register:40f0:8", ["const:a017cc:8", "const:4:8"]]
- 00a0082c ["COPY", "register:40b0:8", ["const:ca4000:8"]]
- 00a00830 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
+ 00a017d8 ["COPY", "register:40b0:8", ["const:ca5000:8"]]
+ 00a017dc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a38:8"]]
~~~


### [`00a00ea0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ea0.md) → [`00a01e4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a01e4c.md) FUN_00a01e4c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a01e70",
      "incomplete_value": false,
      "site": "00a01e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00ec4",
      "incomplete_value": false,
      "site": "00a00ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
        "00c8aaf0",
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
        "00c8bac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00eb4 ["INT_ADD", "register:40f0:8", ["const:a00eb4:8", "const:4:8"]]
+ 00a01e60 ["INT_ADD", "register:40f0:8", ["const:a01e60:8", "const:4:8"]]
- 00a00ebc ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a00ec0 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00a01e68 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a01e6c ["COPY", "tmp:0:8", ["const:ac0:8"]]
~~~


### [`00a00ed4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ed4.md) → [`00a01e80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a01e80.md) FUN_00a01e80

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
      "definition_site": "00a01e8c",
      "incomplete_value": false,
      "site": "00a01e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a00ee0",
      "incomplete_value": false,
      "site": "00a00ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
        "00c8aaf0",
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
        "00c8bac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00ed8 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a00edc ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00a01e84 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a01e88 ["COPY", "tmp:0:8", ["const:ac0:8"]]
~~~


### [`00a00ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a00ef0.md) → [`00a01e9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a01/00a01e9c.md) FUN_00a01e9c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006648e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00664/006648e0.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)
- 新版 呼出元 0件  · 呼出先 21件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`00664c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00664/00664c90.md) [`008524fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b7ea8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ea8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01eec",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00f40",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01f08",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a00f5c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02044",
      "value": [
        "leaf",
        "ram:664c90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01098",
      "value": [
        "leaf",
        "ram:6648e0:8"
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      108,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      424,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006648e0"
      ]
    ]
  ],
  "added": [
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      108,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      424,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00664c90"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a00f24 ["INT_ADD", "register:40f0:8", ["const:a00f24:8", "const:4:8"]]
+ 00a01ed0 ["INT_ADD", "register:40f0:8", ["const:a01ed0:8", "const:4:8"]]
- 00a00f40 ["INT_ADD", "register:40f0:8", ["const:a00f40:8", "const:4:8"]]
- 00a00f40 ["CALL", null, ["ram:47ad34:8"]]
+ 00a01eec ["INT_ADD", "register:40f0:8", ["const:a01eec:8", "const:4:8"]]
+ 00a01eec ["CALL", null, ["ram:47b054:8"]]
- 00a00f5c ["INT_ADD", "register:40f0:8", ["const:a00f5c:8", "const:4:8"]]
- 00a00f5c ["CALL", null, ["ram:47ad34:8"]]
+ 00a01f08 ["INT_ADD", "register:40f0:8", ["const:a01f08:8", "const:4:8"]]
+ 00a01f08 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a01204`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01204.md) → [`00a021b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a021b0.md) FUN_00a021b0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a021d4",
      "incomplete_value": false,
      "site": "00a021d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01228",
      "incomplete_value": false,
      "site": "00a01228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
        "00c8ab70",
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
        "00c8bb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a01218 ["INT_ADD", "register:40f0:8", ["const:a01218:8", "const:4:8"]]
+ 00a021c4 ["INT_ADD", "register:40f0:8", ["const:a021c4:8", "const:4:8"]]
- 00a01220 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a01224 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00a021cc ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a021d0 ["COPY", "tmp:0:8", ["const:b40:8"]]
~~~


### [`00a01238`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01238.md) → [`00a021e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a021e4.md) FUN_00a021e4

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
      "definition_site": "00a021f0",
      "incomplete_value": false,
      "site": "00a021f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01244",
      "incomplete_value": false,
      "site": "00a01244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
        "00c8ab70",
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
        "00c8bb40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0123c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a01240 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00a021e8 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a021ec ["COPY", "tmp:0:8", ["const:b40:8"]]
~~~


### [`00a01254`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01254.md) → [`00a02200`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a02200.md) FUN_00a02200

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00a02238",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0128c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02250",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a012a4",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a01270 ["INT_ADD", "register:40f0:8", ["const:a01270:8", "const:4:8"]]
+ 00a0221c ["INT_ADD", "register:40f0:8", ["const:a0221c:8", "const:4:8"]]
- 00a0128c ["INT_ADD", "register:40f0:8", ["const:a0128c:8", "const:4:8"]]
- 00a0128c ["CALL", null, ["ram:47ad34:8"]]
+ 00a02238 ["INT_ADD", "register:40f0:8", ["const:a02238:8", "const:4:8"]]
+ 00a02238 ["CALL", null, ["ram:47b054:8"]]
- 00a012a4 ["INT_ADD", "register:40f0:8", ["const:a012a4:8", "const:4:8"]]
- 00a012a4 ["CALL", null, ["ram:47ad34:8"]]
+ 00a02250 ["INT_ADD", "register:40f0:8", ["const:a02250:8", "const:4:8"]]
+ 00a02250 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a012f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a012f8.md) → [`00a022a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a022a4.md) FUN_00a022a4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a022c8",
      "incomplete_value": false,
      "site": "00a022c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0131c",
      "incomplete_value": false,
      "site": "00a0131c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
        "00c8abf0",
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
        "00c8bbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0130c ["INT_ADD", "register:40f0:8", ["const:a0130c:8", "const:4:8"]]
+ 00a022b8 ["INT_ADD", "register:40f0:8", ["const:a022b8:8", "const:4:8"]]
- 00a01314 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a01318 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00a022c0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a022c4 ["COPY", "tmp:0:8", ["const:bc0:8"]]
~~~


### [`00a0132c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a0132c.md) → [`00a022d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a022d8.md) FUN_00a022d8

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
      "definition_site": "00a022e4",
      "incomplete_value": false,
      "site": "00a022e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01338",
      "incomplete_value": false,
      "site": "00a01338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
        "00c8abf0",
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
        "00c8bbc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a01330 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a01334 ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00a022dc ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a022e0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
~~~


### [`00a01348`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01348.md) → [`00a022f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a022f4.md) FUN_00a022f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`009fbbcc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fb/009fbbcc.md)

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
      "site": "00a02314",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01368",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00a02320",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a01374",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
        "0047ad34"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a01368 ["INT_ADD", "register:40f0:8", ["const:a01368:8", "const:4:8"]]
- 00a01368 ["CALL", null, ["ram:47ad34:8"]]
+ 00a02314 ["INT_ADD", "register:40f0:8", ["const:a02314:8", "const:4:8"]]
+ 00a02314 ["CALL", null, ["ram:47b054:8"]]
- 00a01374 ["INT_ADD", "register:40f0:8", ["const:a01374:8", "const:4:8"]]
- 00a01374 ["CALL", null, ["ram:47ad34:8"]]
+ 00a02320 ["INT_ADD", "register:40f0:8", ["const:a02320:8", "const:4:8"]]
+ 00a02320 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a013c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a013c8.md) → [`00a02374`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a02374.md) FUN_00a02374

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a02388",
      "incomplete_value": false,
      "site": "00a0238c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a013dc",
      "incomplete_value": false,
      "site": "00a013e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
        "00c8ac70",
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
        "00c8bc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a013d4 ["INT_ADD", "register:40f0:8", ["const:a013d4:8", "const:4:8"]]
+ 00a02380 ["INT_ADD", "register:40f0:8", ["const:a02380:8", "const:4:8"]]
- 00a013d8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a013dc ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00a02384 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a02388 ["COPY", "tmp:0:8", ["const:c40:8"]]
~~~


### [`00a013ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a013ec.md) → [`00a02398`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a02398.md) FUN_00a02398

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
      "definition_site": "00a0239c",
      "incomplete_value": false,
      "site": "00a023a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a013f0",
      "incomplete_value": false,
      "site": "00a013f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
        "00c8ac70",
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
        "00c8bc40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a013ec ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a013f0 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00a02398 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a0239c ["COPY", "tmp:0:8", ["const:c40:8"]]
~~~


### [`00a01404`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a01404.md) → [`00a023b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a023b0.md) FUN_00a023b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008524fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008b894c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b8/008b894c.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00a023d8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0142c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0142c ["INT_ADD", "register:40f0:8", ["const:a0142c:8", "const:4:8"]]
- 00a0142c ["CALL", null, ["ram:47ad34:8"]]
+ 00a023d8 ["INT_ADD", "register:40f0:8", ["const:a023d8:8", "const:4:8"]]
+ 00a023d8 ["CALL", null, ["ram:47b054:8"]]
- 00a01438 ["INT_ADD", "register:40f0:8", ["const:a01438:8", "const:4:8"]]
+ 00a023e4 ["INT_ADD", "register:40f0:8", ["const:a023e4:8", "const:4:8"]]
- 00a01454 ["INT_ADD", "register:40f0:8", ["const:a01454:8", "const:4:8"]]
+ 00a02400 ["INT_ADD", "register:40f0:8", ["const:a02400:8", "const:4:8"]]
~~~


### [`00a014dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a014dc.md) → [`00a02488`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a02488.md) FUN_00a02488

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a024ac",
      "incomplete_value": true,
      "site": "00a024b0",
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
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01500",
      "incomplete_value": true,
      "site": "00a01504",
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
            "const:cf0:8"
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
      40,
      "DATA",
      [
        "storage",
        "00c8acf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c8bcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a014f0 ["INT_ADD", "register:40f0:8", ["const:a014f0:8", "const:4:8"]]
+ 00a0249c ["INT_ADD", "register:40f0:8", ["const:a0249c:8", "const:4:8"]]
- 00a014fc ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a01500 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00a024a8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a024ac ["COPY", "tmp:0:8", ["const:cc0:8"]]
~~~


### [`00a0151c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a01/00a0151c.md) → [`00a024c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a02/00a024c8.md) FUN_00a024c8

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
      "definition_site": "00a024cc",
      "incomplete_value": false,
      "site": "00a024d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a01520",
      "incomplete_value": false,
      "site": "00a01524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
        "00c8acf0",
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
        "00c8bcc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0151c ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a01520 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00a024c8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a024cc ["COPY", "tmp:0:8", ["const:cc0:8"]]
~~~


### [`00a022d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a022d4.md) → [`00a03280`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03280.md) FUN_00a03280

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a032a0",
      "incomplete_value": false,
      "site": "00a032a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a022f4",
      "incomplete_value": false,
      "site": "00a022f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
        "00c8ad70",
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
        "00c8bd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a022e8 ["INT_ADD", "register:40f0:8", ["const:a022e8:8", "const:4:8"]]
+ 00a03294 ["INT_ADD", "register:40f0:8", ["const:a03294:8", "const:4:8"]]
- 00a022f0 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a022f4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00a0329c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a032a0 ["COPY", "tmp:0:8", ["const:d40:8"]]
~~~


### [`00a0230c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0230c.md) → [`00a032b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a032b8.md) FUN_00a032b8

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
      "definition_site": "00a032bc",
      "incomplete_value": false,
      "site": "00a032c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02310",
      "incomplete_value": false,
      "site": "00a02314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
        "00c8ad70",
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
        "00c8bd40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0230c ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a02310 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00a032b8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a032bc ["COPY", "tmp:0:8", ["const:d40:8"]]
~~~


### [`00a0232c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0232c.md) → [`00a032d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a032d8.md) FUN_00a032d8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00442970`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`004678a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`00468fc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`00489f8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00442c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`00467bc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467bc0.md) [`00468114`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468114.md) [`004692e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/004692e8.md) [`0048a2ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md)

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
      "site": "00a035a4",
      "value": [
        "leaf",
        "ram:9f9cac:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a025f8",
      "value": [
        "leaf",
        "ram:9f8d00:8"
      ]
    },
    "ordinal": 30,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a03680",
      "incomplete_value": false,
      "site": "00a03684",
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
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a026d4",
      "incomplete_value": false,
      "site": "00a026d8",
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
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      716,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009f8d00"
      ]
    ],
    [
      860,
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "byte[47]"
      ]
    ],
    [
      936,
      "PARAM",
      [
        "storage",
        "002b3da5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      716,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009f9cac"
      ]
    ],
    [
      860,
      "DATA",
      [
        "storage",
        "00436bd4",
        null,
        "qword"
      ]
    ],
    [
      936,
      "PARAM",
      [
        "storage",
        "002b3e83",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0235c ["INT_ADD", "register:40f0:8", ["const:a0235c:8", "const:4:8"]]
+ 00a03308 ["INT_ADD", "register:40f0:8", ["const:a03308:8", "const:4:8"]]
- 00a0236c ["INT_ADD", "register:40f0:8", ["const:a0236c:8", "const:4:8"]]
+ 00a03318 ["INT_ADD", "register:40f0:8", ["const:a03318:8", "const:4:8"]]
- 00a0237c ["INT_ADD", "register:40f0:8", ["const:a0237c:8", "const:4:8"]]
+ 00a03328 ["INT_ADD", "register:40f0:8", ["const:a03328:8", "const:4:8"]]
~~~


### [`00a02708`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02708.md) → [`00a036b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a036b4.md) FUN_00a036b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a036d8",
      "incomplete_value": false,
      "site": "00a036d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a0272c",
      "incomplete_value": false,
      "site": "00a0272c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
        "00c8adf0",
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
        "00c8bdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0271c ["INT_ADD", "register:40f0:8", ["const:a0271c:8", "const:4:8"]]
+ 00a036c8 ["INT_ADD", "register:40f0:8", ["const:a036c8:8", "const:4:8"]]
- 00a02724 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a02728 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00a036d0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a036d4 ["COPY", "tmp:0:8", ["const:dc0:8"]]
~~~


### [`00a0273c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0273c.md) → [`00a036e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a036e8.md) FUN_00a036e8

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
      "definition_site": "00a036f4",
      "incomplete_value": false,
      "site": "00a036f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02748",
      "incomplete_value": false,
      "site": "00a02748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
        "00c8adf0",
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
        "00c8bdc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a02740 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a02744 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00a036ec ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a036f0 ["COPY", "tmp:0:8", ["const:dc0:8"]]
~~~


### [`00a02758`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02758.md) → [`00a03704`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03704.md) FUN_00a03704

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008b7f4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f4c.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "00a0373c",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a02790",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03754",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a027a8",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a02774 ["INT_ADD", "register:40f0:8", ["const:a02774:8", "const:4:8"]]
+ 00a03720 ["INT_ADD", "register:40f0:8", ["const:a03720:8", "const:4:8"]]
- 00a02790 ["INT_ADD", "register:40f0:8", ["const:a02790:8", "const:4:8"]]
- 00a02790 ["CALL", null, ["ram:47ad34:8"]]
+ 00a0373c ["INT_ADD", "register:40f0:8", ["const:a0373c:8", "const:4:8"]]
+ 00a0373c ["CALL", null, ["ram:47b054:8"]]
- 00a027a8 ["INT_ADD", "register:40f0:8", ["const:a027a8:8", "const:4:8"]]
- 00a027a8 ["CALL", null, ["ram:47ad34:8"]]
+ 00a03754 ["INT_ADD", "register:40f0:8", ["const:a03754:8", "const:4:8"]]
+ 00a03754 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a027f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a027f8.md) → [`00a037a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a037a4.md) FUN_00a037a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a037bc",
      "incomplete_value": false,
      "site": "00a037c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02810",
      "incomplete_value": false,
      "site": "00a0281c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
        "00c8ae70",
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
        "00c8be40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0280c ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a02810 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a037b8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a037bc ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00a02840 ["INT_ADD", "register:40f0:8", ["const:a02840:8", "const:4:8"]]
+ 00a037ec ["INT_ADD", "register:40f0:8", ["const:a037ec:8", "const:4:8"]]
~~~


### [`00a02888`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02888.md) → [`00a03834`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03834.md) FUN_00a03834

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a0384c",
      "incomplete_value": false,
      "site": "00a03858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a028a0",
      "incomplete_value": false,
      "site": "00a028ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
        "00c8ae70",
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
        "00c8be40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0289c ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a028a0 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a03848 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a0384c ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00a028d0 ["INT_ADD", "register:40f0:8", ["const:a028d0:8", "const:4:8"]]
+ 00a0387c ["INT_ADD", "register:40f0:8", ["const:a0387c:8", "const:4:8"]]
- 00a02900 ["INT_ADD", "register:40f0:8", ["const:a02900:8", "const:4:8"]]
+ 00a038ac ["INT_ADD", "register:40f0:8", ["const:a038ac:8", "const:4:8"]]
~~~


### [`00a02914`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02914.md) → [`00a038c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a038c0.md) FUN_00a038c0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a038ec",
      "incomplete_value": false,
      "site": "00a038f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02940",
      "incomplete_value": false,
      "site": "00a02948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      52,
      "DATA",
      [
        "storage",
        "00c8ae70",
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
        "00c8be40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0292c ["INT_ADD", "register:40f0:8", ["const:a0292c:8", "const:4:8"]]
+ 00a038d8 ["INT_ADD", "register:40f0:8", ["const:a038d8:8", "const:4:8"]]
- 00a0293c ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a02940 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a038e8 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a038ec ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00a02968 ["INT_ADD", "register:40f0:8", ["const:a02968:8", "const:4:8"]]
+ 00a03914 ["INT_ADD", "register:40f0:8", ["const:a03914:8", "const:4:8"]]
~~~


### [`00a02a24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02a24.md) → [`00a039d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a039d0.md) FUN_00a039d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00a039f4",
      "incomplete_value": false,
      "site": "00a039fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02a48",
      "incomplete_value": false,
      "site": "00a02a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      44,
      "DATA",
      [
        "storage",
        "00c8ae70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "00c8be40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a02a44 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a02a48 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00a039f0 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a039f4 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00a02a70 ["INT_ADD", "register:40f0:8", ["const:a02a70:8", "const:4:8"]]
+ 00a03a1c ["INT_ADD", "register:40f0:8", ["const:a03a1c:8", "const:4:8"]]
- 00a02aa8 ["INT_ADD", "register:40f0:8", ["const:a02aa8:8", "const:4:8"]]
+ 00a03a54 ["INT_ADD", "register:40f0:8", ["const:a03a54:8", "const:4:8"]]
~~~


### [`00a02c3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) → [`00a03be8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a03/00a03be8.md) FUN_00a03be8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`00459db4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0046d4d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0045a0d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0046d7f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a03f88",
      "incomplete_value": true,
      "site": "00a03f98",
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
                "const:307:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02fdc",
      "incomplete_value": true,
      "site": "00a02fec",
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
                "const:230:8"
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
      "definition_site": "00a03f9c",
      "incomplete_value": true,
      "site": "00a03f9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a02ff0",
      "incomplete_value": true,
      "site": "00a02ff0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a03f90",
      "incomplete_value": true,
      "site": "00a03fa0",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a02fe4",
      "incomplete_value": true,
      "site": "00a02ff4",
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
                "const:490:8"
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
      140,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      180,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      312,
      "DATA",
      [
        "storage",
        "0040edd0",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      140,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      180,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      312,
      "DATA",
      [
        "storage",
        "0040edd0",
        null,
        "byte[55]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a02c74 ["INT_ADD", "register:40f0:8", ["const:a02c74:8", "const:4:8"]]
+ 00a03c20 ["INT_ADD", "register:40f0:8", ["const:a03c20:8", "const:4:8"]]
- 00a02cc8 ["INT_ADD", "register:40f0:8", ["const:a02cc8:8", "const:4:8"]]
- 00a02cc8 ["CALL", null, ["ram:47ad34:8"]]
+ 00a03c74 ["INT_ADD", "register:40f0:8", ["const:a03c74:8", "const:4:8"]]
+ 00a03c74 ["CALL", null, ["ram:47b054:8"]]
- 00a02cf0 ["INT_ADD", "register:40f0:8", ["const:a02cf0:8", "const:4:8"]]
- 00a02cf0 ["CALL", null, ["ram:47ad34:8"]]
+ 00a03c9c ["INT_ADD", "register:40f0:8", ["const:a03c9c:8", "const:4:8"]]
+ 00a03c9c ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a037e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a037e8.md) → [`00a04794`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04794.md) FUN_00a04794

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
      "definition_site": "00a047a0",
      "incomplete_value": false,
      "site": "00a047ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a037f4",
      "incomplete_value": false,
      "site": "00a03800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      24,
      "DATA",
      [
        "storage",
        "00c8aee0",
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
        "00c8beb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a037f0 ["COPY", "register:4050:8", ["const:c8a000:8"]]
- 00a037f4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a0479c ["COPY", "register:4050:8", ["const:c8b000:8"]]
+ 00a047a0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
~~~


### [`00a0382c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a0382c.md) → [`00a047d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a047d8.md) FUN_00a047d8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a047f0",
      "incomplete_value": false,
      "site": "00a047fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03844",
      "incomplete_value": false,
      "site": "00a03850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
        "00c8aee0",
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
        "00c8beb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03840 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03844 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a047ec ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a047f0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00a03874 ["INT_ADD", "register:40f0:8", ["const:a03874:8", "const:4:8"]]
+ 00a04820 ["INT_ADD", "register:40f0:8", ["const:a04820:8", "const:4:8"]]
~~~


### [`00a03918`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03918.md) → [`00a048c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a048c4.md) FUN_00a048c4

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
      "definition_site": "00a048e4",
      "incomplete_value": false,
      "site": "00a048e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03938",
      "incomplete_value": false,
      "site": "00a03938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
        "00c8aee0",
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
        "00c8beb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03930 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03934 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a048dc ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a048e0 ["COPY", "tmp:0:8", ["const:eb0:8"]]
- 00a03954 ["INT_ADD", "register:40f0:8", ["const:a03954:8", "const:4:8"]]
+ 00a04900 ["INT_ADD", "register:40f0:8", ["const:a04900:8", "const:4:8"]]
- 00a03978 ["INT_ADD", "register:40f0:8", ["const:a03978:8", "const:4:8"]]
+ 00a04924 ["INT_ADD", "register:40f0:8", ["const:a04924:8", "const:4:8"]]
~~~


### [`00a03a18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03a18.md) → [`00a049c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a049c4.md) FUN_00a049c4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459db4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a0d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008ba208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md)

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
      "site": "00a04a00",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03a54",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03a54 ["INT_ADD", "register:40f0:8", ["const:a03a54:8", "const:4:8"]]
- 00a03a54 ["CALL", null, ["ram:47ad34:8"]]
+ 00a04a00 ["INT_ADD", "register:40f0:8", ["const:a04a00:8", "const:4:8"]]
+ 00a04a00 ["CALL", null, ["ram:47b054:8"]]
- 00a03a60 ["INT_ADD", "register:40f0:8", ["const:a03a60:8", "const:4:8"]]
+ 00a04a0c ["INT_ADD", "register:40f0:8", ["const:a04a0c:8", "const:4:8"]]
- 00a03abc ["INT_ADD", "register:40f0:8", ["const:a03abc:8", "const:4:8"]]
+ 00a04a68 ["INT_ADD", "register:40f0:8", ["const:a04a68:8", "const:4:8"]]
~~~


### [`00a03b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03b6c.md) → [`00a04b18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04b18.md) FUN_00a04b18

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a04b30",
      "incomplete_value": false,
      "site": "00a04b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03b84",
      "incomplete_value": false,
      "site": "00a03b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
        "00c8af60",
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
        "00c8bf30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03b80 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03b84 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a04b2c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a04b30 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00a03bb4 ["INT_ADD", "register:40f0:8", ["const:a03bb4:8", "const:4:8"]]
+ 00a04b60 ["INT_ADD", "register:40f0:8", ["const:a04b60:8", "const:4:8"]]
~~~


### [`00a03bc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03bc8.md) → [`00a04b74`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04b74.md) FUN_00a04b74

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a04ba0",
      "incomplete_value": false,
      "site": "00a04ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03bf4",
      "incomplete_value": false,
      "site": "00a03bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      44,
      "DATA",
      [
        "storage",
        "00c8af60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "00c8bf30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03bdc ["INT_ADD", "register:40f0:8", ["const:a03bdc:8", "const:4:8"]]
+ 00a04b88 ["INT_ADD", "register:40f0:8", ["const:a04b88:8", "const:4:8"]]
- 00a03be8 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03bec ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a04b94 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a04b98 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00a03c10 ["INT_ADD", "register:40f0:8", ["const:a03c10:8", "const:4:8"]]
+ 00a04bbc ["INT_ADD", "register:40f0:8", ["const:a04bbc:8", "const:4:8"]]
~~~


### [`00a03c58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03c58.md) → [`00a04c04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04c04.md) FUN_00a04c04

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
      "definition_site": "00a04c24",
      "incomplete_value": false,
      "site": "00a04c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03c78",
      "incomplete_value": false,
      "site": "00a03c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
        "00c8af60",
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
        "00c8bf30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03c70 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03c74 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00a04c1c ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a04c20 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00a03c94 ["INT_ADD", "register:40f0:8", ["const:a03c94:8", "const:4:8"]]
+ 00a04c40 ["INT_ADD", "register:40f0:8", ["const:a04c40:8", "const:4:8"]]
- 00a03cb8 ["INT_ADD", "register:40f0:8", ["const:a03cb8:8", "const:4:8"]]
+ 00a04c64 ["INT_ADD", "register:40f0:8", ["const:a04c64:8", "const:4:8"]]
~~~


### [`00a03d58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03d58.md) → [`00a04d04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04d04.md) FUN_00a04d04

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459db4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0045a0d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008ba208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md)

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
      "site": "00a04d40",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a03d94",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03d94 ["INT_ADD", "register:40f0:8", ["const:a03d94:8", "const:4:8"]]
- 00a03d94 ["CALL", null, ["ram:47ad34:8"]]
+ 00a04d40 ["INT_ADD", "register:40f0:8", ["const:a04d40:8", "const:4:8"]]
+ 00a04d40 ["CALL", null, ["ram:47b054:8"]]
- 00a03da0 ["INT_ADD", "register:40f0:8", ["const:a03da0:8", "const:4:8"]]
+ 00a04d4c ["INT_ADD", "register:40f0:8", ["const:a04d4c:8", "const:4:8"]]
- 00a03dfc ["INT_ADD", "register:40f0:8", ["const:a03dfc:8", "const:4:8"]]
+ 00a04da8 ["INT_ADD", "register:40f0:8", ["const:a04da8:8", "const:4:8"]]
~~~


### [`00a03e6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03e6c.md) → [`00a04e18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04e18.md) FUN_00a04e18

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a04e3c",
      "incomplete_value": false,
      "site": "00a04e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03e90",
      "incomplete_value": false,
      "site": "00a03e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
        "00c8aff0",
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
        "00c8bfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03e80 ["INT_ADD", "register:40f0:8", ["const:a03e80:8", "const:4:8"]]
+ 00a04e2c ["INT_ADD", "register:40f0:8", ["const:a04e2c:8", "const:4:8"]]
- 00a03e88 ["COPY", "register:4040:8", ["const:c8a000:8"]]
- 00a03e8c ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00a04e34 ["COPY", "register:4040:8", ["const:c8b000:8"]]
+ 00a04e38 ["COPY", "tmp:0:8", ["const:fc0:8"]]
~~~


### [`00a03ea0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03ea0.md) → [`00a04e4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04e4c.md) FUN_00a04e4c

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
      "definition_site": "00a04e58",
      "incomplete_value": false,
      "site": "00a04e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03eac",
      "incomplete_value": false,
      "site": "00a03eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
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
        "00c8aff0",
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
        "00c8bfc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03ea4 ["COPY", "register:4048:8", ["const:c8a000:8"]]
- 00a03ea8 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00a04e50 ["COPY", "register:4048:8", ["const:c8b000:8"]]
+ 00a04e54 ["COPY", "tmp:0:8", ["const:fc0:8"]]
~~~


### [`00a03ebc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03ebc.md) → [`00a04e68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a04/00a04e68.md) FUN_00a04e68

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`00467ba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ba0.md) [`00469c44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/00469c44.md) [`0046ca04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md) [`00489f8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489f8c.md)
- 新版 呼出元 0件  · 呼出先 25件 [`00467ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467ec0.md) [`00469f64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00469/00469f64.md) [`0046cd24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0046cde4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cde4.md) [`0048a2ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048a/0048a2ac.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a04ec4",
      "incomplete_value": true,
      "site": "00a04ec4",
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
      "definition_site": "00a03f18",
      "incomplete_value": true,
      "site": "00a03f18",
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
      "definition_site": "00a04ecc",
      "incomplete_value": false,
      "site": "00a04edc",
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
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03f20",
      "incomplete_value": false,
      "site": "00a03f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "definition_site": "00a04ed4",
      "incomplete_value": false,
      "site": "00a04edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a03f28",
      "incomplete_value": false,
      "site": "00a03f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      88,
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "00c71a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00ca5a38",
        null,
        "undefined8"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "00c66ef8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "00c72a30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a03f00 ["INT_ADD", "register:40f0:8", ["const:a03f00:8", "const:4:8"]]
+ 00a04eac ["INT_ADD", "register:40f0:8", ["const:a04eac:8", "const:4:8"]]
- 00a03f0c ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 00a04eb8 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 00a03f14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a04ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a38:8"]]
~~~


### [`00a045ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045ac.md) → [`00a05558`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05558.md) FUN_00a05558

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a0557c",
      "incomplete_value": false,
      "site": "00a0557c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a045d0",
      "incomplete_value": false,
      "site": "00a045d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
        "00c8b070",
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
        "00c8c040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a045c0 ["INT_ADD", "register:40f0:8", ["const:a045c0:8", "const:4:8"]]
+ 00a0556c ["INT_ADD", "register:40f0:8", ["const:a0556c:8", "const:4:8"]]
- 00a045c8 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a045cc ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00a05574 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a05578 ["COPY", "tmp:0:8", ["const:40:8"]]
~~~


### [`00a045e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a045e0.md) → [`00a0558c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a0558c.md) FUN_00a0558c

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
      "definition_site": "00a05598",
      "incomplete_value": false,
      "site": "00a05598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a045ec",
      "incomplete_value": false,
      "site": "00a045ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
        "00c8b070",
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
        "00c8c040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a045e4 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a045e8 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00a05590 ["COPY", "register:4048:8", ["const:c8c000:8"]]
+ 00a05594 ["COPY", "tmp:0:8", ["const:40:8"]]
~~~


### [`00a04e18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e18.md) → [`00a05dc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05dc4.md) FUN_00a05dc4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05de8",
      "incomplete_value": false,
      "site": "00a05dec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04e3c",
      "incomplete_value": false,
      "site": "00a04e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
      40,
      "DATA",
      [
        "storage",
        "00c8b0f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c8c0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04e2c ["INT_ADD", "register:40f0:8", ["const:a04e2c:8", "const:4:8"]]
+ 00a05dd8 ["INT_ADD", "register:40f0:8", ["const:a05dd8:8", "const:4:8"]]
- 00a04e38 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04e3c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a05de4 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a05de8 ["COPY", "tmp:0:8", ["const:c0:8"]]
~~~


### [`00a04e58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e58.md) → [`00a05e04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05e04.md) FUN_00a05e04

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
      "definition_site": "00a05e08",
      "incomplete_value": false,
      "site": "00a05e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04e5c",
      "incomplete_value": false,
      "site": "00a04e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:f0:8"
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
        "00c8b0f0",
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
        "00c8c0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04e58 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04e5c ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00a05e04 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a05e08 ["COPY", "tmp:0:8", ["const:c0:8"]]
~~~


### [`00a04ee8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04ee8.md) → [`00a05e94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05e94.md) FUN_00a05e94

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009fb4a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`009fc44c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fc/009fc44c.md) · 呼出先 1件 [`0043bad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a05ea0",
      "incomplete_value": false,
      "site": "00a05ea4",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04ef4",
      "incomplete_value": false,
      "site": "00a04ef8",
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
            "const:f8c:8"
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
        "002b7f8c",
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
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04ef0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a04ef4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a05e9c ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 00a05ea0 ["COPY", "tmp:0:8", ["const:5b:8"]]
- 00a04ef8 ["INT_ADD", "register:40f0:8", ["const:a04ef8:8", "const:4:8"]]
+ 00a05ea4 ["INT_ADD", "register:40f0:8", ["const:a05ea4:8", "const:4:8"]]
~~~


### [`00a04f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f00.md) → [`00a05eac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05eac.md) FUN_00a05eac

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a05ed0",
      "incomplete_value": false,
      "site": "00a05ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04f24",
      "incomplete_value": false,
      "site": "00a04f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      40,
      "DATA",
      [
        "storage",
        "00c8b170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      40,
      "DATA",
      [
        "storage",
        "00c8c140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04f14 ["INT_ADD", "register:40f0:8", ["const:a04f14:8", "const:4:8"]]
+ 00a05ec0 ["INT_ADD", "register:40f0:8", ["const:a05ec0:8", "const:4:8"]]
- 00a04f20 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04f24 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00a05ecc ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a05ed0 ["COPY", "tmp:0:8", ["const:140:8"]]
~~~


### [`00a04f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f40.md) → [`00a05eec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05eec.md) FUN_00a05eec

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
      "definition_site": "00a05ef0",
      "incomplete_value": false,
      "site": "00a05ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a04f44",
      "incomplete_value": false,
      "site": "00a04f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
        "00c8b170",
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
        "00c8c140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04f40 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a04f44 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00a05eec ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a05ef0 ["COPY", "tmp:0:8", ["const:140:8"]]
~~~


### [`00a04f68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04f68.md) → [`00a05f14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a05/00a05f14.md) FUN_00a05f14

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b97f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b97f8.md) [`009df688`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df688.md) [`009df918`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df918.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0048d1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`008524fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md) [`008ba7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba7a4.md) [`009e0634`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e0634.md) [`009e08c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009e0/009e08c4.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a060dc",
      "incomplete_value": true,
      "site": "00a060ec",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:767:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05130",
      "incomplete_value": true,
      "site": "00a05140",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:689:8"
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
      "definition_site": "00a060e0",
      "incomplete_value": true,
      "site": "00a060f0",
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
      "definition_site": "00a05134",
      "incomplete_value": true,
      "site": "00a05144",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a060e4",
      "incomplete_value": true,
      "site": "00a060f4",
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05138",
      "incomplete_value": true,
      "site": "00a05148",
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
                "const:2d0:8"
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
      456,
      "READ",
      [
        "storage",
        "002b5689",
        null,
        "string"
      ]
    ],
    [
      460,
      "READ",
      [
        "storage",
        "002b5695",
        null,
        "string"
      ]
    ],
    [
      464,
      "READ",
      [
        "storage",
        "002c32d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      456,
      "READ",
      [
        "storage",
        "002b5767",
        null,
        "string"
      ]
    ],
    [
      460,
      "READ",
      [
        "storage",
        "002b5773",
        null,
        "string"
      ]
    ],
    [
      464,
      "READ",
      [
        "storage",
        "002c3320",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00a04f9c ["INT_ADD", "register:40f0:8", ["const:a04f9c:8", "const:4:8"]]
+ 00a05f48 ["INT_ADD", "register:40f0:8", ["const:a05f48:8", "const:4:8"]]
- 00a04fb0 ["INT_ADD", "register:40f0:8", ["const:a04fb0:8", "const:4:8"]]
+ 00a05f5c ["INT_ADD", "register:40f0:8", ["const:a05f5c:8", "const:4:8"]]
- 00a04fcc ["INT_ADD", "register:40f0:8", ["const:a04fcc:8", "const:4:8"]]
+ 00a05f78 ["INT_ADD", "register:40f0:8", ["const:a05f78:8", "const:4:8"]]
~~~


### [`00a052a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052a8.md) → [`00a06254`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06254.md) FUN_00a06254

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06278",
      "incomplete_value": false,
      "site": "00a06278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a052cc",
      "incomplete_value": false,
      "site": "00a052cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
        "00c8b1f0",
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
        "00c8c1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a052bc ["INT_ADD", "register:40f0:8", ["const:a052bc:8", "const:4:8"]]
+ 00a06268 ["INT_ADD", "register:40f0:8", ["const:a06268:8", "const:4:8"]]
- 00a052c4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a052c8 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00a06270 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a06274 ["COPY", "tmp:0:8", ["const:1c0:8"]]
~~~


### [`00a052dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052dc.md) → [`00a06288`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06288.md) FUN_00a06288

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
      "definition_site": "00a06294",
      "incomplete_value": true,
      "site": "00a06294",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a052e8",
      "incomplete_value": true,
      "site": "00a052e8",
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
            "const:1f0:8"
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
        "00c8b1f0",
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
        "00c8c1c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a052e0 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a052e4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00a0628c ["COPY", "register:4048:8", ["const:c8c000:8"]]
+ 00a06290 ["COPY", "tmp:0:8", ["const:1c0:8"]]
~~~


### [`00a052f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a052f8.md) → [`00a062a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a062a4.md) FUN_00a062a4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009f7e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f7/009f7e34.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`009f8de0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009f8/009f8de0.md)

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
      "site": "00a062c4",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05318",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00a062d0",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05324",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
        "0047ad34"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a05318 ["INT_ADD", "register:40f0:8", ["const:a05318:8", "const:4:8"]]
- 00a05318 ["CALL", null, ["ram:47ad34:8"]]
+ 00a062c4 ["INT_ADD", "register:40f0:8", ["const:a062c4:8", "const:4:8"]]
+ 00a062c4 ["CALL", null, ["ram:47b054:8"]]
- 00a05324 ["INT_ADD", "register:40f0:8", ["const:a05324:8", "const:4:8"]]
- 00a05324 ["CALL", null, ["ram:47ad34:8"]]
+ 00a062d0 ["INT_ADD", "register:40f0:8", ["const:a062d0:8", "const:4:8"]]
+ 00a062d0 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a05378`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05378.md) → [`00a06324`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06324.md) FUN_00a06324

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06344",
      "incomplete_value": false,
      "site": "00a06348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05398",
      "incomplete_value": false,
      "site": "00a0539c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
        "00c8b270",
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
        "00c8c240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0538c ["INT_ADD", "register:40f0:8", ["const:a0538c:8", "const:4:8"]]
+ 00a06338 ["INT_ADD", "register:40f0:8", ["const:a06338:8", "const:4:8"]]
- 00a05394 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a05398 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00a06340 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a06344 ["COPY", "tmp:0:8", ["const:240:8"]]
~~~


### [`00a053b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a053b0.md) → [`00a0635c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a0635c.md) FUN_00a0635c

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
      "definition_site": "00a06360",
      "incomplete_value": false,
      "site": "00a06364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a053b4",
      "incomplete_value": false,
      "site": "00a053b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
        "00c8b270",
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
        "00c8c240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a053b0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a053b4 ["COPY", "tmp:0:8", ["const:270:8"]]
+ 00a0635c ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a06360 ["COPY", "tmp:0:8", ["const:240:8"]]
~~~


### [`00a053d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a053d0.md) → [`00a0637c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a0637c.md) FUN_00a0637c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0046d4d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0046d7f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`0048d1b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0052e060`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e060.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a0642c",
      "incomplete_value": true,
      "site": "00a0643c",
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
                "const:8cd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05480",
      "incomplete_value": true,
      "site": "00a05490",
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
                "const:7fe:8"
              ]
            ]
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
      "definition_site": "00a06440",
      "incomplete_value": true,
      "site": "00a06440",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a05494",
      "incomplete_value": true,
      "site": "00a05494",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06434",
      "incomplete_value": true,
      "site": "00a06444",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05488",
      "incomplete_value": true,
      "site": "00a05498",
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
                "const:490:8"
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
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      88,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "002b87fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      88,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "002b88cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0540c ["INT_ADD", "register:40f0:8", ["const:a0540c:8", "const:4:8"]]
- 00a0540c ["CALL", null, ["ram:47ad34:8"]]
+ 00a063b8 ["INT_ADD", "register:40f0:8", ["const:a063b8:8", "const:4:8"]]
+ 00a063b8 ["CALL", null, ["ram:47b054:8"]]
- 00a05428 ["INT_ADD", "register:40f0:8", ["const:a05428:8", "const:4:8"]]
- 00a05428 ["CALL", null, ["ram:47ad34:8"]]
+ 00a063d4 ["INT_ADD", "register:40f0:8", ["const:a063d4:8", "const:4:8"]]
+ 00a063d4 ["CALL", null, ["ram:47b054:8"]]
- 00a05464 ["INT_ADD", "register:40f0:8", ["const:a05464:8", "const:4:8"]]
+ 00a06410 ["INT_ADD", "register:40f0:8", ["const:a06410:8", "const:4:8"]]
~~~


### [`00a057e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a057e4.md) → [`00a06790`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06790.md) FUN_00a06790

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a067b4",
      "incomplete_value": false,
      "site": "00a067b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05808",
      "incomplete_value": false,
      "site": "00a05808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
        "00c8b2e0",
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
        "00c8c2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a057f8 ["INT_ADD", "register:40f0:8", ["const:a057f8:8", "const:4:8"]]
+ 00a067a4 ["INT_ADD", "register:40f0:8", ["const:a067a4:8", "const:4:8"]]
- 00a05800 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a05804 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00a067ac ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a067b0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
~~~


### [`00a05818`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05818.md) → [`00a067c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a067c4.md) FUN_00a067c4

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
      "definition_site": "00a067d0",
      "incomplete_value": false,
      "site": "00a067d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05824",
      "incomplete_value": false,
      "site": "00a05824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
        "00c8b2e0",
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
        "00c8c2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0581c ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a05820 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00a067c8 ["COPY", "register:4048:8", ["const:c8c000:8"]]
+ 00a067cc ["COPY", "tmp:0:8", ["const:2b0:8"]]
~~~


### [`00a05834`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05834.md) → [`00a067e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a067e0.md) FUN_00a067e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`008b925c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b925c.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md) [`008ba208`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba208.md)

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
      "site": "00a06808",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0585c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0585c ["INT_ADD", "register:40f0:8", ["const:a0585c:8", "const:4:8"]]
- 00a0585c ["CALL", null, ["ram:47ad34:8"]]
+ 00a06808 ["INT_ADD", "register:40f0:8", ["const:a06808:8", "const:4:8"]]
+ 00a06808 ["CALL", null, ["ram:47b054:8"]]
- 00a05868 ["INT_ADD", "register:40f0:8", ["const:a05868:8", "const:4:8"]]
+ 00a06814 ["INT_ADD", "register:40f0:8", ["const:a06814:8", "const:4:8"]]
~~~


### [`00a058c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a058c0.md) → [`00a0686c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a0686c.md) FUN_00a0686c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06890",
      "incomplete_value": false,
      "site": "00a06890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a058e4",
      "incomplete_value": false,
      "site": "00a058e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
        "00c8b370",
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
        "00c8c340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a058d4 ["INT_ADD", "register:40f0:8", ["const:a058d4:8", "const:4:8"]]
+ 00a06880 ["INT_ADD", "register:40f0:8", ["const:a06880:8", "const:4:8"]]
- 00a058dc ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a058e0 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00a06888 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a0688c ["COPY", "tmp:0:8", ["const:340:8"]]
~~~


### [`00a058f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a058f4.md) → [`00a068a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a068a0.md) FUN_00a068a0

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
      "definition_site": "00a068ac",
      "incomplete_value": false,
      "site": "00a068ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05900",
      "incomplete_value": false,
      "site": "00a05900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
        "00c8b370",
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
        "00c8c340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a058f8 ["COPY", "register:4048:8", ["const:c8b000:8"]]
- 00a058fc ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00a068a4 ["COPY", "register:4048:8", ["const:c8c000:8"]]
+ 00a068a8 ["COPY", "tmp:0:8", ["const:340:8"]]
~~~


### [`00a05910`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05910.md) → [`00a068bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a068bc.md) FUN_00a068bc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`009fac20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fa/009fac20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`009fbbcc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009fb/009fbbcc.md)

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
      "site": "00a068dc",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a05930",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "site": "00a068e8",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a0593c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
        "0047ad34"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a05930 ["INT_ADD", "register:40f0:8", ["const:a05930:8", "const:4:8"]]
- 00a05930 ["CALL", null, ["ram:47ad34:8"]]
+ 00a068dc ["INT_ADD", "register:40f0:8", ["const:a068dc:8", "const:4:8"]]
+ 00a068dc ["CALL", null, ["ram:47b054:8"]]
- 00a0593c ["INT_ADD", "register:40f0:8", ["const:a0593c:8", "const:4:8"]]
- 00a0593c ["CALL", null, ["ram:47ad34:8"]]
+ 00a068e8 ["INT_ADD", "register:40f0:8", ["const:a068e8:8", "const:4:8"]]
+ 00a068e8 ["CALL", null, ["ram:47b054:8"]]
~~~


### [`00a05990`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05990.md) → [`00a0693c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a0693c.md) FUN_00a0693c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06950",
      "incomplete_value": false,
      "site": "00a06954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a059a4",
      "incomplete_value": false,
      "site": "00a059a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
        "00c8b3f0",
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
        "00c8c3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0599c ["INT_ADD", "register:40f0:8", ["const:a0599c:8", "const:4:8"]]
+ 00a06948 ["INT_ADD", "register:40f0:8", ["const:a06948:8", "const:4:8"]]
- 00a059a0 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a059a4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00a0694c ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a06950 ["COPY", "tmp:0:8", ["const:3c0:8"]]
~~~


### [`00a059b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a059b4.md) → [`00a06960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06960.md) FUN_00a06960

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
      "definition_site": "00a06964",
      "incomplete_value": false,
      "site": "00a06968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a059b8",
      "incomplete_value": false,
      "site": "00a059bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8b000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
        "00c8b3f0",
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
        "00c8c3c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a059b4 ["COPY", "register:4040:8", ["const:c8b000:8"]]
- 00a059b8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00a06960 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00a06964 ["COPY", "tmp:0:8", ["const:3c0:8"]]
~~~


### [`00a05aa4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05aa4.md) → [`00a06a50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06a50.md) _INIT_206

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06a8c",
      "incomplete_value": true,
      "site": "00a06aa8",
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
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05ae0",
      "incomplete_value": true,
      "site": "00a05afc",
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
                "const:f66:8"
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
      "definition_site": "00a06ad0",
      "incomplete_value": true,
      "site": "00a06aec",
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05b24",
      "incomplete_value": true,
      "site": "00a05b40",
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
                "const:d6e:8"
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
      "definition_site": "00a06af0",
      "incomplete_value": true,
      "site": "00a06b08",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05b44",
      "incomplete_value": true,
      "site": "00a05b5c",
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
                "const:f15:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
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
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d6e",
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
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a05acc ["COPY", "register:4098:8", ["const:1123000:8"]]
- 00a05ad0 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00a06a78 ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00a06a7c ["COPY", "tmp:0:8", ["const:e10:8"]]
- 00a05ad8 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00a05adc ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 00a06a84 ["COPY", "register:4048:8", ["const:2b8000:8"]]
+ 00a06a88 ["COPY", "tmp:0:8", ["const:35:8"]]
- 00a05af4 ["COPY", "register:4050:8", ["const:2b7000:8"]]
- 00a05af8 ["COPY", "tmp:0:8", ["const:f79:8"]]
+ 00a06aa0 ["COPY", "register:4050:8", ["const:2b8000:8"]]
+ 00a06aa4 ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00a05e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05e34.md) → [`00a06de0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06de0.md) FUN_00a06de0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28ff0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 15件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048795c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)
- 新版 呼出元 1件 [`00b29fe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b29/00b29fe4.md) · 呼出先 15件 [`00441220`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c7c.md) [`00487c9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00488180`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a06e20",
      "incomplete_value": false,
      "site": "00a06e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c65000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05e74",
      "incomplete_value": false,
      "site": "00a05e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c64000:8"
          ],
          [
            "leaf",
            "const:e08:8"
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
      "definition_site": "00a06e58",
      "incomplete_value": true,
      "site": "00a06e64",
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
                "const:7ac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a05eac",
      "incomplete_value": true,
      "site": "00a05eb8",
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
                "const:76c:8"
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
      "definition_site": "00a06fb4",
      "incomplete_value": true,
      "site": "00a06fc0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:769:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a06008",
      "incomplete_value": true,
      "site": "00a06014",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:69a:8"
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
      76,
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a176c",
        null,
        "string"
      ]
    ],
    [
      468,
      "READ",
      [
        "storage",
        "002b969a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      76,
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a17ac",
        null,
        "string"
      ]
    ],
    [
      468,
      "READ",
      [
        "storage",
        "002b9769",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a05e6c ["INT_ADD", "register:40f0:8", ["const:a05e6c:8", "const:4:8"]]
+ 00a06e18 ["INT_ADD", "register:40f0:8", ["const:a06e18:8", "const:4:8"]]
- 00a05e70 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00a05e74 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00a06e1c ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00a06e20 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00a05ea8 ["COPY", "tmp:0:8", ["const:76c:8"]]
+ 00a06e54 ["COPY", "tmp:0:8", ["const:7ac:8"]]
~~~


### [`00a06780`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06780.md) → [`00a0772c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a0772c.md) FUN_00a0772c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007ccf44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007ef378`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef378.md) · 呼出先 11件 [`008003d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00802d44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d44.md) [`00802da4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802da4.md) [`00802dd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802dd0.md) [`00802ec4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802ec4.md)
- 新版 呼出元 2件 [`007cdea8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007cd/007cdea8.md) [`007f02dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007f0/007f02dc.md) · 呼出先 11件 [`00801334`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00801/00801334.md) [`00803ca8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803ca8.md) [`00803d08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803d08.md) [`00803d34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803d34.md) [`00803e28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00803/00803e28.md)

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
      "site": "00a0779c",
      "value": [
        "leaf",
        "ram:a66e50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a067f0",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ],
  "added": [
    [
      112,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a66e50"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a0679c ["INT_ADD", "register:40f0:8", ["const:a0679c:8", "const:4:8"]]
+ 00a07748 ["INT_ADD", "register:40f0:8", ["const:a07748:8", "const:4:8"]]
- 00a067ac ["INT_ADD", "register:40f0:8", ["const:a067ac:8", "const:4:8"]]
+ 00a07758 ["INT_ADD", "register:40f0:8", ["const:a07758:8", "const:4:8"]]
- 00a067b4 ["INT_ADD", "register:40f0:8", ["const:a067b4:8", "const:4:8"]]
+ 00a07760 ["INT_ADD", "register:40f0:8", ["const:a07760:8", "const:4:8"]]
~~~


### [`00a06a4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06a4c.md) → [`00a079f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a079f8.md) FUN_00a079f8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a05e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a05/00a05e34.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00a06de0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a06/00a06de0.md) · 呼出先 1件 [`0043bad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a07a04",
      "incomplete_value": false,
      "site": "00a07a08",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a06a58",
      "incomplete_value": false,
      "site": "00a06a5c",
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
            "const:f8c:8"
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
        "002b7f8c",
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
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a06a54 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a06a58 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a07a00 ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 00a07a04 ["COPY", "tmp:0:8", ["const:5b:8"]]
- 00a06a5c ["INT_ADD", "register:40f0:8", ["const:a06a5c:8", "const:4:8"]]
+ 00a07a08 ["INT_ADD", "register:40f0:8", ["const:a07a08:8", "const:4:8"]]
~~~


### [`00a06a60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06a60.md) → [`00a07a0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a07/00a07a0c.md) _INIT_207

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a07a8c",
      "incomplete_value": true,
      "site": "00a07aa8",
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a06ae0",
      "incomplete_value": true,
      "site": "00a06afc",
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
                "const:d6e:8"
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
      "definition_site": "00a07aac",
      "incomplete_value": true,
      "site": "00a07ac4",
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a06b00",
      "incomplete_value": true,
      "site": "00a06b18",
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
                "const:f15:8"
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
      "definition_site": "00a07ac8",
      "incomplete_value": true,
      "site": "00a07ae4",
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
                "const:643:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a06b1c",
      "incomplete_value": true,
      "site": "00a06b38",
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
                "const:576:8"
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
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d6e",
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
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a06a88 ["COPY", "register:4098:8", ["const:1123000:8"]]
- 00a06a8c ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00a07a34 ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00a07a38 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00a06a94 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00a06a98 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 00a07a40 ["COPY", "register:4048:8", ["const:2b8000:8"]]
+ 00a07a44 ["COPY", "tmp:0:8", ["const:35:8"]]
- 00a06ab0 ["COPY", "register:4050:8", ["const:2b7000:8"]]
- 00a06ab4 ["COPY", "tmp:0:8", ["const:f79:8"]]
+ 00a07a5c ["COPY", "register:4050:8", ["const:2b8000:8"]]
+ 00a07a60 ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00a14ad4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14ad4.md) → [`00a15a80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a15/00a15a80.md) FUN_00a15a80

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b1f034`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f034.md) · 呼出先 14件 [`00481470`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md) [`004814a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004814a0.md) [`004820ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/004820ec.md) [`004825f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/004825f0.md) [`00482620`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482620.md)
- 新版 呼出元 1件 [`00b20028`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b20/00b20028.md) · 呼出先 14件 [`00481790`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481790.md) [`004817c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004817c0.md) [`0048240c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/0048240c.md) [`00482910`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482910.md) [`00482940`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00482/00482940.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a15b9c",
      "incomplete_value": true,
      "site": "00a15ba0",
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
      "definition_site": "00a14bf0",
      "incomplete_value": true,
      "site": "00a14bf4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a15c3c",
      "incomplete_value": true,
      "site": "00a15c40",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:5d0:8"
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
      "definition_site": "00a14c90",
      "incomplete_value": true,
      "site": "00a14c94",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:600:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a15b88",
      "value": [
        "leaf",
        "ram:a07d9c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a14bdc",
      "value": [
        "leaf",
        "ram:a06df0:8"
      ]
    },
    "ordinal": 12,
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
        "002a1580",
        null,
        "string"
      ]
    ],
    [
      264,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a06df0"
      ]
    ],
    [
      276,
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "002a15c0",
        null,
        "string"
      ]
    ],
    [
      264,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a07d9c"
      ]
    ],
    [
      276,
      "READ",
      [
        "storage",
        "00c9bd38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a14afc ["INT_ADD", "register:40f0:8", ["const:a14afc:8", "const:4:8"]]
+ 00a15aa8 ["INT_ADD", "register:40f0:8", ["const:a15aa8:8", "const:4:8"]]
- 00a14b04 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00a15ab0 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00a14b34 ["INT_ADD", "register:40f0:8", ["const:a14b34:8", "const:4:8"]]
+ 00a15ae0 ["INT_ADD", "register:40f0:8", ["const:a15ae0:8", "const:4:8"]]
~~~


### [`00a1a6f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) → [`00a1b6a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b6a4.md) FUN_00a1b6a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 127件 [`0043c298`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0045abac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`0045c948`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c948.md) [`0045d9f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md) [`005996f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00599/005996f4.md) · 呼出先 3件 [`00a14de0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14de0.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 127件 [`0043c5b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043c/0043c5b8.md) [`0045aecc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045aecc.md) [`0045cc68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045c/0045cc68.md) [`0045dd14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045d/0045dd14.md) [`00599a14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599a14.md) · 呼出先 3件 [`00a15d8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a15/00a15d8c.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a1b6d8",
      "incomplete_value": true,
      "site": "00a1b6d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a1a72c",
      "incomplete_value": true,
      "site": "00a1a72c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a1b6e4",
      "value": [
        "leaf",
        "ram:a15d8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a1a738",
      "value": [
        "leaf",
        "ram:a14de0:8"
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
      32,
      "READ",
      [
        "storage",
        "002a1580",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a14de0"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "002a15c0",
        null,
        "string"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a15d8c"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a1a710 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00a1b6bc ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00a1a738 ["INT_ADD", "register:40f0:8", ["const:a1a738:8", "const:4:8"]]
- 00a1a738 ["CALL", null, ["ram:a14de0:8"]]
+ 00a1b6e4 ["INT_ADD", "register:40f0:8", ["const:a1b6e4:8", "const:4:8"]]
+ 00a1b6e4 ["CALL", null, ["ram:a15d8c:8"]]
- 00a1a74c ["INT_ADD", "register:40f0:8", ["const:a1a74c:8", "const:4:8"]]
+ 00a1b6f8 ["INT_ADD", "register:40f0:8", ["const:a1b6f8:8", "const:4:8"]]
~~~


### [`00a25e6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a25/00a25e6c.md) → [`00a26e18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a26/00a26e18.md) FUN_00a26e18

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a1a7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) [`00a47f54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 2件 [`00a1b750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a1b/00a1b750.md) [`00a48f48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a48/00a48f48.md) · 呼出先 1件 [`0043bad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a26e24",
      "incomplete_value": false,
      "site": "00a26e28",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a25e78",
      "incomplete_value": false,
      "site": "00a25e7c",
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
            "const:f8c:8"
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
        "002b7f8c",
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
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a25e74 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a25e78 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a26e20 ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 00a26e24 ["COPY", "tmp:0:8", ["const:5b:8"]]
- 00a25e7c ["INT_ADD", "register:40f0:8", ["const:a25e7c:8", "const:4:8"]]
+ 00a26e28 ["INT_ADD", "register:40f0:8", ["const:a26e28:8", "const:4:8"]]
~~~


### [`00a25e80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a25/00a25e80.md) → [`00a26e2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a26/00a26e2c.md) _INIT_208

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a26e68",
      "incomplete_value": true,
      "site": "00a26e84",
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
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a25ebc",
      "incomplete_value": true,
      "site": "00a25ed8",
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
                "const:f66:8"
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
      "definition_site": "00a26e8c",
      "incomplete_value": true,
      "site": "00a26ea8",
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a25ee0",
      "incomplete_value": true,
      "site": "00a25efc",
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
                "const:f79:8"
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
      "definition_site": "00a26eac",
      "incomplete_value": true,
      "site": "00a26ec8",
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a25f00",
      "incomplete_value": true,
      "site": "00a25f1c",
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
                "const:d6e:8"
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
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d6e",
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
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a25ea8 ["COPY", "register:4098:8", ["const:1123000:8"]]
- 00a25eac ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00a26e54 ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00a26e58 ["COPY", "tmp:0:8", ["const:e40:8"]]
- 00a25eb4 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00a25eb8 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 00a26e60 ["COPY", "register:4048:8", ["const:2b8000:8"]]
+ 00a26e64 ["COPY", "tmp:0:8", ["const:35:8"]]
- 00a25ed0 ["COPY", "register:4050:8", ["const:2b7000:8"]]
- 00a25ed4 ["COPY", "tmp:0:8", ["const:f79:8"]]
+ 00a26e7c ["COPY", "register:4050:8", ["const:2b8000:8"]]
+ 00a26e80 ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00a2a884`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2a884.md) → [`00a2b858`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2b/00a2b858.md) FUN_00a2b858

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 14件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)
- 新版 呼出元 1件 [`00a271bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 14件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004804d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/004804d8.md) [`00480658`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00480750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480750.md) [`00480aa4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480aa4.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 8件, `call_argument_candidate` 2件, `store_condition` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a2ba28",
      "incomplete_value": true,
      "site": "00a2ba2c",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2aa54",
      "incomplete_value": true,
      "site": "00a2aa58",
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
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2b924",
      "incomplete_value": true,
      "site": "00a2b924",
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
      "definition_site": "00a2a950",
      "incomplete_value": true,
      "site": "00a2a950",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              [
                "live",
                "register:4098:8"
              ]
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2b944",
      "incomplete_value": true,
      "site": "00a2b944",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SLESS",
              "INT_SBORROW"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2a970",
      "incomplete_value": true,
      "site": "00a2a970",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              [
                "live",
                "register:101:1"
              ]
            ]
          ],
          [
            "INT_EQUAL",
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
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2a8c4 ["INT_ADD", "register:40f0:8", ["const:a2a8c4:8", "const:4:8"]]
+ 00a2b898 ["INT_ADD", "register:40f0:8", ["const:a2b898:8", "const:4:8"]]
- 00a2a8dc ["INT_ADD", "register:40f0:8", ["const:a2a8dc:8", "const:4:8"]]
+ 00a2b8b0 ["INT_ADD", "register:40f0:8", ["const:a2b8b0:8", "const:4:8"]]
- 00a2a8f0 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00a2b8c4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
~~~


### [`00a2ade0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2ade0.md) → [`00a2bdb4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2b/00a2bdb4.md) FUN_00a2bdb4

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 14件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)
- 新版 呼出元 1件 [`00a271bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 14件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004804d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/004804d8.md) [`00480658`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00480750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480750.md) [`00480aa4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480aa4.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 8件, `store_condition` 3件, `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2bde0",
      "incomplete_value": true,
      "site": "00a2bde0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ae0c",
      "incomplete_value": true,
      "site": "00a2ae0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:e0:8"
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
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2bdec",
      "incomplete_value": true,
      "site": "00a2bdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ae18",
      "incomplete_value": true,
      "site": "00a2ae18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2bdf0",
      "incomplete_value": true,
      "site": "00a2bdf0",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ae1c",
      "incomplete_value": true,
      "site": "00a2ae1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


~~~diff
- 00a2ae20 ["INT_ADD", "register:40f0:8", ["const:a2ae20:8", "const:4:8"]]
+ 00a2bdf4 ["INT_ADD", "register:40f0:8", ["const:a2bdf4:8", "const:4:8"]]
- 00a2ae38 ["INT_ADD", "register:40f0:8", ["const:a2ae38:8", "const:4:8"]]
+ 00a2be0c ["INT_ADD", "register:40f0:8", ["const:a2be0c:8", "const:4:8"]]
- 00a2ae4c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00a2be20 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
~~~


### [`00a2dba8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2dba8.md) → [`00a2eb9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2e/00a2eb9c.md) FUN_00a2eb9c

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 6件 [`00480bd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`005c17dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00691858`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md)
- 新版 呼出元 1件 [`00a2c310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 6件 [`00480ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`004810a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md) [`00481188`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481188.md) [`005c1b8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1b8c.md) [`00691c08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00691/00691c08.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 4件, `store_destination` 10件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2eba0",
      "incomplete_value": true,
      "site": "00a2eba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2dbac",
      "incomplete_value": true,
      "site": "00a2dbac",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2eba0",
      "incomplete_value": true,
      "site": "00a2eba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:30:8"
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
      "definition_site": "00a2dbac",
      "incomplete_value": true,
      "site": "00a2dbac",
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
                "const:30:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2eba4",
      "incomplete_value": true,
      "site": "00a2eba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:90:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2dbb0",
      "incomplete_value": true,
      "site": "00a2dbb0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


~~~diff
- 00a2dbe8 ["INT_ADD", "register:40f0:8", ["const:a2dbe8:8", "const:4:8"]]
+ 00a2ebdc ["INT_ADD", "register:40f0:8", ["const:a2ebdc:8", "const:4:8"]]
- 00a2dbf8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00a2ebec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a2dc04 ["INT_ADD", "register:40f0:8", ["const:a2dc04:8", "const:4:8"]]
+ 00a2ebf8 ["INT_ADD", "register:40f0:8", ["const:a2ebf8:8", "const:4:8"]]
~~~


### [`00a2e5bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2e5bc.md) → [`00a2f5b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2f5b0.md) FUN_00a2f5b0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a22424`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 11件 [`00470880`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00480bd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md) [`00480d88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`0066b9e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066b/0066b9e4.md)
- 新版 呼出元 1件 [`00a233d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a23/00a233d0.md) · 呼出先 11件 [`00470ba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`00480ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`00480f48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480f48.md) [`004810a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md) [`0066bd94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0066b/0066bd94.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2f7c4",
      "incomplete_value": true,
      "site": "00a2f7c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40d0:8"
              ],
              [
                "live",
                "register:40e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2e7d0",
      "incomplete_value": true,
      "site": "00a2e7d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00a2f7f0",
      "incomplete_value": true,
      "site": "00a2f7f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
              ],
              [
                "live",
                "register:40b8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2e7fc",
      "incomplete_value": true,
      "site": "00a2e804",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2f8a4",
      "incomplete_value": true,
      "site": "00a2f8a4",
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
      "definition_site": "00a2e8b0",
      "incomplete_value": true,
      "site": "00a2e8b0",
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
    "ordinal": 9,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2e600 ["INT_ADD", "register:40f0:8", ["const:a2e600:8", "const:4:8"]]
+ 00a2f5f4 ["INT_ADD", "register:40f0:8", ["const:a2f5f4:8", "const:4:8"]]
- 00a2e610 ["INT_ADD", "register:40f0:8", ["const:a2e610:8", "const:4:8"]]
+ 00a2f604 ["INT_ADD", "register:40f0:8", ["const:a2f604:8", "const:4:8"]]
- 00a2e61c ["INT_ADD", "register:40f0:8", ["const:a2e61c:8", "const:4:8"]]
+ 00a2f610 ["INT_ADD", "register:40f0:8", ["const:a2f610:8", "const:4:8"]]
~~~


### [`00a2ea1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md) → [`00a2fa10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fa10.md) FUN_00a2fa10

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a2eb48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2eb48.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a2c310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 4件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00a2fb3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fb3c.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2fb08",
      "incomplete_value": true,
      "site": "00a2fb08",
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
      "definition_site": "00a2eb14",
      "incomplete_value": true,
      "site": "00a2eb14",
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
    "ordinal": 7,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2ea44 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00a2fa38 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00a2ea60 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
+ 00a2fa54 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00a2ea78 ["INT_ADD", "register:40f0:8", ["const:a2ea78:8", "const:4:8"]]
+ 00a2fa6c ["INT_ADD", "register:40f0:8", ["const:a2fa6c:8", "const:4:8"]]
~~~


### [`00a2eb48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2eb48.md) → [`00a2fb3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fb3c.md) FUN_00a2fb3c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2ea1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a2fa10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fa10.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, control_flow, local_def_use, operands_and_dependencies, return_value_candidate, store_condition

優先判定に残った影響 `branch_value` 5件, `return_value_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2fb84",
      "incomplete_value": true,
      "site": "00a2fb84",
      "value": [
        "INT_EQUAL",
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
                "register:4050:4"
              ],
              [
                "live",
                "register:4048:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2eb90",
      "incomplete_value": true,
      "site": "00a2eb90",
      "value": [
        "INT_EQUAL",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a2fbc4",
      "value": [
        "live",
        "register:101:1"
      ]
    },
    "old": {
      "definition_site": "00a2ebc8",
      "incomplete_value": true,
      "site": "00a2ebd0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:4050:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a2fc18",
      "incomplete_value": true,
      "site": "00a2fc18",
      "value": [
        "INT_EQUAL",
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
      "definition_site": "00a2ec24",
      "incomplete_value": true,
      "site": "00a2ec24",
      "value": [
        "INT_EQUAL",
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
                "register:4058:4"
              ],
              [
                "live",
                "register:4050:4"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2eb70 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00a2fb64 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00a2eb74 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00a2fb68 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a2eb90 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
+ 00a2fb84 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
~~~


### [`00a2ecf0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md) → [`00a2fce4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fce4.md) FUN_00a2fce4

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a2ee14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ee14.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00a2c310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 4件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00a2fe08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fe08.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2fcf4",
      "incomplete_value": true,
      "site": "00a2fcf4",
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
            "const:50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ed00",
      "incomplete_value": true,
      "site": "00a2ed00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:60:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:50:8"
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
      "definition_site": "00a2fcf4",
      "incomplete_value": true,
      "site": "00a2fcf4",
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
                "const:50:8"
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
      "definition_site": "00a2ed00",
      "incomplete_value": true,
      "site": "00a2ed00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:50:8"
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a2fd08",
      "incomplete_value": true,
      "site": "00a2fd08",
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
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2ed14",
      "incomplete_value": true,
      "site": "00a2ed14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


~~~diff
- 00a2ed4c ["INT_ADD", "register:40f0:8", ["const:a2ed4c:8", "const:4:8"]]
+ 00a2fd40 ["INT_ADD", "register:40f0:8", ["const:a2fd40:8", "const:4:8"]]
- 00a2ed54 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00a2fd48 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a2ed6c ["INT_ADD", "register:40f0:8", ["const:a2ed6c:8", "const:4:8"]]
+ 00a2fd60 ["INT_ADD", "register:40f0:8", ["const:a2fd60:8", "const:4:8"]]
~~~


### [`00a2ee14`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ee14.md) → [`00a2fe08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fe08.md) FUN_00a2fe08

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a2ecf0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a2fce4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2fce4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00a2ff98",
      "incomplete_value": true,
      "site": "00a2ffa0",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2ef54 ["CBRANCH", null, ["local:b42:8", "tmp:0:1"]]
+ 00a2ff48 ["CBRANCH", null, ["local:b41:8", "tmp:0:1"]]
- 00a2ef68 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
+ 00a2ff5c ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00a2ef8c ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
+ 00a2ff80 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
~~~


### [`00a2efbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md) → [`00a2ffb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2ffb0.md) FUN_00a2ffb0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0086c30c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a271bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 3件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`0086d2b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0086d/0086d2b8.md) [`00c58f30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies

優先判定に残った影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a30130",
      "incomplete_value": true,
      "site": "00a30130",
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
      "definition_site": "00a2f13c",
      "incomplete_value": true,
      "site": "00a2f13c",
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
    "ordinal": 20,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a30144",
      "incomplete_value": true,
      "site": "00a30144",
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
      "definition_site": "00a2f150",
      "incomplete_value": true,
      "site": "00a2f150",
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
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a30188",
      "incomplete_value": true,
      "site": "00a30188",
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
      "definition_site": "00a2f194",
      "incomplete_value": true,
      "site": "00a2f194",
      "value": [
        "INT_EQUAL",
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
    "ordinal": 28,
    "slot": 0
  }
]
~~~


~~~diff
- 00a2efe4 ["CBRANCH", null, ["local:b51:8", "tmp:0:1"]]
+ 00a2ffd8 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 00a2f010 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00a30004 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a2f018 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00a3000c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
~~~


### [`00a2f2dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2f2dc.md) → [`00a302d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a302d0.md) FUN_00a302d0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00a2b33c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) [`00a65e5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a65/00a65e5c.md) [`00a66524`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a66/00a66524.md) · 呼出先 1件 [`00442970`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)
- 新版 呼出元 3件 [`00a2c310`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) [`00a66e50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a66/00a66e50.md) [`00a67518`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a67/00a67518.md) · 呼出先 1件 [`00442c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a302dc",
      "incomplete_value": false,
      "site": "00a302e0",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2f2e8",
      "incomplete_value": false,
      "site": "00a2f2ec",
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
            "const:f8c:8"
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
        "002b7f8c",
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
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a2f2e4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a2f2e8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00a302d8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 00a302dc ["COPY", "tmp:0:8", ["const:5b:8"]]
- 00a2f2ec ["INT_ADD", "register:40f0:8", ["const:a2f2ec:8", "const:4:8"]]
+ 00a302e0 ["INT_ADD", "register:40f0:8", ["const:a302e0:8", "const:4:8"]]
~~~


### [`00a2f2f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2f2f0.md) → [`00a302e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a302e4.md) _INIT_209

根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a30314",
      "incomplete_value": true,
      "site": "00a30314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:f0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2f320",
      "incomplete_value": true,
      "site": "00a2f320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40e8:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a30314",
      "incomplete_value": true,
      "site": "00a30314",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:1660:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2f320",
      "incomplete_value": true,
      "site": "00a2f320",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:28:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00a30328",
      "incomplete_value": true,
      "site": "00a30328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:8:8"
              ],
              [
                "leaf",
                "const:120:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a2f334",
      "incomplete_value": true,
      "site": "00a2f334",
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
            "const:21:8"
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
      60,
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d6e",
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
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a2f318 ["COPY", "register:4098:8", ["const:1123000:8"]]
- 00a2f31c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00a3030c ["COPY", "register:4098:8", ["const:1124000:8"]]
+ 00a30310 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a2f324 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00a2f328 ["COPY", "tmp:0:8", ["const:f66:8"]]
+ 00a30318 ["COPY", "register:4048:8", ["const:2b8000:8"]]
+ 00a3031c ["COPY", "tmp:0:8", ["const:35:8"]]
- 00a2f340 ["COPY", "register:4050:8", ["const:2b7000:8"]]
- 00a2f344 ["COPY", "tmp:0:8", ["const:f79:8"]]
+ 00a30334 ["COPY", "register:4050:8", ["const:2b8000:8"]]
+ 00a30338 ["COPY", "tmp:0:8", ["const:48:8"]]
~~~


### [`00a2f680`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2f/00a2f680.md) → [`00a30674`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a30/00a30674.md) FUN_00a30674

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f4c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 19件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0048796c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487aa4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)
- 新版 呼出元 1件 [`00b204b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b20/00b204b8.md) · 呼出先 19件 [`0043bf04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00487c8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487c9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c9c.md) [`00487dc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 10件, `call_argument_candidate` 12件, `store_condition` 1件, `store_destination` 3件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a306f4",
      "value": [
        "live",
        "register:5000:16"
      ]
    },
    "old": {
      "definition_site": "00a2f6e4",
      "incomplete_value": true,
      "site": "00a2f700",
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
                "const:2be000:8"
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a309bc",
      "incomplete_value": true,
      "site": "00a309bc",
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
              "INT_MULT"
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
      "definition_site": "00a2f9c8",
      "incomplete_value": true,
      "site": "00a2f9c8",
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
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a309c8",
      "incomplete_value": true,
      "site": "00a309c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40c8:8"
              ],
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
      "definition_site": "00a2f9d4",
      "incomplete_value": true,
      "site": "00a2f9d4",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 48,
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
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "002be277",
        null,
        "string"
      ]
    ],
    [
      1448,
      "READ",
      [
        "storage",
        "00c9ac80",
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
        "00c65dd8",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "002be355",
        null,
        "string"
      ]
    ],
    [
      1448,
      "READ",
      [
        "storage",
        "00c9bc50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00a2f6b8 ["INT_ADD", "register:40f0:8", ["const:a2f6b8:8", "const:4:8"]]
+ 00a306ac ["INT_ADD", "register:40f0:8", ["const:a306ac:8", "const:4:8"]]
- 00a2f6c0 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 00a2f6c4 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00a306b4 ["COPY", "register:4040:8", ["const:c65000:8"]]
+ 00a306b8 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00a2f6d4 ["INT_ADD", "register:40f0:8", ["const:a2f6d4:8", "const:4:8"]]
+ 00a306c8 ["INT_ADD", "register:40f0:8", ["const:a306c8:8", "const:4:8"]]
~~~


