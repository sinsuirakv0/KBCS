# v16.0.1 → v16.0.2 · 最優先の変更候補 (46)

[一覧の目次](README.md)

### [`00830e9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830e9c.md) → [`00830ef4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830ef4.md) FUN_00830ef4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00acacc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acacc8.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00acad38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acad38.md)

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
      "site": "00830f1c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00830ec4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00830ec4 ["INT_ADD", "register:40f0:8", ["const:830ec4:8", "const:4:8"]]
- 00830ec4 ["CALL", null, ["ram:47acf4:8"]]
+ 00830f1c ["INT_ADD", "register:40f0:8", ["const:830f1c:8", "const:4:8"]]
+ 00830f1c ["CALL", null, ["ram:47ad34:8"]]
- 00830ed0 ["INT_ADD", "register:40f0:8", ["const:830ed0:8", "const:4:8"]]
+ 00830f28 ["INT_ADD", "register:40f0:8", ["const:830f28:8", "const:4:8"]]
- 00830ef4 ["INT_ADD", "register:40f0:8", ["const:830ef4:8", "const:4:8"]]
+ 00830f4c ["INT_ADD", "register:40f0:8", ["const:830f4c:8", "const:4:8"]]
~~~


### [`00830f44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f44.md) → [`00830f9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830f9c.md) FUN_00830f9c

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
      "definition_site": "00830fa8",
      "incomplete_value": false,
      "site": "00830fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830f50",
      "incomplete_value": false,
      "site": "00830f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
        "00c7e6b8",
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
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00830f50 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00830fa8 ["COPY", "tmp:0:8", ["const:788:8"]]
~~~


### [`00830f88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830f88.md) → [`00830fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00830/00830fe0.md) FUN_00830fe0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00830ff8",
      "incomplete_value": false,
      "site": "00831004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00830fa0",
      "incomplete_value": false,
      "site": "00830fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
        "00c7e6b8",
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
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00830fa0 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00830ff8 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00830fd0 ["INT_ADD", "register:40f0:8", ["const:830fd0:8", "const:4:8"]]
+ 00831028 ["INT_ADD", "register:40f0:8", ["const:831028:8", "const:4:8"]]
~~~


### [`00830fe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00830/00830fe4.md) → [`0083103c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083103c.md) FUN_0083103c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831068",
      "incomplete_value": false,
      "site": "00831068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831010",
      "incomplete_value": false,
      "site": "00831010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
        "00c7e6b8",
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
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00830ff8 ["INT_ADD", "register:40f0:8", ["const:830ff8:8", "const:4:8"]]
+ 00831050 ["INT_ADD", "register:40f0:8", ["const:831050:8", "const:4:8"]]
- 00831008 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00831060 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0083102c ["INT_ADD", "register:40f0:8", ["const:83102c:8", "const:4:8"]]
+ 00831084 ["INT_ADD", "register:40f0:8", ["const:831084:8", "const:4:8"]]
~~~


### [`0083106c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083106c.md) → [`008310c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008310c4.md) FUN_008310c4

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
      "definition_site": "008310e0",
      "incomplete_value": false,
      "site": "008310e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831088",
      "incomplete_value": false,
      "site": "00831088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:6b8:8"
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
        "00c7e6b8",
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
        "00c7e788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831084 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 008310dc ["COPY", "tmp:0:8", ["const:788:8"]]
- 008310a8 ["INT_ADD", "register:40f0:8", ["const:8310a8:8", "const:4:8"]]
+ 00831100 ["INT_ADD", "register:40f0:8", ["const:831100:8", "const:4:8"]]
~~~


### [`00831168`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831168.md) → [`008311c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008311c0.md) FUN_008311c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "008311e8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831190",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831190 ["INT_ADD", "register:40f0:8", ["const:831190:8", "const:4:8"]]
- 00831190 ["CALL", null, ["ram:47acf4:8"]]
+ 008311e8 ["INT_ADD", "register:40f0:8", ["const:8311e8:8", "const:4:8"]]
+ 008311e8 ["CALL", null, ["ram:47ad34:8"]]
- 0083119c ["INT_ADD", "register:40f0:8", ["const:83119c:8", "const:4:8"]]
+ 008311f4 ["INT_ADD", "register:40f0:8", ["const:8311f4:8", "const:4:8"]]
~~~


### [`008311e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008311e0.md) → [`00831238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831238.md) FUN_00831238

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083125c",
      "incomplete_value": false,
      "site": "0083125c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831204",
      "incomplete_value": false,
      "site": "00831204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
        "00c7e738",
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
        "00c7e808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008311f4 ["INT_ADD", "register:40f0:8", ["const:8311f4:8", "const:4:8"]]
+ 0083124c ["INT_ADD", "register:40f0:8", ["const:83124c:8", "const:4:8"]]
- 00831200 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00831258 ["COPY", "tmp:0:8", ["const:808:8"]]
~~~


### [`00831214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831214.md) → [`0083126c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083126c.md) FUN_0083126c

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
      "definition_site": "00831278",
      "incomplete_value": false,
      "site": "00831278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831220",
      "incomplete_value": false,
      "site": "00831220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:738:8"
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
        "00c7e738",
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
        "00c7e808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083121c ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00831274 ["COPY", "tmp:0:8", ["const:808:8"]]
~~~


### [`00831230`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831230.md) → [`00831288`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831288.md) FUN_00831288

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "008312ac",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831254",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831254 ["INT_ADD", "register:40f0:8", ["const:831254:8", "const:4:8"]]
- 00831254 ["CALL", null, ["ram:47acf4:8"]]
+ 008312ac ["INT_ADD", "register:40f0:8", ["const:8312ac:8", "const:4:8"]]
+ 008312ac ["CALL", null, ["ram:47ad34:8"]]
- 00831260 ["INT_ADD", "register:40f0:8", ["const:831260:8", "const:4:8"]]
+ 008312b8 ["INT_ADD", "register:40f0:8", ["const:8312b8:8", "const:4:8"]]
~~~


### [`008312a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312a4.md) → [`008312fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008312fc.md) FUN_008312fc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831320",
      "incomplete_value": false,
      "site": "00831320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008312c8",
      "incomplete_value": false,
      "site": "008312c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
        "00c7e7b8",
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
        "00c7e888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008312b8 ["INT_ADD", "register:40f0:8", ["const:8312b8:8", "const:4:8"]]
+ 00831310 ["INT_ADD", "register:40f0:8", ["const:831310:8", "const:4:8"]]
- 008312c4 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 0083131c ["COPY", "tmp:0:8", ["const:888:8"]]
~~~


### [`008312d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312d8.md) → [`00831330`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831330.md) FUN_00831330

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
      "definition_site": "0083133c",
      "incomplete_value": false,
      "site": "0083133c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008312e4",
      "incomplete_value": false,
      "site": "008312e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:7b8:8"
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
        "00c7e7b8",
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
        "00c7e888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008312e0 ["COPY", "tmp:0:8", ["const:7b8:8"]]
+ 00831338 ["COPY", "tmp:0:8", ["const:888:8"]]
~~~


### [`008312f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008312f4.md) → [`0083134c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083134c.md) FUN_0083134c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 20件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0081fdc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081f/0081fdc8.md) [`0082907c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/0082907c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0081fe20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0081f/0081fe20.md) [`008290d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008290d4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00831424",
      "incomplete_value": true,
      "site": "00831434",
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
                "const:9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008313cc",
      "incomplete_value": true,
      "site": "008313dc",
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
                "const:6d:8"
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
      "definition_site": "00831438",
      "incomplete_value": true,
      "site": "00831438",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008313e0",
      "incomplete_value": true,
      "site": "008313e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0083142c",
      "incomplete_value": true,
      "site": "0083143c",
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
    "old": {
      "definition_site": "008313d4",
      "incomplete_value": true,
      "site": "008313e4",
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
                "const:450:8"
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
      68,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "002b406d",
        null,
        "string"
      ]
    ],
    [
      220,
      "READ",
      [
        "storage",
        "002b407c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      68,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      216,
      "READ",
      [
        "storage",
        "002b409e",
        null,
        "string"
      ]
    ],
    [
      220,
      "READ",
      [
        "storage",
        "002b40ad",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831334 ["INT_ADD", "register:40f0:8", ["const:831334:8", "const:4:8"]]
+ 0083138c ["INT_ADD", "register:40f0:8", ["const:83138c:8", "const:4:8"]]
- 00831338 ["INT_ADD", "register:40f0:8", ["const:831338:8", "const:4:8"]]
- 00831338 ["CALL", null, ["ram:47acf4:8"]]
+ 00831390 ["INT_ADD", "register:40f0:8", ["const:831390:8", "const:4:8"]]
+ 00831390 ["CALL", null, ["ram:47ad34:8"]]
- 00831374 ["INT_ADD", "register:40f0:8", ["const:831374:8", "const:4:8"]]
+ 008313cc ["INT_ADD", "register:40f0:8", ["const:8313cc:8", "const:4:8"]]
~~~


### [`008316cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008316cc.md) → [`00831724`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831724.md) FUN_00831724

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831748",
      "incomplete_value": false,
      "site": "00831748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008316f0",
      "incomplete_value": false,
      "site": "008316f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
        "00c7e828",
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
        "00c7e8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008316e0 ["INT_ADD", "register:40f0:8", ["const:8316e0:8", "const:4:8"]]
+ 00831738 ["INT_ADD", "register:40f0:8", ["const:831738:8", "const:4:8"]]
- 008316ec ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00831744 ["COPY", "tmp:0:8", ["const:8f8:8"]]
~~~


### [`00831700`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831700.md) → [`00831758`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831758.md) FUN_00831758

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
      "definition_site": "00831764",
      "incomplete_value": false,
      "site": "00831764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083170c",
      "incomplete_value": false,
      "site": "0083170c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
        "00c7e828",
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
        "00c7e8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831708 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00831760 ["COPY", "tmp:0:8", ["const:8f8:8"]]
~~~


### [`0083171c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083171c.md) → [`00831774`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831774.md) FUN_00831774

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "00831798",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831740",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831740 ["INT_ADD", "register:40f0:8", ["const:831740:8", "const:4:8"]]
- 00831740 ["CALL", null, ["ram:47acf4:8"]]
+ 00831798 ["INT_ADD", "register:40f0:8", ["const:831798:8", "const:4:8"]]
+ 00831798 ["CALL", null, ["ram:47ad34:8"]]
- 0083174c ["INT_ADD", "register:40f0:8", ["const:83174c:8", "const:4:8"]]
+ 008317a4 ["INT_ADD", "register:40f0:8", ["const:8317a4:8", "const:4:8"]]
~~~


### [`0083178c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/0083178c.md) → [`008317e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317e4.md) FUN_008317e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00829574`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00829/00829574.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 1件 [`008295cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00829/008295cc.md) · 呼出先 1件 [`00442970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008317f0",
      "incomplete_value": false,
      "site": "008317f4",
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
    "old": {
      "definition_site": "00831798",
      "incomplete_value": false,
      "site": "0083179c",
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
            "const:f4c:8"
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
        "002b7f4c",
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
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831798 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 008317f0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0083179c ["INT_ADD", "register:40f0:8", ["const:83179c:8", "const:4:8"]]
+ 008317f4 ["INT_ADD", "register:40f0:8", ["const:8317f4:8", "const:4:8"]]
~~~


### [`008317a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317a4.md) → [`008317fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/008317fc.md) FUN_008317fc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831820",
      "incomplete_value": false,
      "site": "00831820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008317c8",
      "incomplete_value": false,
      "site": "008317c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
        "00c7e8b8",
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
        "00c7e988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008317b8 ["INT_ADD", "register:40f0:8", ["const:8317b8:8", "const:4:8"]]
+ 00831810 ["INT_ADD", "register:40f0:8", ["const:831810:8", "const:4:8"]]
- 008317c4 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 0083181c ["COPY", "tmp:0:8", ["const:988:8"]]
~~~


### [`008317d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317d8.md) → [`00831830`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831830.md) FUN_00831830

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
      "definition_site": "0083183c",
      "incomplete_value": false,
      "site": "0083183c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008317e4",
      "incomplete_value": false,
      "site": "008317e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:8b8:8"
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
        "00c7e8b8",
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
        "00c7e988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008317e0 ["COPY", "tmp:0:8", ["const:8b8:8"]]
+ 00831838 ["COPY", "tmp:0:8", ["const:988:8"]]
~~~


### [`008317f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/008317f4.md) → [`0083184c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/0083184c.md) FUN_0083184c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00826dbc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00826/00826dbc.md) [`008276c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00827/008276c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00442970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00826e14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00826/00826e14.md) [`00827718`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00827/00827718.md)

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
      "site": "00831884",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0083182c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00831a30",
      "incomplete_value": false,
      "site": "00831a34",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008319d8",
      "incomplete_value": false,
      "site": "008319dc",
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
            "const:1bd:8"
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
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      484,
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      56,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      484,
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083182c ["INT_ADD", "register:40f0:8", ["const:83182c:8", "const:4:8"]]
- 0083182c ["CALL", null, ["ram:47acf4:8"]]
+ 00831884 ["INT_ADD", "register:40f0:8", ["const:831884:8", "const:4:8"]]
+ 00831884 ["CALL", null, ["ram:47ad34:8"]]
- 00831858 ["INT_ADD", "register:40f0:8", ["const:831858:8", "const:4:8"]]
+ 008318b0 ["INT_ADD", "register:40f0:8", ["const:8318b0:8", "const:4:8"]]
- 008318ac ["INT_ADD", "register:40f0:8", ["const:8318ac:8", "const:4:8"]]
+ 00831904 ["INT_ADD", "register:40f0:8", ["const:831904:8", "const:4:8"]]
~~~


### [`00831ce8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ce8.md) → [`00831d40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d40.md) FUN_00831d40

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831d60",
      "incomplete_value": false,
      "site": "00831d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831d08",
      "incomplete_value": false,
      "site": "00831d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
        "00c7e938",
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
        "00c7ea08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831cfc ["INT_ADD", "register:40f0:8", ["const:831cfc:8", "const:4:8"]]
+ 00831d54 ["INT_ADD", "register:40f0:8", ["const:831d54:8", "const:4:8"]]
- 00831d08 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00831d60 ["COPY", "tmp:0:8", ["const:a08:8"]]
~~~


### [`00831d20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d20.md) → [`00831d78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d78.md) FUN_00831d78

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
      "definition_site": "00831d7c",
      "incomplete_value": false,
      "site": "00831d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831d24",
      "incomplete_value": false,
      "site": "00831d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:938:8"
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
        "00c7e938",
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
        "00c7ea08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831d24 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00831d7c ["COPY", "tmp:0:8", ["const:a08:8"]]
~~~


### [`00831d40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831d40.md) → [`00831d98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831d98.md) FUN_00831d98

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082c864`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b6efc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

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
      "site": "00831dc0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831d68",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00831dcc",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831d74",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831d68 ["INT_ADD", "register:40f0:8", ["const:831d68:8", "const:4:8"]]
- 00831d68 ["CALL", null, ["ram:47acf4:8"]]
+ 00831dc0 ["INT_ADD", "register:40f0:8", ["const:831dc0:8", "const:4:8"]]
+ 00831dc0 ["CALL", null, ["ram:47ad34:8"]]
- 00831d74 ["INT_ADD", "register:40f0:8", ["const:831d74:8", "const:4:8"]]
- 00831d74 ["CALL", null, ["ram:47acf4:8"]]
+ 00831dcc ["INT_ADD", "register:40f0:8", ["const:831dcc:8", "const:4:8"]]
+ 00831dcc ["CALL", null, ["ram:47ad34:8"]]
- 00831da0 ["INT_ADD", "register:40f0:8", ["const:831da0:8", "const:4:8"]]
+ 00831df8 ["INT_ADD", "register:40f0:8", ["const:831df8:8", "const:4:8"]]
~~~


### [`00831e94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831e94.md) → [`00831eec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831eec.md) FUN_00831eec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00831f10",
      "incomplete_value": false,
      "site": "00831f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831eb8",
      "incomplete_value": false,
      "site": "00831eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
        "00c7e9b8",
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
        "00c7ea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831ea8 ["INT_ADD", "register:40f0:8", ["const:831ea8:8", "const:4:8"]]
+ 00831f00 ["INT_ADD", "register:40f0:8", ["const:831f00:8", "const:4:8"]]
- 00831eb4 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00831f0c ["COPY", "tmp:0:8", ["const:a88:8"]]
~~~


### [`00831ec8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ec8.md) → [`00831f20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f20.md) FUN_00831f20

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
      "definition_site": "00831f2c",
      "incomplete_value": false,
      "site": "00831f2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831ed4",
      "incomplete_value": false,
      "site": "00831ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
        "00c7e9b8",
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
        "00c7ea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831ed0 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00831f28 ["COPY", "tmp:0:8", ["const:a88:8"]]
~~~


### [`00831ee4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ee4.md) → [`00831f3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831f3c.md) FUN_00831f3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082c864`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`008b6ea4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082c8bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082c/0082c8bc.md) [`008b6efc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md) [`00a4692c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a4692c.md)

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
      "site": "00831f60",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831f08",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00831f6c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00831f14",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831f08 ["INT_ADD", "register:40f0:8", ["const:831f08:8", "const:4:8"]]
- 00831f08 ["CALL", null, ["ram:47acf4:8"]]
+ 00831f60 ["INT_ADD", "register:40f0:8", ["const:831f60:8", "const:4:8"]]
+ 00831f60 ["CALL", null, ["ram:47ad34:8"]]
- 00831f14 ["INT_ADD", "register:40f0:8", ["const:831f14:8", "const:4:8"]]
- 00831f14 ["CALL", null, ["ram:47acf4:8"]]
+ 00831f6c ["INT_ADD", "register:40f0:8", ["const:831f6c:8", "const:4:8"]]
+ 00831f6c ["CALL", null, ["ram:47ad34:8"]]
- 00831f40 ["INT_ADD", "register:40f0:8", ["const:831f40:8", "const:4:8"]]
+ 00831f98 ["INT_ADD", "register:40f0:8", ["const:831f98:8", "const:4:8"]]
~~~


### [`00831fa4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fa4.md) → [`00831ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00831/00831ffc.md) FUN_00831ffc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00832020",
      "incomplete_value": false,
      "site": "00832020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831fc8",
      "incomplete_value": false,
      "site": "00831fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
        "00c7ea38",
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
        "00c7eb08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831fb8 ["INT_ADD", "register:40f0:8", ["const:831fb8:8", "const:4:8"]]
+ 00832010 ["INT_ADD", "register:40f0:8", ["const:832010:8", "const:4:8"]]
- 00831fc4 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 0083201c ["COPY", "tmp:0:8", ["const:b08:8"]]
~~~


### [`00831fd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831fd8.md) → [`00832030`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/00832030.md) FUN_00832030

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
      "definition_site": "0083203c",
      "incomplete_value": false,
      "site": "0083203c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00831fe4",
      "incomplete_value": false,
      "site": "00831fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
        "00c7ea38",
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
        "00c7eb08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00831fe0 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00832038 ["COPY", "tmp:0:8", ["const:b08:8"]]
~~~


### [`00831ff4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00831/00831ff4.md) → [`0083204c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083204c.md) FUN_0083204c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0082d290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0082d2e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

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
      "site": "0083206c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00832014",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00832078",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00832020",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
        "0047acf4"
      ]
    ],
    [
      44,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
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
  ]
}
~~~


