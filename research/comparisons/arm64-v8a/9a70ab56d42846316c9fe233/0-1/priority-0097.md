# v16.0.0 → v16.0.1 · 最優先の変更候補 (97)

[一覧の目次](README.md)

### [`00c05264`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05264.md) → [`00c0568c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c0568c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58b00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) · 呼出先 6件 [`00bb5598`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md) [`00c5a3d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`00c58f00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f00.md) · 呼出先 6件 [`00bb59c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md) [`00c5a7d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c056b0",
      "incomplete_value": true,
      "site": "00c056b0",
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
      "definition_site": "00c05288",
      "incomplete_value": true,
      "site": "00c05288",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c056d4",
      "incomplete_value": true,
      "site": "00c056d8",
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
      "definition_site": "00c052ac",
      "incomplete_value": true,
      "site": "00c052b0",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c056fc",
      "incomplete_value": true,
      "site": "00c05700",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c052d4",
      "incomplete_value": true,
      "site": "00c052d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      28,
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05280 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
+ 00c056a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:848:8"]]
- 00c0528c ["INT_ADD", "register:40f0:8", ["const:c0528c:8", "const:4:8"]]
+ 00c056b4 ["INT_ADD", "register:40f0:8", ["const:c056b4:8", "const:4:8"]]
- 00c0529c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
+ 00c056c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
~~~


### [`00c05388`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05388.md) → [`00c057b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c057b0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC1EOS3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c057d8",
      "incomplete_value": true,
      "site": "00c057d8",
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
      "definition_site": "00c053b0",
      "incomplete_value": true,
      "site": "00c053b0",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00c0580c",
      "incomplete_value": true,
      "site": "00c05814",
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
      "definition_site": "00c053e4",
      "incomplete_value": true,
      "site": "00c053ec",
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
      28,
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c053a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 00c057cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
- 00c053b4 ["INT_ADD", "register:40f0:8", ["const:c053b4:8", "const:4:8"]]
+ 00c057dc ["INT_ADD", "register:40f0:8", ["const:c057dc:8", "const:4:8"]]
- 00c053dc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:4f0:8"]]
+ 00c05804 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8f0:8"]]
~~~


