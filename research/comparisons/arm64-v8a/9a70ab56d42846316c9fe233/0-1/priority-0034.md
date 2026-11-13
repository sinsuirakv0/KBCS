# v16.0.0 → v16.0.1 · 最優先の変更候補 (34)

[一覧の目次](README.md)

### [`0070041c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/0070041c.md) → [`0070045c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/0070045c.md) FUN_0070045c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00700488",
      "incomplete_value": false,
      "site": "00700488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700448",
      "incomplete_value": false,
      "site": "00700448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:218:8"
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
      44,
      "DATA",
      [
        "storage",
        "00c77218",
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
        "00c77618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00700440 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 00700480 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00700460 ["INT_ADD", "register:40f0:8", ["const:700460:8", "const:4:8"]]
+ 007004a0 ["INT_ADD", "register:40f0:8", ["const:7004a0:8", "const:4:8"]]
- 00700478 ["INT_ADD", "register:40f0:8", ["const:700478:8", "const:4:8"]]
+ 007004b8 ["INT_ADD", "register:40f0:8", ["const:7004b8:8", "const:4:8"]]
~~~


### [`00700504`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md) → [`00700544`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md) FUN_00700544

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00467820`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467d74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`0046a210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0055a5a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5a4.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00467860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`0046a250`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0055a5e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5e4.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007005e8",
      "incomplete_value": true,
      "site": "007005ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "007005a8",
      "incomplete_value": true,
      "site": "007005ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
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
      "definition_site": "007005d4",
      "incomplete_value": false,
      "site": "007005ec",
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
    "old": {
      "definition_site": "00700594",
      "incomplete_value": false,
      "site": "007005ac",
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
            "const:a58:8"
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
      "definition_site": "007005e0",
      "incomplete_value": false,
      "site": "007005ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007005a0",
      "incomplete_value": false,
      "site": "007005ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      144,
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00c73410",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      144,
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00c73810",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00700538 ["INT_ADD", "register:40f0:8", ["const:700538:8", "const:4:8"]]
+ 00700578 ["INT_ADD", "register:40f0:8", ["const:700578:8", "const:4:8"]]
- 00700544 ["INT_ADD", "register:40f0:8", ["const:700544:8", "const:4:8"]]
+ 00700584 ["INT_ADD", "register:40f0:8", ["const:700584:8", "const:4:8"]]
- 00700550 ["INT_ADD", "register:40f0:8", ["const:700550:8", "const:4:8"]]
+ 00700590 ["INT_ADD", "register:40f0:8", ["const:700590:8", "const:4:8"]]
~~~


### [`00700728`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700728.md) → [`00700768`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700768.md) _INIT_111

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007007a4",
      "incomplete_value": true,
      "site": "007007c0",
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
    "old": {
      "definition_site": "00700764",
      "incomplete_value": true,
      "site": "00700780",
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
                "const:ee6:8"
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
      "definition_site": "007007c8",
      "incomplete_value": true,
      "site": "007007e4",
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
    "old": {
      "definition_site": "00700788",
      "incomplete_value": true,
      "site": "007007a4",
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
                "const:ef9:8"
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
      "definition_site": "007007e8",
      "incomplete_value": true,
      "site": "00700804",
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
    "old": {
      "definition_site": "007007a8",
      "incomplete_value": true,
      "site": "007007c4",
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
                "const:d82:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 00700754 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00700794 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00700760 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 007007a0 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0070077c ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 007007bc ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) → [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) FUN_00700af8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 293件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00856e2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 293件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 65件, `store_destination` 1件, `store_value` 17件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00700b50",
      "incomplete_value": true,
      "site": "00700b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700b10",
      "incomplete_value": true,
      "site": "00700b10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:299:8"
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
      "definition_site": "00700b54",
      "incomplete_value": true,
      "site": "00700b54",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00700b14",
      "incomplete_value": true,
      "site": "00700b14",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00700b90",
      "incomplete_value": true,
      "site": "00700ba4",
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00700b50",
      "incomplete_value": true,
      "site": "00700b64",
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
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
        "002b9299",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002b929e",
        null,
        "string"
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "002b8320",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      56,
      "READ",
      [
        "storage",
        "002b92d9",
        null,
        "string"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "002b92de",
        null,
        "string"
      ]
    ],
    [
      152,
      "READ",
      [
        "storage",
        "002b8360",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00700ae8 ["COPY", "tmp:0:8", ["const:299:8"]]
- 00700ae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00700ae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00700ae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00700b28 ["COPY", "tmp:0:8", ["const:2d9:8"]]
+ 00700b28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00700b28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00700b28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
~~~


### [`00707528`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) → [`00707568`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md) FUN_00707568

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00934734`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) · 呼出先 14件 [`0047e89c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005e1ad8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`005e1af0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`00664860`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md)
- 新版 呼出元 2件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`009348d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009348d0.md) · 呼出先 14件 [`0047e8dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005e1b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e1b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`006648a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "007077ec",
      "incomplete_value": false,
      "site": "007077ec",
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
    "old": {
      "definition_site": "007077ac",
      "incomplete_value": false,
      "site": "007077ac",
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
                "const:b00:8"
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
      "definition_site": "007077f0",
      "incomplete_value": false,
      "site": "007077f0",
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
    "old": {
      "definition_site": "007077b0",
      "incomplete_value": false,
      "site": "007077b0",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007077ec",
      "incomplete_value": false,
      "site": "007077f0",
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
    "old": {
      "definition_site": "007077ac",
      "incomplete_value": false,
      "site": "007077b0",
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
                "const:b00:8"
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
      48,
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00c71578",
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
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      68,
      "PARAM",
      [
        "storage",
        "00c71978",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00707558 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 00707598 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
- 00707564 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 007075a4 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 0070756c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 007075ac ["COPY", "tmp:0:8", ["const:978:8"]]
~~~


### [`0070780c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/0070780c.md) → [`0070784c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070784c.md) FUN_0070784c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 3件 [`00936428`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 3件 [`009365c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00707880",
      "incomplete_value": true,
      "site": "00707894",
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
                "const:30a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00707840",
      "incomplete_value": true,
      "site": "00707854",
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
                "const:2ca:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00707898",
      "incomplete_value": true,
      "site": "00707898",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00707858",
      "incomplete_value": true,
      "site": "00707858",
      "value": [
        "LOAD",
        "8",
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
        "002b92ca",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "002b92d7",
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
        "002b930a",
        null,
        "string"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "002b9317",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00707838 ["COPY", "tmp:0:8", ["const:2ca:8"]]
+ 00707878 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0070786c ["INT_ADD", "register:40f0:8", ["const:70786c:8", "const:4:8"]]
+ 007078ac ["INT_ADD", "register:40f0:8", ["const:7078ac:8", "const:4:8"]]
- 0070788c ["INT_ADD", "register:40f0:8", ["const:70788c:8", "const:4:8"]]
+ 007078cc ["INT_ADD", "register:40f0:8", ["const:7078cc:8", "const:4:8"]]
~~~


### [`00707ea0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) → [`00707ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) FUN_00707ee0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00859b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 174件 [`00467a48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00467ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467abc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467aec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md)
- 新版 呼出元 1件 [`00859b58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 174件 [`00467a88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467af0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467afc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 82件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070a710",
      "incomplete_value": true,
      "site": "0070a728",
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
                "const:2f9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070a6d0",
      "incomplete_value": true,
      "site": "0070a6e8",
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
                "const:2b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 152,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070ac40",
      "incomplete_value": true,
      "site": "0070ac54",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:242:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070ac00",
      "incomplete_value": true,
      "site": "0070ac14",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:202:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 166,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070ac88",
      "incomplete_value": true,
      "site": "0070ac94",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:d8d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070ac48",
      "incomplete_value": true,
      "site": "0070ac54",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:d4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 169,
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
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00c71578",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      112,
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      156,
      "PARAM",
      [
        "storage",
        "00c71978",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 00707f10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:578:8"]]
- 00707f10 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00707f14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:178:8"]]
- 00707f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00707f50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:978:8"]]
+ 00707f50 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00707f54 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:178:8"]]
+ 00707f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
~~~


### [`0070e150`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e150.md) → [`0070e190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e190.md) FUN_0070e190

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e1b4",
      "incomplete_value": false,
      "site": "0070e1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e174",
      "incomplete_value": false,
      "site": "0070e174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
        "00c77298",
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
        "00c77698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e164 ["INT_ADD", "register:40f0:8", ["const:70e164:8", "const:4:8"]]
+ 0070e1a4 ["INT_ADD", "register:40f0:8", ["const:70e1a4:8", "const:4:8"]]
- 0070e170 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0070e1b0 ["COPY", "tmp:0:8", ["const:698:8"]]
~~~


### [`0070e184`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e184.md) → [`0070e1c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1c4.md) FUN_0070e1c4

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
      "definition_site": "0070e1d0",
      "incomplete_value": false,
      "site": "0070e1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e190",
      "incomplete_value": false,
      "site": "0070e190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
        "00c77298",
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
        "00c77698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e18c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 0070e1cc ["COPY", "tmp:0:8", ["const:698:8"]]
~~~


### [`0070e1a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e1a0.md) → [`0070e1e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1e0.md) FUN_0070e1e0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0070e208",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e1c8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e1c8 ["INT_ADD", "register:40f0:8", ["const:70e1c8:8", "const:4:8"]]
- 0070e1c8 ["CALL", null, ["ram:47acb4:8"]]
+ 0070e208 ["INT_ADD", "register:40f0:8", ["const:70e208:8", "const:4:8"]]
+ 0070e208 ["CALL", null, ["ram:47acf4:8"]]
- 0070e1d4 ["INT_ADD", "register:40f0:8", ["const:70e1d4:8", "const:4:8"]]
+ 0070e214 ["INT_ADD", "register:40f0:8", ["const:70e214:8", "const:4:8"]]
~~~


### [`0070e22c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e22c.md) → [`0070e26c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e26c.md) FUN_0070e26c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e290",
      "incomplete_value": false,
      "site": "0070e290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e250",
      "incomplete_value": false,
      "site": "0070e250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
        "00c77318",
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
        "00c77718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e240 ["INT_ADD", "register:40f0:8", ["const:70e240:8", "const:4:8"]]
+ 0070e280 ["INT_ADD", "register:40f0:8", ["const:70e280:8", "const:4:8"]]
- 0070e24c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0070e28c ["COPY", "tmp:0:8", ["const:718:8"]]
~~~


### [`0070e260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e260.md) → [`0070e2a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2a0.md) FUN_0070e2a0

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
      "definition_site": "0070e2ac",
      "incomplete_value": false,
      "site": "0070e2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e26c",
      "incomplete_value": false,
      "site": "0070e26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:318:8"
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
        "00c77318",
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
        "00c77718",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e268 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0070e2a8 ["COPY", "tmp:0:8", ["const:718:8"]]
~~~


### [`0070e27c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e27c.md) → [`0070e2bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2bc.md) FUN_0070e2bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0070e2e4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e2a4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e2a4 ["INT_ADD", "register:40f0:8", ["const:70e2a4:8", "const:4:8"]]
- 0070e2a4 ["CALL", null, ["ram:47acb4:8"]]
+ 0070e2e4 ["INT_ADD", "register:40f0:8", ["const:70e2e4:8", "const:4:8"]]
+ 0070e2e4 ["CALL", null, ["ram:47acf4:8"]]
- 0070e2b0 ["INT_ADD", "register:40f0:8", ["const:70e2b0:8", "const:4:8"]]
+ 0070e2f0 ["INT_ADD", "register:40f0:8", ["const:70e2f0:8", "const:4:8"]]
~~~


### [`0070e314`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e314.md) → [`0070e354`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e354.md) FUN_0070e354

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e374",
      "incomplete_value": false,
      "site": "0070e378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e334",
      "incomplete_value": false,
      "site": "0070e338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
        "00c77398",
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
        "00c77798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e328 ["INT_ADD", "register:40f0:8", ["const:70e328:8", "const:4:8"]]
+ 0070e368 ["INT_ADD", "register:40f0:8", ["const:70e368:8", "const:4:8"]]
- 0070e334 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0070e374 ["COPY", "tmp:0:8", ["const:798:8"]]
~~~


### [`0070e34c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e34c.md) → [`0070e38c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e38c.md) FUN_0070e38c

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
      "definition_site": "0070e390",
      "incomplete_value": false,
      "site": "0070e394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e350",
      "incomplete_value": false,
      "site": "0070e354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:398:8"
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
        "00c77398",
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
        "00c77798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e350 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 0070e390 ["COPY", "tmp:0:8", ["const:798:8"]]
~~~


### [`0070e3a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e3a4.md) → [`0070e3e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e3e4.md) FUN_0070e3e4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e408",
      "incomplete_value": false,
      "site": "0070e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e3c8",
      "incomplete_value": false,
      "site": "0070e3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
        "00c77418",
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
        "00c77818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e3b8 ["INT_ADD", "register:40f0:8", ["const:70e3b8:8", "const:4:8"]]
+ 0070e3f8 ["INT_ADD", "register:40f0:8", ["const:70e3f8:8", "const:4:8"]]
- 0070e3c4 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0070e404 ["COPY", "tmp:0:8", ["const:818:8"]]
~~~


### [`0070e3d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e3d8.md) → [`0070e418`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e418.md) FUN_0070e418

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
      "definition_site": "0070e424",
      "incomplete_value": false,
      "site": "0070e424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e3e4",
      "incomplete_value": false,
      "site": "0070e3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:418:8"
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
        "00c77418",
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
        "00c77818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e3e0 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0070e420 ["COPY", "tmp:0:8", ["const:818:8"]]
~~~


### [`0070e3f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e3f4.md) → [`0070e434`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e434.md) FUN_0070e434

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0070e45c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e41c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e41c ["INT_ADD", "register:40f0:8", ["const:70e41c:8", "const:4:8"]]
- 0070e41c ["CALL", null, ["ram:47acb4:8"]]
+ 0070e45c ["INT_ADD", "register:40f0:8", ["const:70e45c:8", "const:4:8"]]
+ 0070e45c ["CALL", null, ["ram:47acf4:8"]]
- 0070e428 ["INT_ADD", "register:40f0:8", ["const:70e428:8", "const:4:8"]]
+ 0070e468 ["INT_ADD", "register:40f0:8", ["const:70e468:8", "const:4:8"]]
~~~


### [`0070e480`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e480.md) → [`0070e4c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e4c0.md) FUN_0070e4c0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e4e0",
      "incomplete_value": false,
      "site": "0070e4e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e4a0",
      "incomplete_value": false,
      "site": "0070e4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
        "00c77498",
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
        "00c77898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e494 ["INT_ADD", "register:40f0:8", ["const:70e494:8", "const:4:8"]]
+ 0070e4d4 ["INT_ADD", "register:40f0:8", ["const:70e4d4:8", "const:4:8"]]
- 0070e4a0 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0070e4e0 ["COPY", "tmp:0:8", ["const:898:8"]]
~~~


### [`0070e4b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e4b8.md) → [`0070e4f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e4f8.md) FUN_0070e4f8

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
      "definition_site": "0070e4fc",
      "incomplete_value": false,
      "site": "0070e500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e4bc",
      "incomplete_value": false,
      "site": "0070e4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:498:8"
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
        "00c77498",
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
        "00c77898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e4bc ["COPY", "tmp:0:8", ["const:498:8"]]
+ 0070e4fc ["COPY", "tmp:0:8", ["const:898:8"]]
~~~


### [`0070e510`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e510.md) → [`0070e550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e550.md) FUN_0070e550

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e574",
      "incomplete_value": false,
      "site": "0070e574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e534",
      "incomplete_value": false,
      "site": "0070e534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:518:8"
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
        "00c77518",
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
        "00c77918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e524 ["INT_ADD", "register:40f0:8", ["const:70e524:8", "const:4:8"]]
+ 0070e564 ["INT_ADD", "register:40f0:8", ["const:70e564:8", "const:4:8"]]
- 0070e530 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 0070e570 ["COPY", "tmp:0:8", ["const:918:8"]]
~~~


### [`0070e560`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e560.md) → [`0070e5a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e5a0.md) FUN_0070e5a0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "0070e5c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0070e588",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      40,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e588 ["INT_ADD", "register:40f0:8", ["const:70e588:8", "const:4:8"]]
- 0070e588 ["CALL", null, ["ram:47acb4:8"]]
+ 0070e5c8 ["INT_ADD", "register:40f0:8", ["const:70e5c8:8", "const:4:8"]]
+ 0070e5c8 ["CALL", null, ["ram:47acf4:8"]]
- 0070e594 ["INT_ADD", "register:40f0:8", ["const:70e594:8", "const:4:8"]]
+ 0070e5d4 ["INT_ADD", "register:40f0:8", ["const:70e5d4:8", "const:4:8"]]
~~~


### [`0070e5ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e5ec.md) → [`0070e62c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e62c.md) FUN_0070e62c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e64c",
      "incomplete_value": true,
      "site": "0070e650",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e60c",
      "incomplete_value": true,
      "site": "0070e610",
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
            "const:598:8"
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
        "00c77598",
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
        "00c77998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e600 ["INT_ADD", "register:40f0:8", ["const:70e600:8", "const:4:8"]]
+ 0070e640 ["INT_ADD", "register:40f0:8", ["const:70e640:8", "const:4:8"]]
- 0070e60c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 0070e64c ["COPY", "tmp:0:8", ["const:998:8"]]
~~~


### [`0070e624`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e624.md) → [`0070e664`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e664.md) FUN_0070e664

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
      "definition_site": "0070e668",
      "incomplete_value": false,
      "site": "0070e66c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0070e628",
      "incomplete_value": false,
      "site": "0070e62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:598:8"
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
        "00c77598",
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
        "00c77998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e628 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 0070e668 ["COPY", "tmp:0:8", ["const:998:8"]]
~~~


### [`0070e678`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e678.md) → [`0070e6b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e6b8.md) FUN_0070e6b8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0070e6c4",
      "incomplete_value": false,
      "site": "0070e6c8",
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
    "old": {
      "definition_site": "0070e684",
      "incomplete_value": false,
      "site": "0070e688",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0070e684 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0070e6c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0070e688 ["INT_ADD", "register:40f0:8", ["const:70e688:8", "const:4:8"]]
+ 0070e6c8 ["INT_ADD", "register:40f0:8", ["const:70e6c8:8", "const:4:8"]]
~~~


### [`0070e68c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e68c.md) → [`0070e6cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e6cc.md) _INIT_112

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0070e72c",
      "incomplete_value": true,
      "site": "0070e748",
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
    "old": {
      "definition_site": "0070e6ec",
      "incomplete_value": true,
      "site": "0070e708",
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
                "const:ef9:8"
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
      "definition_site": "0070e74c",
      "incomplete_value": true,
      "site": "0070e768",
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
    "old": {
      "definition_site": "0070e70c",
      "incomplete_value": true,
      "site": "0070e728",
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
                "const:d82:8"
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
      "definition_site": "0070e76c",
      "incomplete_value": true,
      "site": "0070e784",
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
    "old": {
      "definition_site": "0070e72c",
      "incomplete_value": true,
      "site": "0070e744",
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
                "const:e95:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0070e6b8 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 0070e6f8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 0070e6c4 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0070e704 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0070e6e0 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0070e720 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00710090`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710090.md) → [`007100d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007100d0.md) FUN_007100d0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 15件 [`00ab9080`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9080.md) [`00af5f88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5f88.md) [`00af5ff8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af5ff8.md) [`00af6068`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af6068.md) [`00af60d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af6/00af60d8.md)
- 新版 呼出元 2件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 15件 [`00ab927c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab9/00ab927c.md) [`00af63b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af63b0.md) [`00af6420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6420.md) [`00af6490`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6490.md) [`00af6500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af6/00af6500.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

~~~diff
- 007100b4 ["INT_ADD", "register:40f0:8", ["const:7100b4:8", "const:4:8"]]
+ 007100f4 ["INT_ADD", "register:40f0:8", ["const:7100f4:8", "const:4:8"]]
- 007100c4 ["INT_ADD", "register:40f0:8", ["const:7100c4:8", "const:4:8"]]
+ 00710104 ["INT_ADD", "register:40f0:8", ["const:710104:8", "const:4:8"]]
- 007100e0 ["INT_ADD", "register:40f0:8", ["const:7100e0:8", "const:4:8"]]
+ 00710120 ["INT_ADD", "register:40f0:8", ["const:710120:8", "const:4:8"]]
~~~


### [`00714ba8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714ba8.md) → [`00714be8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714be8.md) FUN_00714be8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005f7900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) · 呼出先 5件 [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`00af3634`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md) [`00afa6a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa6a0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005f7940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7940.md) · 呼出先 5件 [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`00af3a5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3a5c.md) [`00afaac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaac8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "00714ce8",
      "value": [
        "leaf",
        "ram:70ea5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714ca8",
      "value": [
        "leaf",
        "ram:70ea1c:8"
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
      256,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0070ea1c"
      ]
    ],
    [
      292,
      "READ",
      [
        "storage",
        "002c40a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      256,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0070ea5c"
      ]
    ],
    [
      292,
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00714c00 ["INT_ADD", "register:40f0:8", ["const:714c00:8", "const:4:8"]]
+ 00714c40 ["INT_ADD", "register:40f0:8", ["const:714c40:8", "const:4:8"]]
- 00714c10 ["INT_ADD", "register:40f0:8", ["const:714c10:8", "const:4:8"]]
+ 00714c50 ["INT_ADD", "register:40f0:8", ["const:714c50:8", "const:4:8"]]
- 00714c20 ["INT_ADD", "register:40f0:8", ["const:714c20:8", "const:4:8"]]
+ 00714c60 ["INT_ADD", "register:40f0:8", ["const:714c60:8", "const:4:8"]]
~~~


### [`00714d78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714d78.md) → [`00714db8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714db8.md) FUN_00714db8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005f7900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f7900.md) · 呼出先 5件 [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00af3634`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af3/00af3634.md) [`00afa6a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afa6a0.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`005f7940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7940.md) · 呼出先 5件 [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00af3a5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af3/00af3a5c.md) [`00afaac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afaac8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "00714ebc",
      "value": [
        "leaf",
        "ram:7119f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00714e7c",
      "value": [
        "leaf",
        "ram:7119b0:8"
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
      260,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007119b0"
      ]
    ],
    [
      296,
      "READ",
      [
        "storage",
        "002c40a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      260,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007119f0"
      ]
    ],
    [
      296,
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00714dd0 ["INT_ADD", "register:40f0:8", ["const:714dd0:8", "const:4:8"]]
+ 00714e10 ["INT_ADD", "register:40f0:8", ["const:714e10:8", "const:4:8"]]
- 00714de0 ["INT_ADD", "register:40f0:8", ["const:714de0:8", "const:4:8"]]
+ 00714e20 ["INT_ADD", "register:40f0:8", ["const:714e20:8", "const:4:8"]]
- 00714df0 ["INT_ADD", "register:40f0:8", ["const:714df0:8", "const:4:8"]]
+ 00714e30 ["INT_ADD", "register:40f0:8", ["const:714e30:8", "const:4:8"]]
~~~


### [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) → [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) FUN_00714f8c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005f87e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) · 呼出先 23件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005fe208`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md) [`0070ea1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070ea1c.md) [`007119b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`007196e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196e4.md)
- 新版 呼出元 1件 [`005f8820`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f8/005f8820.md) · 呼出先 23件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`005fe248`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe248.md) [`0070ea5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007119f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00719724`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719724.md)

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
      "site": "00715054",
      "value": [
        "leaf",
        "ram:7119f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00715014",
      "value": [
        "leaf",
        "ram:7119b0:8"
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
      "site": "00715130",
      "value": [
        "leaf",
        "ram:70ea5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007150f0",
      "value": [
        "leaf",
        "ram:70ea1c:8"
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
      44,
      "DATA",
      [
        "storage",
        "003443f8",
        "fde_003443f8",
        "dword"
      ]
    ],
    [
      200,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007119b0"
      ]
    ],
    [
      288,
      "DATA",
      [
        "storage",
        "003443f8",
        "fde_003443f8",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      44,
      "DATA",
      [
        "storage",
        "003443f8",
        null,
        "byte[23]"
      ]
    ],
    [
      200,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007119f0"
      ]
    ],
    [
      288,
      "DATA",
      [
        "storage",
        "003443f8",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00715014 ["INT_ADD", "register:40f0:8", ["const:715014:8", "const:4:8"]]
- 00715014 ["CALL", null, ["ram:7119b0:8"]]
+ 00715054 ["INT_ADD", "register:40f0:8", ["const:715054:8", "const:4:8"]]
+ 00715054 ["CALL", null, ["ram:7119f0:8"]]
- 00715040 ["INT_ADD", "register:40f0:8", ["const:715040:8", "const:4:8"]]
+ 00715080 ["INT_ADD", "register:40f0:8", ["const:715080:8", "const:4:8"]]
- 00715054 ["INT_ADD", "register:40f0:8", ["const:715054:8", "const:4:8"]]
+ 00715094 ["INT_ADD", "register:40f0:8", ["const:715094:8", "const:4:8"]]
~~~


### [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) → [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) FUN_00715500

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 81件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046da08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0046da7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`0046da94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da94.md)
- 新版 呼出元 2件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 81件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046da48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da48.md) [`0046dabc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`0046dad4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dad4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 9件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071569c",
      "incomplete_value": true,
      "site": "007156b0",
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071565c",
      "incomplete_value": true,
      "site": "00715670",
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
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00715c74",
      "incomplete_value": true,
      "site": "00715c84",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00715c34",
      "incomplete_value": true,
      "site": "00715c44",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00715c80",
      "incomplete_value": true,
      "site": "00715c88",
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00715c40",
      "incomplete_value": true,
      "site": "00715c48",
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
                "const:2e0:8"
              ]
            ]
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
      412,
      "READ",
      [
        "storage",
        "002c2750",
        null,
        null
      ]
    ],
    [
      1008,
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      1012,
      "DATA",
      [
        "storage",
        "00ca3bac",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      412,
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ],
    [
      1008,
      "READ",
      [
        "storage",
        "00c9b528",
        null,
        "pointer"
      ]
    ],
    [
      1012,
      "DATA",
      [
        "storage",
        "00ca3fac",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00715530 ["INT_ADD", "register:40f0:8", ["const:715530:8", "const:4:8"]]
- 00715530 ["CALL", null, ["callee:005c3e7c:8"]]
- 00715534 ["INT_LEFT", "tmp:0:8", ["const:84:8", "const:c:4"]]
- 00715534 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00715570 ["INT_ADD", "register:40f0:8", ["const:715570:8", "const:4:8"]]
+ 00715570 ["CALL", null, ["callee:005c3e7c:8"]]
+ 00715574 ["INT_LEFT", "tmp:0:8", ["const:84:8", "const:c:4"]]
+ 00715574 ["COPY", "tmp:1:8", ["tmp:0:8"]]
~~~


### [`00716b40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716b40.md) → [`00716b80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716b80.md) FUN_00716b80

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`007154c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 17件 [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`005e73e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a519e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md)
- 新版 呼出元 2件 [`00715500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00715/00715500.md) [`00716d90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 17件 [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) [`005e7420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a51bd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a51/00a51bd8.md)

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
      "site": "00716cf0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00716cb0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      368,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      368,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00716b6c ["INT_ADD", "register:40f0:8", ["const:716b6c:8", "const:4:8"]]
+ 00716bac ["INT_ADD", "register:40f0:8", ["const:716bac:8", "const:4:8"]]
- 00716b88 ["INT_ADD", "register:40f0:8", ["const:716b88:8", "const:4:8"]]
+ 00716bc8 ["INT_ADD", "register:40f0:8", ["const:716bc8:8", "const:4:8"]]
- 00716b94 ["INT_ADD", "register:40f0:8", ["const:716b94:8", "const:4:8"]]
+ 00716bd4 ["INT_ADD", "register:40f0:8", ["const:716bd4:8", "const:4:8"]]
~~~


### [`00718734`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) → [`00718774`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00718/00718774.md) FUN_00718774

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 24件 [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005e0f50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e15e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 24件 [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005e0f90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`005e1620`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00718a18",
      "value": [
        "leaf",
        "ram:5e7504:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007189d8",
      "value": [
        "leaf",
        "ram:5e74c4:8"
      ]
    },
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00718c38",
      "value": [
        "leaf",
        "ram:5e7504:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00718bf8",
      "value": [
        "leaf",
        "ram:5e74c4:8"
      ]
    },
    "ordinal": 17,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00719074",
      "value": [
        "leaf",
        "ram:5e7504:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00719034",
      "value": [
        "leaf",
        "ram:5e74c4:8"
      ]
    },
    "ordinal": 31,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      676,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e74c4"
      ]
    ],
    [
      1220,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e74c4"
      ]
    ],
    [
      2304,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e74c4"
      ]
    ]
  ],
  "added": [
    [
      676,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e7504"
      ]
    ],
    [
      1220,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e7504"
      ]
    ],
    [
      2304,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e7504"
      ]
    ]
  ]
}
~~~


~~~diff
- 007187a0 ["INT_ADD", "register:40f0:8", ["const:7187a0:8", "const:4:8"]]
+ 007187e0 ["INT_ADD", "register:40f0:8", ["const:7187e0:8", "const:4:8"]]
- 007187e4 ["INT_ADD", "register:40f0:8", ["const:7187e4:8", "const:4:8"]]
+ 00718824 ["INT_ADD", "register:40f0:8", ["const:718824:8", "const:4:8"]]
- 00718808 ["INT_ADD", "register:40f0:8", ["const:718808:8", "const:4:8"]]
+ 00718848 ["INT_ADD", "register:40f0:8", ["const:718848:8", "const:4:8"]]
~~~


### [`0071931c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/0071931c.md) → [`0071935c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/0071935c.md) FUN_0071935c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 19件 [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`005e0898`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0898.md) [`005e08c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08c0.md) [`005e08e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e08e0.md) [`005e0d28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 19件 [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`005e08d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e08d8.md) [`005e0900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0900.md) [`005e0920`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0920.md) [`005e0d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0d68.md)

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
      "site": "0071964c",
      "value": [
        "leaf",
        "ram:a4f3b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0071960c",
      "value": [
        "leaf",
        "ram:a4f1bc:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      752,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a4f1bc"
      ]
    ]
  ],
  "added": [
    [
      752,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a4f3b4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00719348 ["INT_ADD", "register:40f0:8", ["const:719348:8", "const:4:8"]]
+ 00719388 ["INT_ADD", "register:40f0:8", ["const:719388:8", "const:4:8"]]
- 00719358 ["INT_ADD", "register:40f0:8", ["const:719358:8", "const:4:8"]]
+ 00719398 ["INT_ADD", "register:40f0:8", ["const:719398:8", "const:4:8"]]
- 007193f0 ["INT_ADD", "register:40f0:8", ["const:7193f0:8", "const:4:8"]]
+ 00719430 ["INT_ADD", "register:40f0:8", ["const:719430:8", "const:4:8"]]
~~~


### [`007196d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196d0.md) → [`00719710`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719710.md) FUN_00719710

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00713318`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00713358`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00713/00713358.md) [`0071425c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/0071425c.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071971c",
      "incomplete_value": false,
      "site": "00719720",
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
    "old": {
      "definition_site": "007196dc",
      "incomplete_value": false,
      "site": "007196e0",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 007196dc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0071971c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007196e0 ["INT_ADD", "register:40f0:8", ["const:7196e0:8", "const:4:8"]]
+ 00719720 ["INT_ADD", "register:40f0:8", ["const:719720:8", "const:4:8"]]
~~~


### [`007196e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007196e4.md) → [`00719724`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719724.md) FUN_00719724

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00714f4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/00714f4c.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00714f8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00714/00714f8c.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00719730",
      "incomplete_value": false,
      "site": "00719734",
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
    "old": {
      "definition_site": "007196f0",
      "incomplete_value": false,
      "site": "007196f4",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 007196f0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00719730 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 007196f4 ["INT_ADD", "register:40f0:8", ["const:7196f4:8", "const:4:8"]]
+ 00719734 ["INT_ADD", "register:40f0:8", ["const:719734:8", "const:4:8"]]
~~~


### [`007197d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/007197d4.md) → [`00719814`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719814.md) _INIT_113

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00719894",
      "incomplete_value": true,
      "site": "007198b0",
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
    "old": {
      "definition_site": "00719854",
      "incomplete_value": true,
      "site": "00719870",
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
                "const:d82:8"
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
      "definition_site": "007198d0",
      "incomplete_value": true,
      "site": "007198ec",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719890",
      "incomplete_value": true,
      "site": "007198ac",
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
                "const:592:8"
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
      "definition_site": "00719a34",
      "incomplete_value": false,
      "site": "00719a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007199f4",
      "incomplete_value": false,
      "site": "00719a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      60,
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 00719800 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00719840 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 0071980c ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071984c ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00719828 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00719868 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00719c28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719c28.md) → [`00719c68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719c68.md) FUN_00719c68

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d8e7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d8/009d8e7c.md) · 呼出先 18件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`009d9018`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9018.md) · 呼出先 18件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048792c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00719cac",
      "incomplete_value": false,
      "site": "00719cb0",
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
    "old": {
      "definition_site": "00719c6c",
      "incomplete_value": false,
      "site": "00719c70",
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
            "const:938:8"
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
      "definition_site": "00719cdc",
      "incomplete_value": true,
      "site": "00719cec",
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
                "const:cb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00719c9c",
      "incomplete_value": true,
      "site": "00719cac",
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
                "const:c70:8"
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
      "definition_site": "0071a044",
      "incomplete_value": true,
      "site": "0071a048",
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
      "definition_site": "0071a004",
      "incomplete_value": true,
      "site": "0071a008",
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
      72,
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a33a1",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a33b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      72,
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a346e",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a347e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00719c60 ["INT_ADD", "register:40f0:8", ["const:719c60:8", "const:4:8"]]
+ 00719ca0 ["INT_ADD", "register:40f0:8", ["const:719ca0:8", "const:4:8"]]
- 00719c6c ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00719cac ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00719c84 ["INT_ADD", "register:40f0:8", ["const:719c84:8", "const:4:8"]]
+ 00719cc4 ["INT_ADD", "register:40f0:8", ["const:719cc4:8", "const:4:8"]]
~~~


### [`0071a34c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a34c.md) → [`0071a38c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a38c.md) FUN_0071a38c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00719c28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719c28.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00719c68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719c68.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071a398",
      "incomplete_value": false,
      "site": "0071a39c",
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
    "old": {
      "definition_site": "0071a358",
      "incomplete_value": false,
      "site": "0071a35c",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0071a358 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0071a398 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0071a35c ["INT_ADD", "register:40f0:8", ["const:71a35c:8", "const:4:8"]]
+ 0071a39c ["INT_ADD", "register:40f0:8", ["const:71a39c:8", "const:4:8"]]
~~~


### [`0071a360`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a360.md) → [`0071a3a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a3a0.md) FUN_0071a3a0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00719c28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00719/00719c28.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00719c68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719c68.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071a3ac",
      "incomplete_value": false,
      "site": "0071a3b0",
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
    "old": {
      "definition_site": "0071a36c",
      "incomplete_value": false,
      "site": "0071a370",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0071a36c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0071a3ac ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0071a370 ["INT_ADD", "register:40f0:8", ["const:71a370:8", "const:4:8"]]
+ 0071a3b0 ["INT_ADD", "register:40f0:8", ["const:71a3b0:8", "const:4:8"]]
~~~


### [`0071a374`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071a374.md) → [`0071a3b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071a3b4.md) _INIT_114

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071a3f0",
      "incomplete_value": true,
      "site": "0071a40c",
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
    "old": {
      "definition_site": "0071a3b0",
      "incomplete_value": true,
      "site": "0071a3cc",
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
                "const:ee6:8"
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
      "definition_site": "0071a414",
      "incomplete_value": true,
      "site": "0071a430",
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
    "old": {
      "definition_site": "0071a3d4",
      "incomplete_value": true,
      "site": "0071a3f0",
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
                "const:ef9:8"
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
      "definition_site": "0071a434",
      "incomplete_value": true,
      "site": "0071a450",
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
    "old": {
      "definition_site": "0071a3f4",
      "incomplete_value": true,
      "site": "0071a410",
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
                "const:d82:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071a3a0 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 0071a3e0 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0071a3ac ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071a3ec ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071a3c8 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071a408 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0071ad24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) → [`0071ad64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) FUN_0071ad64

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`009d8e7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d8/009d8e7c.md) · 呼出先 23件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`009d9018`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9018.md) · 呼出先 23件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048792c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071adcc",
      "incomplete_value": true,
      "site": "0071addc",
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
                "const:63d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071ad8c",
      "incomplete_value": true,
      "site": "0071ad9c",
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
                "const:570:8"
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
      "definition_site": "0071afbc",
      "incomplete_value": true,
      "site": "0071afd4",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071af7c",
      "incomplete_value": true,
      "site": "0071af94",
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
                "const:2b1000:8"
              ],
              [
                "leaf",
                "const:fdf:8"
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
      "definition_site": "0071b1c8",
      "incomplete_value": true,
      "site": "0071b1dc",
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
                "const:8c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071b188",
      "incomplete_value": true,
      "site": "0071b19c",
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
                "const:880:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 50,
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
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "002a4570",
        null,
        "string"
      ]
    ],
    [
      600,
      "READ",
      [
        "storage",
        "002b1fdf",
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
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "002a463d",
        null,
        "string"
      ]
    ],
    [
      600,
      "READ",
      [
        "storage",
        "002b201f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0071ad64 ["INT_ADD", "register:40f0:8", ["const:71ad64:8", "const:4:8"]]
+ 0071ada4 ["INT_ADD", "register:40f0:8", ["const:71ada4:8", "const:4:8"]]
- 0071ad6c ["COPY", "tmp:0:8", ["const:938:8"]]
+ 0071adac ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0071ad88 ["COPY", "tmp:0:8", ["const:570:8"]]
+ 0071adc8 ["COPY", "tmp:0:8", ["const:63d:8"]]
~~~


### [`0071b4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b4f0.md) → [`0071b530`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071b530.md) FUN_0071b530

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0071ad24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071a/0071ad24.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0071ad64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071a/0071ad64.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0071b53c",
      "incomplete_value": false,
      "site": "0071b540",
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
    "old": {
      "definition_site": "0071b4fc",
      "incomplete_value": false,
      "site": "0071b500",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0071b4fc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0071b53c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0071b500 ["INT_ADD", "register:40f0:8", ["const:71b500:8", "const:4:8"]]
+ 0071b540 ["INT_ADD", "register:40f0:8", ["const:71b540:8", "const:4:8"]]
~~~


### [`0071b504`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071b504.md) → [`0071b544`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071b544.md) _INIT_115

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071b580",
      "incomplete_value": true,
      "site": "0071b59c",
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
    "old": {
      "definition_site": "0071b540",
      "incomplete_value": true,
      "site": "0071b55c",
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
                "const:ee6:8"
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
      "definition_site": "0071b5a4",
      "incomplete_value": true,
      "site": "0071b5c0",
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
    "old": {
      "definition_site": "0071b564",
      "incomplete_value": true,
      "site": "0071b580",
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
                "const:ef9:8"
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
      "definition_site": "0071b5e4",
      "incomplete_value": true,
      "site": "0071b5fc",
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
    "old": {
      "definition_site": "0071b5a4",
      "incomplete_value": true,
      "site": "0071b5bc",
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
                "const:e95:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071b530 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 0071b570 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 0071b53c ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071b57c ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071b558 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071b598 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0071f090`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f090.md) → [`0071f0d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071f0d0.md) _INIT_116

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071f10c",
      "incomplete_value": true,
      "site": "0071f128",
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
    "old": {
      "definition_site": "0071f0cc",
      "incomplete_value": true,
      "site": "0071f0e8",
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
                "const:ee6:8"
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
      "definition_site": "0071f150",
      "incomplete_value": true,
      "site": "0071f16c",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f110",
      "incomplete_value": true,
      "site": "0071f12c",
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
                "const:d82:8"
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
      "definition_site": "0071f170",
      "incomplete_value": true,
      "site": "0071f188",
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
    "old": {
      "definition_site": "0071f130",
      "incomplete_value": true,
      "site": "0071f148",
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
                "const:e95:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071f0bc ["COPY", "tmp:0:8", ["const:850:8"]]
+ 0071f0fc ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0071f0c8 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071f108 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071f0e4 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071f124 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0071f420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f420.md) → [`0071f460`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071f460.md) FUN_0071f460

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009d8e7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d8/009d8e7c.md) · 呼出先 4件 [`004878dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`005e8158`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e8/005e8158.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`009d9018`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d9018.md) · 呼出先 4件 [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`005e8198`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence

~~~diff
- 0071f44c ["INT_ADD", "register:40f0:8", ["const:71f44c:8", "const:4:8"]]
+ 0071f48c ["INT_ADD", "register:40f0:8", ["const:71f48c:8", "const:4:8"]]
- 0071f458 ["INT_ADD", "register:40f0:8", ["const:71f458:8", "const:4:8"]]
+ 0071f498 ["INT_ADD", "register:40f0:8", ["const:71f498:8", "const:4:8"]]
- 0071f464 ["INT_ADD", "register:40f0:8", ["const:71f464:8", "const:4:8"]]
+ 0071f4a4 ["INT_ADD", "register:40f0:8", ["const:71f4a4:8", "const:4:8"]]
~~~


### [`0071f5a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f5a0.md) → [`0071f5e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071f5e0.md) _INIT_117

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071f61c",
      "incomplete_value": true,
      "site": "0071f638",
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
    "old": {
      "definition_site": "0071f5dc",
      "incomplete_value": true,
      "site": "0071f5f8",
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
                "const:ee6:8"
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
      "definition_site": "0071f680",
      "incomplete_value": true,
      "site": "0071f698",
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
    "old": {
      "definition_site": "0071f640",
      "incomplete_value": true,
      "site": "0071f658",
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
                "const:e95:8"
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
      "definition_site": "0071f69c",
      "incomplete_value": true,
      "site": "0071f6b8",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071f65c",
      "incomplete_value": true,
      "site": "0071f678",
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
                "const:592:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071f5cc ["COPY", "tmp:0:8", ["const:868:8"]]
+ 0071f60c ["COPY", "tmp:0:8", ["const:c68:8"]]
- 0071f5d8 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071f618 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071f5f4 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071f634 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0071f930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071f930.md) → [`0071f970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071f970.md) _INIT_118

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071f9ac",
      "incomplete_value": true,
      "site": "0071f9c8",
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
    "old": {
      "definition_site": "0071f96c",
      "incomplete_value": true,
      "site": "0071f988",
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
                "const:ee6:8"
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
      "definition_site": "0071f9f0",
      "incomplete_value": true,
      "site": "0071fa0c",
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
    "old": {
      "definition_site": "0071f9b0",
      "incomplete_value": true,
      "site": "0071f9cc",
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
                "const:d82:8"
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
      "definition_site": "0071fa10",
      "incomplete_value": true,
      "site": "0071fa28",
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
    "old": {
      "definition_site": "0071f9d0",
      "incomplete_value": true,
      "site": "0071f9e8",
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
                "const:e95:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071f95c ["COPY", "tmp:0:8", ["const:880:8"]]
+ 0071f99c ["COPY", "tmp:0:8", ["const:c80:8"]]
- 0071f968 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071f9a8 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071f984 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071f9c4 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0071fcc0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071f/0071fcc0.md) → [`0071fd00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071f/0071fd00.md) _INIT_119

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0071fd3c",
      "incomplete_value": true,
      "site": "0071fd58",
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
    "old": {
      "definition_site": "0071fcfc",
      "incomplete_value": true,
      "site": "0071fd18",
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
                "const:ee6:8"
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
      "definition_site": "0071fdbc",
      "incomplete_value": true,
      "site": "0071fdd8",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0071fd7c",
      "incomplete_value": true,
      "site": "0071fd98",
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
                "const:592:8"
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
      "definition_site": "0071fddc",
      "incomplete_value": true,
      "site": "0071fdf8",
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
    "old": {
      "definition_site": "0071fd9c",
      "incomplete_value": true,
      "site": "0071fdb8",
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0071fcec ["COPY", "tmp:0:8", ["const:898:8"]]
+ 0071fd2c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0071fcf8 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0071fd38 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0071fd14 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0071fd54 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00720050`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) → [`00720090`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) FUN_00720090

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00700ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 49件 [`0046c984`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046d934`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046e4f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md)
- 新版 呼出元 1件 [`00700af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 49件 [`0046c9c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046d974`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046e538`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 40件, `call_target` 33件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00722968",
      "incomplete_value": false,
      "site": "00722968",
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
    "old": {
      "definition_site": "00722928",
      "incomplete_value": false,
      "site": "00722928",
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
                "const:b00:8"
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
    "ordinal": 285,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0072296c",
      "incomplete_value": false,
      "site": "0072296c",
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
    "old": {
      "definition_site": "0072292c",
      "incomplete_value": false,
      "site": "0072292c",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 286,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00722968",
      "incomplete_value": false,
      "site": "0072296c",
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
    "old": {
      "definition_site": "00722928",
      "incomplete_value": false,
      "site": "0072292c",
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
                "const:b00:8"
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
    "ordinal": 286,
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
        "002c4320",
        null,
        "undefined8"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ],
    [
      536,
      "PARAM",
      [
        "storage",
        "00ca4bd8",
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
        "002c4360",
        null,
        "undefined8"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      536,
      "PARAM",
      [
        "storage",
        "00ca4fd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00720158 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
- 00720158 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00720158 ["COPY", "register:5008:8", ["const:0:8"]]
- 00720158 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00720198 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:360:8"]]
+ 00720198 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00720198 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00720198 ["COPY", "register:5010:8", ["const:0:8"]]
~~~


### [`00722bc0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00722/00722bc0.md) → [`00722c00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00722/00722c00.md) FUN_00722c00

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00707ea0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 24件 [`00467aec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468b9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md)
- 新版 呼出元 1件 [`00707ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 24件 [`00467b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468bdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 44件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00722c84",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00722c44",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00722cc0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00722c80",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00722d08",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00722cc8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      192,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      264,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      192,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      264,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


~~~diff
- 00722c2c ["INT_ADD", "register:40f0:8", ["const:722c2c:8", "const:4:8"]]
- 00722c2c ["CALL", null, ["callee:00467b2c:8"]]
- 00722c30 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:1c8:8"]]
- 00722c30 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00722c6c ["INT_ADD", "register:40f0:8", ["const:722c6c:8", "const:4:8"]]
+ 00722c6c ["CALL", null, ["callee:00467b2c:8"]]
+ 00722c70 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:1c8:8"]]
+ 00722c70 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
~~~


### [`00724420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00724/00724420.md) → [`00724460`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00724/00724460.md) _INIT_120

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007244e0",
      "incomplete_value": true,
      "site": "007244fc",
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
    "old": {
      "definition_site": "007244a0",
      "incomplete_value": true,
      "site": "007244bc",
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
                "const:d82:8"
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
      "definition_site": "00724500",
      "incomplete_value": true,
      "site": "00724518",
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
    "old": {
      "definition_site": "007244c0",
      "incomplete_value": true,
      "site": "007244d8",
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
                "const:e95:8"
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
      "definition_site": "0072453c",
      "incomplete_value": true,
      "site": "00724558",
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
    "old": {
      "definition_site": "007244fc",
      "incomplete_value": true,
      "site": "00724518",
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0072444c ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 0072448c ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00724458 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 00724498 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00724474 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 007244b4 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`007247b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00724/007247b0.md) → [`007247f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00724/007247f0.md) FUN_007247f0

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b28b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 21件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00487de0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 21件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00487e20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00724834",
      "incomplete_value": false,
      "site": "00724840",
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
    "old": {
      "definition_site": "007247f4",
      "incomplete_value": false,
      "site": "00724800",
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
            "const:938:8"
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
      "definition_site": "0072486c",
      "incomplete_value": true,
      "site": "0072487c",
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
                "const:29f000:8"
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
      "definition_site": "0072482c",
      "incomplete_value": true,
      "site": "0072483c",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:2ca:8"
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
      "definition_site": "00724870",
      "incomplete_value": true,
      "site": "00724880",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00724830",
      "incomplete_value": true,
      "site": "00724840",
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
                "const:9:8"
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
      80,
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "0029f2ca",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "0029f2d3",
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
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      124,
      "READ",
      [
        "storage",
        "0029f397",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "0029f3a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 007247e8 ["INT_ADD", "register:40f0:8", ["const:7247e8:8", "const:4:8"]]
+ 00724828 ["INT_ADD", "register:40f0:8", ["const:724828:8", "const:4:8"]]
- 007247f4 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00724834 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00724804 ["INT_ADD", "register:40f0:8", ["const:724804:8", "const:4:8"]]
+ 00724844 ["INT_ADD", "register:40f0:8", ["const:724844:8", "const:4:8"]]
~~~


### [`00725424`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725424.md) → [`00725464`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725464.md) FUN_00725464

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075d71c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 19件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`005c175c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00676a20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`0071be98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md)
- 新版 呼出元 1件 [`0075d75c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 19件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`005c179c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00676a60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md) [`0071bed8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)

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
      "site": "00725808",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007257c8",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 19,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      932,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072547c ["INT_ADD", "register:40f0:8", ["const:72547c:8", "const:4:8"]]
+ 007254bc ["INT_ADD", "register:40f0:8", ["const:7254bc:8", "const:4:8"]]
- 0072549c ["INT_ADD", "register:40f0:8", ["const:72549c:8", "const:4:8"]]
+ 007254dc ["INT_ADD", "register:40f0:8", ["const:7254dc:8", "const:4:8"]]
- 00725538 ["INT_ADD", "register:40f0:8", ["const:725538:8", "const:4:8"]]
+ 00725578 ["INT_ADD", "register:40f0:8", ["const:725578:8", "const:4:8"]]
~~~


### [`0072604c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/0072604c.md) → [`0072608c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/0072608c.md) FUN_0072608c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00725e74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00725/00725e74.md) [`0077c150`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c150.md) [`00a38c60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38c60.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`00725eb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00725/00725eb4.md) [`0077c190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c190.md) [`00a38e58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38e58.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00726098",
      "incomplete_value": true,
      "site": "0072609c",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00726058",
      "incomplete_value": true,
      "site": "0072605c",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00726058 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00726098 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0072605c ["INT_ADD", "register:40f0:8", ["const:72605c:8", "const:4:8"]]
+ 0072609c ["INT_ADD", "register:40f0:8", ["const:72609c:8", "const:4:8"]]
~~~


### [`00726220`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726220.md) → [`00726260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726260.md) FUN_00726260

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007260c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007260c4.md) [`0077c51c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c51c.md) [`00a38acc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a38/00a38acc.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`00726104`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726104.md) [`0077c55c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c55c.md) [`00a38cc4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a38/00a38cc4.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0072626c",
      "incomplete_value": true,
      "site": "00726270",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072622c",
      "incomplete_value": true,
      "site": "00726230",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072622c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0072626c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00726230 ["INT_ADD", "register:40f0:8", ["const:726230:8", "const:4:8"]]
+ 00726270 ["INT_ADD", "register:40f0:8", ["const:726270:8", "const:4:8"]]
~~~


### [`007263f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/007263f0.md) → [`00726430`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/00726430.md) _INIT_121

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072646c",
      "incomplete_value": true,
      "site": "00726488",
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
    "old": {
      "definition_site": "0072642c",
      "incomplete_value": true,
      "site": "00726448",
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
                "const:ee6:8"
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
      "definition_site": "00726490",
      "incomplete_value": true,
      "site": "007264ac",
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
    "old": {
      "definition_site": "00726450",
      "incomplete_value": true,
      "site": "0072646c",
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
                "const:ef9:8"
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
      "definition_site": "007264d0",
      "incomplete_value": true,
      "site": "007264e8",
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
    "old": {
      "definition_site": "00726490",
      "incomplete_value": true,
      "site": "007264a8",
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
                "const:e95:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0072641c ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 0072645c ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00726428 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 00726468 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00726444 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00726484 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00726780`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00726/00726780.md) → [`007267c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00726/007267c0.md) FUN_007267c0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 18件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`004879c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004879c0.md)
- 新版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 18件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a00.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00726808",
      "incomplete_value": false,
      "site": "00726818",
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
    "old": {
      "definition_site": "007267c8",
      "incomplete_value": false,
      "site": "007267d8",
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
            "const:938:8"
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
      "definition_site": "00726840",
      "incomplete_value": true,
      "site": "00726840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00726800",
      "incomplete_value": true,
      "site": "00726800",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f19:8"
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
      "definition_site": "00726844",
      "incomplete_value": true,
      "site": "00726844",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00726804",
      "incomplete_value": true,
      "site": "00726804",
      "value": [
        "LOAD",
        "8",
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
      88,
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a8f19",
        null,
        "string"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002a8f1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      88,
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002a8fe6",
        null,
        "string"
      ]
    ],
    [
      116,
      "READ",
      [
        "storage",
        "002a8feb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 007267bc ["INT_ADD", "register:40f0:8", ["const:7267bc:8", "const:4:8"]]
+ 007267fc ["INT_ADD", "register:40f0:8", ["const:7267fc:8", "const:4:8"]]
- 007267c8 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00726808 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 007267dc ["INT_ADD", "register:40f0:8", ["const:7267dc:8", "const:4:8"]]
+ 0072681c ["INT_ADD", "register:40f0:8", ["const:72681c:8", "const:4:8"]]
~~~


### [`00727600`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727600.md) → [`00727640`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/00727640.md) _INIT_122

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072767c",
      "incomplete_value": true,
      "site": "00727698",
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
    "old": {
      "definition_site": "0072763c",
      "incomplete_value": true,
      "site": "00727658",
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
                "const:ee6:8"
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
      "definition_site": "007276e0",
      "incomplete_value": true,
      "site": "007276f8",
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
    "old": {
      "definition_site": "007276a0",
      "incomplete_value": true,
      "site": "007276b8",
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
                "const:e95:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00727860",
      "incomplete_value": false,
      "site": "00727874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00727820",
      "incomplete_value": false,
      "site": "00727834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      60,
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0072762c ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 0072766c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 00727638 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 00727678 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00727654 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00727694 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`007280c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007280c0.md) → [`00728100`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728100.md) FUN_00728100

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 17件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)
- 新版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 17件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 2件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00728144",
      "incomplete_value": false,
      "site": "00728148",
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
    "old": {
      "definition_site": "00728104",
      "incomplete_value": false,
      "site": "00728108",
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
            "const:938:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00728188",
      "incomplete_value": false,
      "site": "00728188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728148",
      "incomplete_value": false,
      "site": "00728148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00728190",
      "incomplete_value": false,
      "site": "00728190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:d14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00728150",
      "incomplete_value": false,
      "site": "00728150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:914:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
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
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "00ca7910",
        null,
        "undefined4"
      ]
    ],
    [
      144,
      "WRITE",
      [
        "storage",
        "00ca7914",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      72,
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "WRITE",
      [
        "storage",
        "00ca7d10",
        null,
        "undefined4"
      ]
    ],
    [
      144,
      "WRITE",
      [
        "storage",
        "00ca7d14",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


~~~diff
- 007280f8 ["INT_ADD", "register:40f0:8", ["const:7280f8:8", "const:4:8"]]
+ 00728138 ["INT_ADD", "register:40f0:8", ["const:728138:8", "const:4:8"]]
- 00728104 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00728144 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00728134 ["INT_ADD", "register:40f0:8", ["const:728134:8", "const:4:8"]]
+ 00728174 ["INT_ADD", "register:40f0:8", ["const:728174:8", "const:4:8"]]
~~~


### [`00728fac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728fac.md) → [`00728fec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728fec.md) FUN_00728fec

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0075ea04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) [`0075eb40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00769d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00773854`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 0件 
- 新版 呼出元 4件 [`0075ea44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075ea44.md) [`0075eb80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00773894`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00729000",
      "incomplete_value": true,
      "site": "00729004",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00728fc0",
      "incomplete_value": true,
      "site": "00728fc4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "DATA",
      [
        "storage",
        "002e1e90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      20,
      "DATA",
      [
        "storage",
        "002e1ed0",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00728fbc ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00728ffc ["COPY", "tmp:0:8", ["const:ed0:8"]]
~~~


### [`007290c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) → [`00729108`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729108.md) FUN_00729108

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0075ea04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) [`00769d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`009cc9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc9e0.md) · 呼出先 23件 [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046da7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`00470800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047e5cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md)
- 新版 呼出元 3件 [`0075ea44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075ea44.md) [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`009ccb7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb7c.md) · 呼出先 23件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046dabc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047e60c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00729444",
      "incomplete_value": true,
      "site": "00729444",
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
      "definition_site": "00729404",
      "incomplete_value": true,
      "site": "00729404",
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
    "ordinal": 28,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007291b4",
      "value": [
        "leaf",
        "ram:728e48:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00729174",
      "value": [
        "leaf",
        "ram:728e08:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007291c0",
      "value": [
        "leaf",
        "ram:729010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00729180",
      "value": [
        "leaf",
        "ram:728fd0:8"
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
      156,
      "DATA",
      [
        "storage",
        "0034444c",
        null,
        "dword"
      ]
    ],
    [
      172,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728e08"
      ]
    ],
    [
      184,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728fd0"
      ]
    ]
  ],
  "added": [
    [
      156,
      "DATA",
      [
        "storage",
        "0034444c",
        null,
        "byte[43]"
      ]
    ],
    [
      172,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728e48"
      ]
    ],
    [
      184,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00729010"
      ]
    ]
  ]
}
~~~


~~~diff
- 00729130 ["INT_ADD", "register:40f0:8", ["const:729130:8", "const:4:8"]]
+ 00729170 ["INT_ADD", "register:40f0:8", ["const:729170:8", "const:4:8"]]
- 0072913c ["INT_ADD", "register:40f0:8", ["const:72913c:8", "const:4:8"]]
+ 0072917c ["INT_ADD", "register:40f0:8", ["const:72917c:8", "const:4:8"]]
- 0072914c ["INT_ADD", "register:40f0:8", ["const:72914c:8", "const:4:8"]]
+ 0072918c ["INT_ADD", "register:40f0:8", ["const:72918c:8", "const:4:8"]]
~~~


### [`0072a2dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072a2dc.md) → [`0072a31c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072a31c.md) FUN_0072a31c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00729e38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) [`0072aaac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aaac.md) · 呼出先 10件 [`00470954`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0063dc88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dc88.md) [`00727990`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`0072ada0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ada0.md) [`00794134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794134.md)
- 新版 呼出元 2件 [`00729e78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729e78.md) [`0072aaec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072aaec.md) · 呼出先 10件 [`00470994`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0063dcc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063dcc8.md) [`007279d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`0072ade0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ade0.md) [`00794174`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794174.md)

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
      "site": "0072a944",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072a904",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 34,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072a9a8",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072a968",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 35,
    "slot": 0
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      1452,
      "DATA",
      [
        "storage",
        "0039ab08",
        null,
        "byte[39]"
      ]
    ],
    [
      1576,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      1676,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      1452,
      "DATA",
      [
        "storage",
        "0039ab08",
        null,
        "dword"
      ]
    ],
    [
      1576,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      1676,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072a334 ["INT_ADD", "register:40f0:8", ["const:72a334:8", "const:4:8"]]
+ 0072a374 ["INT_ADD", "register:40f0:8", ["const:72a374:8", "const:4:8"]]
- 0072a35c ["INT_ADD", "register:40f0:8", ["const:72a35c:8", "const:4:8"]]
+ 0072a39c ["INT_ADD", "register:40f0:8", ["const:72a39c:8", "const:4:8"]]
- 0072a37c ["INT_ADD", "register:40f0:8", ["const:72a37c:8", "const:4:8"]]
+ 0072a3bc ["INT_ADD", "register:40f0:8", ["const:72a3bc:8", "const:4:8"]]
~~~


### [`0072ace0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ace0.md) → [`0072ad20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md) FUN_0072ad20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007640b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md) · 呼出先 4件 [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`00729e38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729e38.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`007640f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/007640f0.md) · 呼出先 4件 [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00729e78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729e78.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "site": "0072ad40",
      "value": [
        "leaf",
        "ram:729e78:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072ad00",
      "value": [
        "leaf",
        "ram:729e38:8"
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
        "00729e38"
      ]
    ]
  ],
  "added": [
    [
      32,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00729e78"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072ad00 ["INT_ADD", "register:40f0:8", ["const:72ad00:8", "const:4:8"]]
- 0072ad00 ["CALL", null, ["ram:729e38:8"]]
+ 0072ad40 ["INT_ADD", "register:40f0:8", ["const:72ad40:8", "const:4:8"]]
+ 0072ad40 ["CALL", null, ["ram:729e78:8"]]
- 0072ad1c ["INT_ADD", "register:40f0:8", ["const:72ad1c:8", "const:4:8"]]
+ 0072ad5c ["INT_ADD", "register:40f0:8", ["const:72ad5c:8", "const:4:8"]]
- 0072ad40 ["INT_ADD", "register:40f0:8", ["const:72ad40:8", "const:4:8"]]
+ 0072ad80 ["INT_ADD", "register:40f0:8", ["const:72ad80:8", "const:4:8"]]
~~~


### [`0072ada0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ada0.md) → [`0072ade0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ade0.md) FUN_0072ade0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0072a2dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072a2dc.md) [`00792444`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792444.md) · 呼出先 4件 [`0072b01c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b01c.md) [`00800338`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`00a65bf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)
- 新版 呼出元 2件 [`0072a31c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072a31c.md) [`00792484`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md) · 呼出先 4件 [`0072b05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b05c.md) [`00800378`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00a65dec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a65/00a65dec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072adf4",
      "value": [
        "leaf",
        "ram:72b05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072adb4",
      "value": [
        "leaf",
        "ram:72b01c:8"
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
      "site": "0072ae54",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072ae14",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072aeac",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072ae6c",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 6,
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
        "0072b01c"
      ]
    ],
    [
      116,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      204,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      20,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b05c"
      ]
    ],
    [
      116,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      204,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072adb4 ["INT_ADD", "register:40f0:8", ["const:72adb4:8", "const:4:8"]]
- 0072adb4 ["CALL", null, ["ram:72b01c:8"]]
+ 0072adf4 ["INT_ADD", "register:40f0:8", ["const:72adf4:8", "const:4:8"]]
+ 0072adf4 ["CALL", null, ["ram:72b05c:8"]]
- 0072adec ["INT_ADD", "register:40f0:8", ["const:72adec:8", "const:4:8"]]
+ 0072ae2c ["INT_ADD", "register:40f0:8", ["const:72ae2c:8", "const:4:8"]]
- 0072adf8 ["INT_ADD", "register:40f0:8", ["const:72adf8:8", "const:4:8"]]
+ 0072ae38 ["INT_ADD", "register:40f0:8", ["const:72ae38:8", "const:4:8"]]
~~~


### [`0072aef0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072aef0.md) → [`0072af30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072af30.md) FUN_0072af30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007911e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/007911e4.md) · 呼出先 7件 [`0072b01c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b01c.md) [`007317c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007317c0.md) [`00731930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731930.md) [`00731938`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731938.md) [`00800338`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)
- 新版 呼出元 1件 [`00791224`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md) · 呼出先 7件 [`0072b05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b05c.md) [`00731800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731800.md) [`00731970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731970.md) [`00731978`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731978.md) [`00800378`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)

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
      "site": "0072af54",
      "value": [
        "leaf",
        "ram:72b05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072af14",
      "value": [
        "leaf",
        "ram:72b01c:8"
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
      "site": "0072afac",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072af6c",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072b004",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072afc4",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 6,
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
        "0072b01c"
      ]
    ],
    [
      124,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      212,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      36,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b05c"
      ]
    ],
    [
      124,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      212,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072af14 ["INT_ADD", "register:40f0:8", ["const:72af14:8", "const:4:8"]]
- 0072af14 ["CALL", null, ["ram:72b01c:8"]]
+ 0072af54 ["INT_ADD", "register:40f0:8", ["const:72af54:8", "const:4:8"]]
+ 0072af54 ["CALL", null, ["ram:72b05c:8"]]
- 0072af44 ["INT_ADD", "register:40f0:8", ["const:72af44:8", "const:4:8"]]
+ 0072af84 ["INT_ADD", "register:40f0:8", ["const:72af84:8", "const:4:8"]]
- 0072af50 ["INT_ADD", "register:40f0:8", ["const:72af50:8", "const:4:8"]]
+ 0072af90 ["INT_ADD", "register:40f0:8", ["const:72af90:8", "const:4:8"]]
~~~


### [`0072b104`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b104.md) → [`0072b144`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b144.md) FUN_0072b144

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007918d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/007918d0.md) · 呼出先 3件 [`0072b01c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b01c.md) [`0081ce00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081c/0081ce00.md) [`0081d18c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0081d/0081d18c.md)
- 新版 呼出元 1件 [`00791910`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md) · 呼出先 3件 [`0072b05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b05c.md) [`0081ce40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081c/0081ce40.md) [`0081d1cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0081d/0081d1cc.md)

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
      "site": "0072b160",
      "value": [
        "leaf",
        "ram:72b05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072b120",
      "value": [
        "leaf",
        "ram:72b01c:8"
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
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b01c"
      ]
    ]
  ],
  "added": [
    [
      28,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b05c"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072b120 ["INT_ADD", "register:40f0:8", ["const:72b120:8", "const:4:8"]]
- 0072b120 ["CALL", null, ["ram:72b01c:8"]]
+ 0072b160 ["INT_ADD", "register:40f0:8", ["const:72b160:8", "const:4:8"]]
+ 0072b160 ["CALL", null, ["ram:72b05c:8"]]
- 0072b138 ["INT_ADD", "register:40f0:8", ["const:72b138:8", "const:4:8"]]
+ 0072b178 ["INT_ADD", "register:40f0:8", ["const:72b178:8", "const:4:8"]]
~~~


### [`0072b160`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b160.md) → [`0072b1a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b1a0.md) FUN_0072b1a0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00791e20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/00791e20.md) · 呼出先 7件 [`0072b01c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b01c.md) [`00800338`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`009a95cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009ad9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad9dc.md)
- 新版 呼出元 1件 [`00791e60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md) · 呼出先 7件 [`0072b05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b05c.md) [`00800378`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`009a9768`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009adb78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb78.md)

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
      "site": "0072b1d0",
      "value": [
        "leaf",
        "ram:72b05c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072b190",
      "value": [
        "leaf",
        "ram:72b01c:8"
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
      "site": "0072b224",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072b1e4",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b01c"
      ]
    ],
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      48,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0072b05c"
      ]
    ],
    [
      132,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072b190 ["INT_ADD", "register:40f0:8", ["const:72b190:8", "const:4:8"]]
- 0072b190 ["CALL", null, ["ram:72b01c:8"]]
+ 0072b1d0 ["INT_ADD", "register:40f0:8", ["const:72b1d0:8", "const:4:8"]]
+ 0072b1d0 ["CALL", null, ["ram:72b05c:8"]]
- 0072b1a4 ["INT_ADD", "register:40f0:8", ["const:72b1a4:8", "const:4:8"]]
+ 0072b1e4 ["INT_ADD", "register:40f0:8", ["const:72b1e4:8", "const:4:8"]]
- 0072b1b0 ["INT_ADD", "register:40f0:8", ["const:72b1b0:8", "const:4:8"]]
+ 0072b1f0 ["INT_ADD", "register:40f0:8", ["const:72b1f0:8", "const:4:8"]]
~~~


### [`0072b4b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b4b8.md) → [`0072b4f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b4f8.md) FUN_0072b4f8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `changed`

- 旧版 呼出元 1件 [`0072b264`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072b264.md) · 呼出先 5件 [`00470954`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0067682c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0072b2a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072b2a4.md) · 呼出先 5件 [`00470994`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0067686c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067686c.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      288,
      "READ",
      [
        "storage",
        "002e1e60",
        "switchD_0072b5e0::switchdataD_002e1e60",
        "byte"
      ]
    ],
    [
      288,
      "READ",
      [
        "storage",
        "002e1e61",
        null,
        "byte"
      ]
    ],
    [
      288,
      "READ",
      [
        "storage",
        "002e1e62",
        null,
        "byte"
      ]
    ]
  ],
  "added": [
    [
      288,
      "READ",
      [
        "storage",
        "002e1ea0",
        "switchD_0072b620::switchdataD_002e1ea0",
        "byte"
      ]
    ],
    [
      288,
      "READ",
      [
        "storage",
        "002e1ea1",
        null,
        "byte"
      ]
    ],
    [
      288,
      "READ",
      [
        "storage",
        "002e1ea2",
        null,
        "byte"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072b504 ["INT_ADD", "register:40f0:8", ["const:72b504:8", "const:4:8"]]
+ 0072b544 ["INT_ADD", "register:40f0:8", ["const:72b544:8", "const:4:8"]]
- 0072b52c ["INT_ADD", "register:40f0:8", ["const:72b52c:8", "const:4:8"]]
+ 0072b56c ["INT_ADD", "register:40f0:8", ["const:72b56c:8", "const:4:8"]]
- 0072b54c ["INT_ADD", "register:40f0:8", ["const:72b54c:8", "const:4:8"]]
+ 0072b58c ["INT_ADD", "register:40f0:8", ["const:72b58c:8", "const:4:8"]]
~~~


### [`0072bf0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072b/0072bf0c.md) → [`0072bf4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072b/0072bf4c.md) FUN_0072bf4c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`006b3b64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006bbc58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`00741590`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741590.md) [`009222f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/009222f8.md) [`0092472c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00924/0092472c.md) · 呼出先 7件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d05c.md) [`0067682c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067682c.md)
- 新版 呼出元 6件 [`006b3ba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3ba4.md) [`006bbc98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`007415d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00741/007415d0.md) [`00922494`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922494.md) [`009248c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00924/009248c8.md) · 呼出先 7件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0047acf4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047d09c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d09c.md) [`0067686c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067686c.md)

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
      "site": "0072bf94",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072bf54",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "0072c118",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072c0d8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      72,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      460,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      72,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      460,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072bf24 ["INT_ADD", "register:40f0:8", ["const:72bf24:8", "const:4:8"]]
+ 0072bf64 ["INT_ADD", "register:40f0:8", ["const:72bf64:8", "const:4:8"]]
- 0072bf3c ["INT_ADD", "register:40f0:8", ["const:72bf3c:8", "const:4:8"]]
+ 0072bf7c ["INT_ADD", "register:40f0:8", ["const:72bf7c:8", "const:4:8"]]
- 0072bf54 ["INT_ADD", "register:40f0:8", ["const:72bf54:8", "const:4:8"]]
- 0072bf54 ["CALL", null, ["ram:47acb4:8"]]
+ 0072bf94 ["INT_ADD", "register:40f0:8", ["const:72bf94:8", "const:4:8"]]
+ 0072bf94 ["CALL", null, ["ram:47acf4:8"]]
~~~


### [`0072c474`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c474.md) → [`0072c4b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c4b4.md) _INIT_123

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0072c4f0",
      "incomplete_value": true,
      "site": "0072c50c",
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
    "old": {
      "definition_site": "0072c4b0",
      "incomplete_value": true,
      "site": "0072c4cc",
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
                "const:ee6:8"
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
      "definition_site": "0072c514",
      "incomplete_value": true,
      "site": "0072c530",
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
    "old": {
      "definition_site": "0072c4d4",
      "incomplete_value": true,
      "site": "0072c4f0",
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
                "const:ef9:8"
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
      "definition_site": "0072c534",
      "incomplete_value": true,
      "site": "0072c550",
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
    "old": {
      "definition_site": "0072c4f4",
      "incomplete_value": true,
      "site": "0072c510",
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
                "const:d82:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 0072c4a0 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0072c4e0 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 0072c4ac ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 0072c4ec ["COPY", "tmp:0:8", ["const:f26:8"]]
- 0072c4c8 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 0072c508 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0072c9d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) → [`0072ca10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) FUN_0072ca10

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 25件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)
- 新版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 25件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `store_destination` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0072ca64",
      "incomplete_value": false,
      "site": "0072ca6c",
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
    "old": {
      "definition_site": "0072ca24",
      "incomplete_value": false,
      "site": "0072ca2c",
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
            "const:938:8"
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
      "definition_site": "0072ca98",
      "incomplete_value": true,
      "site": "0072ca98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:f3e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0072ca58",
      "incomplete_value": true,
      "site": "0072ca58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:efe:8"
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
      "definition_site": "0072ca94",
      "incomplete_value": true,
      "site": "0072ca9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0072ca54",
      "incomplete_value": true,
      "site": "0072ca5c",
      "value": [
        "LOAD",
        "8",
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
      92,
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002b3efe",
        null,
        "string"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "002b3f05",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      92,
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002b3f3e",
        null,
        "string"
      ]
    ],
    [
      132,
      "READ",
      [
        "storage",
        "002b3f45",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072ca08 ["INT_ADD", "register:40f0:8", ["const:72ca08:8", "const:4:8"]]
- 0072ca08 ["CALL", null, ["callee:00487e20:8"]]
- 0072ca0c ["COPY", "register:4040:8", ["register:4098:8"]]
- 0072ca10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
+ 0072ca48 ["INT_ADD", "register:40f0:8", ["const:72ca48:8", "const:4:8"]]
+ 0072ca48 ["CALL", null, ["callee:00487e20:8"]]
+ 0072ca4c ["COPY", "register:4040:8", ["register:4098:8"]]
+ 0072ca50 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
~~~


### [`0072f198`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) → [`0072f1d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) FUN_0072f1d8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005fe62c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) · 呼出先 27件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0049f3b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md)
- 新版 呼出元 1件 [`005fe66c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) · 呼出先 27件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0048ce84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0049f3f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md)

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
      "site": "0072f354",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072f314",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072f944",
      "value": [
        "leaf",
        "ram:730bbc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0072f904",
      "value": [
        "leaf",
        "ram:730b7c:8"
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
      380,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      1900,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00730b7c"
      ]
    ]
  ],
  "added": [
    [
      380,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      1900,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00730bbc"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072f1ec ["INT_ADD", "register:40f0:8", ["const:72f1ec:8", "const:4:8"]]
+ 0072f22c ["INT_ADD", "register:40f0:8", ["const:72f22c:8", "const:4:8"]]
- 0072f218 ["INT_ADD", "register:40f0:8", ["const:72f218:8", "const:4:8"]]
+ 0072f258 ["INT_ADD", "register:40f0:8", ["const:72f258:8", "const:4:8"]]
- 0072f21c ["INT_ADD", "register:40f0:8", ["const:72f21c:8", "const:4:8"]]
+ 0072f25c ["INT_ADD", "register:40f0:8", ["const:72f25c:8", "const:4:8"]]
~~~


### [`0072fac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072fac8.md) → [`0072fb08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072fb08.md) FUN_0072fb08

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0072f198`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) · 呼出先 10件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d770`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0049f3b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00676a20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 1件 [`0072f1d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) · 呼出先 10件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d7b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0049f3f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00676a60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0072fbd4",
      "incomplete_value": false,
      "site": "0072fbd8",
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
    "old": {
      "definition_site": "0072fb94",
      "incomplete_value": false,
      "site": "0072fb98",
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
            "const:f0:8"
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
      "definition_site": "00730248",
      "incomplete_value": false,
      "site": "0073024c",
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
    "old": {
      "definition_site": "00730208",
      "incomplete_value": false,
      "site": "0073020c",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00730268",
      "incomplete_value": false,
      "site": "0073026c",
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
    "old": {
      "definition_site": "00730228",
      "incomplete_value": false,
      "site": "0073022c",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      204,
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      1824,
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      1856,
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      204,
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      1824,
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      1856,
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0072fb08 ["INT_ADD", "register:40f0:8", ["const:72fb08:8", "const:4:8"]]
+ 0072fb48 ["INT_ADD", "register:40f0:8", ["const:72fb48:8", "const:4:8"]]
- 0072fb10 ["INT_ADD", "register:40f0:8", ["const:72fb10:8", "const:4:8"]]
+ 0072fb50 ["INT_ADD", "register:40f0:8", ["const:72fb50:8", "const:4:8"]]
- 0072fb94 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 0072fbd4 ["COPY", "tmp:0:8", ["const:1bd:8"]]
~~~


### [`00731940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731940.md) → [`00731980`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731980.md) FUN_00731980

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0072c9d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0072ca10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0073198c",
      "incomplete_value": false,
      "site": "00731990",
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
    "old": {
      "definition_site": "0073194c",
      "incomplete_value": false,
      "site": "00731950",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 0073194c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0073198c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731950 ["INT_ADD", "register:40f0:8", ["const:731950:8", "const:4:8"]]
+ 00731990 ["INT_ADD", "register:40f0:8", ["const:731990:8", "const:4:8"]]
~~~


### [`00731954`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731954.md) → [`00731994`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731994.md) FUN_00731994

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0072c9d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0072ca10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007319a0",
      "incomplete_value": false,
      "site": "007319a4",
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
    "old": {
      "definition_site": "00731960",
      "incomplete_value": false,
      "site": "00731964",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731960 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 007319a0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731964 ["INT_ADD", "register:40f0:8", ["const:731964:8", "const:4:8"]]
+ 007319a4 ["INT_ADD", "register:40f0:8", ["const:7319a4:8", "const:4:8"]]
~~~


### [`00731a2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a2c.md) → [`00731a6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731a6c.md) FUN_00731a6c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0072c9d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c9d0.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0072ca10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072ca10.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731a78",
      "incomplete_value": false,
      "site": "00731a7c",
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
    "old": {
      "definition_site": "00731a38",
      "incomplete_value": false,
      "site": "00731a3c",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731a38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731a78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731a3c ["INT_ADD", "register:40f0:8", ["const:731a3c:8", "const:4:8"]]
+ 00731a7c ["INT_ADD", "register:40f0:8", ["const:731a7c:8", "const:4:8"]]
~~~


### [`00731a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731a90.md) → [`00731ad0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ad0.md) FUN_00731ad0

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0072ece8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072e/0072ece8.md) [`0072f198`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) · 呼出先 1件 [`0043b738`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`0072ed28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072e/0072ed28.md) [`0072f1d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731adc",
      "incomplete_value": false,
      "site": "00731ae0",
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
    "old": {
      "definition_site": "00731a9c",
      "incomplete_value": false,
      "site": "00731aa0",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731a9c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731adc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731aa0 ["INT_ADD", "register:40f0:8", ["const:731aa0:8", "const:4:8"]]
+ 00731ae0 ["INT_ADD", "register:40f0:8", ["const:731ae0:8", "const:4:8"]]
~~~


### [`00731aa4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731aa4.md) → [`00731ae4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ae4.md) FUN_00731ae4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00730cbc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730cbc.md) [`00730d3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730d3c.md) [`007312e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007312e8.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 3件 [`00730cfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730cfc.md) [`00730d7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730d7c.md) [`00731328`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731328.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731af0",
      "incomplete_value": false,
      "site": "00731af4",
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
    "old": {
      "definition_site": "00731ab0",
      "incomplete_value": false,
      "site": "00731ab4",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731ab0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731af0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731ab4 ["INT_ADD", "register:40f0:8", ["const:731ab4:8", "const:4:8"]]
+ 00731af4 ["INT_ADD", "register:40f0:8", ["const:731af4:8", "const:4:8"]]
~~~


### [`00731ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ab8.md) → [`00731af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731af8.md) FUN_00731af8

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0072c86c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c86c.md) [`0072c8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c8d4.md) [`0072f198`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) [`0072fac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072fac8.md) [`00730334`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 7件 [`0072c8ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c8ac.md) [`0072c914`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c914.md) [`0072f1d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) [`0072fb08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072fb08.md) [`00730374`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730374.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731b04",
      "incomplete_value": false,
      "site": "00731b08",
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
    "old": {
      "definition_site": "00731ac4",
      "incomplete_value": false,
      "site": "00731ac8",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731ac4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731b04 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731ac8 ["INT_ADD", "register:40f0:8", ["const:731ac8:8", "const:4:8"]]
+ 00731b08 ["INT_ADD", "register:40f0:8", ["const:731b08:8", "const:4:8"]]
~~~


### [`00731acc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731acc.md) → [`00731b0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731b0c.md) FUN_00731b0c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00730334`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00730374`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730374.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731b18",
      "incomplete_value": false,
      "site": "00731b1c",
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
    "old": {
      "definition_site": "00731ad8",
      "incomplete_value": false,
      "site": "00731adc",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731ad8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731b18 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731adc ["INT_ADD", "register:40f0:8", ["const:731adc:8", "const:4:8"]]
+ 00731b1c ["INT_ADD", "register:40f0:8", ["const:731b1c:8", "const:4:8"]]
~~~


### [`00731ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731ae0.md) → [`00731b20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731b20.md) FUN_00731b20

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00730334`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00730/00730334.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00730374`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00730/00730374.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00731b2c",
      "incomplete_value": false,
      "site": "00731b30",
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
    "old": {
      "definition_site": "00731aec",
      "incomplete_value": false,
      "site": "00731af0",
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
            "const:f0c:8"
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
        "002b7f0c",
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
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731aec ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00731b2c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00731af0 ["INT_ADD", "register:40f0:8", ["const:731af0:8", "const:4:8"]]
+ 00731b30 ["INT_ADD", "register:40f0:8", ["const:731b30:8", "const:4:8"]]
~~~


### [`00731af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731af4.md) → [`00731b34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731b34.md) _INIT_124

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00731b70",
      "incomplete_value": true,
      "site": "00731b8c",
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
    "old": {
      "definition_site": "00731b30",
      "incomplete_value": true,
      "site": "00731b4c",
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
                "const:ee6:8"
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
      "definition_site": "00731b94",
      "incomplete_value": true,
      "site": "00731bb0",
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
    "old": {
      "definition_site": "00731b54",
      "incomplete_value": true,
      "site": "00731b70",
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
                "const:ef9:8"
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
      "definition_site": "00731bb4",
      "incomplete_value": true,
      "site": "00731bd0",
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
    "old": {
      "definition_site": "00731b74",
      "incomplete_value": true,
      "site": "00731b90",
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
                "const:d82:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 00731b20 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00731b60 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00731b2c ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 00731b6c ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00731b48 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00731b88 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00731e84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731e84.md) → [`00731ec4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ec4.md) FUN_00731ec4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00935514`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md) · 呼出先 4件 [`00489f0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00acb85c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb85c.md) [`00acbd1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbd1c.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`009356b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009356b0.md) · 呼出先 4件 [`00489f4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`00acba58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba58.md) [`00acbf18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbf18.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00731ef0",
      "incomplete_value": false,
      "site": "00731ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00731eb0",
      "incomplete_value": false,
      "site": "00731eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
        "00c77630",
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
        "00c77a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731ea8 ["INT_ADD", "register:40f0:8", ["const:731ea8:8", "const:4:8"]]
+ 00731ee8 ["INT_ADD", "register:40f0:8", ["const:731ee8:8", "const:4:8"]]
- 00731eb0 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00731ef0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00731edc ["INT_ADD", "register:40f0:8", ["const:731edc:8", "const:4:8"]]
+ 00731f1c ["INT_ADD", "register:40f0:8", ["const:731f1c:8", "const:4:8"]]
~~~


### [`00731f2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731f2c.md) → [`00731f6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731f6c.md) FUN_00731f6c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acb88c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00acba88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00731f84",
      "incomplete_value": true,
      "site": "00731f88",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00731f44",
      "incomplete_value": true,
      "site": "00731f48",
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
        "00c77630",
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
        "00c77a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731f44 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00731f84 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00731f58 ["INT_ADD", "register:40f0:8", ["const:731f58:8", "const:4:8"]]
+ 00731f98 ["INT_ADD", "register:40f0:8", ["const:731f98:8", "const:4:8"]]
- 00731f6c ["INT_ADD", "register:40f0:8", ["const:731f6c:8", "const:4:8"]]
+ 00731fac ["INT_ADD", "register:40f0:8", ["const:731fac:8", "const:4:8"]]
~~~


### [`00731f88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731f88.md) → [`00731fc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731fc8.md) FUN_00731fc8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acb88c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00acba88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00731fe0",
      "incomplete_value": false,
      "site": "00731fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00731fa0",
      "incomplete_value": false,
      "site": "00731fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:630:8"
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
        "00c77630",
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
        "00c77a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00731fa0 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00731fe0 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00731fb4 ["INT_ADD", "register:40f0:8", ["const:731fb4:8", "const:4:8"]]
+ 00731ff4 ["INT_ADD", "register:40f0:8", ["const:731ff4:8", "const:4:8"]]
- 00731fc8 ["INT_ADD", "register:40f0:8", ["const:731fc8:8", "const:4:8"]]
+ 00732008 ["INT_ADD", "register:40f0:8", ["const:732008:8", "const:4:8"]]
~~~


### [`0073209c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/0073209c.md) → [`007320dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/007320dc.md) _INIT_125

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00732118",
      "incomplete_value": true,
      "site": "00732134",
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
    "old": {
      "definition_site": "007320d8",
      "incomplete_value": true,
      "site": "007320f4",
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
                "const:ee6:8"
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
      "definition_site": "0073213c",
      "incomplete_value": true,
      "site": "00732158",
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
    "old": {
      "definition_site": "007320fc",
      "incomplete_value": true,
      "site": "00732118",
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
                "const:ef9:8"
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
      "definition_site": "0073215c",
      "incomplete_value": true,
      "site": "00732178",
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
    "old": {
      "definition_site": "0073211c",
      "incomplete_value": true,
      "site": "00732138",
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
                "const:d82:8"
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
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 007320c8 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00732108 ["COPY", "tmp:0:8", ["const:d30:8"]]
- 007320d4 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 00732114 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 007320f0 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 00732130 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`0073242c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/0073242c.md) → [`0073246c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/0073246c.md) _INIT_126

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00732528",
      "incomplete_value": true,
      "site": "00732544",
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
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007324e8",
      "incomplete_value": true,
      "site": "00732504",
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
                "const:592:8"
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
      "definition_site": "00732548",
      "incomplete_value": true,
      "site": "00732564",
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
    "old": {
      "definition_site": "00732508",
      "incomplete_value": true,
      "site": "00732524",
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
                "const:e90:8"
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
      "definition_site": "0073268c",
      "incomplete_value": false,
      "site": "007326a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073264c",
      "incomplete_value": false,
      "site": "00732660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:43a000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      60,
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      128,
      "READ",
      [
        "storage",
        "002b8d82",
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
  ]
}
~~~


~~~diff
- 00732458 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00732498 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00732464 ["COPY", "tmp:0:8", ["const:ee6:8"]]
+ 007324a4 ["COPY", "tmp:0:8", ["const:f26:8"]]
- 00732480 ["COPY", "tmp:0:8", ["const:ef9:8"]]
+ 007324c0 ["COPY", "tmp:0:8", ["const:f39:8"]]
~~~


### [`00732c44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732c44.md) → [`00732c84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732c84.md) FUN_00732c84

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`007bda04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007c7eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c7/007c7eb0.md) [`007cceac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) [`007efc68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 7件 [`007bda44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) [`007c7ef0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007c7/007c7ef0.md) [`007cceec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`007efca8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00732ca8",
      "incomplete_value": true,
      "site": "00732cac",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00732c68",
      "incomplete_value": true,
      "site": "00732c6c",
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
            "const:d34:8"
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
      36,
      "PARAM",
      [
        "storage",
        "002b3d34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      36,
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00732c68 ["COPY", "tmp:0:8", ["const:d34:8"]]
+ 00732ca8 ["COPY", "tmp:0:8", ["const:d74:8"]]
- 00732c6c ["INT_ADD", "register:40f0:8", ["const:732c6c:8", "const:4:8"]]
+ 00732cac ["INT_ADD", "register:40f0:8", ["const:732cac:8", "const:4:8"]]
~~~


### [`00732c70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732c70.md) → [`00732cb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cb0.md) FUN_00732cb0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007df0a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`007df0e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00732cf0",
      "incomplete_value": false,
      "site": "00732cf4",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00732cb0",
      "incomplete_value": false,
      "site": "00732cb4",
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
            "const:d34:8"
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
      64,
      "PARAM",
      [
        "storage",
        "002b3d34",
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
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00732cb0 ["COPY", "tmp:0:8", ["const:d34:8"]]
+ 00732cf0 ["COPY", "tmp:0:8", ["const:d74:8"]]
- 00732cb4 ["INT_ADD", "register:40f0:8", ["const:732cb4:8", "const:4:8"]]
+ 00732cf4 ["INT_ADD", "register:40f0:8", ["const:732cf4:8", "const:4:8"]]
~~~


### [`00732cb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732cb8.md) → [`00732cf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732cf8.md) FUN_00732cf8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00735c9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735c9c.md) · 呼出先 11件 [`0048ccb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`007336c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a33a24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a33/00a33a24.md)
- 新版 呼出元 1件 [`00735cdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735cdc.md) · 呼出先 11件 [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00733708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a33c1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a33/00a33c1c.md)

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
      "site": "00732e78",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00732e38",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "ordinal": 13,
    "slot": 0
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
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      384,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      72,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      184,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      384,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00732cdc ["INT_ADD", "register:40f0:8", ["const:732cdc:8", "const:4:8"]]
+ 00732d1c ["INT_ADD", "register:40f0:8", ["const:732d1c:8", "const:4:8"]]
- 00732ce8 ["INT_ADD", "register:40f0:8", ["const:732ce8:8", "const:4:8"]]
+ 00732d28 ["INT_ADD", "register:40f0:8", ["const:732d28:8", "const:4:8"]]
- 00732cf0 ["INT_ADD", "register:40f0:8", ["const:732cf0:8", "const:4:8"]]
+ 00732d30 ["INT_ADD", "register:40f0:8", ["const:732d30:8", "const:4:8"]]
~~~


### [`00733380`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733380.md) → [`007333c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/007333c0.md) FUN_007333c0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00732e8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00732/00732e8c.md) [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089e838`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 9件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048e078`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`00733804`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733804.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 3件 [`00732ecc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732ecc.md) [`0088c870`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089e87c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 9件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048e0b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`00733844`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733844.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007333f4",
      "incomplete_value": true,
      "site": "00733408",
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
      "definition_site": "007333b4",
      "incomplete_value": true,
      "site": "007333c8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00733404",
      "incomplete_value": true,
      "site": "00733408",
      "value": [
        "INT_SRIGHT",
        "8",
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
            "const:2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007333c4",
      "incomplete_value": true,
      "site": "007333c8",
      "value": [
        "INT_SRIGHT",
        "8",
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
            "const:2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00733430",
      "incomplete_value": true,
      "site": "0073343c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007333f0",
      "incomplete_value": true,
      "site": "007333fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:f:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
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
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00ca7d10",
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
        "00c9b588",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00ca8110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 007333a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:188:8"]]
+ 007333e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 007333c8 ["INT_ADD", "register:40f0:8", ["const:7333c8:8", "const:4:8"]]
+ 00733408 ["INT_ADD", "register:40f0:8", ["const:733408:8", "const:4:8"]]
- 007333e8 ["INT_ADD", "register:40f0:8", ["const:7333e8:8", "const:4:8"]]
+ 00733428 ["INT_ADD", "register:40f0:8", ["const:733428:8", "const:4:8"]]
~~~


### [`00733ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733ab8.md) → [`00733af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733af8.md) FUN_00733af8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0088c830`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 10件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048e078`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e078.md) [`00733e24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733e24.md) [`00733f04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733f04.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`0088c870`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) · 呼出先 10件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048e0b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e0b8.md) [`00733e64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733e64.md) [`00733f44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733f44.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00733c78",
      "incomplete_value": false,
      "site": "00733c84",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00733c38",
      "incomplete_value": false,
      "site": "00733c44",
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
            "const:f:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00733d04",
      "incomplete_value": false,
      "site": "00733d10",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00733cc4",
      "incomplete_value": false,
      "site": "00733cd0",
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
            "const:f:8"
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
      140,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00ca7d10",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "00ca7d10",
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
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      140,
      "READ",
      [
        "storage",
        "00ca8110",
        null,
        "undefined8"
      ]
    ],
    [
      156,
      "READ",
      [
        "storage",
        "00ca8110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00733b10 ["INT_ADD", "register:40f0:8", ["const:733b10:8", "const:4:8"]]
+ 00733b50 ["INT_ADD", "register:40f0:8", ["const:733b50:8", "const:4:8"]]
- 00733b18 ["INT_ADD", "register:40f0:8", ["const:733b18:8", "const:4:8"]]
+ 00733b58 ["INT_ADD", "register:40f0:8", ["const:733b58:8", "const:4:8"]]
- 00733b2c ["INT_ADD", "register:40f0:8", ["const:733b2c:8", "const:4:8"]]
+ 00733b6c ["INT_ADD", "register:40f0:8", ["const:733b6c:8", "const:4:8"]]
~~~


### [`00733f04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733f04.md) → [`00733f44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733f44.md) FUN_00733f44

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00733ab8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/00733ab8.md) · 呼出先 4件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00639350`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639350.md) [`00c57a90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00733af8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733af8.md) · 呼出先 4件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00639390`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00639/00639390.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0073401c",
      "incomplete_value": false,
      "site": "00734038",
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
    "old": {
      "definition_site": "00733fdc",
      "incomplete_value": false,
      "site": "00733ff8",
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
            "const:6b5:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      216,
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      216,
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00733f84 ["INT_ADD", "register:40f0:8", ["const:733f84:8", "const:4:8"]]
+ 00733fc4 ["INT_ADD", "register:40f0:8", ["const:733fc4:8", "const:4:8"]]
- 00733fc8 ["INT_ADD", "register:40f0:8", ["const:733fc8:8", "const:4:8"]]
+ 00734008 ["INT_ADD", "register:40f0:8", ["const:734008:8", "const:4:8"]]
- 00733fdc ["COPY", "tmp:0:8", ["const:6b5:8"]]
+ 0073401c ["COPY", "tmp:0:8", ["const:6f5:8"]]
~~~


### [`00734030`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734030.md) → [`00734070`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/00734070.md) FUN_00734070

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`007330f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007330f4.md) [`00737898`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737898.md) [`00737b24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00737/00737b24.md) [`00739464`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00739/00739464.md) · 呼出先 4件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0073413c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/0073413c.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`00733134`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733134.md) [`007378d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/007378d8.md) [`00737b64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00737/00737b64.md) [`007394a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00739/007394a4.md) · 呼出先 4件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0073417c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/0073417c.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00734094",
      "incomplete_value": true,
      "site": "007340ac",
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
                "const:49e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00734054",
      "incomplete_value": true,
      "site": "0073406c",
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
                "const:3d1:8"
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
      "definition_site": "007340e4",
      "incomplete_value": false,
      "site": "007340f0",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007340a4",
      "incomplete_value": false,
      "site": "007340b0",
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
            "const:500:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
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
        "002a33d1",
        null,
        "string"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "002a7500",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      36,
      "READ",
      [
        "storage",
        "002a349e",
        null,
        "string"
      ]
    ],
    [
      116,
      "PARAM",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00734048 ["COPY", "tmp:0:8", ["const:3d1:8"]]
+ 00734088 ["COPY", "tmp:0:8", ["const:49e:8"]]
- 00734098 ["INT_ADD", "register:40f0:8", ["const:734098:8", "const:4:8"]]
+ 007340d8 ["INT_ADD", "register:40f0:8", ["const:7340d8:8", "const:4:8"]]
- 007340a4 ["COPY", "tmp:0:8", ["const:500:8"]]
+ 007340e4 ["COPY", "tmp:0:8", ["const:5dc:8"]]
~~~


### [`00734388`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734388.md) → [`007343c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007343c8.md) FUN_007343c8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00734260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) [`00735fdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md) [`0075eb40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00922c2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) [`00a8a220`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 17件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00597df8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597df8.md) [`00676a20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md)
- 新版 呼出元 6件 [`007342a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00734/007342a0.md) [`0073601c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/0073601c.md) [`0075eb80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00922dc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) [`00a8a418`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 17件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048ce84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00597e38`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597e38.md) [`00676a60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676a60.md)

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
      "site": "0073465c",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0073461c",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
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
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      420,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      208,
      "READ",
      [
        "storage",
        "00c9b588",
        null,
        "pointer"
      ]
    ],
    [
      420,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 007343e0 ["INT_ADD", "register:40f0:8", ["const:7343e0:8", "const:4:8"]]
+ 00734420 ["INT_ADD", "register:40f0:8", ["const:734420:8", "const:4:8"]]
- 007343e8 ["INT_ADD", "register:40f0:8", ["const:7343e8:8", "const:4:8"]]
+ 00734428 ["INT_ADD", "register:40f0:8", ["const:734428:8", "const:4:8"]]
- 00734410 ["INT_ADD", "register:40f0:8", ["const:734410:8", "const:4:8"]]
+ 00734450 ["INT_ADD", "register:40f0:8", ["const:734450:8", "const:4:8"]]
~~~


### [`0073503c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/0073503c.md) → [`0073507c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/0073507c.md) FUN_0073507c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`004428f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`005c175c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)
- 新版 呼出元 1件 [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`005c179c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007350ec",
      "incomplete_value": false,
      "site": "007350f0",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007350ac",
      "incomplete_value": false,
      "site": "007350b0",
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
            "const:d34:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "PARAM",
      [
        "storage",
        "002b3d34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      112,
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00735074 ["INT_ADD", "register:40f0:8", ["const:735074:8", "const:4:8"]]
+ 007350b4 ["INT_ADD", "register:40f0:8", ["const:7350b4:8", "const:4:8"]]
- 00735080 ["INT_ADD", "register:40f0:8", ["const:735080:8", "const:4:8"]]
+ 007350c0 ["INT_ADD", "register:40f0:8", ["const:7350c0:8", "const:4:8"]]
- 007350ac ["COPY", "tmp:0:8", ["const:d34:8"]]
+ 007350ec ["COPY", "tmp:0:8", ["const:d74:8"]]
~~~


### [`007350b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/007350b4.md) → [`007350f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007350f4.md) FUN_007350f4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b28b2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 19件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)
- 新版 呼出元 1件 [`00b28f54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 19件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0048792c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487a64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00735140",
      "incomplete_value": false,
      "site": "00735148",
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
    "old": {
      "definition_site": "00735100",
      "incomplete_value": false,
      "site": "00735108",
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
            "const:938:8"
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
      "definition_site": "0073517c",
      "incomplete_value": true,
      "site": "0073517c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d85:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073513c",
      "incomplete_value": true,
      "site": "0073513c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d45:8"
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
      "definition_site": "0073558c",
      "incomplete_value": true,
      "site": "00735590",
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
      "definition_site": "0073554c",
      "incomplete_value": true,
      "site": "00735550",
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
    "ordinal": 70,
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
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002bdd45",
        null,
        "string"
      ]
    ],
    [
      1124,
      "READ",
      [
        "storage",
        "00c9a7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      84,
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "002bdd85",
        null,
        "string"
      ]
    ],
    [
      1124,
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 007350ec ["INT_ADD", "register:40f0:8", ["const:7350ec:8", "const:4:8"]]
+ 0073512c ["INT_ADD", "register:40f0:8", ["const:73512c:8", "const:4:8"]]
- 00735100 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00735140 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0073510c ["INT_ADD", "register:40f0:8", ["const:73510c:8", "const:4:8"]]
+ 0073514c ["INT_ADD", "register:40f0:8", ["const:73514c:8", "const:4:8"]]
~~~


### [`00735f0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735f0c.md) → [`00735f4c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/00735f4c.md) FUN_00735f4c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769d44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 4件 [`0048ccb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`007336c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`008514b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00769d84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 4件 [`0048ccf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00733708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`008514f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
      "site": "00735fe8",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00735fa8",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      156,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      156,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00735f5c ["INT_ADD", "register:40f0:8", ["const:735f5c:8", "const:4:8"]]
+ 00735f9c ["INT_ADD", "register:40f0:8", ["const:735f9c:8", "const:4:8"]]
- 00735f68 ["INT_ADD", "register:40f0:8", ["const:735f68:8", "const:4:8"]]
+ 00735fa8 ["INT_ADD", "register:40f0:8", ["const:735fa8:8", "const:4:8"]]
- 00735f78 ["INT_ADD", "register:40f0:8", ["const:735f78:8", "const:4:8"]]
+ 00735fb8 ["INT_ADD", "register:40f0:8", ["const:735fb8:8", "const:4:8"]]
~~~


### [`00736bdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00736/00736bdc.md) → [`00736c1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/00736c1c.md) FUN_00736c1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00738b48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00738/00738b48.md) · 呼出先 10件 [`0043bb64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004945d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`007336c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/007336c8.md) [`00735670`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735670.md) [`0073af1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073af1c.md)
- 新版 呼出元 1件 [`00738b88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00738/00738b88.md) · 呼出先 10件 [`0043bba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00494610`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`00733708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/00733708.md) [`007356b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00735/007356b0.md) [`0073af5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073af5c.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00736e7c",
      "incomplete_value": true,
      "site": "00736e90",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00736e3c",
      "incomplete_value": true,
      "site": "00736e50",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:9f9:8"
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
      "definition_site": "00736e94",
      "incomplete_value": true,
      "site": "00736e94",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00736e54",
      "incomplete_value": true,
      "site": "00736e54",
      "value": [
        "LOAD",
        "8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
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
      "READ",
      [
        "storage",
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00ca7d08",
        null,
        "undefined8"
      ]
    ],
    [
      608,
      "READ",
      [
        "storage",
        "002ad9f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      168,
      "READ",
      [
        "storage",
        "00c9b588",
        null,
        "pointer"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00ca8108",
        null,
        "undefined8"
      ]
    ],
    [
      608,
      "READ",
      [
        "storage",
        "002ada39",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00736c84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:188:8"]]
+ 00736cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:588:8"]]
- 00736ccc ["INT_ADD", "register:40f0:8", ["const:736ccc:8", "const:4:8"]]
+ 00736d0c ["INT_ADD", "register:40f0:8", ["const:736d0c:8", "const:4:8"]]
- 00736ce4 ["INT_ADD", "register:40f0:8", ["const:736ce4:8", "const:4:8"]]
+ 00736d24 ["INT_ADD", "register:40f0:8", ["const:736d24:8", "const:4:8"]]
~~~


