# v15.7.2 → v15.7.3 · 最優先の変更候補 (48)

[一覧の目次](README.md)

### [`008fe148`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe148.md) → [`008fe148`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe148.md) FUN_008fe148

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe15c",
      "incomplete_value": false,
      "site": "008fe160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe15c",
      "incomplete_value": false,
      "site": "008fe160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
        "00c08e60",
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
        "00c08f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe15c ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 008fe15c ["COPY", "tmp:0:8", ["const:f10:8"]]
~~~


### [`008fe16c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe16c.md) → [`008fe16c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe16c.md) FUN_008fe16c

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
      "definition_site": "008fe170",
      "incomplete_value": false,
      "site": "008fe174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe170",
      "incomplete_value": false,
      "site": "008fe174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
        "00c08e60",
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
        "00c08f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe170 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 008fe170 ["COPY", "tmp:0:8", ["const:f10:8"]]
~~~


### [`008fe22c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe22c.md) → [`008fe22c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe22c.md) FUN_008fe22c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe240",
      "incomplete_value": false,
      "site": "008fe244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe240",
      "incomplete_value": false,
      "site": "008fe244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
        "00c08ee0",
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
        "00c08f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe240 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 008fe240 ["COPY", "tmp:0:8", ["const:f90:8"]]
~~~