### [`00c0551c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0551c.md) → [`00c05944`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05944.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED1Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b20.md) · 呼出先 5件 [`00bb5598`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb5/00bb5598.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c59c00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c00.md) [`00c5ba40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5cd90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd90.md)
- 新版 呼出元 1件 [`00c58f20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f20.md) · 呼出先 5件 [`00bb59c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb5/00bb59c0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a000.md) [`00c5be40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5d190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d190.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c05968",
      "incomplete_value": true,
      "site": "00c0596c",
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
      "definition_site": "00c05540",
      "incomplete_value": true,
      "site": "00c05544",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c059d4",
      "incomplete_value": true,
      "site": "00c059d4",
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
      "definition_site": "00c055ac",
      "incomplete_value": true,
      "site": "00c055ac",
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
      28,
      "READ",
      [
        "storage",
        "00c9b4f0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c90b70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c90b88",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c90f70",
        null,
        "undefined1[128]"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c90f88",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05538 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4f0:8"]]
+ 00c05960 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
- 00c05550 ["INT_ADD", "register:40f0:8", ["const:c05550:8", "const:4:8"]]
+ 00c05978 ["INT_ADD", "register:40f0:8", ["const:c05978:8", "const:4:8"]]
- 00c05558 ["INT_ADD", "register:40f0:8", ["const:c05558:8", "const:4:8"]]
+ 00c05980 ["INT_ADD", "register:40f0:8", ["const:c05980:8", "const:4:8"]]
~~~


### [`00c059a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c059a4.md) → [`00c05dcc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05dcc.md) FUN_00c05dcc

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00c04f8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04f8c.md) [`00c0503c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c0503c.md) [`00c050f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c050f8.md) [`00c051a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c051a8.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c053b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c053b4.md) [`00c05464`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05464.md) [`00c05520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05520.md) [`00c055d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c055d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e08",
      "incomplete_value": false,
      "site": "00c05e0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:e8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c059e0",
      "incomplete_value": false,
      "site": "00c059e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:dbd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e18",
      "incomplete_value": false,
      "site": "00c05e1c",
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
            "const:93b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c059f0",
      "incomplete_value": false,
      "site": "00c059f4",
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
            "const:86e:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c05e28",
      "incomplete_value": false,
      "site": "00c05e2c",
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
            "const:561:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05a00",
      "incomplete_value": false,
      "site": "00c05a04",
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
            "const:521:8"
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
      32,
      "DATA",
      [
        "storage",
        "002a746a",
        null,
        null
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00310b10",
        "switchD_00c059d4::switchdataD_00310b10",
        "byte"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "002a2dbd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      32,
      "DATA",
      [
        "storage",
        "002a7546",
        null,
        null
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00310b50",
        "switchD_00c05dfc::switchdataD_00310b50",
        "byte"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "002a2e8a",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c059bc ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 00c05de4 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00c059c4 ["COPY", "tmp:0:8", ["const:46a:8"]]
+ 00c05dec ["COPY", "tmp:0:8", ["const:546:8"]]
- 00c059c8 ["COPY", "register:4050:8", ["const:c059d8:8"]]
+ 00c05df0 ["COPY", "register:4050:8", ["const:c05e00:8"]]
~~~


### [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) → [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) FUN_00c05f58

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 71件 [`00c07464`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) [`00c0a10c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) [`00c0a93c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) [`00c0d580`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) [`00c0dc64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) · 呼出先 4件 [`00c37b44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) [`00c57af0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e080`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e080.md)
- 新版 呼出元 71件 [`00c0788c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) [`00c0a534`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) [`00c0ad64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) [`00c0d9a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) [`00c0e08c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) · 呼出先 4件 [`00c37f6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37f6c.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e480`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e480.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c05f84",
      "incomplete_value": true,
      "site": "00c05f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05b5c",
      "incomplete_value": true,
      "site": "00c05b64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
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
      "definition_site": "00c05f88",
      "incomplete_value": true,
      "site": "00c05f8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05b60",
      "incomplete_value": true,
      "site": "00c05b64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:768:8"
              ]
            ]
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
      44,
      "READ",
      [
        "storage",
        "00c9b760",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "00c96588",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9b768",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "00c9bb60",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "00c96988",
        "_ZTISt8bad_cast",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9bb68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05b44 ["INT_ADD", "register:40f0:8", ["const:c05b44:8", "const:4:8"]]
+ 00c05f6c ["INT_ADD", "register:40f0:8", ["const:c05f6c:8", "const:4:8"]]
- 00c05b4c ["INT_ADD", "register:40f0:8", ["const:c05b4c:8", "const:4:8"]]
+ 00c05f74 ["INT_ADD", "register:40f0:8", ["const:c05f74:8", "const:4:8"]]
- 00c05b5c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:760:8"]]
+ 00c05f84 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b60:8"]]
~~~


### [`00c05bd4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05bd4.md) → [`00c05ffc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05ffc.md) FUN_00c05ffc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06030",
      "incomplete_value": true,
      "site": "00c06030",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c08",
      "incomplete_value": true,
      "site": "00c05c08",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06028",
      "incomplete_value": true,
      "site": "00c06038",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c00",
      "incomplete_value": true,
      "site": "00c05c10",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06034",
      "incomplete_value": true,
      "site": "00c0603c",
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
      "definition_site": "00c05c0c",
      "incomplete_value": true,
      "site": "00c05c14",
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
      28,
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c92e60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      32,
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c93260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05be4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00c0600c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00c05bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 00c06018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 00c05bf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
+ 00c0601c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
~~~


### [`00c05c58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05c58.md) → [`00c06080`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06080.md) FUN_00c06080

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c060a0",
      "incomplete_value": true,
      "site": "00c060b4",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c78",
      "incomplete_value": true,
      "site": "00c05c8c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c060c0",
      "incomplete_value": true,
      "site": "00c060c0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05c98",
      "incomplete_value": true,
      "site": "00c05c98",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c060c4",
      "incomplete_value": true,
      "site": "00c060c8",
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
      "definition_site": "00c05c9c",
      "incomplete_value": true,
      "site": "00c05ca0",
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
      20,
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c92e38",
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
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c93238",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05c68 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c05c6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 00c06090 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c06094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 00c05c88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
+ 00c060b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
- 00c05cac ["INT_ADD", "register:40f0:8", ["const:c05cac:8", "const:4:8"]]
+ 00c060d4 ["INT_ADD", "register:40f0:8", ["const:c060d4:8", "const:4:8"]]
~~~


### [`00c05cdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05cdc.md) → [`00c06104`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06104.md) FUN_00c06104

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5cce0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5d0e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06124",
      "incomplete_value": true,
      "site": "00c06138",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05cfc",
      "incomplete_value": true,
      "site": "00c05d10",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06144",
      "incomplete_value": true,
      "site": "00c06144",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c05d1c",
      "incomplete_value": true,
      "site": "00c05d1c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06148",
      "incomplete_value": true,
      "site": "00c0614c",
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
      "definition_site": "00c05d20",
      "incomplete_value": true,
      "site": "00c05d24",
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
      20,
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9a7c0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c92e38",
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
        "00c9b290",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "READ",
      [
        "storage",
        "00c9abc0",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c93238",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c05cec ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c05cf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 00c06114 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00c06118 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:290:8"]]
- 00c05d0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c0:8"]]
+ 00c06134 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
- 00c05d30 ["INT_ADD", "register:40f0:8", ["const:c05d30:8", "const:4:8"]]
+ 00c06158 ["INT_ADD", "register:40f0:8", ["const:c06158:8", "const:4:8"]]
~~~


### [`00c061b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c061b4.md) → [`00c065dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c065dc.md) FUN_00c065dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c05d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 4件 [`00c57df0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 1件 [`00c06190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 4件 [`00c581f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c06604",
      "incomplete_value": false,
      "site": "00c06610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c061dc",
      "incomplete_value": false,
      "site": "00c061e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:f8:8"
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
      "definition_site": "00c06624",
      "incomplete_value": true,
      "site": "00c06628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c061fc",
      "incomplete_value": true,
      "site": "00c06200",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      52,
      "DATA",
      [
        "storage",
        "00c930f8",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c934f8",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c061d4 ["INT_ADD", "register:40f0:8", ["const:c061d4:8", "const:4:8"]]
+ 00c065fc ["INT_ADD", "register:40f0:8", ["const:c065fc:8", "const:4:8"]]
- 00c061dc ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 00c06604 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 00c061f0 ["INT_ADD", "register:40f0:8", ["const:c061f0:8", "const:4:8"]]
+ 00c06618 ["INT_ADD", "register:40f0:8", ["const:c06618:8", "const:4:8"]]
~~~


### [`00c0625c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c0625c.md) → [`00c06684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06684.md) FUN_00c06684

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c05d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06004`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06004.md) · 呼出先 4件 [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dfe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfe0.md)
- 新版 呼出元 1件 [`00c06190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 4件 [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5a7d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e3e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e3e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c066ac",
      "incomplete_value": false,
      "site": "00c066b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06284",
      "incomplete_value": false,
      "site": "00c06290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "definition_site": "00c066cc",
      "incomplete_value": true,
      "site": "00c066d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c062a4",
      "incomplete_value": true,
      "site": "00c062a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
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
      52,
      "DATA",
      [
        "storage",
        "00c93228",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c93628",
        null,
        "undefined *"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0627c ["INT_ADD", "register:40f0:8", ["const:c0627c:8", "const:4:8"]]
+ 00c066a4 ["INT_ADD", "register:40f0:8", ["const:c066a4:8", "const:4:8"]]
- 00c06284 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00c066ac ["COPY", "tmp:0:8", ["const:628:8"]]
- 00c06298 ["INT_ADD", "register:40f0:8", ["const:c06298:8", "const:4:8"]]
+ 00c066c0 ["INT_ADD", "register:40f0:8", ["const:c066c0:8", "const:4:8"]]
~~~


### [`00c06350`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06350.md) → [`00c06778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06778.md) _ZNSt6__ndk18ios_base4InitC2Ev

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md) · 呼出先 5件 [`00c05d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) [`00c06304`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06304.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c5e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4f0.md) · 呼出先 5件 [`00c06190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) [`00c0672c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c0672c.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c067ac",
      "incomplete_value": false,
      "site": "00c067b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06384",
      "incomplete_value": false,
      "site": "00c06388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c067b8",
      "value": [
        "leaf",
        "ram:c06190:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c06390",
      "value": [
        "leaf",
        "ram:c05d68:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c067c0",
      "incomplete_value": false,
      "site": "00c067d4",
      "value": [
        "leaf",
        "const:c0672c:8"
      ]
    },
    "old": {
      "definition_site": "00c06398",
      "incomplete_value": false,
      "site": "00c063ac",
      "value": [
        "leaf",
        "const:c06304:8"
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
      24,
      "READ",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "01127750",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c05d68"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "01127b50",
        null,
        "undefined1"
      ]
    ],
    [
      64,
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c06190"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c06364 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00c0678c ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00c06384 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00c067ac ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00c06388 ["INT_ADD", "register:40f0:8", ["const:c06388:8", "const:4:8"]]
+ 00c067b0 ["INT_ADD", "register:40f0:8", ["const:c067b0:8", "const:4:8"]]
~~~


### [`00c06414`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06414.md) → [`00c0683c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c0683c.md) FUN_00c0683c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c05d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c06190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 2件 [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c5dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06858",
      "incomplete_value": true,
      "site": "00c06860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06430",
      "incomplete_value": true,
      "site": "00c06438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c068b4",
      "incomplete_value": false,
      "site": "00c068b8",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0648c",
      "incomplete_value": false,
      "site": "00c06490",
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
            "const:cf7:8"
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
      28,
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b5d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c06430 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
+ 00c06858 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8b8:8"]]
- 00c06438 ["INT_ADD", "register:40f0:8", ["const:c06438:8", "const:4:8"]]
+ 00c06860 ["INT_ADD", "register:40f0:8", ["const:c06860:8", "const:4:8"]]
- 00c06448 ["INT_ADD", "register:40f0:8", ["const:c06448:8", "const:4:8"]]
+ 00c06870 ["INT_ADD", "register:40f0:8", ["const:c06870:8", "const:4:8"]]
~~~


### [`00c067a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c067a8.md) → [`00c06bd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06bd0.md) FUN_00c06bd0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06bfc",
      "incomplete_value": true,
      "site": "00c06c00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c067d4",
      "incomplete_value": true,
      "site": "00c067d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      44,
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
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
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c067c8 ["INT_ADD", "register:40f0:8", ["const:c067c8:8", "const:4:8"]]
+ 00c06bf0 ["INT_ADD", "register:40f0:8", ["const:c06bf0:8", "const:4:8"]]
- 00c067d4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:4b8:8"]]
+ 00c06bfc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8b8:8"]]
- 00c067d8 ["INT_ADD", "register:40f0:8", ["const:c067d8:8", "const:4:8"]]
+ 00c06c00 ["INT_ADD", "register:40f0:8", ["const:c06c00:8", "const:4:8"]]
~~~


### [`00c06aa8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06aa8.md) → [`00c06ed0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06ed0.md) FUN_00c06ed0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c05d68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05d68.md) · 呼出先 2件 [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c5dbb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md)
- 新版 呼出元 1件 [`00c06190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06190.md) · 呼出先 2件 [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c5dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06eec",
      "incomplete_value": true,
      "site": "00c06ef4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06ac4",
      "incomplete_value": true,
      "site": "00c06acc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c06f48",
      "incomplete_value": false,
      "site": "00c06f4c",
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
            "const:d37:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06b20",
      "incomplete_value": false,
      "site": "00c06b24",
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
            "const:cf7:8"
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
      28,
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b5cf7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      120,
      "PARAM",
      [
        "storage",
        "002b5d37",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c06ac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7a8:8"]]
+ 00c06eec ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ba8:8"]]
- 00c06acc ["INT_ADD", "register:40f0:8", ["const:c06acc:8", "const:4:8"]]
+ 00c06ef4 ["INT_ADD", "register:40f0:8", ["const:c06ef4:8", "const:4:8"]]
- 00c06adc ["INT_ADD", "register:40f0:8", ["const:c06adc:8", "const:4:8"]]
+ 00c06f04 ["INT_ADD", "register:40f0:8", ["const:c06f04:8", "const:4:8"]]
~~~


### [`00c06e34`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c06e34.md) → [`00c0725c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0725c.md) FUN_00c0725c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c07288",
      "incomplete_value": true,
      "site": "00c0728c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c06e60",
      "incomplete_value": true,
      "site": "00c06e64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
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
      44,
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
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
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "PARAM",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c06e54 ["INT_ADD", "register:40f0:8", ["const:c06e54:8", "const:4:8"]]
+ 00c0727c ["INT_ADD", "register:40f0:8", ["const:c0727c:8", "const:4:8"]]
- 00c06e60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:7a8:8"]]
+ 00c07288 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ba8:8"]]
- 00c06e64 ["INT_ADD", "register:40f0:8", ["const:c06e64:8", "const:4:8"]]
+ 00c0728c ["INT_ADD", "register:40f0:8", ["const:c0728c:8", "const:4:8"]]
~~~


### [`00c070fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c070fc.md) → [`00c07524`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07524.md) _INIT_2

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c063e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c06/00c063e0.md) [`00c57a30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c5e0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e0f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c06808`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c06/00c06808.md) [`00c57e30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c5e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e4f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0753c",
      "incomplete_value": false,
      "site": "00c07540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c07114",
      "incomplete_value": false,
      "site": "00c07118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
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
      24,
      "PARAM",
      [
        "storage",
        "011274c0",
        null,
        null
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c9b7b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      24,
      "PARAM",
      [
        "storage",
        "011278c0",
        null,
        null
      ]
    ],
    [
      40,
      "PARAM",
      [
        "storage",
        "00c62f90",
        null,
        "pointer"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "00c9bbb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c07110 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00c07538 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00c07118 ["INT_ADD", "register:40f0:8", ["const:c07118:8", "const:4:8"]]
+ 00c07540 ["INT_ADD", "register:40f0:8", ["const:c07540:8", "const:4:8"]]
- 00c07124 ["COPY", "register:4010:8", ["const:c62b90:8"]]
- 00c07128 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7b0:8"]]
+ 00c0754c ["COPY", "register:4010:8", ["const:c62f90:8"]]
+ 00c07550 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bb0:8"]]
~~~


### [`00c07464`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c07464.md) → [`00c0788c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c0788c.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c07910",
      "incomplete_value": true,
      "site": "00c07910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c074e8",
      "incomplete_value": true,
      "site": "00c074e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00c07988",
      "incomplete_value": true,
      "site": "00c07988",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c07560",
      "incomplete_value": true,
      "site": "00c07560",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c07918",
      "incomplete_value": true,
      "site": "00c0791c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c074f0",
      "incomplete_value": true,
      "site": "00c074f4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      124,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      124,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c074ac ["INT_ADD", "register:40f0:8", ["const:c074ac:8", "const:4:8"]]
+ 00c078d4 ["INT_ADD", "register:40f0:8", ["const:c078d4:8", "const:4:8"]]
- 00c074d8 ["INT_ADD", "register:40f0:8", ["const:c074d8:8", "const:4:8"]]
+ 00c07900 ["INT_ADD", "register:40f0:8", ["const:c07900:8", "const:4:8"]]
- 00c074e0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
+ 00c07908 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
~~~


### [`00c0a10c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a10c.md) → [`00c0a534`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0a534.md) _ZNKSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0ac28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0a580",
      "incomplete_value": true,
      "site": "00c0a580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a158",
      "incomplete_value": true,
      "site": "00c0a158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0a9fc",
      "incomplete_value": true,
      "site": "00c0a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a5d4",
      "incomplete_value": true,
      "site": "00c0a5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0a588",
      "incomplete_value": true,
      "site": "00c0a58c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0a160",
      "incomplete_value": true,
      "site": "00c0a164",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      68,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      76,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
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
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      76,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0a148 ["INT_ADD", "register:40f0:8", ["const:c0a148:8", "const:4:8"]]
+ 00c0a570 ["INT_ADD", "register:40f0:8", ["const:c0a570:8", "const:4:8"]]
- 00c0a150 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:830:8"]]
+ 00c0a578 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c30:8"]]
- 00c0a180 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0a184 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c0a5a8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0a5ac ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c0a8b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a8b4.md) → [`00c0acdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0acdc.md) _ZNSt6__ndk16__clocEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0ad38",
      "incomplete_value": true,
      "site": "00c0ad38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a910",
      "incomplete_value": true,
      "site": "00c0a910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c0ad18",
      "incomplete_value": false,
      "site": "00c0ad1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a8f0",
      "incomplete_value": false,
      "site": "00c0a8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c0ad28",
      "incomplete_value": false,
      "site": "00c0ad34",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a900",
      "incomplete_value": false,
      "site": "00c0a90c",
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
            "const:13c:8"
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
      28,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      36,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0a8c8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0acf0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0a8d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00c0ad00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
- 00c0a8f0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0ad18 ["COPY", "tmp:0:8", ["const:ca0:8"]]
~~~


### [`00c0a93c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a93c.md) → [`00c0ad64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ad64.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ade8",
      "incomplete_value": true,
      "site": "00c0ade8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0a9c0",
      "incomplete_value": true,
      "site": "00c0a9c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c0ae60",
      "incomplete_value": true,
      "site": "00c0ae60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0aa38",
      "incomplete_value": true,
      "site": "00c0aa38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0adf0",
      "incomplete_value": true,
      "site": "00c0adf4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0a9c8",
      "incomplete_value": true,
      "site": "00c0a9cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      124,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      124,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      132,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0a984 ["INT_ADD", "register:40f0:8", ["const:c0a984:8", "const:4:8"]]
+ 00c0adac ["INT_ADD", "register:40f0:8", ["const:c0adac:8", "const:4:8"]]
- 00c0a9b0 ["INT_ADD", "register:40f0:8", ["const:c0a9b0:8", "const:4:8"]]
+ 00c0add8 ["INT_ADD", "register:40f0:8", ["const:c0add8:8", "const:4:8"]]
- 00c0a9b8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
+ 00c0ade0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
~~~


### [`00c0d580`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0d580.md) → [`00c0d9a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0d/00c0d9a8.md) _ZNKSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjRPv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0a800`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0a800.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0ac28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0ac28.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0d9f4",
      "incomplete_value": true,
      "site": "00c0d9f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0d5cc",
      "incomplete_value": true,
      "site": "00c0d5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0de64",
      "incomplete_value": true,
      "site": "00c0de64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0da3c",
      "incomplete_value": true,
      "site": "00c0da3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0d9fc",
      "incomplete_value": true,
      "site": "00c0da00",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0d5d4",
      "incomplete_value": true,
      "site": "00c0d5d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      68,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      76,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
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
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      76,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0d5bc ["INT_ADD", "register:40f0:8", ["const:c0d5bc:8", "const:4:8"]]
+ 00c0d9e4 ["INT_ADD", "register:40f0:8", ["const:c0d9e4:8", "const:4:8"]]
- 00c0d5c4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:740:8"]]
+ 00c0d9ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b40:8"]]
- 00c0d5f4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0d5f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c0da1c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0da20 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c0dc64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0d/00c0dc64.md) → [`00c0e08c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e08c.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_prepERNS_8ios_baseEPcRcS5_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e150`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e150.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e550`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e550.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e144",
      "incomplete_value": true,
      "site": "00c0e14c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0dd1c",
      "incomplete_value": true,
      "site": "00c0dd24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0e0f8",
      "incomplete_value": true,
      "site": "00c0e100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0dcd0",
      "incomplete_value": true,
      "site": "00c0dcd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      "definition_site": "00c0e0f4",
      "incomplete_value": false,
      "site": "00c0e100",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c0dccc",
      "incomplete_value": false,
      "site": "00c0dcd8",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      56,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
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
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0dc94 ["INT_ADD", "register:40f0:8", ["const:c0dc94:8", "const:4:8"]]
+ 00c0e0bc ["INT_ADD", "register:40f0:8", ["const:c0e0bc:8", "const:4:8"]]
- 00c0dc9c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
+ 00c0e0c4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
- 00c0dccc ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0dcd0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c0e0f4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0e0f8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c0e078`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e078.md) → [`00c0e4a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e4a0.md) _ZNSt6__ndk19__num_getIcE17__stage2_int_prepERNS_8ios_baseEPcRc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e120`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e120.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e520.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e554",
      "incomplete_value": true,
      "site": "00c0e55c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e12c",
      "incomplete_value": true,
      "site": "00c0e134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0e544",
      "incomplete_value": true,
      "site": "00c0e54c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e11c",
      "incomplete_value": true,
      "site": "00c0e124",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c0:8"
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
      "definition_site": "00c0e548",
      "incomplete_value": true,
      "site": "00c0e54c",
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
            "const:1a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e120",
      "incomplete_value": true,
      "site": "00c0e124",
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
            "const:1a:8"
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
      52,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
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
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0e0a4 ["INT_ADD", "register:40f0:8", ["const:c0e0a4:8", "const:4:8"]]
+ 00c0e4cc ["INT_ADD", "register:40f0:8", ["const:c0e4cc:8", "const:4:8"]]
- 00c0e0ac ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00c0e4d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
- 00c0e0dc ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0e0e0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c0e504 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0e508 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c0e1f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e1f8.md) → [`00c0e620`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0e620.md) _ZNSt6__ndk19__num_getIwE19__stage2_float_prepERNS_8ios_baseEPwRwS5_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1b0.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5b0.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e658",
      "incomplete_value": true,
      "site": "00c0e660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e230",
      "incomplete_value": true,
      "site": "00c0e238",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0e6d8",
      "incomplete_value": true,
      "site": "00c0e6e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e2b0",
      "incomplete_value": true,
      "site": "00c0e2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0e668",
      "incomplete_value": true,
      "site": "00c0e66c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0e240",
      "incomplete_value": true,
      "site": "00c0e244",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      56,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
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
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      64,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0e228 ["INT_ADD", "register:40f0:8", ["const:c0e228:8", "const:4:8"]]
+ 00c0e650 ["INT_ADD", "register:40f0:8", ["const:c0e650:8", "const:4:8"]]
- 00c0e230 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
+ 00c0e658 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
- 00c0e260 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0e264 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c0e688 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0e68c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c0e5f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e5f8.md) → [`00c0ea20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ea20.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_prepERNS_8ios_baseEPwRw

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e190.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e590`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e590.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ea54",
      "incomplete_value": true,
      "site": "00c0ea5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e62c",
      "incomplete_value": true,
      "site": "00c0e634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c0ead4",
      "incomplete_value": true,
      "site": "00c0eadc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e6ac",
      "incomplete_value": true,
      "site": "00c0e6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0ea64",
      "incomplete_value": true,
      "site": "00c0ea68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0e63c",
      "incomplete_value": true,
      "site": "00c0e640",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      52,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
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
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      64,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0e624 ["INT_ADD", "register:40f0:8", ["const:c0e624:8", "const:4:8"]]
+ 00c0ea4c ["INT_ADD", "register:40f0:8", ["const:c0ea4c:8", "const:4:8"]]
- 00c0e62c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:740:8"]]
+ 00c0ea54 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b40:8"]]
- 00c0e65c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0e660 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c0ea84 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0ea88 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c0e778`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e778.md) → [`00c0eba0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0eba0.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c0ec08",
      "incomplete_value": true,
      "site": "00c0ec08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e7e0",
      "incomplete_value": true,
      "site": "00c0e7e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c0ec10",
      "incomplete_value": true,
      "site": "00c0ec14",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0e7e8",
      "incomplete_value": true,
      "site": "00c0e7ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0ec34",
      "incomplete_value": true,
      "site": "00c0ec3c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0e80c",
      "incomplete_value": true,
      "site": "00c0e814",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7b8:8"
              ]
            ]
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
      96,
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      96,
      "READ",
      [
        "storage",
        "00c9bbb8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "DATA",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0e7d0 ["INT_ADD", "register:40f0:8", ["const:c0e7d0:8", "const:4:8"]]
+ 00c0ebf8 ["INT_ADD", "register:40f0:8", ["const:c0ebf8:8", "const:4:8"]]
- 00c0e7d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7b8:8"]]
+ 00c0ec00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
- 00c0e808 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0e80c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7b8:8"]]
+ 00c0ec30 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c0ec34 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bb8:8"]]
~~~


### [`00c0e958`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e958.md) → [`00c0ed80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed80.md) FUN_00c0ed80

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0e948`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0e948.md) · 呼出先 8件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0ed70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0ed70.md) · 呼出先 8件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0ef7c",
      "incomplete_value": true,
      "site": "00c0ef7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eb54",
      "incomplete_value": true,
      "site": "00c0eb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0ee60",
      "incomplete_value": true,
      "site": "00c0ee78",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ea38",
      "incomplete_value": true,
      "site": "00c0ea50",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c0ef5c",
      "incomplete_value": false,
      "site": "00c0ef60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eb34",
      "incomplete_value": false,
      "site": "00c0eb38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      212,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "011278a0",
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
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0ea28 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0ee50 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0ea38 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c0ee60 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c0ea50 ["INT_ADD", "register:40f0:8", ["const:c0ea50:8", "const:4:8"]]
+ 00c0ee78 ["INT_ADD", "register:40f0:8", ["const:c0ee78:8", "const:4:8"]]
~~~


### [`00c0eba4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md) → [`00c0efcc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efcc.md) FUN_00c0efcc

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0eb94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eb94.md) · 呼出先 8件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0efbc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0e/00c0efbc.md) · 呼出先 8件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f1c8",
      "incomplete_value": true,
      "site": "00c0f1c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eda0",
      "incomplete_value": true,
      "site": "00c0eda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f0ac",
      "incomplete_value": true,
      "site": "00c0f0c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ec84",
      "incomplete_value": true,
      "site": "00c0ec9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c0f1a8",
      "incomplete_value": false,
      "site": "00c0f1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ed80",
      "incomplete_value": false,
      "site": "00c0ed84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      212,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "011278a0",
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
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0ec74 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0f09c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0ec84 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c0f0ac ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c0ec9c ["INT_ADD", "register:40f0:8", ["const:c0ec9c:8", "const:4:8"]]
+ 00c0f0c4 ["INT_ADD", "register:40f0:8", ["const:c0f0c4:8", "const:4:8"]]
~~~


### [`00c0edf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0edf0.md) → [`00c0f218`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f218.md) FUN_00c0f218

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0ede0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0ede0.md) · 呼出先 8件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0f208`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f208.md) · 呼出先 8件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f3f8",
      "incomplete_value": true,
      "site": "00c0f3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0efd0",
      "incomplete_value": true,
      "site": "00c0efd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f2dc",
      "incomplete_value": true,
      "site": "00c0f2f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0eeb4",
      "incomplete_value": true,
      "site": "00c0eecc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c0f3d8",
      "incomplete_value": false,
      "site": "00c0f3dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0efb0",
      "incomplete_value": false,
      "site": "00c0efb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      184,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      184,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0eea4 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0f2cc ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0eeb4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c0f2dc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c0eecc ["INT_ADD", "register:40f0:8", ["const:c0eecc:8", "const:4:8"]]
+ 00c0f2f4 ["INT_ADD", "register:40f0:8", ["const:c0f2f4:8", "const:4:8"]]
~~~


### [`00c0f020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f020.md) → [`00c0f448`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f448.md) FUN_00c0f448

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0f010`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f010.md) · 呼出先 8件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c0f438`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f438.md) · 呼出先 8件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f628",
      "incomplete_value": true,
      "site": "00c0f628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f200",
      "incomplete_value": true,
      "site": "00c0f200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c0f50c",
      "incomplete_value": true,
      "site": "00c0f524",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f0e4",
      "incomplete_value": true,
      "site": "00c0f0fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c0f608",
      "incomplete_value": false,
      "site": "00c0f60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f1e0",
      "incomplete_value": false,
      "site": "00c0f1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      184,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      184,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0f0d4 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0f4fc ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0f0e4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c0f50c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c0f0fc ["INT_ADD", "register:40f0:8", ["const:c0f0fc:8", "const:4:8"]]