~~~diff
- 00832014 ["INT_ADD", "register:40f0:8", ["const:832014:8", "const:4:8"]]
- 00832014 ["CALL", null, ["ram:47acf4:8"]]
+ 0083206c ["INT_ADD", "register:40f0:8", ["const:83206c:8", "const:4:8"]]
+ 0083206c ["CALL", null, ["ram:47ad34:8"]]
- 00832020 ["INT_ADD", "register:40f0:8", ["const:832020:8", "const:4:8"]]
- 00832020 ["CALL", null, ["ram:47acf4:8"]]
+ 00832078 ["INT_ADD", "register:40f0:8", ["const:832078:8", "const:4:8"]]
+ 00832078 ["CALL", null, ["ram:47ad34:8"]]
- 00832034 ["INT_ADD", "register:40f0:8", ["const:832034:8", "const:4:8"]]
+ 0083208c ["INT_ADD", "register:40f0:8", ["const:83208c:8", "const:4:8"]]
~~~


### [`00832084`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/00832084.md) → [`008320dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/008320dc.md) FUN_008320dc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00832100",
      "incomplete_value": false,
      "site": "00832100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008320a8",
      "incomplete_value": false,
      "site": "008320a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
        "00c7eab8",
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
        "00c7eb88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00832098 ["INT_ADD", "register:40f0:8", ["const:832098:8", "const:4:8"]]
+ 008320f0 ["INT_ADD", "register:40f0:8", ["const:8320f0:8", "const:4:8"]]
- 008320a4 ["COPY", "tmp:0:8", ["const:ab8:8"]]
+ 008320fc ["COPY", "tmp:0:8", ["const:b88:8"]]
~~~


### [`008320d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) → [`0083212c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) FUN_0083212c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 41件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046daf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)
- 新版 呼出元 0件  · 呼出先 41件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046db34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`00470880`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 4件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083276c",
      "incomplete_value": true,
      "site": "0083277c",
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
                "const:146:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00832714",
      "incomplete_value": true,
      "site": "00832724",
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
                "const:117:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00832770",
      "incomplete_value": true,
      "site": "00832780",
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
      "definition_site": "00832718",
      "incomplete_value": true,
      "site": "00832728",
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
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008327a4",
      "incomplete_value": false,
      "site": "008327a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083274c",
      "incomplete_value": false,
      "site": "0083274c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      112,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      376,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cb88"
      ]
    ]
  ],
  "added": [
    [
      76,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      112,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      376,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0081cbe0"
      ]
    ]
  ]
}
~~~


~~~diff
- 00832120 ["INT_ADD", "register:40f0:8", ["const:832120:8", "const:4:8"]]
- 00832120 ["CALL", null, ["ram:47acf4:8"]]
+ 00832178 ["INT_ADD", "register:40f0:8", ["const:832178:8", "const:4:8"]]
+ 00832178 ["CALL", null, ["ram:47ad34:8"]]
- 00832144 ["INT_ADD", "register:40f0:8", ["const:832144:8", "const:4:8"]]
- 00832144 ["CALL", null, ["ram:47acf4:8"]]
+ 0083219c ["INT_ADD", "register:40f0:8", ["const:83219c:8", "const:4:8"]]
+ 0083219c ["CALL", null, ["ram:47ad34:8"]]
- 0083218c ["INT_ADD", "register:40f0:8", ["const:83218c:8", "const:4:8"]]
+ 008321e4 ["INT_ADD", "register:40f0:8", ["const:8321e4:8", "const:4:8"]]
~~~