### [`008fe250`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe250.md) → [`008fe250`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe250.md) FUN_008fe250

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
      "definition_site": "008fe254",
      "incomplete_value": false,
      "site": "008fe258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe254",
      "incomplete_value": false,
      "site": "008fe258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
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
      8,
      "DATA",
      [
        "storage",
        "00c08ee0",
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
        "00c08f90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe254 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 008fe254 ["COPY", "tmp:0:8", ["const:f90:8"]]
~~~


### [`008fe310`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe310.md) → [`008fe310`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe310.md) FUN_008fe310

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe324",
      "incomplete_value": false,
      "site": "008fe328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe324",
      "incomplete_value": false,
      "site": "008fe328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
        "00c08f70",
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
        "00c09020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe320 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008fe324 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 008fe320 ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 008fe324 ["COPY", "tmp:0:8", ["const:20:8"]]
~~~


### [`008fe334`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe334.md) → [`008fe334`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe334.md) FUN_008fe334

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
      "definition_site": "008fe338",
      "incomplete_value": false,
      "site": "008fe33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe338",
      "incomplete_value": false,
      "site": "008fe33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f70:8"
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
        "00c08f70",
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
        "00c09020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe334 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008fe338 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 008fe334 ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 008fe338 ["COPY", "tmp:0:8", ["const:20:8"]]
~~~


### [`008fe34c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe34c.md) → [`008fe34c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe34c.md) FUN_008fe34c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 22件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe51c",
      "incomplete_value": false,
      "site": "008fe52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe51c",
      "incomplete_value": false,
      "site": "008fe52c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
      "definition_site": "008fe554",
      "incomplete_value": false,
      "site": "008fe564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe554",
      "incomplete_value": false,
      "site": "008fe564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "definition_site": "008fe61c",
      "incomplete_value": true,
      "site": "008fe634",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe61c",
      "incomplete_value": true,
      "site": "008fe634",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:279:8"
              ]
            ]
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
      480,
      "DATA",
      [
        "storage",
        "00c08fe0",
        null,
        "undefined *"
      ]
    ],
    [
      536,
      "DATA",
      [
        "storage",
        "00c09060",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "READ",
      [
        "storage",
        "00c09000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      480,
      "DATA",
      [
        "storage",
        "00c09090",
        null,
        "undefined *"
      ]
    ],
    [
      536,
      "DATA",
      [
        "storage",
        "00c09110",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "READ",
      [
        "storage",
        "00c090b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe518 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008fe51c ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 008fe518 ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 008fe51c ["COPY", "tmp:0:8", ["const:90:8"]]
- 008fe554 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 008fe554 ["COPY", "tmp:0:8", ["const:110:8"]]
- 008fe614 ["COPY", "tmp:0:8", ["const:279:8"]]
+ 008fe614 ["COPY", "tmp:0:8", ["const:272:8"]]
~~~


### [`008fe76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe76c.md) → [`008fe76c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe76c.md) FUN_008fe76c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe780",
      "incomplete_value": false,
      "site": "008fe784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe780",
      "incomplete_value": false,
      "site": "008fe784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
        "00c08fe0",
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
        "00c09090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe77c ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008fe780 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 008fe77c ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 008fe780 ["COPY", "tmp:0:8", ["const:90:8"]]
~~~


### [`008fe790`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe790.md) → [`008fe790`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe790.md) FUN_008fe790

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
      "definition_site": "008fe794",
      "incomplete_value": false,
      "site": "008fe798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe794",
      "incomplete_value": false,
      "site": "008fe798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:fe0:8"
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
        "00c08fe0",
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
        "00c09090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe790 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008fe794 ["COPY", "tmp:0:8", ["const:fe0:8"]]
+ 008fe790 ["COPY", "register:4040:8", ["const:c09000:8"]]
+ 008fe794 ["COPY", "tmp:0:8", ["const:90:8"]]
~~~


### [`008fe850`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe850.md) → [`008fe850`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe850.md) FUN_008fe850

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe864",
      "incomplete_value": false,
      "site": "008fe868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe864",
      "incomplete_value": false,
      "site": "008fe868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
        "00c09060",
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
        "00c09110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe864 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 008fe864 ["COPY", "tmp:0:8", ["const:110:8"]]
~~~


### [`008fe874`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe874.md) → [`008fe874`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe874.md) FUN_008fe874

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
      "definition_site": "008fe878",
      "incomplete_value": false,
      "site": "008fe87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe878",
      "incomplete_value": false,
      "site": "008fe87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
        "00c09060",
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
        "00c09110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe878 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 008fe878 ["COPY", "tmp:0:8", ["const:110:8"]]
~~~


### [`008fe934`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe934.md) → [`008fe934`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe934.md) FUN_008fe934

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fe954",
      "incomplete_value": false,
      "site": "008fe958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe954",
      "incomplete_value": false,
      "site": "008fe958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      36,
      "DATA",
      [
        "storage",
        "00c090f0",
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
        "00c091a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe954 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 008fe954 ["COPY", "tmp:0:8", ["const:1a0:8"]]
~~~


### [`008fe96c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe96c.md) → [`008fe96c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe96c.md) FUN_008fe96c

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
      "definition_site": "008fe970",
      "incomplete_value": false,
      "site": "008fe974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe970",
      "incomplete_value": false,
      "site": "008fe974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
        "00c090f0",
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
        "00c091a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fe970 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 008fe970 ["COPY", "tmp:0:8", ["const:1a0:8"]]
~~~


### [`008fea5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea5c.md) → [`008fea5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fea5c.md) FUN_008fea5c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fea7c",
      "incomplete_value": false,
      "site": "008fea80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fea7c",
      "incomplete_value": false,
      "site": "008fea80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      36,
      "DATA",
      [
        "storage",
        "00c09170",
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
        "00c09220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fea7c ["COPY", "tmp:0:8", ["const:170:8"]]
+ 008fea7c ["COPY", "tmp:0:8", ["const:220:8"]]
~~~


### [`008fea94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fea94.md) → [`008fea94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fea94.md) FUN_008fea94

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
      "definition_site": "008fea98",
      "incomplete_value": false,
      "site": "008fea9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fea98",
      "incomplete_value": false,
      "site": "008fea9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
        "00c09170",
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
        "00c09220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fea98 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 008fea98 ["COPY", "tmp:0:8", ["const:220:8"]]
~~~


### [`008feb84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feb84.md) → [`008feb84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feb84.md) FUN_008feb84

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008feb98",
      "incomplete_value": false,
      "site": "008feb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008feb98",
      "incomplete_value": false,
      "site": "008feb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
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
        "00c091f0",
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
        "00c092a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008feb98 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 008feb98 ["COPY", "tmp:0:8", ["const:2a0:8"]]
~~~


### [`008feba8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feba8.md) → [`008feba8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feba8.md) FUN_008feba8

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
      "definition_site": "008febac",
      "incomplete_value": false,
      "site": "008febb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008febac",
      "incomplete_value": false,
      "site": "008febb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      8,
      "DATA",
      [
        "storage",
        "00c091f0",
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
        "00c092a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008febac ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 008febac ["COPY", "tmp:0:8", ["const:2a0:8"]]
~~~


### [`008febc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008febc0.md) → [`008febc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008febc0.md) FUN_008febc0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006fd45c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd45c.md) [`006fd460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd460.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006fd45c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd45c.md) [`006fd460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd460.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008fec90",
      "incomplete_value": true,
      "site": "008feca4",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:113:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fec90",
      "incomplete_value": true,
      "site": "008feca4",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:86:8"
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
      "definition_site": "008feca8",
      "incomplete_value": true,
      "site": "008feca8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008feca8",
      "incomplete_value": true,
      "site": "008feca8",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fecbc",
      "incomplete_value": false,
      "site": "008fecc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fecbc",
      "incomplete_value": false,
      "site": "008fecc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      208,
      "READ",
      [
        "storage",
        "00295086",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "00295093",
        null,
        "string"
      ]
    ],
    [
      260,
      "DATA",
      [
        "storage",
        "00c09260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      208,
      "READ",
      [
        "storage",
        "00295113",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "00295120",
        null,
        "string"
      ]
    ],
    [
      260,
      "DATA",
      [
        "storage",
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fec8c ["COPY", "tmp:0:8", ["const:86:8"]]
+ 008fec8c ["COPY", "tmp:0:8", ["const:113:8"]]
- 008fecbc ["COPY", "tmp:0:8", ["const:260:8"]]
+ 008fecbc ["COPY", "tmp:0:8", ["const:310:8"]]
~~~


### [`008fee6c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee6c.md) → [`008fee6c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fee6c.md) FUN_008fee6c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fee80",
      "incomplete_value": false,
      "site": "008fee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fee80",
      "incomplete_value": false,
      "site": "008fee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
        "00c09260",
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
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fee80 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 008fee80 ["COPY", "tmp:0:8", ["const:310:8"]]
~~~


### [`008fee90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fee90.md) → [`008fee90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fee90.md) FUN_008fee90

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
      "definition_site": "008fee94",
      "incomplete_value": false,
      "site": "008fee98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fee94",
      "incomplete_value": false,
      "site": "008fee98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
        "00c09260",
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
        "00c09310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fee94 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 008fee94 ["COPY", "tmp:0:8", ["const:310:8"]]
~~~


### [`008fef1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef1c.md) → [`008fef1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fef1c.md) FUN_008fef1c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fef30",
      "incomplete_value": false,
      "site": "008fef34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fef30",
      "incomplete_value": false,
      "site": "008fef34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
        "00c092f0",
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
        "00c093a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fef30 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008fef30 ["COPY", "tmp:0:8", ["const:3a0:8"]]
~~~


### [`008fef40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fef40.md) → [`008fef40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fef40.md) FUN_008fef40

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
      "definition_site": "008fef44",
      "incomplete_value": false,
      "site": "008fef48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fef44",
      "incomplete_value": false,
      "site": "008fef48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
        "00c092f0",
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
        "00c093a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008fef44 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008fef44 ["COPY", "tmp:0:8", ["const:3a0:8"]]
~~~


### [`008ff09c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff09c.md) → [`008ff09c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff09c.md) FUN_008ff09c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff0b0",
      "incomplete_value": false,
      "site": "008ff0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff0b0",
      "incomplete_value": false,
      "site": "008ff0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
        "00c09370",
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
        "00c09420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff0b0 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 008ff0b0 ["COPY", "tmp:0:8", ["const:420:8"]]
~~~


### [`008ff0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff0c0.md) → [`008ff0c0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff0c0.md) FUN_008ff0c0

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
      "definition_site": "008ff0c4",
      "incomplete_value": false,
      "site": "008ff0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff0c4",
      "incomplete_value": false,
      "site": "008ff0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      8,
      "DATA",
      [
        "storage",
        "00c09370",
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
        "00c09420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff0c4 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 008ff0c4 ["COPY", "tmp:0:8", ["const:420:8"]]
~~~


### [`008ff208`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff208.md) → [`008ff208`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff208.md) FUN_008ff208

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff228",
      "incomplete_value": false,
      "site": "008ff22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff228",
      "incomplete_value": false,
      "site": "008ff22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
        "00c093f0",
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
        "00c094a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff228 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 008ff228 ["COPY", "tmp:0:8", ["const:4a0:8"]]
~~~


### [`008ff240`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff240.md) → [`008ff240`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff240.md) FUN_008ff240

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
      "definition_site": "008ff244",
      "incomplete_value": false,
      "site": "008ff248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff244",
      "incomplete_value": false,
      "site": "008ff248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
        "00c093f0",
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
        "00c094a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff244 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 008ff244 ["COPY", "tmp:0:8", ["const:4a0:8"]]
~~~


### [`008ff330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff330.md) → [`008ff330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff330.md) FUN_008ff330

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff350",
      "incomplete_value": false,
      "site": "008ff354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff350",
      "incomplete_value": false,
      "site": "008ff354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
        "00c09470",
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
        "00c09520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff350 ["COPY", "tmp:0:8", ["const:470:8"]]
+ 008ff350 ["COPY", "tmp:0:8", ["const:520:8"]]
~~~


### [`008ff368`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff368.md) → [`008ff368`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff368.md) FUN_008ff368

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
      "definition_site": "008ff36c",
      "incomplete_value": true,
      "site": "008ff370",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff36c",
      "incomplete_value": true,
      "site": "008ff370",
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
            "const:470:8"
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
        "00c09470",
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
        "00c09520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff36c ["COPY", "tmp:0:8", ["const:470:8"]]
+ 008ff36c ["COPY", "tmp:0:8", ["const:520:8"]]
~~~


### [`008ff458`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff458.md) → [`008ff458`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff458.md) FUN_008ff458

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff47c",
      "incomplete_value": false,
      "site": "008ff47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff47c",
      "incomplete_value": false,
      "site": "008ff47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
        "00c094f0",
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
        "00c095a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff478 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008ff478 ["COPY", "tmp:0:8", ["const:5a0:8"]]
~~~


### [`008ff48c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff48c.md) → [`008ff48c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff48c.md) FUN_008ff48c

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
      "definition_site": "008ff498",
      "incomplete_value": false,
      "site": "008ff498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff498",
      "incomplete_value": false,
      "site": "008ff498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
        "00c094f0",
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
        "00c095a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff494 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008ff494 ["COPY", "tmp:0:8", ["const:5a0:8"]]
~~~


### [`008ff4a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff4a8.md) → [`008ff4a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff4a8.md) FUN_008ff4a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0065059c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00650/0065059c.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0065059c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/0065059c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff5c8",
      "incomplete_value": true,
      "site": "008ff5d8",
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
                "const:b87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff5c8",
      "incomplete_value": true,
      "site": "008ff5d8",
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
                "const:afa:8"
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
      "definition_site": "008ff658",
      "incomplete_value": true,
      "site": "008ff664",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:e69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff658",
      "incomplete_value": true,
      "site": "008ff664",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:e63:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ff7e8",
      "incomplete_value": false,
      "site": "008ff7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ff7e8",
      "incomplete_value": false,
      "site": "008ff7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
      288,
      "READ",
      [
        "storage",
        "0029eafa",
        null,
        "string"
      ]
    ],
    [
      432,
      "READ",
      [
        "storage",
        "002abe63",
        null,
        "string"
      ]
    ],
    [
      504,
      "PARAM",
      [
        "storage",
        "0029d986",
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
        "0029eb87",
        null,
        "string"
      ]
    ],
    [
      432,
      "READ",
      [
        "storage",
        "002abe69",
        null,
        "string"
      ]
    ],
    [
      504,
      "PARAM",
      [
        "storage",
        "0029da13",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ff5c0 ["COPY", "tmp:0:8", ["const:afa:8"]]
+ 008ff5c0 ["COPY", "tmp:0:8", ["const:b87:8"]]
- 008ff650 ["COPY", "tmp:0:8", ["const:e63:8"]]
+ 008ff650 ["COPY", "tmp:0:8", ["const:e69:8"]]
- 008ff6a0 ["COPY", "tmp:0:8", ["const:986:8"]]
+ 008ff6a0 ["COPY", "tmp:0:8", ["const:a13:8"]]
~~~


### [`008ff9e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff9e4.md) → [`008ff9e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff9e4.md) FUN_008ff9e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ffa08",
      "incomplete_value": false,
      "site": "008ffa08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffa08",
      "incomplete_value": false,
      "site": "008ffa08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
        "00c09560",
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
        "00c09610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffa04 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 008ffa04 ["COPY", "tmp:0:8", ["const:610:8"]]
~~~


### [`008ffa18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffa18.md) → [`008ffa18`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffa18.md) FUN_008ffa18

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
      "definition_site": "008ffa24",
      "incomplete_value": false,
      "site": "008ffa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffa24",
      "incomplete_value": false,
      "site": "008ffa24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:560:8"
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
        "00c09560",
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
        "00c09610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffa20 ["COPY", "tmp:0:8", ["const:560:8"]]
+ 008ffa20 ["COPY", "tmp:0:8", ["const:610:8"]]
~~~


### [`008ffb28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb28.md) → [`008ffb28`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffb28.md) FUN_008ffb28

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ffb48",
      "incomplete_value": false,
      "site": "008ffb4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffb48",
      "incomplete_value": false,
      "site": "008ffb4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
        "00c095f0",
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
        "00c096a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffb48 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 008ffb48 ["COPY", "tmp:0:8", ["const:6a0:8"]]
~~~


### [`008ffb60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffb60.md) → [`008ffb60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffb60.md) FUN_008ffb60

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
      "definition_site": "008ffb64",
      "incomplete_value": false,
      "site": "008ffb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffb64",
      "incomplete_value": false,
      "site": "008ffb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
        "00c095f0",
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
        "00c096a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffb64 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 008ffb64 ["COPY", "tmp:0:8", ["const:6a0:8"]]
~~~


### [`008ffc98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffc98.md) → [`008ffc98`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffc98.md) FUN_008ffc98

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ffcbc",
      "incomplete_value": false,
      "site": "008ffcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffcbc",
      "incomplete_value": false,
      "site": "008ffcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
        "00c09670",
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
        "00c09720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffcbc ["COPY", "tmp:0:8", ["const:670:8"]]
+ 008ffcbc ["COPY", "tmp:0:8", ["const:720:8"]]
~~~


### [`008ffcd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffcd8.md) → [`008ffcd8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffcd8.md) FUN_008ffcd8

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
      "definition_site": "008ffcdc",
      "incomplete_value": false,
      "site": "008ffce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ffcdc",
      "incomplete_value": false,
      "site": "008ffce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
        "00c09670",
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
        "00c09720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffcdc ["COPY", "tmp:0:8", ["const:670:8"]]
+ 008ffcdc ["COPY", "tmp:0:8", ["const:720:8"]]
~~~


### [`008ffd00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ffd00.md) → [`008ffd00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ffd00.md) FUN_008ffd00

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`006dd65c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006dd/006dd65c.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`005b3ebc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`006dd65c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fff7c",
      "incomplete_value": false,
      "site": "008fff7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fff7c",
      "incomplete_value": false,
      "site": "008fff7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008ffe10",
      "incomplete_value": true,
      "site": "008ffe10",
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
      "definition_site": "008ffe10",
      "incomplete_value": true,
      "site": "008ffe10",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ffe18",
      "incomplete_value": false,
      "site": "008ffe28",
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
    "old": {
      "definition_site": "008ffe18",
      "incomplete_value": false,
      "site": "008ffe28",
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
            "const:d98:8"
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
      256,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      280,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      288,
      "PARAM",
      [
        "storage",
        "00bf4450",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      256,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      280,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      288,
      "PARAM",
      [
        "storage",
        "00bf4500",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 008ffe00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
+ 008ffe00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 008ffe18 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 008ffe18 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008ffe20 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 008ffe20 ["COPY", "tmp:0:8", ["const:500:8"]]
~~~


### [`00900138`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900138.md) → [`00900138`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900138.md) FUN_00900138

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0090015c",
      "incomplete_value": false,
      "site": "0090015c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090015c",
      "incomplete_value": false,
      "site": "0090015c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
        "00c096e0",
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
        "00c09790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00900158 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00900158 ["COPY", "tmp:0:8", ["const:790:8"]]
~~~


### [`0090016c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090016c.md) → [`0090016c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/0090016c.md) FUN_0090016c

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
      "definition_site": "00900178",
      "incomplete_value": false,
      "site": "00900178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900178",
      "incomplete_value": false,
      "site": "00900178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
        "00c096e0",
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
        "00c09790",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00900174 ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 00900174 ["COPY", "tmp:0:8", ["const:790:8"]]
~~~


### [`009002a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002a8.md) → [`009002a8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002a8.md) FUN_009002a8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009002bc",
      "incomplete_value": false,
      "site": "009002c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009002bc",
      "incomplete_value": false,
      "site": "009002c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
        "00c09770",
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
        "00c09820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009002bc ["COPY", "tmp:0:8", ["const:770:8"]]
+ 009002bc ["COPY", "tmp:0:8", ["const:820:8"]]
~~~


### [`009002cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002cc.md) → [`009002cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002cc.md) FUN_009002cc

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
      "definition_site": "009002d0",
      "incomplete_value": false,
      "site": "009002d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009002d0",
      "incomplete_value": false,
      "site": "009002d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      8,
      "DATA",
      [
        "storage",
        "00c09770",
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
        "00c09820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009002d0 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 009002d0 ["COPY", "tmp:0:8", ["const:820:8"]]
~~~


### [`009002e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009002e4.md) → [`009002e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009002e4.md) FUN_009002e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`006fd45c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd45c.md) [`006fd460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fd/006fd460.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006fd45c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd45c.md) [`006fd460`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006fd/006fd460.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009003b4",
      "incomplete_value": true,
      "site": "009003c8",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:113:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009003b4",
      "incomplete_value": true,
      "site": "009003c8",
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
                "const:295000:8"
              ],
              [
                "leaf",
                "const:86:8"
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
      "definition_site": "009003cc",
      "incomplete_value": true,
      "site": "009003cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "009003cc",
      "incomplete_value": true,
      "site": "009003cc",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009003e0",
      "incomplete_value": false,
      "site": "009003e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009003e0",
      "incomplete_value": false,
      "site": "009003e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      208,
      "READ",
      [
        "storage",
        "00295086",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "00295093",
        null,
        "string"
      ]
    ],
    [
      260,
      "DATA",
      [
        "storage",
        "00c097e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      208,
      "READ",
      [
        "storage",
        "00295113",
        null,
        "string"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "00295120",
        null,
        "string"
      ]
    ],
    [
      260,
      "DATA",
      [
        "storage",
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009003b0 ["COPY", "tmp:0:8", ["const:86:8"]]
+ 009003b0 ["COPY", "tmp:0:8", ["const:113:8"]]
- 009003e0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 009003e0 ["COPY", "tmp:0:8", ["const:890:8"]]
~~~


### [`00900590`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900590.md) → [`00900590`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900590.md) FUN_00900590

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009005a4",
      "incomplete_value": false,
      "site": "009005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009005a4",
      "incomplete_value": false,
      "site": "009005a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
        "00c097e0",
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
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009005a4 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 009005a4 ["COPY", "tmp:0:8", ["const:890:8"]]
~~~


### [`009005b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009005b4.md) → [`009005b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009005b4.md) FUN_009005b4

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
      "definition_site": "009005b8",
      "incomplete_value": false,
      "site": "009005bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009005b8",
      "incomplete_value": false,
      "site": "009005bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
        "00c097e0",
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
        "00c09890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009005b8 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 009005b8 ["COPY", "tmp:0:8", ["const:890:8"]]
~~~


### [`0090063c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/0090063c.md) → [`0090063c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/0090063c.md) _INIT_179

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00900678",
      "incomplete_value": true,
      "site": "00900694",
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
    "old": {
      "definition_site": "00900678",
      "incomplete_value": true,
      "site": "00900694",
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
                "const:2e4:8"
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
      "definition_site": "0090069c",
      "incomplete_value": true,
      "site": "009006b8",
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
    "old": {
      "definition_site": "0090069c",
      "incomplete_value": true,
      "site": "009006b8",
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
                "const:2f7:8"
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
      "definition_site": "009006bc",
      "incomplete_value": true,
      "site": "009006d8",
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
    "old": {
      "definition_site": "009006bc",
      "incomplete_value": true,
      "site": "009006d8",
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
                "const:da:8"
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 00900668 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00900668 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00900674 ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 00900674 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00900690 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 00900690 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`009009cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/009009cc.md) → [`009009cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) FUN_009009cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00982c5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900ae0.md) [`00a6d884`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d884.md) [`00bd6d60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 1件 [`00982c5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 3件 [`00900ae0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900ae0.md) [`00a6d884`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d884.md) [`00bd6e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900a0c",
      "incomplete_value": false,
      "site": "00900a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:870:8"
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
      72,
      "DATA",
      [
        "storage",
        "00c09870",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      72,
      "DATA",
      [
        "storage",
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00900a0c ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00900a0c ["COPY", "tmp:0:8", ["const:920:8"]]
~~~


### [`00900d80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900d80.md) → [`00900d80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900d80.md) FUN_00900d80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md) [`00bd6d90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00a6d8b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900d98",
      "incomplete_value": false,
      "site": "00900da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      36,
      "DATA",
      [
        "storage",
        "00c09870",
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
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00900d98 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00900d98 ["COPY", "tmp:0:8", ["const:920:8"]]
~~~


### [`00900e0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900e0c.md) → [`00900e0c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900e0c.md) FUN_00900e0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a6d/00a6d8b4.md) [`00bd6d90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00a6d8b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a6d/00a6d8b4.md) [`00bd6e50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00900e24",
      "incomplete_value": false,
      "site": "00900e30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
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
      36,
      "DATA",
      [
        "storage",
        "00c09870",
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
        "00c09920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00900e24 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00900e24 ["COPY", "tmp:0:8", ["const:920:8"]]
~~~


### [`00901338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901338.md) → [`00901338`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901338.md) FUN_00901338

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090133c",
      "incomplete_value": false,
      "site": "00901340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
        "00c098c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      8,
      "DATA",
      [
        "storage",
        "00c09970",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0090133c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0090133c ["COPY", "tmp:0:8", ["const:970:8"]]
~~~


### [`00901388`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901388.md) → [`00901388`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901388.md) _INIT_180

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
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
    "old": {
      "definition_site": "00901428",
      "incomplete_value": true,
      "site": "00901440",
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 009013b4 ["COPY", "tmp:0:8", ["const:780:8"]]
+ 009013b4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 009013c0 ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 009013c0 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 009013dc ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 009013dc ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`00901718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901718.md) → [`00901718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901718.md) FUN_00901718

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac8f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 15件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`0044a6d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00464a54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464b8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00ac9054`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044a6d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00464a54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00901750",
      "incomplete_value": true,
      "site": "0090175c",
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
            "const:c78:8"
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
      "definition_site": "0090190c",
      "incomplete_value": true,
      "site": "00901910",
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
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      448,
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      452,
      "READ",
      [
        "storage",
        "00c1acc8",
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
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      448,
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      452,
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00901750 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00901750 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
+ 009018d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 009018dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cc8:8"]]
+ 009018dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
~~~


### [`00901d24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/00901d24.md) → [`00901d24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/00901d24.md) _INIT_181

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
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
    "old": {
      "definition_site": "00901d60",
      "incomplete_value": true,
      "site": "00901d7c",
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
                "const:2e4:8"
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
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
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
    "old": {
      "definition_site": "00901d84",
      "incomplete_value": true,
      "site": "00901da0",
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
                "const:2f7:8"
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
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
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
    "old": {
      "definition_site": "00901da4",
      "incomplete_value": true,
      "site": "00901dc0",
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
                "const:da:8"
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 00901d50 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00901d50 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00901d5c ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 00901d5c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00901d78 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 00901d78 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`009020e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00902/009020e4.md) → [`009020e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00902/009020e4.md) FUN_009020e4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac8f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 21件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044d/0044d968.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9054`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 21件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
    "old": {
      "definition_site": "00902128",
      "incomplete_value": false,
      "site": "00902134",
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
            "const:c78:8"
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
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
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
                "const:f46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902148",
      "incomplete_value": true,
      "site": "00902164",
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
                "const:eb9:8"
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
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00902878",
      "incomplete_value": true,
      "site": "00902888",
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
                "const:a7b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 111,
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
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00292eb9",
        null,
        "string"
      ]
    ],
    [
      500,
      "READ",
      [
        "storage",
        "002a5a42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      80,
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00292f46",
        null,
        "string"
      ]
    ],
    [
      500,
      "READ",
      [
        "storage",
        "002a5a3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00902128 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00902128 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00902140 ["COPY", "tmp:0:8", ["const:eb9:8"]]
+ 00902140 ["COPY", "tmp:0:8", ["const:f46:8"]]
- 009022d0 ["COPY", "tmp:0:8", ["const:a42:8"]]
+ 009022d0 ["COPY", "tmp:0:8", ["const:a3b:8"]]
~~~


### [`00904150`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/00904150.md) → [`00904150`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/00904150.md) _INIT_182

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
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
    "old": {
      "definition_site": "009041b0",
      "incomplete_value": true,
      "site": "009041cc",
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
                "const:2f7:8"
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
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
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
    "old": {
      "definition_site": "009041d0",
      "incomplete_value": true,
      "site": "009041ec",
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
                "const:da:8"
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
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
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
    "old": {
      "definition_site": "009041f0",
      "incomplete_value": true,
      "site": "00904208",
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 0090417c ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 0090417c ["COPY", "tmp:0:8", ["const:870:8"]]
- 00904188 ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 00904188 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 009041a4 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 009041a4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`009044e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00904/009044e0.md) → [`009044e0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00904/009044e0.md) FUN_009044e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac8f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 20件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046555c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046555c.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00ac9054`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 20件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
    "old": {
      "definition_site": "00904524",
      "incomplete_value": false,
      "site": "00904530",
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
            "const:c78:8"
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
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
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
                "const:b22:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00904544",
      "incomplete_value": true,
      "site": "0090455c",
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
                "const:a95:8"
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00904560",
      "incomplete_value": true,
      "site": "00904560",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
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
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "0029ca95",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "0029caa2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      80,
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "0029cb22",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "0029cb2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00904524 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00904524 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00904540 ["COPY", "tmp:0:8", ["const:a95:8"]]
+ 00904540 ["COPY", "tmp:0:8", ["const:b22:8"]]
- 009046b8 ["COPY", "tmp:0:8", ["const:bb9:8"]]
+ 009046b8 ["COPY", "tmp:0:8", ["const:c46:8"]]
~~~


### [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) → [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) FUN_00906b9c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`0086b704`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 51件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00906c3c",
      "incomplete_value": true,
      "site": "00906c58",
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
                "const:aab:8"
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00906c5c",
      "incomplete_value": true,
      "site": "00906c5c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:a29:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00906f9c",
      "incomplete_value": true,
      "site": "00906fac",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:99c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
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
        "0029caab",
        null,
        "string"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "0029cab8",
        null,
        "string"
      ]
    ],
    [
      668,
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      160,
      "READ",
      [
        "storage",
        "0029cb38",
        null,
        "string"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "0029cb45",
        null,
        "string"
      ]
    ],
    [
      668,
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00906c2c ["COPY", "tmp:0:8", ["const:aab:8"]]
- 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00906c2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00906c2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
~~~


### [`0090a308`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090a/0090a308.md) → [`0090a308`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a308.md) FUN_0090a308

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0090a130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0090a130`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090a/0090a130.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
    "old": {
      "definition_site": "0090a314",
      "incomplete_value": false,
      "site": "0090a318",
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
        "002a730a",
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
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0090a314 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0090a314 ["COPY", "tmp:0:8", ["const:303:8"]]
~~~


### [`0090f6f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f6f4.md) → [`0090f6f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f6f4.md) FUN_0090f6f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
    "old": {
      "definition_site": "0090f700",
      "incomplete_value": false,
      "site": "0090f704",
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
        "002a730a",
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
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0090f700 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0090f700 ["COPY", "tmp:0:8", ["const:303:8"]]
~~~


### [`0090f708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md) → [`0090f708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) FUN_0090f708

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) [`0090f708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) [`0090f708`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:30a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090f860",
      "incomplete_value": true,
      "site": "0090f868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:311:8"
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
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
    "old": {
      "definition_site": "0090f9b8",
      "incomplete_value": false,
      "site": "0090f9c0",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0090fa60",
      "incomplete_value": false,
      "site": "0090fa6c",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0090fa60",
      "incomplete_value": false,
      "site": "0090fa6c",
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
            "const:7da:8"
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
      344,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      688,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      856,
      "PARAM",
      [
        "storage",
        "002967da",
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
        "002a730a",
        null,
        null
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
    ],
    [
      856,
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0090f860 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 0090f860 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0090f9b8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 0090f9b8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0090fa60 ["COPY", "tmp:0:8", ["const:7da:8"]]
+ 0090fa60 ["COPY", "tmp:0:8", ["const:867:8"]]
~~~


### [`009101cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00910/009101cc.md) → [`009101cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00910/009101cc.md) FUN_009101cc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00906b9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00906/00906b9c.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
    "old": {
      "definition_site": "009101d8",
      "incomplete_value": false,
      "site": "009101dc",
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
        "002a730a",
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
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 009101d8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 009101d8 ["COPY", "tmp:0:8", ["const:303:8"]]
~~~


### [`00911e34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00911/00911e34.md) → [`00911e34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00911/00911e34.md) _INIT_183

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
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
    "old": {
      "definition_site": "00911e70",
      "incomplete_value": true,
      "site": "00911e8c",
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
                "const:2e4:8"
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
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
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
    "old": {
      "definition_site": "00911e94",
      "incomplete_value": true,
      "site": "00911eb0",
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
                "const:2f7:8"
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
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
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
    "old": {
      "definition_site": "00911eb4",
      "incomplete_value": true,
      "site": "00911ed0",
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
                "const:da:8"
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 00911e60 ["COPY", "tmp:0:8", ["const:7c8:8"]]
+ 00911e60 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00911e6c ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 00911e6c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00911e88 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 00911e88 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`0092bc08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md) → [`0092bc08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) FUN_0092bc08

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`005a7c94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a7/005a7c94.md) [`005dfeb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005df/005dfeb0.md) [`0063e6d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063e6d4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005a7c94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a7/005a7c94.md) [`005dfeb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md) [`0063e6d4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c71c",
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
                "const:f40:8"
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
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0092c720",
      "incomplete_value": false,
      "site": "0092c720",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0092c71c",
      "incomplete_value": false,
      "site": "0092c720",
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
                "const:f40:8"
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
    "ordinal": 39,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      2140,
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      2172,
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      2288,
      "READ",
      [
        "storage",
        "00c1adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      2140,
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      2172,
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      2288,
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0092c458 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 0092c45c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c458 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0092c45c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0092c45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0092c45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
~~~


### [`00938cc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00938/00938cc0.md) → [`00938cc0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00938/00938cc0.md) FUN_00938cc0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `boundary_candidate`

- 旧版 呼出元 0件  · 呼出先 4件 [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00827b94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827b94.md) [`009a6f44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/009a6/009a6f44.md) [`00ace4cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00827b94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827b94.md) [`009a6f44`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a6/009a6f44.md) [`00ace594`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md)

変更の種類 branch_condition_or_target, branch_count, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

優先判定に残った影響 `branch_count` 1件, `branch_value` 6件, `call_argument_candidate` 25件, `call_count` 1件, `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00937950",
      "incomplete_value": true,
      "site": "0093795c",
      "value": [
        "INT_SLESS",
        "1",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "leaf",
                "const:0:4"
              ],
              [
                "live",
                "register:4040:4"
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
    "old": {
      "definition_site": "00938ccc",
      "incomplete_value": true,
      "site": "00938ccc",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00938cdc",
      "incomplete_value": true,
      "site": "00938cdc",
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
    "old": {
      "definition_site": "00938cec",
      "incomplete_value": true,
      "site": "00938cec",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00938cec",
      "incomplete_value": true,
      "site": "00938cec",
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
      "definition_site": "00938cfc",
      "incomplete_value": true,
      "site": "00938cfc",
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
                "register:4040:4"
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
      112,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ],
    [
      244,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ],
    [
      260,
      "UNCONDITIONAL_JUMP",
      [
        "unresolved_target",
        "0093794c"
      ]
    ]
  ],
  "added": [
    [
      -4952,
      "READ",
      [
        "storage",
        "Stack[0x78]",
        null,
        null
      ]
    ],
    [
      -4920,
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00446d2c"
      ]
    ],
    [
      -4916,
      "UNCONDITIONAL_JUMP",
      [
        "unresolved_target",
        "0092ef94"
      ]
    ]
  ]
}
~~~


~~~diff
+ 0093794c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:16:8"]]
+ 0093794c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0093794c ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00937950 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00938d0c ["CBRANCH", null, ["local:b12:8", "tmp:3:1"]]
+ 00938d0c ["CBRANCH", null, ["local:b14:8", "tmp:3:1"]]
- 00938d24 ["CBRANCH", null, ["local:b12:8", "tmp:3:1"]]
+ 00938d24 ["CBRANCH", null, ["local:b14:8", "tmp:3:1"]]
~~~


### [`0093f290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f290.md) → [`0093f290`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0093f/0093f290.md) FUN_0093f290

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0092e43c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092e/0092e43c.md) · 呼出先 1件 [`00ace4cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md)
- 新版 呼出元 1件 [`0092e43c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092e/0092e43c.md) · 呼出先 1件 [`00ace594`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md)

変更の種類 call, call_target, operands_and_dependencies

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f298",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f298",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      8,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ]
  ]
}
~~~


~~~diff
- 0093f298 ["CALL", null, ["ram:ace4cc:8"]]
+ 0093f298 ["CALL", null, ["ram:ace594:8"]]
~~~


### [`0093f2dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0093f/0093f2dc.md) → [`0093f2dc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0093f/0093f2dc.md) FUN_0093f2dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0093249c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00932/0093249c.md) · 呼出先 3件 [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00ace4cc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ace/00ace4cc.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`0093249c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00932/0093249c.md) · 呼出先 3件 [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00ace594`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ace/00ace594.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call, call_target, operands_and_dependencies

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f2e4",
      "value": [
        "leaf",
        "ram:ace594:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0093f2e4",
      "value": [
        "leaf",
        "ram:ace4cc:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace4cc"
      ]
    ]
  ],
  "added": [
    [
      8,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ace594"
      ]
    ]
  ]
}
~~~


~~~diff
- 0093f2e4 ["CALL", null, ["ram:ace4cc:8"]]
+ 0093f2e4 ["CALL", null, ["ram:ace594:8"]]
~~~


### [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) → [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) FUN_009428a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00942564`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/00942564.md) [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00942564`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/00942564.md) [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
    "old": {
      "definition_site": "00942a38",
      "incomplete_value": false,
      "site": "00942a40",
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
            "const:311:8"
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
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
    "old": {
      "definition_site": "00942af0",
      "incomplete_value": false,
      "site": "00942af8",
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
            "const:2f5:8"
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
      "definition_site": "00943208",
      "incomplete_value": false,
      "site": "00943214",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00943208",
      "incomplete_value": false,
      "site": "00943214",
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
            "const:7da:8"
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
      404,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      588,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      1708,
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      404,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      588,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      1708,
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00942a38 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 00942a38 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00942af0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 00942af0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00942f50 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 00942f50 ["COPY", "tmp:0:8", ["const:672:8"]]
~~~


### [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) → [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) FUN_00943aa0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00942/009428a4.md) [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`009428a4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00942/009428a4.md) [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
    "old": {
      "definition_site": "00943c28",
      "incomplete_value": false,
      "site": "00943c30",
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
            "const:311:8"
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
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
    "old": {
      "definition_site": "00943ce0",
      "incomplete_value": false,
      "site": "00943ce8",
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
            "const:2f5:8"
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
      "definition_site": "009440f8",
      "incomplete_value": false,
      "site": "00944108",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009440f8",
      "incomplete_value": false,
      "site": "00944108",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      392,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      576,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      1624,
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      392,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      576,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      1624,
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00943c28 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 00943c28 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00943ce0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 00943ce0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 009440f8 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 009440f8 ["COPY", "tmp:0:8", ["const:672:8"]]
~~~


### [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) → [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) FUN_00944ab4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00943/00943aa0.md) [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00943aa0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00943/00943aa0.md) [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
    "old": {
      "definition_site": "00944c20",
      "incomplete_value": false,
      "site": "00944c28",
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
            "const:311:8"
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
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
    "old": {
      "definition_site": "00944db0",
      "incomplete_value": false,
      "site": "00944db8",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00944e88",
      "incomplete_value": false,
      "site": "00944e94",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00944e88",
      "incomplete_value": false,
      "site": "00944e94",
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
            "const:7da:8"
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
      364,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      764,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      980,
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
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
      764,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      980,
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00944c20 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 00944c20 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00944db0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 00944db0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00944e88 ["COPY", "tmp:0:8", ["const:7da:8"]]
+ 00944e88 ["COPY", "tmp:0:8", ["const:867:8"]]
~~~


### [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) → [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) FUN_00945a50

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00944/00944ab4.md) [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00944ab4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00944/00944ab4.md) [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) · 呼出先 21件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
    "old": {
      "definition_site": "00945bc8",
      "incomplete_value": false,
      "site": "00945bd0",
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
            "const:311:8"
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
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
    "old": {
      "definition_site": "00945c80",
      "incomplete_value": false,
      "site": "00945c88",
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
            "const:2f5:8"
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
      "definition_site": "00946044",
      "incomplete_value": false,
      "site": "00946054",
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
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00946044",
      "incomplete_value": false,
      "site": "00946054",
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
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      376,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      560,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      1524,
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      376,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      560,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      1524,
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00945bc8 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 00945bc8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00945c80 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 00945c80 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00946044 ["COPY", "tmp:0:8", ["const:5e5:8"]]
+ 00946044 ["COPY", "tmp:0:8", ["const:672:8"]]
~~~


### [`00946864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md) → [`00946864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) FUN_00946864

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00945/00945a50.md) [`00946864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00945a50`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00945/00945a50.md) [`00946864`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00946/00946864.md) · 呼出先 22件 [`00418c24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
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
            "const:867:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00946bc8",
      "incomplete_value": false,
      "site": "00946bd4",
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
            "const:7da:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094704c",
      "incomplete_value": false,
      "site": "00947054",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      356,
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      700,
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      868,
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      356,
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      700,
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      868,
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 009469c8 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 009469c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00946b20 ["COPY", "tmp:0:8", ["const:2f5:8"]]
+ 00946b20 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00946bc8 ["COPY", "tmp:0:8", ["const:7da:8"]]
+ 00946bc8 ["COPY", "tmp:0:8", ["const:867:8"]]
~~~


### [`0094757c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094757c.md) → [`0094757c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094757c.md) FUN_0094757c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947590",
      "incomplete_value": false,
      "site": "00947594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:910:8"
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
        "00c09910",
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
        "00c099c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00947590 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 00947590 ["COPY", "tmp:0:8", ["const:9c0:8"]]
~~~


### [`0094762c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/0094762c.md) → [`0094762c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/0094762c.md) FUN_0094762c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094764c",
      "incomplete_value": false,
      "site": "00947650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:990:8"
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
        "00c09990",
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
        "00c09a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094764c ["COPY", "tmp:0:8", ["const:990:8"]]
+ 0094764c ["COPY", "tmp:0:8", ["const:a40:8"]]
~~~


### [`00947684`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947684.md) → [`00947684`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947684.md) FUN_00947684

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md) [`0065ec80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065e/0065ec80.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0065ec80`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
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
                "const:976:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094771c",
      "incomplete_value": true,
      "site": "0094772c",
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
                "const:97d:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947774",
      "incomplete_value": false,
      "site": "00947774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      152,
      "READ",
      [
        "storage",
        "002a297d",
        null,
        "string"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00c09a00",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "READ",
      [
        "storage",
        "00c09a20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      152,
      "READ",
      [
        "storage",
        "002a2976",
        null,
        "string"
      ]
    ],
    [
      240,
      "DATA",
      [
        "storage",
        "00c09ab0",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "READ",
      [
        "storage",
        "00c09ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00947714 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 00947714 ["COPY", "tmp:0:8", ["const:976:8"]]
- 0094776c ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 0094776c ["COPY", "tmp:0:8", ["const:ab0:8"]]
~~~


### [`00947964`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947964.md) → [`00947964`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947964.md) FUN_00947964

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947988",
      "incomplete_value": false,
      "site": "00947988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
        "00c09a00",
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
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00947984 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00947984 ["COPY", "tmp:0:8", ["const:ab0:8"]]
~~~


### [`00947998`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947998.md) → [`00947998`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947998.md) FUN_00947998

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
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009479a4",
      "incomplete_value": false,
      "site": "009479a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
        "00c09a00",
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
        "00c09ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009479a0 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 009479a0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
~~~


### [`00947c00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947c00.md) → [`00947c00`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947c00.md) FUN_00947c00

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947c14",
      "incomplete_value": false,
      "site": "00947c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
        "00c09a90",
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
        "00c09b40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00947c14 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 00947c14 ["COPY", "tmp:0:8", ["const:b40:8"]]
~~~


### [`00947d34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00947/00947d34.md) → [`00947d34`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00947/00947d34.md) FUN_00947d34

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00947d48",
      "incomplete_value": true,
      "site": "00947d4c",
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
            "const:b10:8"
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
        "00c09b10",
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
        "00c09bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00947d48 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 00947d48 ["COPY", "tmp:0:8", ["const:bc0:8"]]
~~~


### [`00948440`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948440.md) → [`00948440`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948440.md) FUN_00948440

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948454",
      "incomplete_value": false,
      "site": "00948458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
        "00c09b90",
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
        "00c09c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00948454 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00948454 ["COPY", "tmp:0:8", ["const:c40:8"]]
~~~


### [`0094847c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/0094847c.md) → [`0094847c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/0094847c.md) FUN_0094847c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00447a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`0088600c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00447a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
      "definition_site": "00948884",
      "incomplete_value": true,
      "site": "00948884",
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
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
    "old": {
      "definition_site": "0094888c",
      "incomplete_value": false,
      "site": "0094889c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00948894",
      "incomplete_value": false,
      "site": "0094889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      1028,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      1040,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      1048,
      "PARAM",
      [
        "storage",
        "00bf3c50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      1028,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      1040,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      1048,
      "PARAM",
      [
        "storage",
        "00bf3d00",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 00948880 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0094888c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0094888c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00948894 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00948894 ["COPY", "tmp:0:8", ["const:d00:8"]]
~~~


### [`00948a24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948a24.md) → [`00948a24`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948a24.md) _INIT_184

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
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
    "old": {
      "definition_site": "00948aa4",
      "incomplete_value": true,
      "site": "00948ac0",
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
                "const:da:8"
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
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
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
    "old": {
      "definition_site": "00948ac4",
      "incomplete_value": true,
      "site": "00948adc",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
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
    "old": {
      "definition_site": "00948ae0",
      "incomplete_value": true,
      "site": "00948afc",
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
                "const:2e1:8"
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 00948a50 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00948a50 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00948a5c ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 00948a5c ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00948a78 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 00948a78 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`00948db4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00948/00948db4.md) → [`00948db4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00948/00948db4.md) FUN_00948db4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00949ed8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`005748e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/005748e4.md) [`00574bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574bb4.md) [`009496f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/009496f0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00949ed8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) · 呼出先 6件 [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005748e4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) [`00574bb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574bb4.md) [`009496f0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/009496f0.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "009491d0",
      "incomplete_value": true,
      "site": "009491d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949328",
      "incomplete_value": true,
      "site": "00949328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 68,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009494c4",
      "incomplete_value": true,
      "site": "009494c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:62c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      308,
      "READ",
      [
        "storage",
        "002abee4",
        null,
        "string"
      ]
    ],
    [
      580,
      "READ",
      [
        "storage",
        "002a779e",
        null,
        "string"
      ]
    ],
    [
      1040,
      "READ",
      [
        "storage",
        "002936c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      308,
      "READ",
      [
        "storage",
        "002abeea",
        null,
        "string"
      ]
    ],
    [
      580,
      "READ",
      [
        "storage",
        "002a770a",
        null,
        "string"
      ]
    ],
    [
      1040,
      "READ",
      [
        "storage",
        "0029374e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00948ee0 ["COPY", "tmp:0:8", ["const:ee4:8"]]
+ 00948ee0 ["COPY", "tmp:0:8", ["const:eea:8"]]
- 00948ff0 ["COPY", "tmp:0:8", ["const:79e:8"]]
+ 00948ff0 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 009491b8 ["COPY", "tmp:0:8", ["const:6c1:8"]]
+ 009491b8 ["COPY", "tmp:0:8", ["const:74e:8"]]
~~~


### [`00949c4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949c4c.md) → [`00949c4c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) FUN_00949c4c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00428cb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428cb4.md) [`00428e88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428e88.md) [`0053ee5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053e/0053ee5c.md) [`0053f0f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053f/0053f0f8.md)
- 新版 呼出元 1件 [`00419718`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) · 呼出先 11件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00428cb4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428cb4.md) [`00428e88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428e88.md) [`0053ee5c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`0053f0f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00949d00",
      "incomplete_value": false,
      "site": "00949d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "00949cd8",
      "incomplete_value": true,
      "site": "00949ce0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cd8:8"
              ]
            ]
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
      140,
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ],
    [
      180,
      "DATA",
      [
        "storage",
        "00c09c28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      140,
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      140,
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      180,
      "DATA",
      [
        "storage",
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
+ 00949cd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
- 00949cf8 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00949cf8 ["COPY", "tmp:0:8", ["const:cd8:8"]]
~~~


### [`00949ed8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00949/00949ed8.md) → [`00949ed8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949ed8.md) FUN_00949ed8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0094bc30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md) [`00ac8f8c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 26件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md) [`0045f0ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f0ac.md)
- 新版 呼出元 2件 [`0094bc30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) [`00ac9054`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 26件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f0ac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f0ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00949f44",
      "incomplete_value": true,
      "site": "00949f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cb:8"
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
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0094a010",
      "incomplete_value": true,
      "site": "0094a010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
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
    "old": {
      "definition_site": "0094a254",
      "incomplete_value": true,
      "site": "0094a264",
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
                "const:79e:8"
              ]
            ]
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
      88,
      "READ",
      [
        "storage",
        "002a57cb",
        null,
        "string"
      ]
    ],
    [
      128,
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      296,
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
      88,
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      128,
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      296,
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00949f24 ["COPY", "tmp:0:8", ["const:7cb:8"]]
+ 00949f24 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 00949f58 ["COPY", "tmp:0:8", ["const:253:8"]]
+ 00949f58 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 00949ff8 ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 00949ff8 ["COPY", "tmp:0:8", ["const:952:8"]]
~~~


### [`0094ac20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094ac20.md) → [`0094ac20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094a/0094ac20.md) FUN_0094ac20

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00868124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) [`0094abb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094abb8.md) · 呼出先 13件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00469e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`0046ad74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ad74.md) [`0046d7c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md)
- 新版 呼出元 2件 [`00868124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`0094abb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094a/0094abb8.md) · 呼出先 13件 [`00418fe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`0046ad74`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad74.md) [`0046d7c4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d7c4.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094af80",
      "incomplete_value": true,
      "site": "0094af80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094af80",
      "incomplete_value": true,
      "site": "0094af80",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:4a1:8"
              ]
            ]
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
      848,
      "READ",
      [
        "storage",
        "002aa4a1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      848,
      "READ",
      [
        "storage",
        "002aa4a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094af68 ["COPY", "tmp:0:8", ["const:4a1:8"]]
+ 0094af68 ["COPY", "tmp:0:8", ["const:4a7:8"]]
~~~


### [`0094bbe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bbe0.md) → [`0094bbe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bbe0.md) FUN_0094bbe0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc04",
      "incomplete_value": false,
      "site": "0094bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
        "00c09c28",
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
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094bc00 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 0094bc00 ["COPY", "tmp:0:8", ["const:cd8:8"]]
~~~


### [`0094bc14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc14.md) → [`0094bc14`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc14.md) FUN_0094bc14

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
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094bc20",
      "incomplete_value": false,
      "site": "0094bc20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
        "00c09c28",
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
        "00c09cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094bc1c ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 0094bc1c ["COPY", "tmp:0:8", ["const:cd8:8"]]
~~~


### [`0094bc30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094b/0094bc30.md) → [`0094bc30`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094b/0094bc30.md) FUN_0094bc30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md) [`0045f524`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f524.md) [`0045f660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f660.md) [`0045f6d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045f6d8.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0041b064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0045e558`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md) [`0045f524`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f524.md) [`0045f660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f660.md) [`0045f6d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045f6d8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0094bd0c",
      "incomplete_value": true,
      "site": "0094bd0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cb:8"
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
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0094bdd4",
      "incomplete_value": true,
      "site": "0094bdd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
    "old": {
      "definition_site": "0094bec8",
      "incomplete_value": false,
      "site": "0094becc",
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
                "const:470:8"
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
      200,
      "READ",
      [
        "storage",
        "002a57cb",
        null,
        "string"
      ]
    ],
    [
      240,
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      404,
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
      200,
      "READ",
      [
        "storage",
        "002a57c4",
        null,
        "string"
      ]
    ],
    [
      240,
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      404,
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094bcec ["COPY", "tmp:0:8", ["const:7cb:8"]]
+ 0094bcec ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 0094bd20 ["COPY", "tmp:0:8", ["const:253:8"]]
+ 0094bd20 ["COPY", "tmp:0:8", ["const:1bf:8"]]
- 0094bdbc ["COPY", "tmp:0:8", ["const:8c5:8"]]
+ 0094bdbc ["COPY", "tmp:0:8", ["const:952:8"]]
~~~


### [`0094c570`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094c570.md) → [`0094c570`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c570.md) FUN_0094c570

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0094c174`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0094c174`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094c174.md) · 呼出先 1件 [`00418c38`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
    "old": {
      "definition_site": "0094c57c",
      "incomplete_value": false,
      "site": "0094c580",
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
        "002a730a",
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
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094c57c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0094c57c ["COPY", "tmp:0:8", ["const:303:8"]]
~~~


### [`0094cd94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094c/0094cd94.md) → [`0094cd94`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094c/0094cd94.md) _INIT_185

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
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
    "old": {
      "definition_site": "0094cdd0",
      "incomplete_value": true,
      "site": "0094cdec",
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
                "const:2e4:8"
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
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
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
    "old": {
      "definition_site": "0094cdf4",
      "incomplete_value": true,
      "site": "0094ce10",
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
                "const:2f7:8"
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
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
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
    "old": {
      "definition_site": "0094ce14",
      "incomplete_value": true,
      "site": "0094ce30",
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
                "const:da:8"
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
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002a80da",
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
  ]
}
~~~


~~~diff
- 0094cdc0 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 0094cdc0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0094cdcc ["COPY", "tmp:0:8", ["const:2e4:8"]]
+ 0094cdcc ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 0094cde8 ["COPY", "tmp:0:8", ["const:2f7:8"]]
+ 0094cde8 ["COPY", "tmp:0:8", ["const:2f0:8"]]
~~~


### [`0094d124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094d/0094d124.md) → [`0094d124`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md) FUN_0094d124

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0094f7d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459a90.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`004752f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004752f8.md) [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060d/0060d83c.md)
- 新版 呼出元 2件 [`0094f7d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 22件 [`00459a90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`004752f8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md) [`0060d83c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 36件, `store_condition` 2件, `store_destination` 31件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094d178",
      "incomplete_value": true,
      "site": "0094d178",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
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
                "const:b55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094df6c",
      "incomplete_value": true,
      "site": "0094df80",
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 99,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0094e0c4",
      "incomplete_value": true,
      "site": "0094e0d8",
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
                "const:b55:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094e0c4",
      "incomplete_value": true,
      "site": "0094e0d8",
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 114,
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
      "READ",
      [
        "storage",
        "00c24630",
        null,
        "undefined4"
      ]
    ],
    [
      84,
      "WRITE",
      [
        "storage",
        "00c24630",
        null,
        "undefined4"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      68,
      "READ",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      84,
      "WRITE",
      [
        "storage",
        "00c246e0",
        null,
        "undefined4"
      ]
    ],
    [
      88,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:630:8"]]
- 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 0094d16c ["INT_LESSEQUAL", "register:105:1", ["register:40c0:4", "register:4048:4"]]
+ 0094d168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6e0:8"]]
+ 0094d168 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0094d168 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 0094d16c ["INT_LESSEQUAL", "register:105:1", ["register:40c0:4", "register:4048:4"]]
~~~


### [`0094efec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094e/0094efec.md) → [`0094efec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md) FUN_0094efec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00680c84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00680/00680c84.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00640490`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00640/00640490.md) [`0066f824`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0066f/0066f824.md) [`0094f64c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f64c.md)
- 新版 呼出元 2件 [`00680c84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 14件 [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00640490`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md) [`0066f824`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f824.md) [`0094f64c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f64c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 13件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3dc",
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
                "const:f40:8"
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
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094f3e0",
      "incomplete_value": false,
      "site": "0094f3e0",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0094f3dc",
      "incomplete_value": false,
      "site": "0094f3e0",
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
                "const:f40:8"
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
      72,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      92,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      72,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      92,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 0094f034 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0094f048 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0094f048 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0094f050 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0094f050 ["COPY", "tmp:0:8", ["const:d48:8"]]
~~~


### [`00957320`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957320.md) → [`00957320`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957320.md) FUN_00957320

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00680c84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00680/00680c84.md) [`0092bc08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0092b/0092bc08.md) [`0094f7d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094f/0094f7d0.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042cde4.md) [`0044b660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`005bdd1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005bd/005bdd1c.md) [`005dfeb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005df/005dfeb0.md)
- 新版 呼出元 4件 [`00680c84`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00680/00680c84.md) [`0092bc08`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) [`0094f7d0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094f/0094f7d0.md) [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 18件 [`0042cde4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`0044b660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`0045ba04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`005bdd1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bd/005bdd1c.md) [`005dfeb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfeb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
      "definition_site": "009573ac",
      "incomplete_value": true,
      "site": "009573ac",
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
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
    "old": {
      "definition_site": "009573b4",
      "incomplete_value": false,
      "site": "009573c4",
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
            "const:d98:8"
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
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009573bc",
      "incomplete_value": false,
      "site": "009573c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      136,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      136,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 009573a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 009573b4 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 009573b4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 009573bc ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 009573bc ["COPY", "tmp:0:8", ["const:d48:8"]]
~~~


### [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) → [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) FUN_00957f9c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00449bac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449bac.md) [`0044b660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b660.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 128件 [`0041b298`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0044b660`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b660.md) [`00457e1c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 65件, `store_condition` 2件, `store_destination` 40件, `store_value` 18件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
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
                "const:2dc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009583ec",
      "incomplete_value": true,
      "site": "009583fc",
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
                "const:24f:8"
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
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
      "definition_site": "009583f0",
      "incomplete_value": true,
      "site": "00958400",
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00958424",
      "incomplete_value": false,
      "site": "00958424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      1104,
      "READ",
      [
        "storage",
        "0029824f",
        null,
        "string"
      ]
    ],
    [
      1108,
      "READ",
      [
        "storage",
        "0029825c",
        null,
        "string"
      ]
    ],
    [
      1160,
      "DATA",
      [
        "storage",
        "00c09fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      1104,
      "READ",
      [
        "storage",
        "002982dc",
        null,
        "string"
      ]
    ],
    [
      1108,
      "READ",
      [
        "storage",
        "002982e9",
        null,
        "string"
      ]
    ],
    [
      1160,
      "DATA",
      [
        "storage",
        "00c0a068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 009583e4 ["COPY", "tmp:0:8", ["const:24f:8"]]
- 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["COPY", "tmp:0:8", ["const:2dc:8"]]
+ 009583e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009583e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
~~~


### [`00960d40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00960/00960d40.md) → [`00960d40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00960/00960d40.md) FUN_00960d40

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`008865b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`008879f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/008879f4.md) [`0096dfdc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfdc.md) [`0096dfe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096dfe0.md)
- 新版 呼出元 1件 [`00957f9c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00957/00957f9c.md) · 呼出先 7件 [`00469f7c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`008865b0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0096dfdc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfdc.md) [`0096dfe0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096dfe0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d7c",
      "incomplete_value": true,
      "site": "00960d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:26d:8"
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
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d74",
      "incomplete_value": true,
      "site": "00960d80",
      "value": [
        "LOAD",
        "8",
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
                "const:7:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00960d98",
      "incomplete_value": false,
      "site": "00960da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      36,
      "READ",
      [
        "storage",
        "0029826d",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00298274",
        null,
        "string"
      ]
    ],
    [
      96,
      "DATA",
      [
        "storage",
        "00c0a1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002982fa",
        null,
        "string"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00298301",
        null,
        "string"
      ]
    ],
    [
      96,
      "DATA",
      [
        "storage",
        "00c0a268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00960d5c ["COPY", "tmp:0:8", ["const:26d:8"]]
+ 00960d5c ["COPY", "tmp:0:8", ["const:2fa:8"]]
- 00960d98 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 00960d98 ["COPY", "tmp:0:8", ["const:268:8"]]
~~~


### [`009613bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md) → [`009613bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) FUN_009613bc

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md)
- 新版 呼出元 1件 [`00827ba0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 35件 [`00419064`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
      "definition_site": "00961444",
      "incomplete_value": true,
      "site": "00961444",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
      "definition_site": "0096149c",
      "incomplete_value": true,
      "site": "0096149c",
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
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
    "old": {
      "definition_site": "0096144c",
      "incomplete_value": false,
      "site": "0096145c",
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
            "const:d98:8"
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
      100,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      152,
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      152,
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:9b8:8"]]
- 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00961424 ["INT_LEFT", "tmp:0:8", ["const:32e:8", "const:c:4"]]
- 00961424 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00961420 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a78:8"]]
+ 00961420 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00961424 ["INT_LEFT", "tmp:0:8", ["const:32e:8", "const:c:4"]]
+ 00961424 ["COPY", "tmp:1:8", ["tmp:0:8"]]
~~~


### [`00965df0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00965/00965df0.md) → [`00965df0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00965/00965df0.md) FUN_00965df0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`009613bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00961/009613bc.md) [`0096de04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00445044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md)
- 新版 呼出元 2件 [`009613bc`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00961/009613bc.md) [`0096de04`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096de04.md) · 呼出先 33件 [`00444c54`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445044`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) [`0044507c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e48",
      "incomplete_value": true,
      "site": "00965e48",
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
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
    "old": {
      "definition_site": "00965e50",
      "incomplete_value": false,
      "site": "00965e60",
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
            "const:d98:8"
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
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00965e58",
      "incomplete_value": false,
      "site": "00965e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      76,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      96,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      76,
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      96,
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00965e40 ["INT_LEFT", "tmp:0:8", ["const:32f:8", "const:c:4"]]
- 00965e40 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00965e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00965e3c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00965e40 ["INT_LEFT", "tmp:0:8", ["const:32f:8", "const:c:4"]]
+ 00965e40 ["COPY", "tmp:1:8", ["tmp:0:8"]]
~~~


### [`0096b7d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096b/0096b7d8.md) → [`0096b7d8`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096b/0096b7d8.md) FUN_0096b7d8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963004`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444988.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00447a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00447/00447a10.md) [`00448034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448034.md) [`00bdaf90`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00963004`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00963/00963004.md) · 呼出先 6件 [`00444988`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00447a10`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00448034`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00bdb040`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b81c",
      "incomplete_value": true,
      "site": "0096b81c",
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
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
    "old": {
      "definition_site": "0096b824",
      "incomplete_value": false,
      "site": "0096b838",
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
            "const:d98:8"
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
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096b82c",
      "incomplete_value": false,
      "site": "0096b838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf3000:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      64,
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      84,
      "PARAM",
      [
        "storage",
        "00bf3c98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
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
        "00bf3d48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
+ 0096b818 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0096b824 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 0096b824 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0096b82c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 0096b82c ["COPY", "tmp:0:8", ["const:d48:8"]]
~~~


### [`0096d13c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d13c.md) → [`0096d13c`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d13c.md) FUN_0096d13c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d160",
      "incomplete_value": false,
      "site": "0096d160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
        "00c09ca8",
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
        "00c09d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0096d15c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 0096d15c ["COPY", "tmp:0:8", ["const:d58:8"]]
~~~


### [`0096d530`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0096d/0096d530.md) → [`0096d530`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d530.md) FUN_0096d530

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](https://github.com/sinsuirakv0/KBCS/blob/668fae668b310448d5966384f610aefa9bc5e4bf/research/reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0096d554",
      "incomplete_value": false,
      "site": "0096d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
        "00c09d38",
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
        "00c09de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0096d550 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0096d550 ["COPY", "tmp:0:8", ["const:de8:8"]]
~~~