+ 00c0f524 ["INT_ADD", "register:40f0:8", ["const:c0f524:8", "const:4:8"]]
~~~


### [`00c0f250`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) → [`00c0f678`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f678.md) FUN_00c0f678

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0f240`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f240.md) · 呼出先 12件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c0f668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0f668.md) · 呼出先 12件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f9bc",
      "incomplete_value": false,
      "site": "00c0f9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f594",
      "incomplete_value": false,
      "site": "00c0f594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0f9fc",
      "incomplete_value": false,
      "site": "00c0f9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f5d4",
      "incomplete_value": false,
      "site": "00c0f5d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0fa34",
      "incomplete_value": true,
      "site": "00c0fa34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0f60c",
      "incomplete_value": true,
      "site": "00c0f60c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
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
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      268,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      256,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      268,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0f348 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0f770 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0f35c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
+ 00c0f784 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c0f36c ["INT_ADD", "register:40f0:8", ["const:c0f36c:8", "const:4:8"]]
+ 00c0f794 ["INT_ADD", "register:40f0:8", ["const:c0f794:8", "const:4:8"]]
~~~


### [`00c0f6e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md) → [`00c0fb08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0fb08.md) FUN_00c0fb08

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c0f6d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6d0.md) · 呼出先 12件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c0faf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0faf8.md) · 呼出先 12件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0fe44",
      "incomplete_value": false,
      "site": "00c0fe44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa1c",
      "incomplete_value": false,
      "site": "00c0fa1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0fe84",
      "incomplete_value": false,
      "site": "00c0fe84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa5c",
      "incomplete_value": false,
      "site": "00c0fa5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c0febc",
      "incomplete_value": true,
      "site": "00c0febc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fa94",
      "incomplete_value": true,
      "site": "00c0fa94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      252,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      252,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0f7d4 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0fbfc ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0f7e4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
+ 00c0fc0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c0f7f8 ["INT_ADD", "register:40f0:8", ["const:c0f7f8:8", "const:4:8"]]
+ 00c0fc20 ["INT_ADD", "register:40f0:8", ["const:c0fc20:8", "const:4:8"]]
~~~


### [`00c0fb58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fb58.md) → [`00c0ff80`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0f/00c0ff80.md) _ZNKSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_RNS_8ios_baseEcPKv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c10074",
      "incomplete_value": true,
      "site": "00c10074",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fc4c",
      "incomplete_value": true,
      "site": "00c0fc4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10164",
      "incomplete_value": true,
      "site": "00c10164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0fd3c",
      "incomplete_value": true,
      "site": "00c0fd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1007c",
      "incomplete_value": true,
      "site": "00c10080",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0fc54",
      "incomplete_value": true,
      "site": "00c0fc58",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "002a621f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      44,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      68,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      76,
      "PARAM",
      [
        "storage",
        "002a62fb",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0fb7c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c0ffa4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c0fb9c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c0ffc4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c0fba4 ["COPY", "tmp:0:8", ["const:21f:8"]]
+ 00c0ffcc ["COPY", "tmp:0:8", ["const:2fb:8"]]
~~~


### [`00c0feac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0feac.md) → [`00c102d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c102d4.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1033c",
      "incomplete_value": true,
      "site": "00c1033c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ff14",
      "incomplete_value": true,
      "site": "00c0ff14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c10344",
      "incomplete_value": true,
      "site": "00c10348",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c0ff1c",
      "incomplete_value": true,
      "site": "00c0ff20",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10368",
      "incomplete_value": true,
      "site": "00c10370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c0ff40",
      "incomplete_value": true,
      "site": "00c0ff48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
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
      96,
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      96,
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      104,
      "DATA",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c0ff04 ["INT_ADD", "register:40f0:8", ["const:c0ff04:8", "const:4:8"]]
+ 00c1032c ["INT_ADD", "register:40f0:8", ["const:c1032c:8", "const:4:8"]]
- 00c0ff0c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:7c8:8"]]
+ 00c10334 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bc8:8"]]
- 00c0ff3c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c0ff40 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7c8:8"]]
+ 00c10364 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c10368 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bc8:8"]]
~~~


### [`00c1008c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1008c.md) → [`00c104b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c104b4.md) FUN_00c104b4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c1007c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c1007c.md) · 呼出先 8件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c104a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c104a4.md) · 呼出先 8件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c106b0",
      "incomplete_value": true,
      "site": "00c106b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10288",
      "incomplete_value": true,
      "site": "00c10288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10594",
      "incomplete_value": true,
      "site": "00c105ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1016c",
      "incomplete_value": true,
      "site": "00c10184",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c10690",
      "incomplete_value": false,
      "site": "00c10694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10268",
      "incomplete_value": false,
      "site": "00c1026c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      212,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "011278a0",
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
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1015c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c10584 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c1016c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c10594 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c10184 ["INT_ADD", "register:40f0:8", ["const:c10184:8", "const:4:8"]]
+ 00c105ac ["INT_ADD", "register:40f0:8", ["const:c105ac:8", "const:4:8"]]
~~~


### [`00c102d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102d8.md) → [`00c10700`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10700.md) FUN_00c10700

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c102c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c102c8.md) · 呼出先 8件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c106f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c106f0.md) · 呼出先 8件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c108fc",
      "incomplete_value": true,
      "site": "00c108fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c104d4",
      "incomplete_value": true,
      "site": "00c104d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c107e0",
      "incomplete_value": true,
      "site": "00c107f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c103b8",
      "incomplete_value": true,
      "site": "00c103d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c108dc",
      "incomplete_value": false,
      "site": "00c108e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c104b4",
      "incomplete_value": false,
      "site": "00c104b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      212,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "011278a0",
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
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      224,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      476,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c103a8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c107d0 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c103b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c107e0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c103d0 ["INT_ADD", "register:40f0:8", ["const:c103d0:8", "const:4:8"]]
+ 00c107f8 ["INT_ADD", "register:40f0:8", ["const:c107f8:8", "const:4:8"]]
~~~