### [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) → [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) FUN_0083418c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`008320d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00832/008320d4.md) [`00835168`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md) [`0083526c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md) [`00835500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md) [`00835604`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 7件 [`0083212c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00832/0083212c.md) [`008351c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) [`008352c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) [`00835558`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) [`0083565c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00834198",
      "incomplete_value": false,
      "site": "0083419c",
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
    "old": {
      "definition_site": "00834140",
      "incomplete_value": false,
      "site": "00834144",
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
            "const:f4c:8"
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
        "002b7f4c",
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
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00834140 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00834198 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00834144 ["INT_ADD", "register:40f0:8", ["const:834144:8", "const:4:8"]]
+ 0083419c ["INT_ADD", "register:40f0:8", ["const:83419c:8", "const:4:8"]]
~~~


### [`00835104`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835104.md) → [`0083515c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083515c.md) FUN_0083515c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835168",
      "incomplete_value": false,
      "site": "0083516c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835110",
      "incomplete_value": false,
      "site": "00835114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      16,
      "DATA",
      [
        "storage",
        "00c7eb28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835110 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00835168 ["COPY", "tmp:0:8", ["const:bf8:8"]]
~~~


### [`00835128`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835128.md) → [`00835180`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835180.md) FUN_00835180

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835188",
      "incomplete_value": false,
      "site": "0083518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835130",
      "incomplete_value": false,
      "site": "00835134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
        "00c7eb28",
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
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835130 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00835188 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00835154 ["INT_ADD", "register:40f0:8", ["const:835154:8", "const:4:8"]]
+ 008351ac ["INT_ADD", "register:40f0:8", ["const:8351ac:8", "const:4:8"]]
~~~


### [`00835168`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835168.md) → [`008351c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008351c0.md) FUN_008351c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008351f4",
      "incomplete_value": false,
      "site": "008351f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083519c",
      "incomplete_value": false,
      "site": "0083519c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      52,
      "DATA",
      [
        "storage",
        "00c7eb28",
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
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835184 ["INT_ADD", "register:40f0:8", ["const:835184:8", "const:4:8"]]
+ 008351dc ["INT_ADD", "register:40f0:8", ["const:8351dc:8", "const:4:8"]]
- 00835190 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 008351e8 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 008351dc ["INT_ADD", "register:40f0:8", ["const:8351dc:8", "const:4:8"]]
+ 00835234 ["INT_ADD", "register:40f0:8", ["const:835234:8", "const:4:8"]]
~~~


### [`0083526c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083526c.md) → [`008352c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008352c4.md) FUN_008352c4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008352f4",
      "incomplete_value": false,
      "site": "008352f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083529c",
      "incomplete_value": false,
      "site": "0083529c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:b28:8"
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
      48,
      "DATA",
      [
        "storage",
        "00c7eb28",
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
        "00c7ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835294 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 008352ec ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 008352d4 ["INT_ADD", "register:40f0:8", ["const:8352d4:8", "const:4:8"]]
+ 0083532c ["INT_ADD", "register:40f0:8", ["const:83532c:8", "const:4:8"]]
- 00835310 ["INT_ADD", "register:40f0:8", ["const:835310:8", "const:4:8"]]
+ 00835368 ["INT_ADD", "register:40f0:8", ["const:835368:8", "const:4:8"]]
~~~


### [`008353a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008353a4.md) → [`008353fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008353fc.md) FUN_008353fc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a83260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83260.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a832d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a832d0.md)

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
      "site": "00835430",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008353d8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      52,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 008353d4 ["INT_ADD", "register:40f0:8", ["const:8353d4:8", "const:4:8"]]
+ 0083542c ["INT_ADD", "register:40f0:8", ["const:83542c:8", "const:4:8"]]
- 008353d8 ["INT_ADD", "register:40f0:8", ["const:8353d8:8", "const:4:8"]]
- 008353d8 ["CALL", null, ["ram:47acf4:8"]]
+ 00835430 ["INT_ADD", "register:40f0:8", ["const:835430:8", "const:4:8"]]
+ 00835430 ["CALL", null, ["ram:47ad34:8"]]
- 008353fc ["INT_ADD", "register:40f0:8", ["const:8353fc:8", "const:4:8"]]
+ 00835454 ["INT_ADD", "register:40f0:8", ["const:835454:8", "const:4:8"]]
~~~


### [`0083549c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083549c.md) → [`008354f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008354f4.md) FUN_008354f4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835500",
      "incomplete_value": false,
      "site": "00835504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008354a8",
      "incomplete_value": false,
      "site": "008354ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      16,
      "DATA",
      [
        "storage",
        "00c7eba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008354a8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 00835500 ["COPY", "tmp:0:8", ["const:c78:8"]]
~~~


### [`008354c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/008354c0.md) → [`00835518`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835518.md) FUN_00835518

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835520",
      "incomplete_value": false,
      "site": "00835524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008354c8",
      "incomplete_value": false,
      "site": "008354cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
        "00c7eba8",
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
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 008354c8 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 00835520 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008354ec ["INT_ADD", "register:40f0:8", ["const:8354ec:8", "const:4:8"]]
+ 00835544 ["INT_ADD", "register:40f0:8", ["const:835544:8", "const:4:8"]]
~~~


### [`00835500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835500.md) → [`00835558`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835558.md) FUN_00835558

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083558c",
      "incomplete_value": false,
      "site": "0083558c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835534",
      "incomplete_value": false,
      "site": "00835534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      52,
      "DATA",
      [
        "storage",
        "00c7eba8",
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
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083551c ["INT_ADD", "register:40f0:8", ["const:83551c:8", "const:4:8"]]
+ 00835574 ["INT_ADD", "register:40f0:8", ["const:835574:8", "const:4:8"]]
- 00835528 ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 00835580 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00835574 ["INT_ADD", "register:40f0:8", ["const:835574:8", "const:4:8"]]
+ 008355cc ["INT_ADD", "register:40f0:8", ["const:8355cc:8", "const:4:8"]]
~~~


### [`00835604`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835604.md) → [`0083565c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/0083565c.md) FUN_0083565c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083568c",
      "incomplete_value": false,
      "site": "0083568c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835634",
      "incomplete_value": false,
      "site": "00835634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      48,
      "DATA",
      [
        "storage",
        "00c7eba8",
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
        "00c7ec78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083562c ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 00835684 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 0083566c ["INT_ADD", "register:40f0:8", ["const:83566c:8", "const:4:8"]]
+ 008356c4 ["INT_ADD", "register:40f0:8", ["const:8356c4:8", "const:4:8"]]
- 008356a8 ["INT_ADD", "register:40f0:8", ["const:8356a8:8", "const:4:8"]]
+ 00835700 ["INT_ADD", "register:40f0:8", ["const:835700:8", "const:4:8"]]
~~~


### [`00835918`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835918.md) → [`00835970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835970.md) FUN_00835970

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083597c",
      "incomplete_value": false,
      "site": "00835980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835924",
      "incomplete_value": false,
      "site": "00835928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
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
      16,
      "DATA",
      [
        "storage",
        "00c7ec28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835924 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 0083597c ["COPY", "tmp:0:8", ["const:cf8:8"]]
~~~


### [`0083597c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/0083597c.md) → [`008359d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/008359d4.md) FUN_008359d4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835a08",
      "incomplete_value": false,
      "site": "00835a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008359b0",
      "incomplete_value": false,
      "site": "008359b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      52,
      "DATA",
      [
        "storage",
        "00c7ec28",
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
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835998 ["INT_ADD", "register:40f0:8", ["const:835998:8", "const:4:8"]]
+ 008359f0 ["INT_ADD", "register:40f0:8", ["const:8359f0:8", "const:4:8"]]
- 008359a4 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 008359fc ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 008359f0 ["INT_ADD", "register:40f0:8", ["const:8359f0:8", "const:4:8"]]
+ 00835a48 ["INT_ADD", "register:40f0:8", ["const:835a48:8", "const:4:8"]]
~~~


### [`00835a80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835a80.md) → [`00835ad8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835ad8.md) FUN_00835ad8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00834134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00834/00834134.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0083418c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00834/0083418c.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835b08",
      "incomplete_value": false,
      "site": "00835b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835ab0",
      "incomplete_value": false,
      "site": "00835ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      48,
      "DATA",
      [
        "storage",
        "00c7ec28",
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
        "00c7ecf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835aa8 ["COPY", "tmp:0:8", ["const:c28:8"]]
+ 00835b00 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00835ae8 ["INT_ADD", "register:40f0:8", ["const:835ae8:8", "const:4:8"]]
+ 00835b40 ["INT_ADD", "register:40f0:8", ["const:835b40:8", "const:4:8"]]
- 00835b24 ["INT_ADD", "register:40f0:8", ["const:835b24:8", "const:4:8"]]
+ 00835b7c ["INT_ADD", "register:40f0:8", ["const:835b7c:8", "const:4:8"]]
~~~


### [`00835bb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md) → [`00835c10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md) FUN_00835c10

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00467860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`0055a5e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5e4.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008628a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/008628a8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004678a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467df4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467df4.md) [`0055a624`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a624.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00862900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862900.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00835ca8",
      "incomplete_value": true,
      "site": "00835cac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835c50",
      "incomplete_value": true,
      "site": "00835c54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:978:8"
              ]
            ]
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
      "definition_site": "00835c94",
      "incomplete_value": false,
      "site": "00835cac",
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
    "old": {
      "definition_site": "00835c3c",
      "incomplete_value": false,
      "site": "00835c54",
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
            "const:e58:8"
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
      "definition_site": "00835ca0",
      "incomplete_value": false,
      "site": "00835cac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835c48",
      "incomplete_value": false,
      "site": "00835c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:510:8"
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
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "PARAM",
      [
        "storage",
        "00c7e510",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      132,
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      144,
      "PARAM",
      [
        "storage",
        "00c7e5e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835be0 ["INT_ADD", "register:40f0:8", ["const:835be0:8", "const:4:8"]]
+ 00835c38 ["INT_ADD", "register:40f0:8", ["const:835c38:8", "const:4:8"]]
- 00835bec ["INT_ADD", "register:40f0:8", ["const:835bec:8", "const:4:8"]]
+ 00835c44 ["INT_ADD", "register:40f0:8", ["const:835c44:8", "const:4:8"]]
- 00835bf8 ["INT_ADD", "register:40f0:8", ["const:835bf8:8", "const:4:8"]]
+ 00835c50 ["INT_ADD", "register:40f0:8", ["const:835c50:8", "const:4:8"]]
~~~


### [`00835d6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d6c.md) → [`00835dc4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835dc4.md) FUN_00835dc4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00835dd8",
      "incomplete_value": false,
      "site": "00835ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835d80",
      "incomplete_value": false,
      "site": "00835d84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
        "00c7eca8",
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
        "00c7ed78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835d78 ["INT_ADD", "register:40f0:8", ["const:835d78:8", "const:4:8"]]
+ 00835dd0 ["INT_ADD", "register:40f0:8", ["const:835dd0:8", "const:4:8"]]
- 00835d80 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00835dd8 ["COPY", "tmp:0:8", ["const:d78:8"]]
~~~


### [`00835d90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835d90.md) → [`00835de8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835de8.md) FUN_00835de8

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
      "definition_site": "00835dec",
      "incomplete_value": false,
      "site": "00835df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00835d94",
      "incomplete_value": false,
      "site": "00835d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
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
        "00c7eca8",
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
        "00c7ed78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835d94 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00835dec ["COPY", "tmp:0:8", ["const:d78:8"]]
~~~


### [`00835da8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835da8.md) → [`00835e00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e00.md) FUN_00835e00

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

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
      "site": "00835e24",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00835dcc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835dcc ["INT_ADD", "register:40f0:8", ["const:835dcc:8", "const:4:8"]]
- 00835dcc ["CALL", null, ["ram:47acf4:8"]]
+ 00835e24 ["INT_ADD", "register:40f0:8", ["const:835e24:8", "const:4:8"]]
+ 00835e24 ["CALL", null, ["ram:47ad34:8"]]
- 00835dd8 ["INT_ADD", "register:40f0:8", ["const:835dd8:8", "const:4:8"]]
+ 00835e30 ["INT_ADD", "register:40f0:8", ["const:835e30:8", "const:4:8"]]
~~~


### [`00835fcc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835fcc.md) → [`00836024`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00836/00836024.md) FUN_00836024

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00835e18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835e18.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00835e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835e70.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00836030",
      "incomplete_value": false,
      "site": "00836034",
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
    "old": {
      "definition_site": "00835fd8",
      "incomplete_value": false,
      "site": "00835fdc",
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
            "const:f4c:8"
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
        "002b7f4c",
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
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00835fd8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00836030 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00835fdc ["INT_ADD", "register:40f0:8", ["const:835fdc:8", "const:4:8"]]
+ 00836034 ["INT_ADD", "register:40f0:8", ["const:836034:8", "const:4:8"]]
~~~


### [`008378d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md) → [`00837930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) FUN_00837930

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0082ee20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) · 呼出先 12件 [`0047e60c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0067e19c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) [`00862c50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/00862c50.md) [`00864538`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864538.md)
- 新版 呼出元 1件 [`0082ee78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082e/0082ee78.md) · 呼出先 12件 [`0047e64c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0067e1dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e1dc.md) [`00862ca8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862ca8.md) [`00864590`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864590.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 44件, `store_destination` 7件, `store_value` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00837970",
      "incomplete_value": true,
      "site": "00837974",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00837918",
      "incomplete_value": true,
      "site": "0083791c",
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
            "const:d38:8"
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
      "definition_site": "008379b4",
      "incomplete_value": true,
      "site": "008379b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:3ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083795c",
      "incomplete_value": true,
      "site": "0083795c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:38e:8"
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
      "definition_site": "008379cc",
      "incomplete_value": true,
      "site": "008379cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f47:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00837974",
      "incomplete_value": true,
      "site": "00837974",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f16:8"
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
      68,
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002b638e",
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
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002b63ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083790c ["INT_ADD", "register:40f0:8", ["const:83790c:8", "const:4:8"]]
+ 00837964 ["INT_ADD", "register:40f0:8", ["const:837964:8", "const:4:8"]]
- 00837918 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00837970 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00837920 ["COPY", "register:40c0:8", ["const:ca4000:8"]]
- 00837924 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00837978 ["COPY", "register:40c0:8", ["const:ca5000:8"]]
+ 0083797c ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00838888`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838888.md) → [`008388e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008388e0.md) FUN_008388e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00682324`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682364`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008388f8",
      "incomplete_value": false,
      "site": "008388fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008388a0",
      "incomplete_value": false,
      "site": "008388a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838964",
      "incomplete_value": false,
      "site": "00838968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083890c",
      "incomplete_value": false,
      "site": "00838910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      28,
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 008388a0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008388f8 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008388b4 ["INT_ADD", "register:40f0:8", ["const:8388b4:8", "const:4:8"]]
+ 0083890c ["INT_ADD", "register:40f0:8", ["const:83890c:8", "const:4:8"]]
- 008388c8 ["INT_ADD", "register:40f0:8", ["const:8388c8:8", "const:4:8"]]
+ 00838920 ["INT_ADD", "register:40f0:8", ["const:838920:8", "const:4:8"]]
~~~


### [`00838950`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838950.md) → [`008389a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/008389a8.md) FUN_008389a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00682324`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682364`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682364.md) [`00c53da0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008389c0",
      "incomplete_value": false,
      "site": "008389c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838968",
      "incomplete_value": false,
      "site": "0083896c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838a2c",
      "incomplete_value": false,
      "site": "00838a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008389d4",
      "incomplete_value": false,
      "site": "008389d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
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
      28,
      "DATA",
      [
        "storage",
        "00c7ed38",
        null,
        "pointer"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "DATA",
      [
        "storage",
        "00c7ee08",
        null,
        "pointer"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "00c748e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838968 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008389c0 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 0083897c ["INT_ADD", "register:40f0:8", ["const:83897c:8", "const:4:8"]]
+ 008389d4 ["INT_ADD", "register:40f0:8", ["const:8389d4:8", "const:4:8"]]
- 00838990 ["INT_ADD", "register:40f0:8", ["const:838990:8", "const:4:8"]]
+ 008389e8 ["INT_ADD", "register:40f0:8", ["const:8389e8:8", "const:4:8"]]
~~~


### [`00838a24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a24.md) → [`00838a7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838a7c.md) FUN_00838a7c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838aa0",
      "incomplete_value": false,
      "site": "00838aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838a48",
      "incomplete_value": false,
      "site": "00838a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
        "00c7ed58",
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
        "00c7ee28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838a38 ["INT_ADD", "register:40f0:8", ["const:838a38:8", "const:4:8"]]
+ 00838a90 ["INT_ADD", "register:40f0:8", ["const:838a90:8", "const:4:8"]]
- 00838a44 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00838a9c ["COPY", "tmp:0:8", ["const:e28:8"]]
~~~


### [`00838a58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a58.md) → [`00838ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ab0.md) FUN_00838ab0

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
      "definition_site": "00838abc",
      "incomplete_value": false,
      "site": "00838abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838a64",
      "incomplete_value": false,
      "site": "00838a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
        "00c7ed58",
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
        "00c7ee28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838a60 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00838ab8 ["COPY", "tmp:0:8", ["const:e28:8"]]
~~~


### [`00838ac0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ac0.md) → [`00838b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b18.md) FUN_00838b18

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838b3c",
      "incomplete_value": false,
      "site": "00838b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838ae4",
      "incomplete_value": false,
      "site": "00838ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
        "00c7edd8",
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
        "00c7eea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838ad4 ["INT_ADD", "register:40f0:8", ["const:838ad4:8", "const:4:8"]]
+ 00838b2c ["INT_ADD", "register:40f0:8", ["const:838b2c:8", "const:4:8"]]
- 00838ae0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00838b38 ["COPY", "tmp:0:8", ["const:ea8:8"]]
~~~


### [`00838af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838af4.md) → [`00838b4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838b4c.md) FUN_00838b4c

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
      "definition_site": "00838b58",
      "incomplete_value": false,
      "site": "00838b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b00",
      "incomplete_value": false,
      "site": "00838b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
        "00c7edd8",
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
        "00c7eea8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838afc ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00838b54 ["COPY", "tmp:0:8", ["const:ea8:8"]]
~~~


### [`00838b50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b50.md) → [`00838ba8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838ba8.md) FUN_00838ba8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838bcc",
      "incomplete_value": false,
      "site": "00838bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b74",
      "incomplete_value": false,
      "site": "00838b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
        "00c7ee58",
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
        "00c7ef28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838b64 ["INT_ADD", "register:40f0:8", ["const:838b64:8", "const:4:8"]]
+ 00838bbc ["INT_ADD", "register:40f0:8", ["const:838bbc:8", "const:4:8"]]
- 00838b70 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00838bc8 ["COPY", "tmp:0:8", ["const:f28:8"]]
~~~


### [`00838b84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838b84.md) → [`00838bdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bdc.md) FUN_00838bdc

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
      "definition_site": "00838be8",
      "incomplete_value": false,
      "site": "00838be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838b90",
      "incomplete_value": false,
      "site": "00838b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
        "00c7ee58",
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
        "00c7ef28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838b8c ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00838be4 ["COPY", "tmp:0:8", ["const:f28:8"]]
~~~


### [`00838ba0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838ba0.md) → [`00838bf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838bf8.md) FUN_00838bf8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0082d290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082d/0082d290.md) [`00838d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d00.md) [`00838d04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d04.md) [`00acabd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0082d2e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0082d/0082d2e8.md) [`00838d58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d58.md) [`00838d5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d5c.md) [`00acac44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aca/00acac44.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838c2c",
      "incomplete_value": false,
      "site": "00838c2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838bd4",
      "incomplete_value": false,
      "site": "00838bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      52,
      "DATA",
      [
        "storage",
        "00c7eec8",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c7eee8",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c7eef0",
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
        "00c7ef98",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c7efb8",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "00c7efc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838bc4 ["INT_ADD", "register:40f0:8", ["const:838bc4:8", "const:4:8"]]
+ 00838c1c ["INT_ADD", "register:40f0:8", ["const:838c1c:8", "const:4:8"]]
- 00838bcc ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00838c24 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 00838be8 ["INT_ADD", "register:40f0:8", ["const:838be8:8", "const:4:8"]]
+ 00838c40 ["INT_ADD", "register:40f0:8", ["const:838c40:8", "const:4:8"]]
~~~


### [`00838cb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cb8.md) → [`00838d10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d10.md) FUN_00838d10

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00838d34",
      "incomplete_value": false,
      "site": "00838d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838cdc",
      "incomplete_value": false,
      "site": "00838cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
        "00c7eec8",
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
        "00c7ef98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838ccc ["INT_ADD", "register:40f0:8", ["const:838ccc:8", "const:4:8"]]
+ 00838d24 ["INT_ADD", "register:40f0:8", ["const:838d24:8", "const:4:8"]]
- 00838cd8 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00838d30 ["COPY", "tmp:0:8", ["const:f98:8"]]
~~~


### [`00838cec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838cec.md) → [`00838d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d44.md) FUN_00838d44

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
      "definition_site": "00838d50",
      "incomplete_value": false,
      "site": "00838d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838cf8",
      "incomplete_value": false,
      "site": "00838cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
        "00c7eec8",
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
        "00c7ef98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838cf4 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00838d4c ["COPY", "tmp:0:8", ["const:f98:8"]]
~~~


### [`00838d08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838d08.md) → [`00838d60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838d60.md) FUN_00838d60

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`007562a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085bb70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bb70.md) [`00ac863c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac863c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007562fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085bbc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085bbc8.md) [`00ac86ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac86ac.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_value, call, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_target` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00838da4",
      "incomplete_value": false,
      "site": "00838da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838d4c",
      "incomplete_value": false,
      "site": "00838d4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00838d98",
      "incomplete_value": true,
      "site": "00838da4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838d40",
      "incomplete_value": true,
      "site": "00838d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:978:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00838da8",
      "incomplete_value": false,
      "site": "00838da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00838d50",
      "incomplete_value": false,
      "site": "00838d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:978:8"
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
      56,
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "WRITE",
      [
        "storage",
        "00ca4a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00838d20 ["INT_ADD", "register:40f0:8", ["const:838d20:8", "const:4:8"]]
+ 00838d78 ["INT_ADD", "register:40f0:8", ["const:838d78:8", "const:4:8"]]
- 00838d2c ["INT_ADD", "register:40f0:8", ["const:838d2c:8", "const:4:8"]]
+ 00838d84 ["INT_ADD", "register:40f0:8", ["const:838d84:8", "const:4:8"]]
- 00838d30 ["INT_ADD", "register:40f0:8", ["const:838d30:8", "const:4:8"]]
+ 00838d88 ["INT_ADD", "register:40f0:8", ["const:838d88:8", "const:4:8"]]
~~~


### [`00838e0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838e0c.md) → [`00838e64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00838/00838e64.md) _INIT_153

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00838ea0",
      "incomplete_value": true,
      "site": "00838ebc",
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
    "old": {
      "definition_site": "00838e48",
      "incomplete_value": true,
      "site": "00838e64",
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
                "const:f26:8"
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
      "definition_site": "00838ec4",
      "incomplete_value": true,
      "site": "00838ee0",
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
    "old": {
      "definition_site": "00838e6c",
      "incomplete_value": true,
      "site": "00838e88",
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
                "const:f39:8"
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
      "definition_site": "00838ee4",
      "incomplete_value": true,
      "site": "00838f00",
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
    "old": {
      "definition_site": "00838e8c",
      "incomplete_value": true,
      "site": "00838ea8",
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
                "const:dc2:8"
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
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8dc2",
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
  ]
}
~~~


~~~diff
- 00838e38 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 00838e90 ["COPY", "tmp:0:8", ["const:1c0:8"]]
- 00838e44 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 00838e9c ["COPY", "tmp:0:8", ["const:f66:8"]]
- 00838e60 ["COPY", "tmp:0:8", ["const:f39:8"]]
+ 00838eb8 ["COPY", "tmp:0:8", ["const:f79:8"]]
~~~


### [`0083919c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/0083919c.md) → [`008391f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/008391f4.md) _INIT_154

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00839254",
      "incomplete_value": true,
      "site": "00839270",
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
                "register:4050:8"
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
      "definition_site": "008391fc",
      "incomplete_value": true,
      "site": "00839218",
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:f39:8"
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
      "definition_site": "00839274",
      "incomplete_value": true,
      "site": "00839290",
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
    "old": {
      "definition_site": "0083921c",
      "incomplete_value": true,
      "site": "00839238",
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
                "const:dc2:8"
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
      "definition_site": "00839294",
      "incomplete_value": true,
      "site": "008392ac",
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
    "old": {
      "definition_site": "0083923c",
      "incomplete_value": true,
      "site": "00839254",
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
                "const:f62:8"
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
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8dc2",
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
  ]
}
~~~


~~~diff
- 008391c8 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00839220 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 008391d4 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 0083922c ["COPY", "tmp:0:8", ["const:f66:8"]]
- 008391f0 ["COPY", "tmp:0:8", ["const:f39:8"]]
+ 00839248 ["COPY", "tmp:0:8", ["const:f79:8"]]
~~~


### [`00839d4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/00839d4c.md) → [`00839da4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839da4.md) _INIT_155

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`0083952c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00839/0083952c.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00839584`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00839/00839584.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00839e80",
      "incomplete_value": true,
      "site": "00839e9c",
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
                "const:2a0000:8"
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
    "old": {
      "definition_site": "00839e28",
      "incomplete_value": true,
      "site": "00839e44",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f5d:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00839ea0",
      "incomplete_value": true,
      "site": "00839ee4",
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
                "const:ebc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00839e48",
      "incomplete_value": true,
      "site": "00839e8c",
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
                "const:f09:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00839fec",
      "incomplete_value": false,
      "site": "00839fec",
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
                "const:ca8000:8"
              ],
              [
                "leaf",
                "const:208:8"
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
      "definition_site": "00839f94",
      "incomplete_value": false,
      "site": "00839f94",
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
                "const:ca8000:8"
              ],
              [
                "leaf",
                "const:108:8"
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
    "ordinal": 45,
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
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8dc2",
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
  ]
}
~~~


~~~diff
- 00839d78 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00839dd0 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00839d84 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 00839ddc ["COPY", "tmp:0:8", ["const:f66:8"]]
- 00839da0 ["COPY", "tmp:0:8", ["const:f39:8"]]
+ 00839df8 ["COPY", "tmp:0:8", ["const:f79:8"]]
~~~


### [`0083a120`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) → [`0083a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) FUN_0083a178

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084a040`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084a/0084a040.md) · 呼出先 150件 [`0044ab38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ab38.md) [`0044ab48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ab48.md) [`0044ab50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044a/0044ab50.md) [`0044d808`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044d808.md) [`0044dc68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044d/0044dc68.md)
- 新版 呼出元 1件 [`0084a098`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 150件 [`0044ab50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab50.md) [`0044ab78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044a/0044ab78.md) [`0044d730`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d730.md) [`0044d848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044d/0044d848.md) [`0044e108`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083a1b8",
      "incomplete_value": false,
      "site": "0083a1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083a160",
      "incomplete_value": false,
      "site": "0083a168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "definition_site": "0083e098",
      "incomplete_value": false,
      "site": "0083e09c",
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
                "const:c80000:8"
              ],
              [
                "leaf",
                "const:2f0:8"
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
      "definition_site": "0083e040",
      "incomplete_value": false,
      "site": "0083e044",
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
                "const:c80000:8"
              ],
              [
                "leaf",
                "const:220:8"
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
    "ordinal": 254,
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
        "00c7ef58",
        null,
        "undefined *"
      ]
    ],
    [
      152,
      "DATA",
      [
        "storage",
        "00477d48",
        null,
        null
      ]
    ],
    [
      168,
      "DATA",
      [
        "storage",
        "00477d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      72,
      "DATA",
      [
        "storage",
        "00c7f028",
        null,
        "undefined *"
      ]
    ],
    [
      1108,
      "DATA",
      [
        "storage",
        "0044e1f8",
        null,
        null
      ]
    ],
    [
      1116,
      "DATA",
      [
        "storage",
        "0044e200",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0083a15c ["COPY", "register:4040:8", ["const:c7e000:8"]]
- 0083a160 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0083a160 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0083a160 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0083a1b4 ["COPY", "register:4040:8", ["const:c7f000:8"]]
+ 0083a1b8 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0083a1b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0083a1b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
~~~


### [`0083f468`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f468.md) → [`0083f4c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f4c0.md) FUN_0083f4c0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00814bf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00814/00814bf8.md) [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 8件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00473540`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004913d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00491/004913d0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`00814c50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00814/00814c50.md) [`00856e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 8件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00473580`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0048cd38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00491410`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00491/00491410.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083f544",
      "incomplete_value": true,
      "site": "0083f550",
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
                "const:3e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f4ec",
      "incomplete_value": true,
      "site": "0083f4f8",
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
                "const:43b:8"
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
      "definition_site": "0083f598",
      "incomplete_value": true,
      "site": "0083f5a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0083f540",
      "incomplete_value": true,
      "site": "0083f550",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0083f594",
      "incomplete_value": true,
      "site": "0083f5b0",
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
                "const:726:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f53c",
      "incomplete_value": true,
      "site": "0083f558",
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
                "const:773:8"
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
      44,
      "READ",
      [
        "storage",
        "00c9aca8",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00ca5150",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00ca5150",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00ca5250",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "00ca5250",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083f494 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:ca8:8"]]
+ 0083f4ec ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d78:8"]]
- 0083f4c4 ["INT_ADD", "register:40f0:8", ["const:83f4c4:8", "const:4:8"]]
+ 0083f51c ["INT_ADD", "register:40f0:8", ["const:83f51c:8", "const:4:8"]]
- 0083f4d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 0083f52c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
~~~


### [`0083f884`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f884.md) → [`0083f8dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f8dc.md) FUN_0083f8dc

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0084a040`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084a/0084a040.md) · 呼出先 39件 [`0044e1e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044e1e0.md) [`0046e7c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046eef8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`00472a00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472a00.md) [`0048ccc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccc8.md)
- 新版 呼出元 1件 [`0084a098`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084a/0084a098.md) · 呼出先 39件 [`0044e108`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md) [`0046e804`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) [`0046ef38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) [`00472a40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472a40.md) [`0048cd08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd08.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 9件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0083f91c",
      "incomplete_value": false,
      "site": "0083f9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0083f8c4",
      "incomplete_value": false,
      "site": "0083f980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0084082c",
      "incomplete_value": false,
      "site": "00840830",
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
                "const:c81000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
      "definition_site": "008407d4",
      "incomplete_value": false,
      "site": "008407d8",
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
                "const:c81000:8"
              ],
              [
                "leaf",
                "const:a30:8"
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
    "ordinal": 612,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00840848",
      "incomplete_value": false,
      "site": "0084084c",
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
                "const:c82000:8"
              ],
              [
                "leaf",
                "const:3e8:8"
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
      "definition_site": "008407f0",
      "incomplete_value": false,
      "site": "008407f4",
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
                "const:c82000:8"
              ],
              [
                "leaf",
                "const:318:8"
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
    "ordinal": 613,
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
        "00c7ef58",
        null,
        "undefined *"
      ]
    ],
    [
      3924,
      "DATA",
      [
        "storage",
        "00c81a40",
        null,
        "undefined *"
      ]
    ],
    [
      3952,
      "DATA",
      [
        "storage",
        "00c82328",
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
        "00c7f028",
        null,
        "undefined *"
      ]
    ],
    [
      3924,
      "DATA",
      [
        "storage",
        "00c81b10",
        null,
        "undefined *"
      ]
    ],
    [
      3952,
      "DATA",
      [
        "storage",
        "00c823f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0083f8c0 ["COPY", "register:4048:8", ["const:c7e000:8"]]
- 0083f8c4 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 0083f8c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0083f8c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f918 ["COPY", "register:4048:8", ["const:c7f000:8"]]
+ 0083f91c ["COPY", "tmp:0:8", ["const:28:8"]]
+ 0083f91c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0083f91c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
~~~


### [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) → [`00851550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) FUN_00851550

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2197件 [`0043c258`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dfb0.md) [`0045ab6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) [`0045b8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md) [`0045c908`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c908.md) · 呼出先 0件 
- 新版 呼出元 2198件 [`0043c298`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043dff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dff0.md) [`0045abac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) [`0045b914`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md) [`0045c948`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c948.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00851554",
      "incomplete_value": false,
      "site": "00851558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca8000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008514fc",
      "incomplete_value": false,
      "site": "00851500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca8000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "DATA",
      [
        "storage",
        "00ca8170",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      4,
      "DATA",
      [
        "storage",
        "00ca8270",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 008514fc ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00851554 ["COPY", "tmp:0:8", ["const:270:8"]]
~~~


### [`00851504`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) → [`0085155c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) FUN_0085155c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 43件 [`004440e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`00444678`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444678.md) [`00472da4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`00473194`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md) [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md)
- 新版 呼出元 0件  · 呼出先 43件 [`00444120`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`004446b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/004446b8.md) [`00472de4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`004731d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004731d4.md) [`0048cd38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00851894",
      "incomplete_value": false,
      "site": "008518a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085183c",
      "incomplete_value": false,
      "site": "00851848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00851764",
      "value": [
        "leaf",
        "ram:768420:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085170c",
      "value": [
        "leaf",
        "ram:7683c8:8"
      ]
    },
    "ordinal": 36,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085177c",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00851724",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "ordinal": 37,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      520,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683c8"
      ]
    ],
    [
      544,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      656,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087e70c"
      ]
    ]
  ],
  "added": [
    [
      520,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768420"
      ]
    ],
    [
      544,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      656,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0087e764"
      ]
    ]
  ]
}
~~~


~~~diff
- 00851530 ["INT_ADD", "register:40f0:8", ["const:851530:8", "const:4:8"]]
+ 00851588 ["INT_ADD", "register:40f0:8", ["const:851588:8", "const:4:8"]]
- 00851538 ["INT_ADD", "register:40f0:8", ["const:851538:8", "const:4:8"]]
+ 00851590 ["INT_ADD", "register:40f0:8", ["const:851590:8", "const:4:8"]]
- 0085154c ["INT_ADD", "register:40f0:8", ["const:85154c:8", "const:4:8"]]
+ 008515a4 ["INT_ADD", "register:40f0:8", ["const:8515a4:8", "const:4:8"]]
~~~


### [`00851954`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851954.md) → [`008519ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/008519ac.md) FUN_008519ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2c200`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) · 呼出先 4件 [`0048b390`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md) [`00851a0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00b2c29c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md) · 呼出先 4件 [`0048b3d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md) [`00851a64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008519e8",
      "incomplete_value": true,
      "site": "008519e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851990",
      "incomplete_value": true,
      "site": "00851990",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
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
      32,
      "READ",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "002a7580",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085196c ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 008519c4 ["COPY", "tmp:0:8", ["const:580:8"]]
- 0085199c ["INT_ADD", "register:40f0:8", ["const:85199c:8", "const:4:8"]]
+ 008519f4 ["INT_ADD", "register:40f0:8", ["const:8519f4:8", "const:4:8"]]
- 008519ac ["INT_ADD", "register:40f0:8", ["const:8519ac:8", "const:4:8"]]
+ 00851a04 ["INT_ADD", "register:40f0:8", ["const:851a04:8", "const:4:8"]]
~~~


### [`00851a0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) → [`00851a64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) FUN_00851a64

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 21件 [`006788e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00678/006788e0.md) [`006bbc98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`007ac3c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007ac3c0.md) [`00851954`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851954.md) [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 60件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e94c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043ec60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`00442b38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md)
- 新版 呼出元 21件 [`00678920`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00678/00678920.md) [`006bbcf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007ac418`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007ac418.md) [`008519ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/008519ac.md) [`00856e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 60件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e98c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`00442b78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, control_flow, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 34件, `call_target` 16件, `store_destination` 23件, `store_value` 20件

アドレスに依存する影響 `branch_value` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00851b6c",
      "incomplete_value": true,
      "site": "00851b70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851b14",
      "incomplete_value": true,
      "site": "00851b18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "definition_site": "00851c64",
      "incomplete_value": true,
      "site": "00851c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851c0c",
      "incomplete_value": true,
      "site": "00851c0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:617:8"
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
      "definition_site": "00851c68",
      "incomplete_value": true,
      "site": "00851c68",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851c10",
      "incomplete_value": true,
      "site": "00851c10",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
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
      264,
      "READ",
      [
        "storage",
        "002c3ca8",
        null,
        "undefined8"
      ]
    ],
    [
      272,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      476,
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      264,
      "READ",
      [
        "storage",
        "002c3ce8",
        null,
        "undefined8"
      ]
    ],
    [
      272,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      476,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00851aac ["INT_ADD", "register:40f0:8", ["const:851aac:8", "const:4:8"]]
- 00851aac ["CALL", null, ["callee:005e0da8:8"]]
- 00851ab0 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00851ab0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00851b04 ["INT_ADD", "register:40f0:8", ["const:851b04:8", "const:4:8"]]
+ 00851b04 ["CALL", null, ["callee:005e0da8:8"]]
+ 00851b08 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
+ 00851b08 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
~~~


### [`00853308`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) → [`00853360`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) FUN_00853360

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043e94c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043ec60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`00472da4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`0047326c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047326c.md) [`00473270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043e98c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043eca0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`00472de4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`004732ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004732ac.md) [`004732b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004732b0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 3件, `store_destination` 8件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008534ec",
      "incomplete_value": true,
      "site": "008534ec",
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
                "const:ca8000:8"
              ],
              [
                "leaf",
                "const:270:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
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
      "definition_site": "00853494",
      "incomplete_value": true,
      "site": "00853494",
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
                "const:ca8000:8"
              ],
              [
                "leaf",
                "const:170:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
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
      "definition_site": "00853620",
      "incomplete_value": false,
      "site": "00853620",
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
                "const:ca5000:8"
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
      "definition_site": "008535c8",
      "incomplete_value": false,
      "site": "008535c8",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00853624",
      "incomplete_value": false,
      "site": "00853624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008535cc",
      "incomplete_value": false,
      "site": "008535cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009ccb7c"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009ccbd0"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085333c ["INT_ADD", "register:40f0:8", ["const:85333c:8", "const:4:8"]]
+ 00853394 ["INT_ADD", "register:40f0:8", ["const:853394:8", "const:4:8"]]
- 00853340 ["INT_ADD", "register:40f0:8", ["const:853340:8", "const:4:8"]]
+ 00853398 ["INT_ADD", "register:40f0:8", ["const:853398:8", "const:4:8"]]
- 00853344 ["INT_ADD", "register:40f0:8", ["const:853344:8", "const:4:8"]]
+ 0085339c ["INT_ADD", "register:40f0:8", ["const:85339c:8", "const:4:8"]]
~~~


### [`008536a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/008536a0.md) → [`008536f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/008536f8.md) FUN_008536f8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00853308`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) · 呼出先 22件 [`0047e60c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`004894a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004894a8.md) [`0048abd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048abd0.md) [`0048ac08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048ac08.md)
- 新版 呼出元 1件 [`00853360`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) · 呼出先 22件 [`0047e64c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`004894e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004894e8.md) [`0048ac10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac10.md) [`0048ac48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048ac48.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00853760",
      "incomplete_value": true,
      "site": "00853760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853708",
      "incomplete_value": true,
      "site": "00853708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
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
      "definition_site": "00853770",
      "incomplete_value": true,
      "site": "00853770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853718",
      "incomplete_value": true,
      "site": "00853718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
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
      "definition_site": "00853768",
      "incomplete_value": true,
      "site": "00853774",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00853710",
      "incomplete_value": true,
      "site": "0085371c",
      "value": [
        "LOAD",
        "8",
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
      84,
      "READ",
      [
        "storage",
        "002b099a",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002b802c",
        null,
        "string"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002b8033",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      84,
      "READ",
      [
        "storage",
        "002b093e",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002b806c",
        null,
        "string"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002b8073",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 008536e8 ["COPY", "tmp:0:8", ["const:99a:8"]]
+ 00853740 ["COPY", "tmp:0:8", ["const:93e:8"]]
- 00853700 ["COPY", "tmp:0:8", ["const:2c:8"]]
+ 00853758 ["COPY", "tmp:0:8", ["const:6c:8"]]
- 00853730 ["INT_ADD", "register:40f0:8", ["const:853730:8", "const:4:8"]]
+ 00853788 ["INT_ADD", "register:40f0:8", ["const:853788:8", "const:4:8"]]
~~~


### [`00853c78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) → [`00853cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) FUN_00853cd0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce20.md) [`0047cf08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0047d1bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1bc.md) [`0047d1f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce60.md) [`0047cf48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`0047d1fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d1fc.md) [`0047d238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d238.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 5件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00853d84",
      "incomplete_value": true,
      "site": "00853d88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:caa000:8"
              ],
              [
                "leaf",
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853d2c",
      "incomplete_value": true,
      "site": "00853d30",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:caa000:8"
              ],
              [
                "leaf",
                "const:410:8"
              ]
            ]
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
      "definition_site": "00853da4",
      "incomplete_value": true,
      "site": "00853da8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:caa000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853d4c",
      "incomplete_value": true,
      "site": "00853d50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:caa000:8"
              ],
              [
                "leaf",
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00853dc4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00853d6c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      180,
      "READ",
      [
        "storage",
        "00caa410",
        null,
        "undefined8"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "00caa418",
        null,
        "undefined8"
      ]
    ],
    [
      244,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      180,
      "READ",
      [
        "storage",
        "00caa510",
        null,
        "undefined8"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "00caa518",
        null,
        "undefined8"
      ]
    ],
    [
      244,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00853cf4 ["INT_ADD", "register:40f0:8", ["const:853cf4:8", "const:4:8"]]
+ 00853d4c ["INT_ADD", "register:40f0:8", ["const:853d4c:8", "const:4:8"]]
- 00853cfc ["INT_ADD", "register:40f0:8", ["const:853cfc:8", "const:4:8"]]
+ 00853d54 ["INT_ADD", "register:40f0:8", ["const:853d54:8", "const:4:8"]]
- 00853d24 ["INT_ADD", "register:40f0:8", ["const:853d24:8", "const:4:8"]]
+ 00853d7c ["INT_ADD", "register:40f0:8", ["const:853d7c:8", "const:4:8"]]
~~~


### [`0085408c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/0085408c.md) → [`008540e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/008540e4.md) FUN_008540e4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 14件 [`005fe66c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`006bbc98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006bed5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`007bda44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007cceec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 15件 [`005509b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) [`0069ef14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) [`006a2b78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`006a2d48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d48.md) [`006a2d4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d4c.md)
- 新版 呼出元 14件 [`005fe6ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`006bbcf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`006bedb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`007bda9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) [`007ccf44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 15件 [`005509f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md) [`0069ef6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) [`006a2bd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`006a2da0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da0.md) [`006a2da4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085412c",
      "incomplete_value": false,
      "site": "00854134",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008540d4",
      "incomplete_value": false,
      "site": "008540dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "definition_site": "008541ac",
      "incomplete_value": true,
      "site": "008541c0",
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
                "const:8b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00854154",
      "incomplete_value": true,
      "site": "00854168",
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
                "const:875:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00854248",
      "incomplete_value": false,
      "site": "00854250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008541f0",
      "incomplete_value": false,
      "site": "008541f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      80,
      "DATA",
      [
        "storage",
        "00c7f740",
        null,
        "undefined *"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "002b7875",
        null,
        "string"
      ]
    ],
    [
      304,
      "PARAM",
      [
        "storage",
        "006a2d48",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      80,
      "DATA",
      [
        "storage",
        "00c7f810",
        null,
        "undefined *"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "002b78b5",
        null,
        "string"
      ]
    ],
    [
      304,
      "PARAM",
      [
        "storage",
        "006a2da0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 008540bc ["INT_ADD", "register:40f0:8", ["const:8540bc:8", "const:4:8"]]
+ 00854114 ["INT_ADD", "register:40f0:8", ["const:854114:8", "const:4:8"]]
- 008540d4 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 0085412c ["COPY", "tmp:0:8", ["const:810:8"]]
- 008540e8 ["INT_ADD", "register:40f0:8", ["const:8540e8:8", "const:4:8"]]
+ 00854140 ["INT_ADD", "register:40f0:8", ["const:854140:8", "const:4:8"]]
~~~


### [`008542f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008542f8.md) → [`00854350`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854350.md) FUN_00854350

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0043c258`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0075b9c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) [`00853c78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 14件 [`005509b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b0.md) [`0069ef14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) [`006a2b78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) [`006a2d48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d48.md) [`006a2d4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d4c.md)
- 新版 呼出元 4件 [`0043c298`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0075ba1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075b/0075ba1c.md) [`00853cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) [`00856e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 14件 [`005509f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f0.md) [`0069ef6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) [`006a2bd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) [`006a2da0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da0.md) [`006a2da4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00854384",
      "incomplete_value": false,
      "site": "0085438c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085432c",
      "incomplete_value": false,
      "site": "00854334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "definition_site": "00854410",
      "incomplete_value": true,
      "site": "00854410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008543b8",
      "incomplete_value": true,
      "site": "008543b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec9:8"
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
      "definition_site": "00854404",
      "incomplete_value": true,
      "site": "00854414",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008543ac",
      "incomplete_value": true,
      "site": "008543bc",
      "value": [
        "LOAD",
        "8",
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
      "DATA",
      [
        "storage",
        "00c7f840",
        null,
        "undefined *"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "002aeec9",
        null,
        "string"
      ]
    ],
    [
      180,
      "READ",
      [
        "storage",
        "002aeed0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      60,
      "DATA",
      [
        "storage",
        "00c7f910",
        null,
        "undefined *"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "002aee6d",
        null,
        "string"
      ]
    ],
    [
      180,
      "READ",
      [
        "storage",
        "002aee74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085432c ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00854384 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00854340 ["INT_ADD", "register:40f0:8", ["const:854340:8", "const:4:8"]]
+ 00854398 ["INT_ADD", "register:40f0:8", ["const:854398:8", "const:4:8"]]
- 00854350 ["INT_ADD", "register:40f0:8", ["const:854350:8", "const:4:8"]]
+ 008543a8 ["INT_ADD", "register:40f0:8", ["const:8543a8:8", "const:4:8"]]
~~~


### [`0085460c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/0085460c.md) → [`00854664`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854664.md) FUN_00854664

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047ce28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`00597638`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597638.md) [`005e0d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d68.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`00597678`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597678.md) [`005e0da8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0da8.md)

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
      "site": "00854678",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00854620",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      20,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 00854620 ["INT_ADD", "register:40f0:8", ["const:854620:8", "const:4:8"]]
- 00854620 ["CALL", null, ["ram:47acf4:8"]]
- 00854624 ["INT_ADD", "register:40f0:8", ["const:854624:8", "const:4:8"]]
+ 00854678 ["INT_ADD", "register:40f0:8", ["const:854678:8", "const:4:8"]]
+ 00854678 ["CALL", null, ["ram:47ad34:8"]]
+ 0085467c ["INT_ADD", "register:40f0:8", ["const:85467c:8", "const:4:8"]]
- 00854634 ["INT_ADD", "register:40f0:8", ["const:854634:8", "const:4:8"]]
+ 0085468c ["INT_ADD", "register:40f0:8", ["const:85468c:8", "const:4:8"]]
- 0085463c ["INT_ADD", "register:40f0:8", ["const:85463c:8", "const:4:8"]]
+ 00854694 ["INT_ADD", "register:40f0:8", ["const:854694:8", "const:4:8"]]
~~~


### [`00854670`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/00854670.md) → [`008546c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/008546c8.md) FUN_008546c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047b7c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7c0.md) [`0047b848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b848.md) [`0047bd00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md) [`0069ec1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ec1c.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047ad34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047b800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b800.md) [`0047b888`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b888.md) [`0047bd40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047bd40.md) [`0069ec74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ec74.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008547e0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00854788",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008547f4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085479c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00854804",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008547ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      300,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      316,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      300,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      316,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


~~~diff
- 008546d8 ["INT_ADD", "register:40f0:8", ["const:8546d8:8", "const:4:8"]]
+ 00854730 ["INT_ADD", "register:40f0:8", ["const:854730:8", "const:4:8"]]
- 008546ec ["INT_ADD", "register:40f0:8", ["const:8546ec:8", "const:4:8"]]
+ 00854744 ["INT_ADD", "register:40f0:8", ["const:854744:8", "const:4:8"]]
- 008546f4 ["INT_ADD", "register:40f0:8", ["const:8546f4:8", "const:4:8"]]
+ 0085474c ["INT_ADD", "register:40f0:8", ["const:85474c:8", "const:4:8"]]
~~~


### [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) → [`00856e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) FUN_00856e84

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 167件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00440b00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`0044b188`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b188.md)
- 新版 呼出元 0件  · 呼出先 167件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e868`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`00440b40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`0044b1c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b1c8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 46件, `call_target` 50件, `store_destination` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00857140",
      "incomplete_value": true,
      "site": "00857140",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008570e8",
      "incomplete_value": true,
      "site": "008570e8",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008573e4",
      "incomplete_value": true,
      "site": "008573f4",
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
                "const:3cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085738c",
      "incomplete_value": true,
      "site": "0085739c",
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
                "const:39b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008573e8",
      "incomplete_value": true,
      "site": "008573f8",
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
      "definition_site": "00857390",
      "incomplete_value": true,
      "site": "008573a0",
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
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      236,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      248,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      252,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048dcb8"
      ]
    ]
  ],
  "added": [
    [
      236,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      248,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      252,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048dcf8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00856e74 ["INT_ADD", "register:40f0:8", ["const:856e74:8", "const:4:8"]]
- 00856e74 ["CALL", null, ["callee:00472de4:8"]]
- 00856e78 ["INT_ADD", "register:40f0:8", ["const:856e78:8", "const:4:8"]]
- 00856e78 ["CALL", null, ["callee:00474050:8"]]
+ 00856ecc ["INT_ADD", "register:40f0:8", ["const:856ecc:8", "const:4:8"]]
+ 00856ecc ["CALL", null, ["callee:00472de4:8"]]
+ 00856ed0 ["INT_ADD", "register:40f0:8", ["const:856ed0:8", "const:4:8"]]
+ 00856ed0 ["CALL", null, ["callee:00474050:8"]]
~~~


### [`00859a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859a90.md) → [`00859ae8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859ae8.md) FUN_00859ae8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 3件 [`00764ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00856e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 3件 [`00764f38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/00764f38.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "site": "00859b08",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00859ab0",
      "value": [
        "leaf",
        "ram:764ee0:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


~~~diff
- 00859ab0 ["INT_ADD", "register:40f0:8", ["const:859ab0:8", "const:4:8"]]
- 00859ab0 ["CALL", null, ["ram:764ee0:8"]]
+ 00859b08 ["INT_ADD", "register:40f0:8", ["const:859b08:8", "const:4:8"]]
+ 00859b08 ["CALL", null, ["ram:764f38:8"]]
- 00859ac8 ["INT_ADD", "register:40f0:8", ["const:859ac8:8", "const:4:8"]]
+ 00859b20 ["INT_ADD", "register:40f0:8", ["const:859b20:8", "const:4:8"]]
- 00859af4 ["INT_ADD", "register:40f0:8", ["const:859af4:8", "const:4:8"]]
+ 00859b4c ["INT_ADD", "register:40f0:8", ["const:859b4c:8", "const:4:8"]]
~~~


### [`00859b58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) → [`00859bb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) FUN_00859bb0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 81件 [`00467860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467afc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467be8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467be8.md)
- 新版 呼出元 0件  · 呼出先 81件 [`004678a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00467b3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b3c.md) [`00467b6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467c28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467c28.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件, `call_target` 14件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0085a95c",
      "incomplete_value": true,
      "site": "0085a95c",
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
      "definition_site": "0085a904",
      "incomplete_value": true,
      "site": "0085a904",
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
    "ordinal": 97,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0085a9a0",
      "incomplete_value": true,
      "site": "0085a9a0",
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
      "definition_site": "0085a948",
      "incomplete_value": true,
      "site": "0085a948",
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
    "ordinal": 99,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0085aa00",
      "incomplete_value": true,
      "site": "0085aa00",
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
      "definition_site": "0085a9a8",
      "incomplete_value": true,
      "site": "0085a9a8",
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
    "ordinal": 103,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "00ca4c7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      148,
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "00ca4d78",
        null,
        "undefined4"
      ]
    ],
    [
      164,
      "READ",
      [
        "storage",
        "00ca4d7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00859b94 ["INT_ADD", "register:40f0:8", ["const:859b94:8", "const:4:8"]]
+ 00859bec ["INT_ADD", "register:40f0:8", ["const:859bec:8", "const:4:8"]]
- 00859bb0 ["INT_ADD", "register:40f0:8", ["const:859bb0:8", "const:4:8"]]
+ 00859c08 ["INT_ADD", "register:40f0:8", ["const:859c08:8", "const:4:8"]]
- 00859bb4 ["INT_ADD", "register:40f0:8", ["const:859bb4:8", "const:4:8"]]
+ 00859c0c ["INT_ADD", "register:40f0:8", ["const:859c0c:8", "const:4:8"]]
~~~


### [`0085ade0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ade0.md) → [`0085ae38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085a/0085ae38.md) FUN_0085ae38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 15件 [`00467860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467a88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00468c60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046c9c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)
- 新版 呼出元 1件 [`00859bb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 15件 [`004678a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467ac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00468ca0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468ca0.md) [`00468fc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046ca04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0085ae70",
      "incomplete_value": true,
      "site": "0085ae70",
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
      "definition_site": "0085ae18",
      "incomplete_value": true,
      "site": "0085ae18",
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
      "definition_site": "0085ae78",
      "incomplete_value": false,
      "site": "0085ae8c",
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
    "old": {
      "definition_site": "0085ae20",
      "incomplete_value": false,
      "site": "0085ae34",
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
            "const:e58:8"
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
      "definition_site": "0085ae80",
      "incomplete_value": false,
      "site": "0085ae8c",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085ae28",
      "incomplete_value": false,
      "site": "0085ae34",
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
            "const:e68:8"
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
      52,
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00c65e68",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ],
    [
      64,
      "PARAM",
      [
        "storage",
        "00c65f28",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "00c65f38",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085ae14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 0085ae6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0085ae20 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 0085ae78 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 0085ae28 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 0085ae80 ["COPY", "tmp:0:8", ["const:f38:8"]]
~~~


### [`0085b138`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b138.md) → [`0085b190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b190.md) FUN_0085b190

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0046ca54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`0048ce4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce4c.md) [`0048d280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d280.md) [`0083f290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083f/0083f290.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0046ca94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca94.md) [`0046cb4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`0048ce8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce8c.md) [`0048d2c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2c0.md) [`0083f2e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083f/0083f2e8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0085b208",
      "incomplete_value": true,
      "site": "0085b20c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b1b0",
      "incomplete_value": true,
      "site": "0085b1b4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:b68:8"
              ]
            ]
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
      "definition_site": "0085b248",
      "incomplete_value": false,
      "site": "0085b24c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b1f0",
      "incomplete_value": false,
      "site": "0085b1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:c70:8"
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
      120,
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      120,
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085b188 ["INT_ADD", "register:40f0:8", ["const:85b188:8", "const:4:8"]]
+ 0085b1e0 ["INT_ADD", "register:40f0:8", ["const:85b1e0:8", "const:4:8"]]
- 0085b18c ["INT_ADD", "register:40f0:8", ["const:85b18c:8", "const:4:8"]]
+ 0085b1e4 ["INT_ADD", "register:40f0:8", ["const:85b1e4:8", "const:4:8"]]
- 0085b1b0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b68:8"]]
+ 0085b208 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c38:8"]]
~~~


### [`0085b430`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b430.md) → [`0085b488`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b488.md) FUN_0085b488

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00851a0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00877a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877a70.md) [`00877d50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00877/00877d50.md) · 呼出先 25件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00447ef4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`004953d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/004953d4.md)
- 新版 呼出元 3件 [`00851a64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00877ac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877ac8.md) [`00877da8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00877/00877da8.md) · 呼出先 25件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00447f34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`00495414`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/00495414.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085b53c",
      "incomplete_value": false,
      "site": "0085b548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b4e4",
      "incomplete_value": false,
      "site": "0085b4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0085b5b8",
      "incomplete_value": false,
      "site": "0085b5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b560",
      "incomplete_value": false,
      "site": "0085b560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca4000:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085b5ac",
      "incomplete_value": true,
      "site": "0085b5b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085b554",
      "incomplete_value": true,
      "site": "0085b560",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:978:8"
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
      "PARAM",
      [
        "storage",
        "00c65470",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00c7fb50",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      192,
      "DATA",
      [
        "storage",
        "00c7fb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      60,
      "PARAM",
      [
        "storage",
        "00c65540",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00c7fc20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      192,
      "DATA",
      [
        "storage",
        "00c7fc48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085b45c ["INT_ADD", "register:40f0:8", ["const:85b45c:8", "const:4:8"]]
+ 0085b4b4 ["INT_ADD", "register:40f0:8", ["const:85b4b4:8", "const:4:8"]]
- 0085b46c ["COPY", "tmp:0:8", ["const:470:8"]]
+ 0085b4c4 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0085b474 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 0085b4cc ["COPY", "tmp:0:8", ["const:c20:8"]]
~~~


### [`0085c14c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085c14c.md) → [`0085c1a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085c1a4.md) FUN_0085c1a4

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`006dfc2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006df/006dfc2c.md) [`007bbe1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`0085ccf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085ccf0.md) [`009ccb7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb7c.md) [`00a8a418`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 17件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`006e0500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e0/006e0500.md)
- 新版 呼出元 5件 [`006dfc84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006df/006dfc84.md) [`007bbe74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) [`0085cd48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085cd48.md) [`009ccbd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009cc/009ccbd0.md) [`00a8a488`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 17件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`006e0558`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e0/006e0558.md)

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
      "site": "0085c2bc",
      "value": [
        "leaf",
        "ram:8040cc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0085c264",
      "value": [
        "leaf",
        "ram:804074:8"
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
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00804074"
      ]
    ]
  ],
  "added": [
    [
      280,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008040cc"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085c200 ["INT_ADD", "register:40f0:8", ["const:85c200:8", "const:4:8"]]
+ 0085c258 ["INT_ADD", "register:40f0:8", ["const:85c258:8", "const:4:8"]]
- 0085c240 ["INT_ADD", "register:40f0:8", ["const:85c240:8", "const:4:8"]]
+ 0085c298 ["INT_ADD", "register:40f0:8", ["const:85c298:8", "const:4:8"]]
- 0085c24c ["INT_ADD", "register:40f0:8", ["const:85c24c:8", "const:4:8"]]
+ 0085c2a4 ["INT_ADD", "register:40f0:8", ["const:85c2a4:8", "const:4:8"]]
~~~


### [`0085cefc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085c/0085cefc.md) → [`0085cf54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085c/0085cf54.md) FUN_0085cf54

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`006bbc98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006bea88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bea88.md) [`00a8a418`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) [`00a8e5b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) [`00ab0ddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab0ddc.md) · 呼出先 7件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`007457bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/007457bc.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`006bbcf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`006beae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006beae0.md) [`00a8a488`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) [`00a8e624`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) [`00ab0e4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab0e4c.md) · 呼出先 7件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00745814`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00745/00745814.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d038",
      "incomplete_value": true,
      "site": "0085d040",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085cfe0",
      "incomplete_value": true,
      "site": "0085cfe8",
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
                "const:ca3000:8"
              ],
              [
                "leaf",
                "const:f50:8"
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
      "definition_site": "0085d05c",
      "incomplete_value": true,
      "site": "0085d06c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d004",
      "incomplete_value": true,
      "site": "0085d014",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:ca3000:8"
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0085d0c0",
      "incomplete_value": true,
      "site": "0085d0cc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085d068",
      "incomplete_value": true,
      "site": "0085d074",
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
                "const:ca3000:8"
              ],
              [
                "leaf",
                "const:f70:8"
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
      196,
      "DATA",
      [
        "storage",
        "003c7c70",
        null,
        "qword"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00ca3f50",
        null,
        null
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "00ca3f38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      196,
      "DATA",
      [
        "storage",
        "003c7c70",
        null,
        "dword"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00ca4020",
        null,
        null
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "00ca4008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085cfd8 ["COPY", "register:4040:8", ["const:ca3000:8"]]
- 0085cfdc ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 0085d030 ["COPY", "register:4040:8", ["const:ca4000:8"]]
+ 0085d034 ["COPY", "tmp:0:8", ["const:20:8"]]
- 0085cffc ["COPY", "register:4040:8", ["const:ca3000:8"]]
+ 0085d054 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0085d004 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 0085d05c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8:8"]]
~~~


### [`0085d4f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) → [`0085d54c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) FUN_0085d54c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0075ea44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075ea44.md) [`0075eb80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00ab0ddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab0ddc.md) · 呼出先 33件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00459d74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00730cd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cd4.md) [`00730cfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cfc.md) [`00731970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731970.md)
- 新版 呼出元 4件 [`0075ea9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ea9c.md) [`0075ebd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) [`00769ddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00ab0e4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab0e4c.md) · 呼出先 33件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00459db4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00730d2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00730/00730d2c.md) [`00730d54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00730/00730d54.md) [`007319c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00731/007319c8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 33件, `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085da88",
      "incomplete_value": false,
      "site": "0085da88",
      "value": [
        "leaf",
        "const:860a30:8"
      ]
    },
    "old": {
      "definition_site": "0085da30",
      "incomplete_value": false,
      "site": "0085da30",
      "value": [
        "leaf",
        "const:8609d8:8"
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085dc80",
      "incomplete_value": false,
      "site": "0085dc80",
      "value": [
        "leaf",
        "const:860a30:8"
      ]
    },
    "old": {
      "definition_site": "0085dc28",
      "incomplete_value": false,
      "site": "0085dc28",
      "value": [
        "leaf",
        "const:8609d8:8"
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0085ddfc",
      "incomplete_value": false,
      "site": "0085ddfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085dda4",
      "incomplete_value": false,
      "site": "0085dda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "ordinal": 66,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      136,
      "DATA",
      [
        "storage",
        "0038e030",
        "fde_0038e030",
        "dword"
      ]
    ],
    [
      176,
      "DATA",
      [
        "storage",
        "0038e030",
        "fde_0038e030",
        "dword"
      ]
    ],
    [
      196,
      "DATA",
      [
        "storage",
        "0038e028",
        null,
        "byte[27]"
      ]
    ]
  ],
  "added": [
    [
      136,
      "DATA",
      [
        "storage",
        "0038e030",
        null,
        "byte[27]"
      ]
    ],
    [
      176,
      "DATA",
      [
        "storage",
        "0038e030",
        null,
        "byte[27]"
      ]
    ],
    [
      196,
      "DATA",
      [
        "storage",
        "0038e028",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


~~~diff
- 0085d550 ["INT_ADD", "register:40f0:8", ["const:85d550:8", "const:4:8"]]
- 0085d550 ["CALL", null, ["callee:00c58160:8"]]
- 0085d554 ["COPY", "register:4040:8", ["const:160b:8"]]
- 0085d558 ["COPY", "register:4048:8", ["const:33d9:8"]]
+ 0085d5a8 ["INT_ADD", "register:40f0:8", ["const:85d5a8:8", "const:4:8"]]
+ 0085d5a8 ["CALL", null, ["callee:00c58160:8"]]
+ 0085d5ac ["COPY", "register:4040:8", ["const:160b:8"]]
+ 0085d5b0 ["COPY", "register:4048:8", ["const:33d9:8"]]
~~~


### [`00860588`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/00860588.md) → [`008605e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00860/008605e0.md) FUN_008605e0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`0069a504`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) [`00806614`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00806/00806614.md) [`0085d4f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085d/0085d4f4.md) [`00871988`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871988.md) [`0089e87c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 8件 [`007279d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00800378`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`008056ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/008056ec.md) [`008077f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00807/008077f8.md)
- 新版 呼出元 11件 [`0069a55c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) [`0080666c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00806/0080666c.md) [`0085d54c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085d/0085d54c.md) [`008719e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/008719e0.md) [`0089e8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 8件 [`00727a28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00727/00727a28.md) [`008003d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00800684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800684.md) [`00805744`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00805/00805744.md) [`00807850`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00807/00807850.md)

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
      "site": "00860940",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008608e8",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
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
        "002edc66",
        "switchD_008605c0::switchdataD_002edc66",
        "byte"
      ]
    ],
    [
      864,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "002edca6",
        "switchD_00860618::switchdataD_002edca6",
        "byte"
      ]
    ],
    [
      864,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


~~~diff
- 008605a8 ["COPY", "tmp:0:8", ["const:c66:8"]]
+ 00860600 ["COPY", "tmp:0:8", ["const:ca6:8"]]
- 008605b0 ["COPY", "register:4050:8", ["const:8605c4:8"]]
+ 00860608 ["COPY", "register:4050:8", ["const:86061c:8"]]
- 00860624 ["INT_ADD", "register:40f0:8", ["const:860624:8", "const:4:8"]]
+ 0086067c ["INT_ADD", "register:40f0:8", ["const:86067c:8", "const:4:8"]]
~~~


### [`00860a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/00860a90.md) → [`00860ae8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00860/00860ae8.md) FUN_00860ae8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005fe66c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00a06d9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a85294`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a85/00a85294.md) · 呼出先 12件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005c1844`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1844.md)
- 新版 呼出元 3件 [`005fe6ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fe/005fe6ac.md) [`00a06df0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) [`00a85304`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a85/00a85304.md) · 呼出先 12件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`005c1884`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1884.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00861060",
      "incomplete_value": true,
      "site": "00861060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00861008",
      "incomplete_value": true,
      "site": "00861008",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 81,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008610e4",
      "incomplete_value": true,
      "site": "008610ec",
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086108c",
      "incomplete_value": true,
      "site": "00861094",
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 86,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      1380,
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      1532,
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      1380,
      "READ",
      [
        "storage",
        "002b8dc9",
        null,
        "string"
      ]
    ],
    [
      1532,
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00860ae0 ["INT_ADD", "register:40f0:8", ["const:860ae0:8", "const:4:8"]]
+ 00860b38 ["INT_ADD", "register:40f0:8", ["const:860b38:8", "const:4:8"]]
- 00860b38 ["INT_ADD", "register:40f0:8", ["const:860b38:8", "const:4:8"]]
+ 00860b90 ["INT_ADD", "register:40f0:8", ["const:860b90:8", "const:4:8"]]
- 00860b80 ["INT_ADD", "register:40f0:8", ["const:860b80:8", "const:4:8"]]
+ 00860bd8 ["INT_ADD", "register:40f0:8", ["const:860bd8:8", "const:4:8"]]
~~~


### [`00861388`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/00861388.md) → [`008613e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008613e0.md) FUN_008613e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00a06d9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 9件 [`005509b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509b8.md) [`00871b84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b84.md) [`00871b88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00871/00871b88.md) [`0087d504`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d504.md) [`0087d508`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087d/0087d508.md)
- 新版 呼出元 2件 [`00769ddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00a06df0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 9件 [`005509f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509f8.md) [`00871bdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871bdc.md) [`00871be0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00871/00871be0.md) [`0087d55c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d55c.md) [`0087d560`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087d/0087d560.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00861410",
      "incomplete_value": false,
      "site": "00861410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008613b8",
      "incomplete_value": false,
      "site": "008613b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086141c",
      "value": [
        "leaf",
        "ram:5509f8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008613c4",
      "value": [
        "leaf",
        "ram:5509b8:8"
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
      48,
      "DATA",
      [
        "storage",
        "00c7f9d0",
        null,
        "undefined *"
      ]
    ],
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005509b8"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c7f9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "DATA",
      [
        "storage",
        "00c7faa0",
        null,
        "undefined *"
      ]
    ],
    [
      60,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005509f8"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "00c7fac0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 008613b4 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 0086140c ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 008613c4 ["INT_ADD", "register:40f0:8", ["const:8613c4:8", "const:4:8"]]
- 008613c4 ["CALL", null, ["ram:5509b8:8"]]
+ 0086141c ["INT_ADD", "register:40f0:8", ["const:86141c:8", "const:4:8"]]
+ 0086141c ["CALL", null, ["ram:5509f8:8"]]
- 008613f0 ["INT_ADD", "register:40f0:8", ["const:8613f0:8", "const:4:8"]]
+ 00861448 ["INT_ADD", "register:40f0:8", ["const:861448:8", "const:4:8"]]
~~~


### [`0086155c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00861/0086155c.md) → [`008615b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00861/008615b4.md) FUN_008615b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 18件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md) [`00487e20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 1件 [`00b28ff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 18件 [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487bc0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487bc0.md) [`00487e60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008615f8",
      "incomplete_value": false,
      "site": "00861600",
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
    "old": {
      "definition_site": "008615a0",
      "incomplete_value": false,
      "site": "008615a8",
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
            "const:d38:8"
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
      "definition_site": "00861628",
      "incomplete_value": true,
      "site": "00861638",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:836:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008615d0",
      "incomplete_value": true,
      "site": "008615e0",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:88a:8"
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
      "definition_site": "00862714",
      "incomplete_value": true,
      "site": "00862718",
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
      "definition_site": "008626bc",
      "incomplete_value": true,
      "site": "008626c0",
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
    "ordinal": 207,
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
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002ba88a",
        null,
        "string"
      ]
    ],
    [
      4432,
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
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
      116,
      "READ",
      [
        "storage",
        "002ba836",
        null,
        "string"
      ]
    ],
    [
      4432,
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00861594 ["INT_ADD", "register:40f0:8", ["const:861594:8", "const:4:8"]]
+ 008615ec ["INT_ADD", "register:40f0:8", ["const:8615ec:8", "const:4:8"]]
- 008615a0 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 008615f8 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 008615b4 ["INT_ADD", "register:40f0:8", ["const:8615b4:8", "const:4:8"]]
+ 0086160c ["INT_ADD", "register:40f0:8", ["const:86160c:8", "const:4:8"]]
~~~


### [`008628a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/008628a8.md) → [`00862900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862900.md) FUN_00862900

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00700544`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md) [`00773894`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00835bb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00835/00835bb8.md) [`00a022d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) · 呼出先 8件 [`00467860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467e9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md) [`00467ea4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ea4.md) [`0046c9c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)
- 新版 呼出元 4件 [`0070059c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/0070059c.md) [`007738ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`00835c10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00835/00835c10.md) [`00a0232c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a0232c.md) · 呼出先 8件 [`004678a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`00467edc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467edc.md) [`00467ee4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ee4.md) [`0046ca04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046cac4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cac4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00862930",
      "incomplete_value": true,
      "site": "00862934",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
      "definition_site": "008628d8",
      "incomplete_value": true,
      "site": "008628dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00862944",
      "incomplete_value": false,
      "site": "00862948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca8000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008628ec",
      "incomplete_value": false,
      "site": "008628f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca8000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      36,
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00ca8170",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00ca8270",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 008628cc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b68:8"]]
+ 00862924 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c38:8"]]
- 008628dc ["INT_ADD", "register:40f0:8", ["const:8628dc:8", "const:4:8"]]
+ 00862934 ["INT_ADD", "register:40f0:8", ["const:862934:8", "const:4:8"]]
- 008628e4 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 0086293c ["COPY", "tmp:0:8", ["const:270:8"]]
~~~


### [`00862980`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/00862980.md) → [`008629d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/008629d8.md) FUN_008629d8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008acd54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acd54.md) · 呼出先 5件 [`00597ebc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`008acdac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ac/008acdac.md) · 呼出先 5件 [`00597efc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00c53da0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 4件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00862a04",
      "incomplete_value": true,
      "site": "00862a04",
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
                "const:caa000:8"
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
              "INT_ZEXT",
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
      "definition_site": "008629ac",
      "incomplete_value": true,
      "site": "008629ac",
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
                "const:ca9000:8"
              ],
              [
                "leaf",
                "const:f48:8"
              ]
            ]
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_ZEXT",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00862a08",
      "incomplete_value": false,
      "site": "00862a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:caa000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008629b0",
      "incomplete_value": false,
      "site": "008629b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca9000:8"
          ],
          [
            "leaf",
            "const:f48:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00862a0c",
      "incomplete_value": false,
      "site": "00862a0c",
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
                "const:caa000:8"
              ],
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "008629b4",
      "incomplete_value": false,
      "site": "008629b4",
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
                "const:ca9000:8"
              ],
              [
                "leaf",
                "const:f48:8"
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
      44,
      "WRITE",
      [
        "storage",
        "0112183a",
        null,
        "undefined2"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "00ca9f48",
        null,
        "undefined4"
      ]
    ],
    [
      52,
      "WRITE",
      [
        "storage",
        "00ca9f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      44,
      "WRITE",
      [
        "storage",
        "0112193a",
        null,
        "undefined2"
      ]
    ],
    [
      48,
      "WRITE",
      [
        "storage",
        "00caa048",
        null,
        "undefined4"
      ]
    ],
    [
      52,
      "WRITE",
      [
        "storage",
        "00caa050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 008629a4 ["COPY", "register:4040:8", ["const:ca9000:8"]]
- 008629a8 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 008629fc ["COPY", "register:4040:8", ["const:caa000:8"]]
+ 00862a00 ["COPY", "tmp:0:8", ["const:48:8"]]
- 008629c4 ["INT_ADD", "register:40f0:8", ["const:8629c4:8", "const:4:8"]]
+ 00862a1c ["INT_ADD", "register:40f0:8", ["const:862a1c:8", "const:4:8"]]
- 008629d4 ["INT_ADD", "register:40f0:8", ["const:8629d4:8", "const:4:8"]]
+ 00862a2c ["INT_ADD", "register:40f0:8", ["const:862a2c:8", "const:4:8"]]
~~~


### [`00862c50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/00862c50.md) → [`00862ca8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00862/00862ca8.md) FUN_00862ca8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`0067d4d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d4d0.md) [`007562a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`0078c21c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007b0a18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`008378d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md) · 呼出先 13件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)
- 新版 呼出元 13件 [`0067d510`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067d/0067d510.md) [`007562fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`0078c274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078c/0078c274.md) [`007b0a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`00837930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) · 呼出先 13件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00447f34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 26件, `store_condition` 5件, `store_destination` 33件, `store_value` 18件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00862d14",
      "incomplete_value": true,
      "site": "00862d20",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00862cbc",
      "incomplete_value": true,
      "site": "00862cc8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00862d10",
      "incomplete_value": true,
      "site": "00862d28",
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
                "const:224:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862cb8",
      "incomplete_value": true,
      "site": "00862cd0",
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
                "const:1f5:8"
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
      "definition_site": "00862d2c",
      "incomplete_value": true,
      "site": "00862d44",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00862cd4",
      "incomplete_value": true,
      "site": "00862cec",
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
                "const:2a0:8"
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
      52,
      "PARAM",
      [
        "storage",
        "00ca8d50",
        null,
        null
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "002a91f5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      52,
      "PARAM",
      [
        "storage",
        "00ca8e50",
        null,
        null
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "002a9224",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00862c84 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00862cdc ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00862c8c ["INT_ADD", "register:40f0:8", ["const:862c8c:8", "const:4:8"]]
+ 00862ce4 ["INT_ADD", "register:40f0:8", ["const:862ce4:8", "const:4:8"]]
- 00862c94 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00862c98 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00862cec ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00862cf0 ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`008636dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00863/008636dc.md) → [`00863734`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00863/00863734.md) FUN_00863734

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`006b0238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b0/006b0238.md) [`0073b9fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b9fc.md) [`008d0cb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d0/008d0cb8.md) [`008e0c30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008e0/008e0c30.md) [`00908314`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00908/00908314.md) · 呼出先 13件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 7件 [`006b0290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b0/006b0290.md) [`0073ba54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073ba54.md) [`008d0d0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d0/008d0d0c.md) [`008e0c84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008e0/008e0c84.md) [`00908368`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00908/00908368.md) · 呼出先 13件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00447f34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047edf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 22件, `store_condition` 5件, `store_destination` 24件, `store_value` 14件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0086379c",
      "incomplete_value": true,
      "site": "008637a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00863744",
      "incomplete_value": true,
      "site": "00863750",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00863798",
      "incomplete_value": true,
      "site": "008637b0",
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
                "const:224:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00863740",
      "incomplete_value": true,
      "site": "00863758",
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
                "const:1f5:8"
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
      "definition_site": "008637b4",
      "incomplete_value": true,
      "site": "008637cc",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0086375c",
      "incomplete_value": true,
      "site": "00863774",
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
                "const:2a0:8"
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
      44,
      "PARAM",
      [
        "storage",
        "00ca8d50",
        null,
        null
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "002a91f5",
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
        "00ca8e50",
        null,
        null
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      100,
      "READ",
      [
        "storage",
        "002a9224",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00863708 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00863760 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00863714 ["INT_ADD", "register:40f0:8", ["const:863714:8", "const:4:8"]]
+ 0086376c ["INT_ADD", "register:40f0:8", ["const:86376c:8", "const:4:8"]]
- 0086371c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00863720 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00863774 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 00863778 ["COPY", "tmp:0:8", ["const:38:8"]]
~~~


### [`00864160`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864160.md) → [`008641b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/008641b8.md) FUN_008641b8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`006714ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00671/006714ac.md) [`00754910`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00754/00754910.md) [`007562a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`0078c21c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007b0a18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 9件 [`0047e60c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00744208`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 11件 [`006714ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00671/006714ec.md) [`00754968`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00754/00754968.md) [`007562fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00756/007562fc.md) [`0078c274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078c/0078c274.md) [`007b0a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) · 呼出先 9件 [`0047e64c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00744260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 18件, `store_destination` 21件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00864208",
      "incomplete_value": true,
      "site": "00864238",
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
                "const:23d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008641b0",
      "incomplete_value": true,
      "site": "008641e0",
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
                "const:20e:8"
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
      "definition_site": "0086423c",
      "incomplete_value": true,
      "site": "0086423c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:5f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008641e4",
      "incomplete_value": true,
      "site": "008641e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:646:8"
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
      "definition_site": "00864240",
      "incomplete_value": true,
      "site": "00864240",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008641e8",
      "incomplete_value": true,
      "site": "008641e8",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002a920e",
        null,
        "string"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a0646",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002a923d",
        null,
        "string"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a05f9",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0086418c ["INT_ADD", "register:40f0:8", ["const:86418c:8", "const:4:8"]]
+ 008641e4 ["INT_ADD", "register:40f0:8", ["const:8641e4:8", "const:4:8"]]
- 00864194 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00864198 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008641ec ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 008641f0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008641ac ["COPY", "tmp:0:8", ["const:20e:8"]]
+ 00864204 ["COPY", "tmp:0:8", ["const:23d:8"]]
~~~


### [`00864538`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864538.md) → [`00864590`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864590.md) FUN_00864590

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0067d4d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067d/0067d4d0.md) [`006b0238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b0/006b0238.md) [`0073b9fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073b/0073b9fc.md) [`007b0a18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`008378d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00837/008378d8.md) · 呼出先 9件 [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00633374`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`00744208`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 10件 [`0067d510`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067d/0067d510.md) [`006b0290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b0/006b0290.md) [`0073ba54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073b/0073ba54.md) [`007b0a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) [`00837930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00837/00837930.md) · 呼出先 9件 [`0047edf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`006333b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) [`00744260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00744/00744260.md) [`00c57f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 17件, `store_destination` 21件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008645e0",
      "incomplete_value": true,
      "site": "00864610",
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
                "const:23d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00864588",
      "incomplete_value": true,
      "site": "008645b8",
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
                "const:20e:8"
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
      "definition_site": "00864614",
      "incomplete_value": true,
      "site": "00864614",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:5f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008645bc",
      "incomplete_value": true,
      "site": "008645bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:646:8"
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
      "definition_site": "00864618",
      "incomplete_value": true,
      "site": "00864618",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008645c0",
      "incomplete_value": true,
      "site": "008645c0",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002a920e",
        null,
        "string"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a0646",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      60,
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002a923d",
        null,
        "string"
      ]
    ],
    [
      120,
      "READ",
      [
        "storage",
        "002a05f9",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00864564 ["INT_ADD", "register:40f0:8", ["const:864564:8", "const:4:8"]]
+ 008645bc ["INT_ADD", "register:40f0:8", ["const:8645bc:8", "const:4:8"]]
- 0086456c ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 00864570 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 008645c4 ["COPY", "register:4040:8", ["const:ca5000:8"]]
+ 008645c8 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00864584 ["COPY", "tmp:0:8", ["const:20e:8"]]
+ 008645dc ["COPY", "tmp:0:8", ["const:23d:8"]]
~~~


### [`00864910`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864910.md) → [`00864968`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864968.md) FUN_00864968

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048dd40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dd40.md) [`0048e900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e900.md) · 呼出先 15件 [`0046d6ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d6ac.md) [`0048e0b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`0048e194`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e194.md) [`00493980`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493980.md) [`00493a48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493a48.md)
- 新版 呼出元 2件 [`0048dd80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048dd80.md) [`0048e940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e940.md) · 呼出先 15件 [`0046d6ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d6ec.md) [`0048e0f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e0f8.md) [`0048e1d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e1d4.md) [`004939c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939c0.md) [`00493a88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493a88.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00864aec",
      "incomplete_value": false,
      "site": "00864b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00864a94",
      "incomplete_value": false,
      "site": "00864aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
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
        "002bb253",
        null,
        "string"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "002bb25a",
        null,
        "string"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "002bb1ff",
        null,
        "string"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "002bb206",
        null,
        "string"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 0086493c ["COPY", "tmp:0:8", ["const:253:8"]]
+ 00864994 ["COPY", "tmp:0:8", ["const:1ff:8"]]
- 00864970 ["INT_ADD", "register:40f0:8", ["const:864970:8", "const:4:8"]]
+ 008649c8 ["INT_ADD", "register:40f0:8", ["const:8649c8:8", "const:4:8"]]
- 00864984 ["INT_ADD", "register:40f0:8", ["const:864984:8", "const:4:8"]]
+ 008649dc ["INT_ADD", "register:40f0:8", ["const:8649dc:8", "const:4:8"]]
~~~


### [`00864ce0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00864/00864ce0.md) → [`00864d38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00864/00864d38.md) FUN_00864d38

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0089788c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) [`008a54b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a54b4.md) · 呼出先 12件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492ccc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492ccc.md) [`00564588`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00564/00564588.md)
- 新版 呼出元 2件 [`008978e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) [`008a550c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a5/008a550c.md) · 呼出先 12件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`0048cd38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492d0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d0c.md) [`005645c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00564/005645c8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00864ed8",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00864e80",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00864f00",
      "incomplete_value": false,
      "site": "00864f0c",
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
            "const:10f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00864ea8",
      "incomplete_value": false,
      "site": "00864eb4",
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
            "const:16b:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00864f2c",
      "incomplete_value": false,
      "site": "00864f34",
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
            "const:126:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00864ed4",
      "incomplete_value": false,
      "site": "00864edc",
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
            "const:182:8"
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
      116,
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ],
    [
      416,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      116,
      "PARAM",
      [
        "storage",
        "002a6430",
        null,
        null
      ]
    ],
    [
      132,
      "PARAM",
      [
        "storage",
        "002a6430",
        null,
        null
      ]
    ],
    [
      416,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


~~~diff
- 00864d34 ["COPY", "tmp:0:8", ["const:48c:8"]]
+ 00864d8c ["COPY", "tmp:0:8", ["const:430:8"]]
- 00864d5c ["INT_ADD", "register:40f0:8", ["const:864d5c:8", "const:4:8"]]
+ 00864db4 ["INT_ADD", "register:40f0:8", ["const:864db4:8", "const:4:8"]]
- 00864d68 ["INT_ADD", "register:40f0:8", ["const:864d68:8", "const:4:8"]]
+ 00864dc0 ["INT_ADD", "register:40f0:8", ["const:864dc0:8", "const:4:8"]]
~~~


### [`00865110`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865110.md) → [`00865168`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865168.md) FUN_00865168

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008a69c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a69c4.md) [`008a6c2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6c2c.md) [`008a75d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a75d0.md) [`008a7758`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7758.md) · 呼出先 14件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`004928ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/004928ac.md) [`00492d04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492d04.md)
- 新版 呼出元 4件 [`008a6a1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a6/008a6a1c.md) [`008a6c84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a6/008a6c84.md) [`008a7628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a7628.md) [`008a77b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008a7/008a77b0.md) · 呼出先 14件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048cd38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`0048e820`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048e/0048e820.md) [`004928ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004928ec.md) [`00492d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d44.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008652c8",
      "incomplete_value": true,
      "site": "008652c8",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00865270",
      "incomplete_value": true,
      "site": "00865270",
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
            "const:a60:8"
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
      "definition_site": "00865388",
      "incomplete_value": false,
      "site": "00865388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00865330",
      "incomplete_value": false,
      "site": "00865330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00865264",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0086520c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      252,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      260,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      352,
      "DATA",
      [
        "storage",
        "00c7fa60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      252,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      260,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      352,
      "DATA",
      [
        "storage",
        "00c7fb30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0086517c ["INT_ADD", "register:40f0:8", ["const:86517c:8", "const:4:8"]]
+ 008651d4 ["INT_ADD", "register:40f0:8", ["const:8651d4:8", "const:4:8"]]
- 0086520c ["INT_ADD", "register:40f0:8", ["const:86520c:8", "const:4:8"]]
- 0086520c ["CALL", null, ["ram:48ccf8:8"]]
- 00865210 ["INT_ADD", "register:40f0:8", ["const:865210:8", "const:4:8"]]
+ 00865264 ["INT_ADD", "register:40f0:8", ["const:865264:8", "const:4:8"]]
+ 00865264 ["CALL", null, ["ram:48cd38:8"]]
+ 00865268 ["INT_ADD", "register:40f0:8", ["const:865268:8", "const:4:8"]]
- 00865214 ["INT_ADD", "register:40f0:8", ["const:865214:8", "const:4:8"]]
- 00865214 ["CALL", null, ["ram:48ccf8:8"]]
+ 0086526c ["INT_ADD", "register:40f0:8", ["const:86526c:8", "const:4:8"]]
+ 0086526c ["CALL", null, ["ram:48cd38:8"]]
~~~