### [`00c10524`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10524.md) → [`00c1094c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c1094c.md) FUN_00c1094c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10514`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10514.md) · 呼出先 8件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c1093c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c1093c.md) · 呼出先 8件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10b2c",
      "incomplete_value": true,
      "site": "00c10b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10704",
      "incomplete_value": true,
      "site": "00c10704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10b0c",
      "incomplete_value": false,
      "site": "00c10b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c106e4",
      "incomplete_value": false,
      "site": "00c106e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      "definition_site": "00c10b1c",
      "incomplete_value": false,
      "site": "00c10b28",
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
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c106f4",
      "incomplete_value": false,
      "site": "00c10700",
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
            "const:13c:8"
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
      184,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      184,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c105d8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c10a00 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c105e8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c10a10 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c10600 ["INT_ADD", "register:40f0:8", ["const:c10600:8", "const:4:8"]]
+ 00c10a28 ["INT_ADD", "register:40f0:8", ["const:c10a28:8", "const:4:8"]]
~~~


### [`00c10754`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10754.md) → [`00c10b7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10b7c.md) FUN_00c10b7c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10744`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10744.md) · 呼出先 8件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 1件 [`00c10b6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10b6c.md) · 呼出先 8件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c10d5c",
      "incomplete_value": true,
      "site": "00c10d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10934",
      "incomplete_value": true,
      "site": "00c10934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c10c40",
      "incomplete_value": true,
      "site": "00c10c58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10818",
      "incomplete_value": true,
      "site": "00c10830",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c10d3c",
      "incomplete_value": false,
      "site": "00c10d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10914",
      "incomplete_value": false,
      "site": "00c10918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
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
      184,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      184,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      196,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c10808 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c10c30 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c10818 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c10c40 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c10830 ["INT_ADD", "register:40f0:8", ["const:c10830:8", "const:4:8"]]
+ 00c10c58 ["INT_ADD", "register:40f0:8", ["const:c10c58:8", "const:4:8"]]
~~~


### [`00c10984`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) → [`00c10dac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10dac.md) FUN_00c10dac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10974`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10974.md) · 呼出先 12件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c10d9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c10d9c.md) · 呼出先 12件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c110f0",
      "incomplete_value": false,
      "site": "00c110f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10cc8",
      "incomplete_value": false,
      "site": "00c10cc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11130",
      "incomplete_value": true,
      "site": "00c11130",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10d08",
      "incomplete_value": true,
      "site": "00c10d08",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11168",
      "incomplete_value": true,
      "site": "00c11168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c10d40",
      "incomplete_value": true,
      "site": "00c10d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
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
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      268,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      256,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      268,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      336,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c10a7c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c10ea4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c10a90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
+ 00c10eb8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c10aa0 ["INT_ADD", "register:40f0:8", ["const:c10aa0:8", "const:4:8"]]
+ 00c10ec8 ["INT_ADD", "register:40f0:8", ["const:c10ec8:8", "const:4:8"]]
~~~


### [`00c10e14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md) → [`00c1123c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1123c.md) FUN_00c1123c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c10e04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e04.md) · 呼出先 12件 [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c1122c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c1122c.md) · 呼出先 12件 [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c11578",
      "incomplete_value": false,
      "site": "00c11578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11150",
      "incomplete_value": false,
      "site": "00c11150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c115b8",
      "incomplete_value": false,
      "site": "00c115b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11190",
      "incomplete_value": false,
      "site": "00c11190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c115f0",
      "incomplete_value": true,
      "site": "00c115f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c111c8",
      "incomplete_value": true,
      "site": "00c111c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      252,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      252,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      332,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c10f08 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c11330 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c10f18 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
+ 00c11340 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
- 00c10f2c ["INT_ADD", "register:40f0:8", ["const:c10f2c:8", "const:4:8"]]
+ 00c11354 ["INT_ADD", "register:40f0:8", ["const:c11354:8", "const:4:8"]]
~~~


### [`00c1128c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c1128c.md) → [`00c116b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c116b4.md) _ZNKSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_RNS_8ios_baseEwPKv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0fd7c.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c101a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c10/00c101a4.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c118a4",
      "incomplete_value": true,
      "site": "00c118a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1147c",
      "incomplete_value": true,
      "site": "00c1147c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00c116fc",
      "incomplete_value": true,
      "site": "00c11718",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:c98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c112d4",
      "incomplete_value": true,
      "site": "00c112f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
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
      "definition_site": "00c11704",
      "incomplete_value": false,
      "site": "00c11718",
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
            "const:2fb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c112dc",
      "incomplete_value": false,
      "site": "00c112f0",
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
            "const:21f:8"
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
      48,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002a621f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      80,
      "PARAM",
      [
        "storage",
        "002a62fb",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c112b4 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c116dc ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c112d4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:898:8"]]
+ 00c116fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c98:8"]]
- 00c112dc ["COPY", "tmp:0:8", ["const:21f:8"]]
+ 00c11704 ["COPY", "tmp:0:8", ["const:2fb:8"]]
~~~


### [`00c116bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c116bc.md) → [`00c11ae4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c11ae4.md) _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1d0.md) · 呼出先 4件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5d0.md) · 呼出先 4件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11b2c",
      "incomplete_value": true,
      "site": "00c11b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11704",
      "incomplete_value": true,
      "site": "00c11704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00c11b94",
      "incomplete_value": true,
      "site": "00c11b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1176c",
      "incomplete_value": true,
      "site": "00c1176c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c11b38",
      "incomplete_value": true,
      "site": "00c11b3c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c11710",
      "incomplete_value": true,
      "site": "00c11714",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c116ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:830:8"]]
+ 00c11b14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c30:8"]]
- 00c1172c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c11b54 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c11738 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c11b60 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c11ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c11ab0.md) → [`00c11ed8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c11ed8.md) _ZNSt6__ndk19__num_putIcE23__widen_and_group_floatEPcS2_S2_S2_RS2_S3_RKNS_6localeE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1e0.md) · 呼出先 7件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5e5e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5e0.md) · 呼出先 7件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c11f20",
      "incomplete_value": true,
      "site": "00c11f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11af8",
      "incomplete_value": true,
      "site": "00c11af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00c11f88",
      "incomplete_value": true,
      "site": "00c11f88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11b60",
      "incomplete_value": true,
      "site": "00c11b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1212c",
      "incomplete_value": true,
      "site": "00c1212c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c11d04",
      "incomplete_value": true,
      "site": "00c11d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
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
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c11ae0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:830:8"]]
+ 00c11f08 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c30:8"]]
- 00c11b20 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c11f48 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c11b2c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c11f54 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c120a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c120a8.md) → [`00c124d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c12/00c124d0.md) _ZNSt6__ndk19__num_putIwE21__widen_and_group_intEPcS2_S2_PwRS3_S4_RKNS_6localeE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e1f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e1f0.md) · 呼出先 4件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e5f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e5f0.md) · 呼出先 4件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12518",
      "incomplete_value": true,
      "site": "00c12518",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c120f0",
      "incomplete_value": true,
      "site": "00c120f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c12580",
      "incomplete_value": true,
      "site": "00c12580",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c12158",
      "incomplete_value": true,
      "site": "00c12158",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c12524",
      "incomplete_value": true,
      "site": "00c12528",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c120fc",
      "incomplete_value": true,
      "site": "00c12100",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c120d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:740:8"]]
+ 00c12500 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b40:8"]]
- 00c12118 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c12540 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c12124 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c1254c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c124a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c12/00c124a4.md) → [`00c128cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c12/00c128cc.md) _ZNSt6__ndk19__num_putIwE23__widen_and_group_floatEPcS2_S2_PwRS3_S4_RKNS_6localeE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e200`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e200.md) · 呼出先 7件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c5e600`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e600.md) · 呼出先 7件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c12914",
      "incomplete_value": true,
      "site": "00c12914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c124ec",
      "incomplete_value": true,
      "site": "00c124ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12b18",
      "incomplete_value": true,
      "site": "00c12b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c126f0",
      "incomplete_value": true,
      "site": "00c126f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c12b98",
      "incomplete_value": false,
      "site": "00c12b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c12770",
      "incomplete_value": false,
      "site": "00c12770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
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
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c124d4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:740:8"]]
+ 00c128fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:b40:8"]]
- 00c12514 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1293c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c12520 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c12948 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c13050`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13050.md) → [`00c13478`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13478.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c134b8",
      "incomplete_value": true,
      "site": "00c134c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13090",
      "incomplete_value": true,
      "site": "00c13098",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c134c8",
      "incomplete_value": true,
      "site": "00c134cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c130a0",
      "incomplete_value": true,
      "site": "00c130a4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c134e8",
      "incomplete_value": true,
      "site": "00c134f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c130c0",
      "incomplete_value": true,
      "site": "00c130c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c13088 ["INT_ADD", "register:40f0:8", ["const:c13088:8", "const:4:8"]]
+ 00c134b0 ["INT_ADD", "register:40f0:8", ["const:c134b0:8", "const:4:8"]]
- 00c13090 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
+ 00c134b8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
- 00c130bc ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c130c0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c134e4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c134e8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c13264`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13264.md) → [`00c1368c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c1368c.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c136cc",
      "incomplete_value": true,
      "site": "00c136d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c132a4",
      "incomplete_value": true,
      "site": "00c132ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c136dc",
      "incomplete_value": true,
      "site": "00c136e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c132b4",
      "incomplete_value": true,
      "site": "00c132b8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c136fc",
      "incomplete_value": true,
      "site": "00c13704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c132d4",
      "incomplete_value": true,
      "site": "00c132dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1329c ["INT_ADD", "register:40f0:8", ["const:c1329c:8", "const:4:8"]]
+ 00c136c4 ["INT_ADD", "register:40f0:8", ["const:c136c4:8", "const:4:8"]]
- 00c132a4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:830:8"]]
+ 00c136cc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c30:8"]]
- 00c132d0 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c132d4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c136f8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c136fc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c13468`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c13468.md) → [`00c13890`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13890.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c14484`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c148ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c138cc",
      "incomplete_value": true,
      "site": "00c138d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c134a4",
      "incomplete_value": true,
      "site": "00c134ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c13900",
      "incomplete_value": true,
      "site": "00c13908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c134d8",
      "incomplete_value": true,
      "site": "00c134e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      "definition_site": "00c138fc",
      "incomplete_value": false,
      "site": "00c13908",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c134d4",
      "incomplete_value": false,
      "site": "00c134e0",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      60,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
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
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1349c ["INT_ADD", "register:40f0:8", ["const:c1349c:8", "const:4:8"]]
+ 00c138c4 ["INT_ADD", "register:40f0:8", ["const:c138c4:8", "const:4:8"]]
- 00c134a4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00c138cc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
- 00c134d4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c134d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c138fc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c13900 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c135ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c13/00c135ec.md) → [`00c13a14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c13/00c13a14.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c076f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c07/00c076f0.md) [`00c14484`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c07b18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c07/00c07b18.md) [`00c148ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c148ac.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c13a6c",
      "incomplete_value": true,
      "site": "00c13a6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13644",
      "incomplete_value": true,
      "site": "00c13644",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:830:8"
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
      "definition_site": "00c13c60",
      "incomplete_value": true,
      "site": "00c13c74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:ebf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c13838",
      "incomplete_value": true,
      "site": "00c1384c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:e7f:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c13a74",
      "incomplete_value": true,
      "site": "00c13a78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1364c",
      "incomplete_value": true,
      "site": "00c13650",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      80,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c13634 ["INT_ADD", "register:40f0:8", ["const:c13634:8", "const:4:8"]]
+ 00c13a5c ["INT_ADD", "register:40f0:8", ["const:c13a5c:8", "const:4:8"]]
- 00c1363c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:830:8"]]
+ 00c13a64 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c30:8"]]
- 00c1366c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c13670 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c13a94 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c13a98 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c147c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c147c8.md) → [`00c14bf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c14/00c14bf0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE3getES4_S4_RNS_8ios_baseERjP2tmPKwSC_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e230`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5e630`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e630.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c14c78",
      "incomplete_value": true,
      "site": "00c14c80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14850",
      "incomplete_value": true,
      "site": "00c14858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      "definition_site": "00c14c74",
      "incomplete_value": false,
      "site": "00c14c80",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c1484c",
      "incomplete_value": false,
      "site": "00c14858",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      84,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      92,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      84,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      92,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      96,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c14814 ["INT_ADD", "register:40f0:8", ["const:c14814:8", "const:4:8"]]
+ 00c14c3c ["INT_ADD", "register:40f0:8", ["const:c14c3c:8", "const:4:8"]]
- 00c1481c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:740:8"]]
+ 00c14c44 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:b40:8"]]
- 00c1484c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c14850 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c14c74 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c14c78 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c14cc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14cc8.md) → [`00c150f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c150f0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_timeES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5e230`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e630`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e630.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1510c",
      "incomplete_value": true,
      "site": "00c15118",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2e1000:8"
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
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2e1000:8"
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1510c",
      "incomplete_value": true,
      "site": "00c15118",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c14ce4",
      "incomplete_value": true,
      "site": "00c14cf0",
      "value": [
        "LOAD",
        "16",
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
      "READ",
      [
        "storage",
        "002e1938",
        null,
        null
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "002e1948",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      28,
      "READ",
      [
        "storage",
        "002e1978",
        null,
        null
      ]
    ],
    [
      28,
      "READ",
      [
        "storage",
        "002e1988",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c14cdc ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00c15104 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00c14cf4 ["INT_ADD", "register:40f0:8", ["const:c14cf4:8", "const:4:8"]]
+ 00c1511c ["INT_ADD", "register:40f0:8", ["const:c1511c:8", "const:4:8"]]
~~~


### [`00c14d98`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d98.md) → [`00c151c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c151c0.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE14do_get_weekdayES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15200",
      "incomplete_value": true,
      "site": "00c15208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14dd8",
      "incomplete_value": true,
      "site": "00c14de0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15210",
      "incomplete_value": true,
      "site": "00c15214",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c14de8",
      "incomplete_value": true,
      "site": "00c14dec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c15230",
      "incomplete_value": true,
      "site": "00c15238",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14e08",
      "incomplete_value": true,
      "site": "00c14e10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c14dd0 ["INT_ADD", "register:40f0:8", ["const:c14dd0:8", "const:4:8"]]
+ 00c151f8 ["INT_ADD", "register:40f0:8", ["const:c151f8:8", "const:4:8"]]
- 00c14dd8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
+ 00c15200 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
- 00c14e04 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c14e08 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c1522c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c15230 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c14fac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14fac.md) → [`00c153d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c153d4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE16do_get_monthnameES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15414",
      "incomplete_value": true,
      "site": "00c1541c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c14fec",
      "incomplete_value": true,
      "site": "00c14ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15424",
      "incomplete_value": true,
      "site": "00c15428",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c14ffc",
      "incomplete_value": true,
      "site": "00c15000",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c15444",
      "incomplete_value": true,
      "site": "00c1544c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1501c",
      "incomplete_value": true,
      "site": "00c15024",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      64,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      76,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c14fe4 ["INT_ADD", "register:40f0:8", ["const:c14fe4:8", "const:4:8"]]
+ 00c1540c ["INT_ADD", "register:40f0:8", ["const:c1540c:8", "const:4:8"]]
- 00c14fec ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:740:8"]]
+ 00c15414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:b40:8"]]
- 00c15018 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c1501c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c15440 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c15444 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c151b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c151b0.md) → [`00c155d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c155d8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_yearES4_S4_RNS_8ios_baseERjP2tm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c161c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c165f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c15614",
      "incomplete_value": true,
      "site": "00c1561c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c151ec",
      "incomplete_value": true,
      "site": "00c151f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c15624",
      "incomplete_value": true,
      "site": "00c15628",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c151fc",
      "incomplete_value": true,
      "site": "00c15200",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c15648",
      "incomplete_value": true,
      "site": "00c15650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c15220",
      "incomplete_value": true,
      "site": "00c15228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      60,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
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
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      68,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      72,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c151e4 ["INT_ADD", "register:40f0:8", ["const:c151e4:8", "const:4:8"]]
+ 00c1560c ["INT_ADD", "register:40f0:8", ["const:c1560c:8", "const:4:8"]]
- 00c151ec ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:740:8"]]
+ 00c15614 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b40:8"]]
- 00c1521c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c15220 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c15644 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c15648 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c15334`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15334.md) → [`00c1575c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c15/00c1575c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_RNS_8ios_baseERjP2tmcc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c0abc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0a/00c0abc8.md) [`00c161c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c0aff0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c0a/00c0aff0.md) [`00c165f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c165f0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c157b4",
      "incomplete_value": true,
      "site": "00c157b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1538c",
      "incomplete_value": true,
      "site": "00c1538c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c159a4",
      "incomplete_value": true,
      "site": "00c159b8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:ecc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1557c",
      "incomplete_value": true,
      "site": "00c15590",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:310000:8"
              ],
              [
                "leaf",
                "const:e8c:8"
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
      "definition_site": "00c159a4",
      "incomplete_value": true,
      "site": "00c159b8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00c1557c",
      "incomplete_value": true,
      "site": "00c15590",
      "value": [
        "LOAD",
        "16",
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
      80,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1537c ["INT_ADD", "register:40f0:8", ["const:c1537c:8", "const:4:8"]]
+ 00c157a4 ["INT_ADD", "register:40f0:8", ["const:c157a4:8", "const:4:8"]]
- 00c15384 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:740:8"]]
+ 00c157ac ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:b40:8"]]
- 00c153b4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c153b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c157dc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c157e0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c16524`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16524.md) → [`00c1694c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c1694c.md) _ZNKSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE3putES4_RNS_8ios_baseEcPK2tmPKcSC_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5a380`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a380.md) · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 1件 [`00c5a780`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a780.md) · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1699c",
      "incomplete_value": true,
      "site": "00c169a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16574",
      "incomplete_value": true,
      "site": "00c1657c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c169ac",
      "incomplete_value": true,
      "site": "00c169b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c16584",
      "incomplete_value": true,
      "site": "00c16588",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c169cc",
      "incomplete_value": true,
      "site": "00c169d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c165a4",
      "incomplete_value": true,
      "site": "00c165ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      80,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1656c ["INT_ADD", "register:40f0:8", ["const:c1656c:8", "const:4:8"]]
+ 00c16994 ["INT_ADD", "register:40f0:8", ["const:c16994:8", "const:4:8"]]
- 00c16574 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:830:8"]]
+ 00c1699c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c30:8"]]
- 00c165a0 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c165a4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c169c8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c169cc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c16904`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16904.md) → [`00c16d2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c16/00c16d2c.md) _ZNKSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE3putES4_RNS_8ios_baseEwPK2tmPKwSC_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c16d7c",
      "incomplete_value": true,
      "site": "00c16d84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16954",
      "incomplete_value": true,
      "site": "00c1695c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c16d8c",
      "incomplete_value": true,
      "site": "00c16d90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c16964",
      "incomplete_value": true,
      "site": "00c16968",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c16dac",
      "incomplete_value": true,
      "site": "00c16db4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16984",
      "incomplete_value": true,
      "site": "00c1698c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      80,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      80,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      88,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1694c ["INT_ADD", "register:40f0:8", ["const:c1694c:8", "const:4:8"]]
+ 00c16d74 ["INT_ADD", "register:40f0:8", ["const:c16d74:8", "const:4:8"]]
- 00c16954 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:740:8"]]
+ 00c16d7c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:b40:8"]]
- 00c16980 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c16984 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c16da8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c16dac ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c16c70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md) → [`00c17098`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17098.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e270.md) · 呼出先 5件 [`00440bfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c5dbb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) [`00c5e170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e260`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md) [`00c5e280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e280.md)
- 新版 呼出元 1件 [`00c5e670`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e670.md) · 呼出先 5件 [`00440c3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c5dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) [`00c5e570`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md) [`00c5e680`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e680.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c17170",
      "incomplete_value": false,
      "site": "00c17174",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16d48",
      "incomplete_value": false,
      "site": "00c16d4c",
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
            "const:d18:8"
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
      216,
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      216,
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c16cd0 ["INT_ADD", "register:40f0:8", ["const:c16cd0:8", "const:4:8"]]
+ 00c170f8 ["INT_ADD", "register:40f0:8", ["const:c170f8:8", "const:4:8"]]
- 00c16ce8 ["INT_ADD", "register:40f0:8", ["const:c16ce8:8", "const:4:8"]]
+ 00c17110 ["INT_ADD", "register:40f0:8", ["const:c17110:8", "const:4:8"]]
- 00c16d04 ["INT_ADD", "register:40f0:8", ["const:c16d04:8", "const:4:8"]]
+ 00c1712c ["INT_ADD", "register:40f0:8", ["const:c1712c:8", "const:4:8"]]
~~~


### [`00c16ec0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md) → [`00c172e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c172e8.md) _ZNKSt6__ndk110moneypunctIwLb0EE16do_negative_signEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c172f4",
      "incomplete_value": true,
      "site": "00c172fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16ecc",
      "incomplete_value": true,
      "site": "00c16ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
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
      12,
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002c3fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c16ecc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
+ 00c172f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
~~~


### [`00c16f50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md) → [`00c17378`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17378.md) _ZNKSt6__ndk110moneypunctIwLb1EE16do_negative_signEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00c17384",
      "incomplete_value": true,
      "site": "00c1738c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16f5c",
      "incomplete_value": true,
      "site": "00c16f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
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
      12,
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      12,
      "READ",
      [
        "storage",
        "002c3fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c16f5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
+ 00c17384 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
~~~


### [`00c17388`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md) → [`00c177b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c177b0.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57bd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57fd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1780c",
      "incomplete_value": true,
      "site": "00c17814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c173e4",
      "incomplete_value": true,
      "site": "00c173ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "definition_site": "00c178b8",
      "incomplete_value": true,
      "site": "00c178c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17490",
      "incomplete_value": true,
      "site": "00c1749c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cbf:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c17840",
      "incomplete_value": true,
      "site": "00c17848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17418",
      "incomplete_value": true,
      "site": "00c17420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      48,
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c173b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d0:8"]]
+ 00c177e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 00c173dc ["INT_ADD", "register:40f0:8", ["const:c173dc:8", "const:4:8"]]
+ 00c17804 ["INT_ADD", "register:40f0:8", ["const:c17804:8", "const:4:8"]]
- 00c173e4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:830:8"]]
+ 00c1780c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c30:8"]]
~~~


### [`00c176d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md) → [`00c17afc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17afc.md) _ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIcEERNS_10unique_ptr

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e290`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e290.md) · 呼出先 11件 [`00440bfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58200`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)
- 新版 呼出元 1件 [`00c5e690`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e690.md) · 呼出先 11件 [`00440c3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c17af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58600`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17c68",
      "incomplete_value": true,
      "site": "00c17c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17840",
      "incomplete_value": true,
      "site": "00c17848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17f44",
      "incomplete_value": true,
      "site": "00c17f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17b1c",
      "incomplete_value": true,
      "site": "00c17b20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17f7c",
      "incomplete_value": true,
      "site": "00c17f80",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17b54",
      "incomplete_value": true,
      "site": "00c17b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
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
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      372,
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      912,
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      364,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      372,
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      912,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c17748 ["INT_ADD", "register:40f0:8", ["const:c17748:8", "const:4:8"]]
- 00c17748 ["CALLIND", null, ["register:0:8"]]
- 00c1774c ["COPY", "tmp:0:4", ["const:1:4"]]
- 00c1774c ["INT_CARRY", "register:105:1", ["register:4000:4", "tmp:0:4"]]
+ 00c17b70 ["INT_ADD", "register:40f0:8", ["const:c17b70:8", "const:4:8"]]
+ 00c17b70 ["CALLIND", null, ["register:0:8"]]
+ 00c17b74 ["COPY", "tmp:0:4", ["const:1:4"]]
+ 00c17b74 ["INT_CARRY", "register:105:1", ["register:4000:4", "tmp:0:4"]]
~~~


### [`00c188dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) → [`00c18d04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18d04.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIcS3_NS_9allocato

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c18b9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c18fc4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18d4c",
      "incomplete_value": true,
      "site": "00c18d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c18924",
      "incomplete_value": true,
      "site": "00c18924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
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
      "definition_site": "00c18d68",
      "incomplete_value": true,
      "site": "00c18d68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c18940",
      "incomplete_value": true,
      "site": "00c18940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c18d70",
      "incomplete_value": true,
      "site": "00c18d74",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c18948",
      "incomplete_value": true,
      "site": "00c1894c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1890c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d0:8"]]
+ 00c18d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 00c18930 ["INT_ADD", "register:40f0:8", ["const:c18930:8", "const:4:8"]]
+ 00c18d58 ["INT_ADD", "register:40f0:8", ["const:c18d58:8", "const:4:8"]]
- 00c18938 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:830:8"]]
+ 00c18d60 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c30:8"]]
~~~


### [`00c19224`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md) → [`00c1964c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c19/00c1964c.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19694",
      "incomplete_value": true,
      "site": "00c19694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1926c",
      "incomplete_value": true,
      "site": "00c1926c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
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
      "definition_site": "00c196a8",
      "incomplete_value": true,
      "site": "00c196b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19280",
      "incomplete_value": true,
      "site": "00c19288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c19754",
      "incomplete_value": true,
      "site": "00c19760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1932c",
      "incomplete_value": true,
      "site": "00c19338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cbf:8"
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
      48,
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      48,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      72,
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      92,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c19254 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d0:8"]]
+ 00c1967c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
- 00c19278 ["INT_ADD", "register:40f0:8", ["const:c19278:8", "const:4:8"]]
+ 00c196a0 ["INT_ADD", "register:40f0:8", ["const:c196a0:8", "const:4:8"]]
- 00c19280 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:740:8"]]
+ 00c196a8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:b40:8"]]
~~~


### [`00c1956c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md) → [`00c19994`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c19/00c19994.md) _ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIwEERNS_10unique_ptr

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e2c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2c0.md) · 呼出先 11件 [`00440bfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c59c20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c5e6c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e6c0.md) · 呼出先 11件 [`00440c3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c17af4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

優先判定に残った影響 `branch_value` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19b24",
      "incomplete_value": true,
      "site": "00c19b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c196fc",
      "incomplete_value": true,
      "site": "00c19704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19de8",
      "incomplete_value": true,
      "site": "00c19df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c199c0",
      "incomplete_value": true,
      "site": "00c199c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19e3c",
      "incomplete_value": true,
      "site": "00c19e40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19a14",
      "incomplete_value": true,
      "site": "00c19a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
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
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      408,
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      924,
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      400,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      408,
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      924,
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c195f4 ["INT_ADD", "register:40f0:8", ["const:c195f4:8", "const:4:8"]]
- 00c195f4 ["CALLIND", null, ["register:0:8"]]
- 00c195f8 ["COPY", "tmp:0:4", ["const:1:4"]]
- 00c195f8 ["INT_CARRY", "register:105:1", ["register:4000:4", "tmp:0:4"]]
+ 00c19a1c ["INT_ADD", "register:40f0:8", ["const:c19a1c:8", "const:4:8"]]
+ 00c19a1c ["CALLIND", null, ["register:0:8"]]
+ 00c19a20 ["COPY", "tmp:0:4", ["const:1:4"]]
+ 00c19a20 ["INT_CARRY", "register:105:1", ["register:4000:4", "tmp:0:4"]]
~~~


### [`00c1b10c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md) → [`00c1b534`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b534.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEce

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1b60c",
      "incomplete_value": true,
      "site": "00c1b614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1b1e4",
      "incomplete_value": true,
      "site": "00c1b1ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1b8d4",
      "incomplete_value": true,
      "site": "00c1b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1b4ac",
      "incomplete_value": true,
      "site": "00c1b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1b61c",
      "incomplete_value": true,
      "site": "00c1b620",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1b1f4",
      "incomplete_value": true,
      "site": "00c1b1f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      52,
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      52,
      "PARAM",
      [
        "storage",
        "002b17b0",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1b140 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00c1b568 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00c1b15c ["INT_ADD", "register:40f0:8", ["const:c1b15c:8", "const:4:8"]]
+ 00c1b584 ["INT_ADD", "register:40f0:8", ["const:c1b584:8", "const:4:8"]]
- 00c1b16c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c1b594 ["COPY", "tmp:0:8", ["const:ca0:8"]]
~~~


### [`00c1bd04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md) → [`00c1c12c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1c12c.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEcRKNS_12basic_stringIcS3_NS_9allocatorIc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00459628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c17c",
      "incomplete_value": true,
      "site": "00c1c17c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1bd54",
      "incomplete_value": true,
      "site": "00c1bd54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1c184",
      "incomplete_value": true,
      "site": "00c1c188",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1bd5c",
      "incomplete_value": true,
      "site": "00c1bd60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c1c1a8",
      "incomplete_value": true,
      "site": "00c1c1b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1bd80",
      "incomplete_value": true,
      "site": "00c1bd88",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:830:8"
              ]
            ]
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
      72,
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      72,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1bd44 ["INT_ADD", "register:40f0:8", ["const:c1bd44:8", "const:4:8"]]
+ 00c1c16c ["INT_ADD", "register:40f0:8", ["const:c1c16c:8", "const:4:8"]]
- 00c1bd4c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
+ 00c1c174 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
- 00c1bd7c ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c1bd80 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c1c1a4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c1c1a8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c1c088`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md) → [`00c1c4b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1c4b0.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwe

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c588",
      "incomplete_value": true,
      "site": "00c1c590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c160",
      "incomplete_value": true,
      "site": "00c1c168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1c85c",
      "incomplete_value": true,
      "site": "00c1c85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c434",
      "incomplete_value": true,
      "site": "00c1c434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1c598",
      "incomplete_value": true,
      "site": "00c1c59c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1c170",
      "incomplete_value": true,
      "site": "00c1c174",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      52,
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      52,
      "PARAM",
      [
        "storage",
        "002b17b0",
        null,
        "string"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      112,
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1c0bc ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00c1c4e4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00c1c0d8 ["INT_ADD", "register:40f0:8", ["const:c1c0d8:8", "const:4:8"]]
+ 00c1c500 ["INT_ADD", "register:40f0:8", ["const:c1c500:8", "const:4:8"]]
- 00c1c0e8 ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00c1c510 ["COPY", "tmp:0:8", ["const:ca0:8"]]
~~~


### [`00c1cbec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md) → [`00c1d014`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d014.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIw

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c118e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d064",
      "incomplete_value": true,
      "site": "00c1d064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1cc3c",
      "incomplete_value": true,
      "site": "00c1cc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c1d090",
      "incomplete_value": true,
      "site": "00c1d098",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1cc68",
      "incomplete_value": true,
      "site": "00c1cc70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:740:8"
              ]
            ]
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
      "definition_site": "00c1d08c",
      "incomplete_value": false,
      "site": "00c1d098",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c1cc64",
      "incomplete_value": false,
      "site": "00c1cc70",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      72,
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      72,
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      84,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1cc2c ["INT_ADD", "register:40f0:8", ["const:c1cc2c:8", "const:4:8"]]
+ 00c1d054 ["INT_ADD", "register:40f0:8", ["const:c1d054:8", "const:4:8"]]
- 00c1cc34 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:740:8"]]
+ 00c1d05c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b40:8"]]
- 00c1cc64 ["COPY", "register:4010:8", ["const:c35b90:8"]]
- 00c1cc68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c1d08c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
+ 00c1d090 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c1d274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) → [`00c1d69c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) FUN_00c1d69c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c1f71c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) · 呼出先 12件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c1fb44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fb44.md) · 呼出先 12件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

優先判定に残った影響 `branch_value` 13件, `call_argument_candidate` 57件, `store_condition` 26件, `store_destination` 43件, `store_value` 42件

アドレスに依存する影響 `call_argument_candidate` 25件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d6d8",
      "incomplete_value": false,
      "site": "00c1d6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d2b0",
      "incomplete_value": false,
      "site": "00c1d2b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "00c1d750",
      "incomplete_value": true,
      "site": "00c1d75c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d328",
      "incomplete_value": true,
      "site": "00c1d334",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d820",
      "incomplete_value": true,
      "site": "00c1d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d3f8",
      "incomplete_value": true,
      "site": "00c1d40c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
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
      60,
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      172,
      "READ",
      [
        "storage",
        "00c9b7f8",
        null,
        "pointer"
      ]
    ],
    [
      180,
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      60,
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      172,
      "READ",
      [
        "storage",
        "00c9bbf8",
        null,
        "pointer"
      ]
    ],
    [
      180,
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1d2a4 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c1d2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c1d2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c1d2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c1d6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
~~~


### [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) → [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) FUN_00c1f48c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c24ad4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md) [`00c24c0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md) · 呼出先 43件 [`0043bae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c1d274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c1f7a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md)
- 新版 呼出元 2件 [`00c24efc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24efc.md) [`00c25034`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md) · 呼出先 43件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c1d69c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c1fbd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f4bc",
      "incomplete_value": false,
      "site": "00c1f4bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f094",
      "incomplete_value": false,
      "site": "00c1f094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "00c1f668",
      "incomplete_value": true,
      "site": "00c1f668",
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
      "definition_site": "00c1f240",
      "incomplete_value": true,
      "site": "00c1f240",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f6a4",
      "incomplete_value": true,
      "site": "00c1f6a8",
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
      "definition_site": "00c1f27c",
      "incomplete_value": true,
      "site": "00c1f280",
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
      48,
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      48,
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      200,
      "READ",
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
- 00c1f088 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00c1f4b0 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00c1f114 ["INT_ADD", "register:40f0:8", ["const:c1f114:8", "const:4:8"]]
+ 00c1f53c ["INT_ADD", "register:40f0:8", ["const:c1f53c:8", "const:4:8"]]
- 00c1f11c ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00c1f544 ["COPY", "tmp:0:8", ["const:de8:8"]]
~~~


### [`00c1f71c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) → [`00c1fb44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fb44.md) _ZNSt6__ndk16locale7classicEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e4c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4c0.md) · 呼出先 3件 [`00c1d274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c57a50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c5e8c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8c0.md) · 呼出先 3件 [`00c1d69c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1fbac",
      "incomplete_value": true,
      "site": "00c1fbac",
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
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f784",
      "incomplete_value": true,
      "site": "00c1f784",
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
            "const:9e0:8"
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
      "definition_site": "00c1fb80",
      "incomplete_value": false,
      "site": "00c1fb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f758",
      "incomplete_value": false,
      "site": "00c1f75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
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
      "definition_site": "00c1fb98",
      "incomplete_value": false,
      "site": "00c1fb9c",
      "value": [
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
    },
    "old": {
      "definition_site": "00c1f770",
      "incomplete_value": false,
      "site": "00c1f774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      24,
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      24,
      "READ",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      36,
      "DATA",
      [
        "storage",
        "01127de0",
        null,
        "undefined8"
      ]
    ],
    [
      60,
      "PARAM",
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
- 00c1f730 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00c1fb58 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00c1f740 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00c1fb68 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 00c1f758 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00c1fb80 ["COPY", "tmp:0:8", ["const:de8:8"]]
~~~


### [`00c1f7a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) → [`00c1fbd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) FUN_00c1fbd0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fbf4",
      "incomplete_value": true,
      "site": "00c1fbf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f7cc",
      "incomplete_value": true,
      "site": "00c1f7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fc00",
      "incomplete_value": true,
      "site": "00c1fc04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1f7d8",
      "incomplete_value": true,
      "site": "00c1f7dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c1fc28",
      "incomplete_value": true,
      "site": "00c1fc2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f800",
      "incomplete_value": true,
      "site": "00c1f804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
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
        "00c9b378",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1f7c0 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c1fbe8 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c1f7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f78:8"]]
+ 00c1fbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00c1f7e8 ["COPY", "register:4000:8", ["const:c9a000:8"]]
+ 00c1fc10 ["COPY", "register:4000:8", ["const:c9b000:8"]]
~~~


### [`00c1f8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) → [`00c1fcfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) FUN_00c1fcfc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fd20",
      "incomplete_value": true,
      "site": "00c1fd24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f8f8",
      "incomplete_value": true,
      "site": "00c1f8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fd2c",
      "incomplete_value": true,
      "site": "00c1fd30",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1f904",
      "incomplete_value": true,
      "site": "00c1f908",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c1fd54",
      "incomplete_value": true,
      "site": "00c1fd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f92c",
      "incomplete_value": true,
      "site": "00c1f930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b808",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
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
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1f8f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:808:8"]]
+ 00c1fd20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c08:8"]]
- 00c1f920 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1fd48 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1f92c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:808:8"]]
+ 00c1fd54 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c08:8"]]
~~~


### [`00c1fa00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) → [`00c1fe28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) FUN_00c1fe28

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fe4c",
      "incomplete_value": true,
      "site": "00c1fe50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fa24",
      "incomplete_value": true,
      "site": "00c1fa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fe58",
      "incomplete_value": true,
      "site": "00c1fe5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1fa30",
      "incomplete_value": true,
      "site": "00c1fa34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c1fe80",
      "incomplete_value": true,
      "site": "00c1fe84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fa58",
      "incomplete_value": true,
      "site": "00c1fa5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
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
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1fa24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00c1fe4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
- 00c1fa4c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1fe74 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fa58 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:830:8"]]
+ 00c1fe80 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c30:8"]]
~~~


### [`00c1fb2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md) → [`00c1ff54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md) FUN_00c1ff54

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1ff78",
      "incomplete_value": true,
      "site": "00c1ff7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fb50",
      "incomplete_value": true,
      "site": "00c1fb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1ff84",
      "incomplete_value": true,
      "site": "00c1ff88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1fb5c",
      "incomplete_value": true,
      "site": "00c1fb60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c1ffac",
      "incomplete_value": true,
      "site": "00c1ffb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fb84",
      "incomplete_value": true,
      "site": "00c1fb88",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:740:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
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
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1fb50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00c1ff78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
- 00c1fb78 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1ffa0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fb84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:740:8"]]
+ 00c1ffac ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b40:8"]]
~~~


### [`00c1fc58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md) → [`00c20080`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20080.md) FUN_00c20080

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c200a4",
      "incomplete_value": true,
      "site": "00c200a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fc7c",
      "incomplete_value": true,
      "site": "00c1fc80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c200b0",
      "incomplete_value": true,
      "site": "00c200b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1fc88",
      "incomplete_value": true,
      "site": "00c1fc8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c200d8",
      "incomplete_value": true,
      "site": "00c200dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fcb0",
      "incomplete_value": true,
      "site": "00c1fcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
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
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1fc7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
+ 00c200a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00c1fca4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c200cc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fcb0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:4b8:8"]]
+ 00c200d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8b8:8"]]
~~~


### [`00c1fd84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md) → [`00c201ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c201ac.md) FUN_00c201ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c201d0",
      "incomplete_value": true,
      "site": "00c201d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fda8",
      "incomplete_value": true,
      "site": "00c1fdac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c201dc",
      "incomplete_value": true,
      "site": "00c201e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1fdb4",
      "incomplete_value": true,
      "site": "00c1fdb8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20204",
      "incomplete_value": true,
      "site": "00c20208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fddc",
      "incomplete_value": true,
      "site": "00c1fde0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
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
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1fda8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
+ 00c201d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
- 00c1fdd0 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c201f8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fddc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7a8:8"]]
+ 00c20204 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:ba8:8"]]
~~~


### [`00c1feb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md) → [`00c202d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c202d8.md) FUN_00c202d8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c202fc",
      "incomplete_value": true,
      "site": "00c20300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fed4",
      "incomplete_value": true,
      "site": "00c1fed8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20308",
      "incomplete_value": true,
      "site": "00c2030c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c1fee0",
      "incomplete_value": true,
      "site": "00c1fee4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20330",
      "incomplete_value": true,
      "site": "00c20334",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1ff08",
      "incomplete_value": true,
      "site": "00c1ff0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b828",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
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
        "00c9bc28",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c1fed4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00c202fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
- 00c1fefc ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20324 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1ff08 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:828:8"]]
+ 00c20330 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c28:8"]]
~~~


### [`00c1ffdc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md) → [`00c20404`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20404.md) FUN_00c20404

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20428",
      "incomplete_value": true,
      "site": "00c2042c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20000",
      "incomplete_value": true,
      "site": "00c20004",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20434",
      "incomplete_value": true,
      "site": "00c20438",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c2000c",
      "incomplete_value": true,
      "site": "00c20010",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2045c",
      "incomplete_value": true,
      "site": "00c20460",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00c20034",
      "incomplete_value": true,
      "site": "00c20038",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:838:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
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
        "00c9bc38",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20000 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
+ 00c20428 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
- 00c20028 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20450 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20034 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:838:8"]]
+ 00c2045c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c38:8"]]
~~~


### [`00c20108`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md) → [`00c20530`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20530.md) FUN_00c20530

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20554",
      "incomplete_value": true,
      "site": "00c20558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2012c",
      "incomplete_value": true,
      "site": "00c20130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20560",
      "incomplete_value": true,
      "site": "00c20564",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c20138",
      "incomplete_value": true,
      "site": "00c2013c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20588",
      "incomplete_value": true,
      "site": "00c2058c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20160",
      "incomplete_value": true,
      "site": "00c20164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
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
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c2012c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:848:8"]]
+ 00c20554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
- 00c20154 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2057c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20160 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:848:8"]]
+ 00c20588 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c48:8"]]
~~~


### [`00c20234`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md) → [`00c2065c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c2065c.md) FUN_00c2065c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20680",
      "incomplete_value": true,
      "site": "00c20684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20258",
      "incomplete_value": true,
      "site": "00c2025c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2068c",
      "incomplete_value": true,
      "site": "00c20690",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c20264",
      "incomplete_value": true,
      "site": "00c20268",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c206b4",
      "incomplete_value": true,
      "site": "00c206b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2028c",
      "incomplete_value": true,
      "site": "00c20290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
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
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20258 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
+ 00c20680 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
- 00c20280 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c206a8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c2028c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:858:8"]]
+ 00c206b4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c58:8"]]
~~~


### [`00c20360`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md) → [`00c20788`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20788.md) FUN_00c20788

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c207ac",
      "incomplete_value": true,
      "site": "00c207b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20384",
      "incomplete_value": true,
      "site": "00c20388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c207b8",
      "incomplete_value": true,
      "site": "00c207bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c20390",
      "incomplete_value": true,
      "site": "00c20394",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c207e0",
      "incomplete_value": true,
      "site": "00c207e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c203b8",
      "incomplete_value": true,
      "site": "00c203bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
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
        "00c9bbb8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00c207ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
- 00c203ac ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c207d4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c203b8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7b8:8"]]
+ 00c207e0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bb8:8"]]
~~~


### [`00c2048c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md) → [`00c208b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c208b4.md) FUN_00c208b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c208d8",
      "incomplete_value": true,
      "site": "00c208dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c204b0",
      "incomplete_value": true,
      "site": "00c204b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c208e4",
      "incomplete_value": true,
      "site": "00c208e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c204bc",
      "incomplete_value": true,
      "site": "00c204c0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c2090c",
      "incomplete_value": true,
      "site": "00c20910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c204e4",
      "incomplete_value": true,
      "site": "00c204e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
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
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c204b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
+ 00c208d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bc8:8"]]
- 00c204d8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20900 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c204e4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7c8:8"]]
+ 00c2090c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bc8:8"]]
~~~


### [`00c205b8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md) → [`00c209e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c209e0.md) FUN_00c209e0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20a04",
      "incomplete_value": true,
      "site": "00c20a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c205dc",
      "incomplete_value": true,
      "site": "00c205e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20a10",
      "incomplete_value": true,
      "site": "00c20a14",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c205e8",
      "incomplete_value": true,
      "site": "00c205ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20a38",
      "incomplete_value": true,
      "site": "00c20a3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20610",
      "incomplete_value": true,
      "site": "00c20614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7e0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
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
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c205dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00c20a04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
- 00c20604 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20a2c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20610 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7e0:8"]]
+ 00c20a38 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:be0:8"]]
~~~


### [`00c206e4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md) → [`00c20b0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20b0c.md) FUN_00c20b0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4d0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20b3c",
      "incomplete_value": true,
      "site": "00c20b3c",
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
      "definition_site": "00c20714",
      "incomplete_value": true,
      "site": "00c20714",
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
      32,
      "READ",
      [
        "storage",
        "00c9b998",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95000",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9bd98",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95400",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
+ 00c20b2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00c20740 ["INT_ADD", "register:40f0:8", ["const:c20740:8", "const:4:8"]]
+ 00c20b68 ["INT_ADD", "register:40f0:8", ["const:c20b68:8", "const:4:8"]]
~~~


### [`00c207c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md) → [`00c20bf0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20bf0.md) FUN_00c20bf0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20c14",
      "incomplete_value": true,
      "site": "00c20c18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c207ec",
      "incomplete_value": true,
      "site": "00c207f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20c20",
      "incomplete_value": true,
      "site": "00c20c24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c207f8",
      "incomplete_value": true,
      "site": "00c207fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20c48",
      "incomplete_value": true,
      "site": "00c20c4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20820",
      "incomplete_value": true,
      "site": "00c20824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
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
        "00c9bbd8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c207ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
+ 00c20c14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd8:8"]]
- 00c20814 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20c3c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20820 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7d8:8"]]
+ 00c20c48 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bd8:8"]]
~~~


### [`00c208f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md) → [`00c20d1c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20d1c.md) FUN_00c20d1c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8e0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20d4c",
      "incomplete_value": true,
      "site": "00c20d4c",
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
      "definition_site": "00c20924",
      "incomplete_value": true,
      "site": "00c20924",
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
      32,
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95088",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9bda0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95488",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
+ 00c20d3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00c20950 ["INT_ADD", "register:40f0:8", ["const:c20950:8", "const:4:8"]]
+ 00c20d78 ["INT_ADD", "register:40f0:8", ["const:c20d78:8", "const:4:8"]]
~~~


### [`00c209d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md) → [`00c20e00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20e00.md) FUN_00c20e00

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20e24",
      "incomplete_value": true,
      "site": "00c20e28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c209fc",
      "incomplete_value": true,
      "site": "00c20a00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
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
      "definition_site": "00c20e58",
      "incomplete_value": true,
      "site": "00c20e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20a30",
      "incomplete_value": true,
      "site": "00c20a34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
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
      "definition_site": "00c20e4c",
      "incomplete_value": false,
      "site": "00c20e5c",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c20a24",
      "incomplete_value": false,
      "site": "00c20a34",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      36,
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
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
        "00c9bbf0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c209fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
+ 00c20e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
- 00c20a24 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20e4c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20a30 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7f0:8"]]
+ 00c20e58 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:bf0:8"]]
~~~


### [`00c20b04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md) → [`00c20f2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20f2c.md) FUN_00c20f2c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20f5c",
      "incomplete_value": true,
      "site": "00c20f5c",
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
      "definition_site": "00c20b34",
      "incomplete_value": true,
      "site": "00c20b34",
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
      32,
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95110",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95510",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
+ 00c20f4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
- 00c20b60 ["INT_ADD", "register:40f0:8", ["const:c20b60:8", "const:4:8"]]
+ 00c20f88 ["INT_ADD", "register:40f0:8", ["const:c20f88:8", "const:4:8"]]
~~~


### [`00c20be8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md) → [`00c21010`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21010.md) FUN_00c21010

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21034",
      "incomplete_value": true,
      "site": "00c21038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20c0c",
      "incomplete_value": true,
      "site": "00c20c10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21040",
      "incomplete_value": true,
      "site": "00c21044",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c20c18",
      "incomplete_value": true,
      "site": "00c20c1c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c21068",
      "incomplete_value": true,
      "site": "00c2106c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20c40",
      "incomplete_value": true,
      "site": "00c20c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
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
        "00c9bbe8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20c0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00c21034 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00c20c34 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2105c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20c40 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:7e8:8"]]
+ 00c21068 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:be8:8"]]
~~~


### [`00c20d14`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md) → [`00c2113c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c2113c.md) FUN_00c2113c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e500.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e900.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2116c",
      "incomplete_value": true,
      "site": "00c2116c",
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
      "definition_site": "00c20d44",
      "incomplete_value": true,
      "site": "00c20d44",
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
      32,
      "READ",
      [
        "storage",
        "00c9b9b0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95198",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9bdb0",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c95598",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
+ 00c2115c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
- 00c20d70 ["INT_ADD", "register:40f0:8", ["const:c20d70:8", "const:4:8"]]
+ 00c21198 ["INT_ADD", "register:40f0:8", ["const:c21198:8", "const:4:8"]]
~~~


### [`00c20df8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md) → [`00c21220`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21220.md) FUN_00c21220

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21244",
      "incomplete_value": true,
      "site": "00c21248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20e1c",
      "incomplete_value": true,
      "site": "00c20e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21250",
      "incomplete_value": true,
      "site": "00c21254",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c20e28",
      "incomplete_value": true,
      "site": "00c20e2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c21278",
      "incomplete_value": true,
      "site": "00c2127c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20e50",
      "incomplete_value": true,
      "site": "00c20e54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
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
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20e10 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c21238 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c20e1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef0:8"]]
+ 00c21244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00c20e38 ["COPY", "register:4000:8", ["const:c9a000:8"]]
+ 00c21260 ["COPY", "register:4000:8", ["const:c9b000:8"]]
~~~


### [`00c20f24`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md) → [`00c2134c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c2134c.md) FUN_00c2134c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c213a4",
      "incomplete_value": true,
      "site": "00c213a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20f7c",
      "incomplete_value": true,
      "site": "00c20f80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
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
      "definition_site": "00c21398",
      "incomplete_value": false,
      "site": "00c213a8",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c20f70",
      "incomplete_value": false,
      "site": "00c20f80",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      36,
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
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
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c20f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00c21370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00c20f70 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c21398 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20f7c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8f0:8"]]
+ 00c213a4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cf0:8"]]
~~~


### [`00c21050`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md) → [`00c21478`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21478.md) FUN_00c21478

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2149c",
      "incomplete_value": true,
      "site": "00c214a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21074",
      "incomplete_value": true,
      "site": "00c21078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c214a8",
      "incomplete_value": true,
      "site": "00c214ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c21080",
      "incomplete_value": true,
      "site": "00c21084",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c214d0",
      "incomplete_value": true,
      "site": "00c214d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c210a8",
      "incomplete_value": true,
      "site": "00c210ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
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
        "00c9b2f8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c21068 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c21490 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c21074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef8:8"]]
+ 00c2149c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
- 00c21090 ["COPY", "register:4000:8", ["const:c9a000:8"]]
+ 00c214b8 ["COPY", "register:4000:8", ["const:c9b000:8"]]
~~~


### [`00c2117c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md) → [`00c215a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c215a4.md) FUN_00c215a4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c215c8",
      "incomplete_value": true,
      "site": "00c215cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c211a0",
      "incomplete_value": true,
      "site": "00c211a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c215d4",
      "incomplete_value": true,
      "site": "00c215d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c211ac",
      "incomplete_value": true,
      "site": "00c211b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c215fc",
      "incomplete_value": true,
      "site": "00c21600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c211d4",
      "incomplete_value": true,
      "site": "00c211d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
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
        "00c9bd10",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c211a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00c215c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
- 00c211c8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c215f0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c211d4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:910:8"]]
+ 00c215fc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d10:8"]]
~~~


### [`00c212a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md) → [`00c216d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c216d0.md) FUN_00c216d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c216f4",
      "incomplete_value": true,
      "site": "00c216f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c212cc",
      "incomplete_value": true,
      "site": "00c212d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
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
      "definition_site": "00c21728",
      "incomplete_value": true,
      "site": "00c2172c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21300",
      "incomplete_value": true,
      "site": "00c21304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
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
      "definition_site": "00c2171c",
      "incomplete_value": false,
      "site": "00c2172c",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c212f4",
      "incomplete_value": false,
      "site": "00c21304",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      36,
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
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
        "00c9bd20",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c212cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00c216f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
- 00c212f4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2171c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c21300 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:920:8"]]
+ 00c21728 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d20:8"]]
~~~


### [`00c213d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md) → [`00c217fc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c217fc.md) FUN_00c217fc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21820",
      "incomplete_value": true,
      "site": "00c21824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c213f8",
      "incomplete_value": true,
      "site": "00c213fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2182c",
      "incomplete_value": true,
      "site": "00c21830",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
      "definition_site": "00c21404",
      "incomplete_value": true,
      "site": "00c21408",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c21854",
      "incomplete_value": true,
      "site": "00c21858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2142c",
      "incomplete_value": true,
      "site": "00c21430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
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
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
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
        "00c9bd30",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      44,
      "READ",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c213f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
+ 00c21820 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
- 00c21420 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c21848 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c2142c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:930:8"]]
+ 00c21854 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d30:8"]]
~~~


### [`00c21500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) → [`00c21928`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) FUN_00c21928

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c24c78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md) [`00c24dc8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md) · 呼出先 40件 [`00c1d138`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c1f7a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) [`00c1fb2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md)
- 新版 呼出元 2件 [`00c250a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c250a0.md) [`00c251f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md) · 呼出先 40件 [`00c1d560`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) [`00c1fbd0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) [`00c1ff54`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 13件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2195c",
      "incomplete_value": false,
      "site": "00c2195c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21534",
      "incomplete_value": false,
      "site": "00c21534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "00c21aec",
      "incomplete_value": true,
      "site": "00c21aec",
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
      "definition_site": "00c216c4",
      "incomplete_value": true,
      "site": "00c216c4",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21b24",
      "incomplete_value": true,
      "site": "00c21b28",
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
      "definition_site": "00c216fc",
      "incomplete_value": true,
      "site": "00c21700",
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
      52,
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      444,
      "READ",
      [
        "storage",
        "00c9b938",
        null,
        "pointer"
      ]
    ],
    [
      452,
      "DATA",
      [
        "storage",
        "00c955d0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      52,
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      444,
      "READ",
      [
        "storage",
        "00c9bd38",
        null,
        "pointer"
      ]
    ],
    [
      452,
      "DATA",
      [
        "storage",
        "00c959d0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c21528 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00c21950 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00c215a8 ["INT_ADD", "register:40f0:8", ["const:c215a8:8", "const:4:8"]]
+ 00c219d0 ["INT_ADD", "register:40f0:8", ["const:c219d0:8", "const:4:8"]]
- 00c215c4 ["INT_ADD", "register:40f0:8", ["const:c215c4:8", "const:4:8"]]
+ 00c219ec ["INT_ADD", "register:40f0:8", ["const:c219ec:8", "const:4:8"]]
~~~


### [`00c21b50`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) → [`00c21f78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) FUN_00c21f78

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c24e40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md) · 呼出先 33件 [`00c1d138`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c21eb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md) [`00c21ff8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md) [`00c2213c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md) [`00c22280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md)
- 新版 呼出元 1件 [`00c25268`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md) · 呼出先 33件 [`00c1d560`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) [`00c222dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c222dc.md) [`00c22420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22420.md) [`00c22564`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22564.md) [`00c226a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c226a8.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21fa8",
      "incomplete_value": false,
      "site": "00c21fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21b80",
      "incomplete_value": false,
      "site": "00c21b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      48,
      "DATA",
      [
        "storage",
        "00c932c0",
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
        "00c936c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c21b74 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00c21f9c ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00c21bf4 ["INT_ADD", "register:40f0:8", ["const:c21bf4:8", "const:4:8"]]
+ 00c2201c ["INT_ADD", "register:40f0:8", ["const:c2201c:8", "const:4:8"]]
- 00c21c10 ["INT_ADD", "register:40f0:8", ["const:c21c10:8", "const:4:8"]]
+ 00c22038 ["INT_ADD", "register:40f0:8", ["const:c22038:8", "const:4:8"]]
~~~


