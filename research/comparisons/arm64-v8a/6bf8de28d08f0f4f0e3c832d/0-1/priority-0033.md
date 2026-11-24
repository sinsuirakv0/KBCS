# v16.0.0 → v16.0.1 · 最優先の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-748f3792e5d7e9203c733405496500f8"></a>

### [`006e29b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md) → [`006e29f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e29f0.md) FUN_006e29f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006e2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md) · 呼出先 11件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`0048795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`006e2c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e2c74.md) · 呼出先 11件 [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048799c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048799c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2a2c",
      "incomplete_value": false,
      "site": "006e2a38",
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
      "definition_site": "006e29ec",
      "incomplete_value": false,
      "site": "006e29f8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2a30",
      "incomplete_value": true,
      "site": "006e2a44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:371:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e29f0",
      "incomplete_value": true,
      "site": "006e2a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2a4:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006e2b44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e2a30",
      "READ",
      [
        "storage",
        "002a22a4",
        null,
        "string"
      ]
    ],
    [
      "006e2a38",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006e2b34",
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
      "006e2a30",
      "READ",
      [
        "storage",
        "002a2371",
        null,
        "string"
      ]
    ],
    [
      "006e2a38",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "006e2b74",
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


#### 変更候補の命令位置

- 旧版 [`006e2a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md#insn-006e2a38) · [`006e2b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md#insn-006e2b44) · [`006e2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md#insn-006e2b48)
- 新版 [`006e2a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e29f0.md#insn-006e2a78)

~~~diff
- 006e2a38 ["INT_ADD", "register:40f0:8", ["const:6e2a38:8", "const:4:8"]]
- 006e2a38 ["CALL", null, ["callee:0048792c:8"]]
+ 006e2a78 ["INT_ADD", "register:40f0:8", ["const:6e2a78:8", "const:4:8"]]
+ 006e2a78 ["CALL", null, ["callee:0048792c:8"]]
- 006e2a38 bytes ad93f697
+ 006e2a78 bytes ad93f697
- 006e2b44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006e2b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006e2b44 bytes e81300f9
- 006e2b48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 006e2b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006e2b48 bytes e93700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9959c97d1dc53589b42d32a25bb71b"></a>

### [`006e2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md) → [`006e2c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e2c74.md) FUN_006e2c74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 22件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.37% / 新版 91.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2d4c",
      "incomplete_value": true,
      "site": "006e2d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
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
      "definition_site": "006e2d0c",
      "incomplete_value": true,
      "site": "006e2d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3a7:8"
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
      "definition_site": "006e2e5c",
      "incomplete_value": true,
      "site": "006e2e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f85:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e2e1c",
      "incomplete_value": true,
      "site": "006e2e1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006e309c",
      "incomplete_value": false,
      "site": "006e309c",
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
      "definition_site": "006e305c",
      "incomplete_value": false,
      "site": "006e305c",
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
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e2cc8",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006e2d3c",
      "READ",
      [
        "storage",
        "002c13a7",
        null,
        "string"
      ]
    ],
    [
      "006e2d90",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e2cc8",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "006e2d3c",
      "READ",
      [
        "storage",
        "002c13e7",
        null,
        "string"
      ]
    ],
    [
      "006e2d90",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e2d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md#insn-006e2d64) · [`006e2da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md#insn-006e2da4) · [`006e3020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md#insn-006e3020)
- 新版 [`006e2da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e2c74.md#insn-006e2da4) · [`006e2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e2c74.md#insn-006e2de4) · [`006e3060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e2/006e2c74.md#insn-006e3060)

~~~diff
- 006e2d64 ["INT_ADD", "register:40f0:8", ["const:6e2d64:8", "const:4:8"]]
- 006e2d64 ["CALL", null, ["callee:0047e60c:8"]]
+ 006e2da4 ["INT_ADD", "register:40f0:8", ["const:6e2da4:8", "const:4:8"]]
+ 006e2da4 ["CALL", null, ["callee:0047e60c:8"]]
- 006e2d64 bytes 1a6ef697
+ 006e2da4 bytes 1a6ef697
- 006e2da4 ["INT_ADD", "register:40f0:8", ["const:6e2da4:8", "const:4:8"]]
- 006e2da4 ["CALL", null, ["callee:00c57e80:8"]]
+ 006e2de4 ["INT_ADD", "register:40f0:8", ["const:6e2de4:8", "const:4:8"]]
+ 006e2de4 ["CALL", null, ["callee:00c57e80:8"]]
- 006e2da4 bytes 37d31594
+ 006e2de4 bytes 27d41594
- 006e3020 ["INT_ADD", "register:40f0:8", ["const:6e3020:8", "const:4:8"]]
- 006e3020 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006e3060 ["INT_ADD", "register:40f0:8", ["const:6e3060:8", "const:4:8"]]
+ 006e3060 ["CALL", null, ["callee:00c57eb0:8"]]
- 006e3020 bytes a4d21594
+ 006e3060 bytes 94d31594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d686a3b293fec77873ca76682dc415"></a>

### [`006e3218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3218.md) → [`006e3258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3258.md) FUN_006e3258

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 5件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e32b8",
      "incomplete_value": true,
      "site": "006e32cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e3278",
      "incomplete_value": true,
      "site": "006e328c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:f50:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e3274",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e3234",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e3274",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006e32b8",
      "READ",
      [
        "storage",
        "002c3f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e3274",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006e32b8",
      "READ",
      [
        "storage",
        "002c3f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e3234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3218.md#insn-006e3234) · [`006e324c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3218.md#insn-006e324c) · [`006e3230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e3218.md#insn-006e3230)
- 新版 [`006e3274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3258.md#insn-006e3274) · [`006e328c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3258.md#insn-006e328c) · [`006e3270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3258.md#insn-006e3270)

~~~diff
- 006e3234 ["INT_ADD", "register:40f0:8", ["const:6e3234:8", "const:4:8"]]
- 006e3234 ["CALL", null, ["ram:46c984:8"]]
+ 006e3274 ["INT_ADD", "register:40f0:8", ["const:6e3274:8", "const:4:8"]]
+ 006e3274 ["CALL", null, ["ram:46c9c4:8"]]
- 006e3234 bytes d425f697
+ 006e3274 bytes d425f697
- 006e324c ["INT_ADD", "register:40f0:8", ["const:6e324c:8", "const:4:8"]]
- 006e324c ["CALL", null, ["callee:0046d7b0:8"]]
+ 006e328c ["INT_ADD", "register:40f0:8", ["const:6e328c:8", "const:4:8"]]
+ 006e328c ["CALL", null, ["callee:0046d7b0:8"]]
- 006e324c bytes 4929f697
+ 006e328c bytes 4929f697
- 006e3230 ["INT_ADD", "register:40f0:8", ["const:6e3230:8", "const:4:8"]]
- 006e3230 ["CALL", null, ["callee:008514f8:8"]]
+ 006e3270 ["INT_ADD", "register:40f0:8", ["const:6e3270:8", "const:4:8"]]
+ 006e3270 ["CALL", null, ["callee:008514f8:8"]]
- 006e3230 bytes a2b80594
+ 006e3270 bytes a2b80594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10855a21903e2449b7965fd02ded21d2"></a>

### [`006e32e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e32e0.md) → [`006e3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3320.md) FUN_006e3320

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 11件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 11件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.84% / 新版 97.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e3858",
      "incomplete_value": true,
      "site": "006e3860",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e3818",
      "incomplete_value": true,
      "site": "006e3820",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
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
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e3410",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e33d0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006e351c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e34dc",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e3378",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "byte[23]"
      ]
    ],
    [
      "006e338c",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "qword"
      ]
    ],
    [
      "006e33a0",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "byte[23]"
      ]
    ]
  ],
  "added": [
    [
      "006e3378",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "dword"
      ]
    ],
    [
      "006e338c",
      "DATA",
      [
        "storage",
        "00431680",
        null,
        "uleb128"
      ]
    ],
    [
      "006e33a0",
      "DATA",
      [
        "storage",
        "004316b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e3390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e32e0.md#insn-006e3390) · [`006e33d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e32e0.md#insn-006e33d0) · [`006e34dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e3/006e32e0.md#insn-006e34dc)
- 新版 [`006e33d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3320.md#insn-006e33d0) · [`006e3410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3320.md#insn-006e3410) · [`006e351c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3320.md#insn-006e351c)

~~~diff
- 006e3390 ["INT_ADD", "register:40f0:8", ["const:6e3390:8", "const:4:8"]]
- 006e3390 ["CALL", null, ["callee:008514f8:8"]]
+ 006e33d0 ["INT_ADD", "register:40f0:8", ["const:6e33d0:8", "const:4:8"]]
+ 006e33d0 ["CALL", null, ["callee:008514f8:8"]]
- 006e3390 bytes 4ab80594
+ 006e33d0 bytes 4ab80594
- 006e33d0 ["INT_ADD", "register:40f0:8", ["const:6e33d0:8", "const:4:8"]]
- 006e33d0 ["CALL", null, ["ram:47acb4:8"]]
+ 006e3410 ["INT_ADD", "register:40f0:8", ["const:6e3410:8", "const:4:8"]]
+ 006e3410 ["CALL", null, ["ram:47acf4:8"]]
- 006e33d0 bytes 395ef697
+ 006e3410 bytes 395ef697
- 006e34dc ["INT_ADD", "register:40f0:8", ["const:6e34dc:8", "const:4:8"]]
- 006e34dc ["CALL", null, ["ram:47acb4:8"]]
+ 006e351c ["INT_ADD", "register:40f0:8", ["const:6e351c:8", "const:4:8"]]
+ 006e351c ["CALL", null, ["ram:47acf4:8"]]
- 006e34dc bytes f65df697
+ 006e351c bytes f65df697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f846b4b2132fbf23ba5be285aff59a4"></a>

### [`006e42d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md) → [`006e4314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4314.md) FUN_006e4314

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00444b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444b98.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e4388",
      "incomplete_value": true,
      "site": "006e4388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4348",
      "incomplete_value": true,
      "site": "006e4348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:194:8"
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
      "definition_site": "006e4380",
      "incomplete_value": true,
      "site": "006e438c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006e4340",
      "incomplete_value": true,
      "site": "006e434c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e437c",
      "READ",
      [
        "storage",
        "002c0194",
        null,
        "string"
      ]
    ],
    [
      "006e4380",
      "READ",
      [
        "storage",
        "002c019b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006e437c",
      "READ",
      [
        "storage",
        "002c01d4",
        null,
        "string"
      ]
    ],
    [
      "006e4380",
      "READ",
      [
        "storage",
        "002c01db",
        null,
        "string"
      ]
    ],
    [
      "006e43a8",
      "DATA",
      [
        "storage",
        "00444ba8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e4308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md#insn-006e4308) · [`006e42f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md#insn-006e42f0) · [`006e4320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e42d4.md#insn-006e4320)
- 新版 [`006e4348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4314.md#insn-006e4348) · [`006e4330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4314.md#insn-006e4330) · [`006e4360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4314.md#insn-006e4360)

~~~diff
- 006e4308 ["INT_ADD", "register:40f0:8", ["const:6e4308:8", "const:4:8"]]
- 006e4308 ["CALL", null, ["callee:008514f8:8"]]
+ 006e4348 ["INT_ADD", "register:40f0:8", ["const:6e4348:8", "const:4:8"]]
+ 006e4348 ["CALL", null, ["callee:008514f8:8"]]
- 006e4308 bytes 6cb40594
+ 006e4348 bytes 6cb40594
- 006e42f0 ["INT_ADD", "register:40f0:8", ["const:6e42f0:8", "const:4:8"]]
- 006e42f0 ["CALL", null, ["callee:008514f8:8"]]
+ 006e4330 ["INT_ADD", "register:40f0:8", ["const:6e4330:8", "const:4:8"]]
+ 006e4330 ["CALL", null, ["callee:008514f8:8"]]
- 006e42f0 bytes 72b40594
+ 006e4330 bytes 72b40594
- 006e4320 ["INT_ADD", "register:40f0:8", ["const:6e4320:8", "const:4:8"]]
- 006e4320 ["CALL", null, ["callee:008514f8:8"]]
+ 006e4360 ["INT_ADD", "register:40f0:8", ["const:6e4360:8", "const:4:8"]]
+ 006e4360 ["CALL", null, ["callee:008514f8:8"]]
- 006e4320 bytes 66b40594
+ 006e4360 bytes 66b40594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-509b56c7e3d91bab7678b50256d3a2c0"></a>

### [`006e44a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md) → [`006e44e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md) FUN_006e44e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) · 呼出先 16件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 2件 [`006e4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4d6c.md) [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) · 呼出先 16件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.70% / 新版 83.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 2件, `store_destination` 14件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e454c",
      "incomplete_value": true,
      "site": "006e4558",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "006e450c",
      "incomplete_value": true,
      "site": "006e4518",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
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
      "definition_site": "006e45c4",
      "incomplete_value": true,
      "site": "006e45d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e4584",
      "incomplete_value": true,
      "site": "006e4590",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f60:8"
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
      "definition_site": "006e45d4",
      "incomplete_value": true,
      "site": "006e45d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006e4594",
      "incomplete_value": true,
      "site": "006e4594",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 22,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e454c",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ],
    [
      "006e4584",
      "DATA",
      [
        "storage",
        "00430ee8",
        null,
        "byte[23]"
      ]
    ],
    [
      "006e45a0",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "006e454c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "006e4584",
      "DATA",
      [
        "storage",
        "00430ee8",
        null,
        "dword"
      ]
    ],
    [
      "006e45a0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md#insn-006e456c) · [`006e45ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md#insn-006e45ac) · [`006e461c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e44a0.md#insn-006e461c)
- 新版 [`006e45ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md#insn-006e45ac) · [`006e45ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md#insn-006e45ec) · [`006e465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e44e0.md#insn-006e465c)

~~~diff
- 006e456c ["INT_ADD", "register:40f0:8", ["const:6e456c:8", "const:4:8"]]
- 006e456c ["CALL", null, ["callee:00c57e90:8"]]
+ 006e45ac ["INT_ADD", "register:40f0:8", ["const:6e45ac:8", "const:4:8"]]
+ 006e45ac ["CALL", null, ["callee:00c57e90:8"]]
- 006e456c bytes 49cd1594
+ 006e45ac bytes 39ce1594
- 006e45ac ["INT_ADD", "register:40f0:8", ["const:6e45ac:8", "const:4:8"]]
- 006e45ac ["CALL", null, ["ram:6e4a84:8"]]
+ 006e45ec ["INT_ADD", "register:40f0:8", ["const:6e45ec:8", "const:4:8"]]
+ 006e45ec ["CALL", null, ["ram:6e4ac4:8"]]
- 006e45ac bytes 36010094
+ 006e45ec bytes 36010094
- 006e461c ["INT_ADD", "register:40f0:8", ["const:6e461c:8", "const:4:8"]]
- 006e461c ["CALL", null, ["callee:0047e60c:8"]]
+ 006e465c ["INT_ADD", "register:40f0:8", ["const:6e465c:8", "const:4:8"]]
+ 006e465c ["CALL", null, ["callee:0047e60c:8"]]
- 006e461c bytes ec67f697
+ 006e465c bytes ec67f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55e6b40285ce792e56573d422ea07f8d"></a>

### [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) → [`006e53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md) FUN_006e53d4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006eec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006eec6c.md) [`006fe5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md)
- 新版 呼出元 4件 [`006e4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4d6c.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006eecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006eecac.md) [`006fe604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe604.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e5440",
      "value": [
        "leaf",
        "ram:9d0320:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e5400",
      "value": [
        "leaf",
        "ram:9d0184:8"
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
      "site": "006e5544",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006e5504",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e5440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d0184"
      ]
    ],
    [
      "006e5498",
      "DATA",
      [
        "storage",
        "00436d8c",
        null,
        "byte[63]"
      ]
    ],
    [
      "006e5544",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006e5440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d0320"
      ]
    ],
    [
      "006e5498",
      "DATA",
      [
        "storage",
        "00436d8c",
        null,
        "dword"
      ]
    ],
    [
      "006e5544",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006e5400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md#insn-006e5400) · [`006e5504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md#insn-006e5504) · [`006e53cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md#insn-006e53cc)
- 新版 [`006e5440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md#insn-006e5440) · [`006e5544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md#insn-006e5544) · [`006e540c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md#insn-006e540c)

~~~diff
- 006e5400 ["INT_ADD", "register:40f0:8", ["const:6e5400:8", "const:4:8"]]
- 006e5400 ["CALL", null, ["ram:9d0184:8"]]
+ 006e5440 ["INT_ADD", "register:40f0:8", ["const:6e5440:8", "const:4:8"]]
+ 006e5440 ["CALL", null, ["ram:9d0320:8"]]
- 006e5400 bytes 61ab0b94
+ 006e5440 bytes b8ab0b94
- 006e5504 ["INT_ADD", "register:40f0:8", ["const:6e5504:8", "const:4:8"]]
- 006e5504 ["CALL", null, ["ram:6e4a84:8"]]
+ 006e5544 ["INT_ADD", "register:40f0:8", ["const:6e5544:8", "const:4:8"]]
+ 006e5544 ["CALL", null, ["ram:6e4ac4:8"]]
- 006e5504 bytes 60fdff97
+ 006e5544 bytes 60fdff97
- 006e53cc ["INT_ADD", "register:40f0:8", ["const:6e53cc:8", "const:4:8"]]
- 006e53cc ["CALL", null, ["callee:0048ce84:8"]]
+ 006e540c ["INT_ADD", "register:40f0:8", ["const:6e540c:8", "const:4:8"]]
+ 006e540c ["CALL", null, ["callee:0048ce84:8"]]
- 006e53cc bytes 9e9ef697
+ 006e540c bytes 9e9ef697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0a3b5d24e6e0bafa55669ff5d27977"></a>

### [`006e5d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md) → [`006e5d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md) FUN_006e5d70

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 59件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 59件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_value, call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 16件, `call_target` 20件, `store_value` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e6648",
      "incomplete_value": false,
      "site": "006e6648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e6608",
      "incomplete_value": false,
      "site": "006e6608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
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
      "definition_site": "006e671c",
      "incomplete_value": false,
      "site": "006e671c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e66dc",
      "incomplete_value": false,
      "site": "006e66dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006e687c",
      "incomplete_value": false,
      "site": "006e6884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e683c",
      "incomplete_value": false,
      "site": "006e6844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e5dac",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006e5db8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e5dc0",
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
      "006e5dac",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006e5db8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e5dc0",
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


#### 変更候補の命令位置

- 旧版 [`006e5d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md#insn-006e5d88) · [`006e5e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md#insn-006e5e50) · [`006e5ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5d30.md#insn-006e5ed4)
- 新版 [`006e5dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md#insn-006e5dc8) · [`006e5e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md#insn-006e5e90) · [`006e5f14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e5d70.md#insn-006e5f14)

~~~diff
- 006e5d88 ["INT_ADD", "register:40f0:8", ["const:6e5d88:8", "const:4:8"]]
- 006e5d88 ["CALL", null, ["callee:00c58610:8"]]
+ 006e5dc8 ["INT_ADD", "register:40f0:8", ["const:6e5dc8:8", "const:4:8"]]
+ 006e5dc8 ["CALL", null, ["callee:00c58610:8"]]
- 006e5d88 bytes 22c91594
+ 006e5dc8 bytes 12ca1594
- 006e5e50 ["INT_ADD", "register:40f0:8", ["const:6e5e50:8", "const:4:8"]]
- 006e5e50 ["CALL", null, ["ram:6e72c0:8"]]
+ 006e5e90 ["INT_ADD", "register:40f0:8", ["const:6e5e90:8", "const:4:8"]]
+ 006e5e90 ["CALL", null, ["ram:6e7300:8"]]
- 006e5e50 bytes 1c050094
+ 006e5e90 bytes 1c050094
- 006e5ed4 ["INT_ADD", "register:40f0:8", ["const:6e5ed4:8", "const:4:8"]]
- 006e5ed4 ["CALL", null, ["ram:6e4a84:8"]]
+ 006e5f14 ["INT_ADD", "register:40f0:8", ["const:6e5f14:8", "const:4:8"]]
+ 006e5f14 ["CALL", null, ["ram:6e4ac4:8"]]
- 006e5ed4 bytes ecfaff97
+ 006e5f14 bytes ecfaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b009324cac448c908039e64a43f9d768"></a>

### [`006e7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md) → [`006e7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md) FUN_006e7990

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) · 呼出先 12件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 1件 [`006f8a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md) · 呼出先 12件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006e79c0",
      "incomplete_value": true,
      "site": "006e79c0",
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
      "definition_site": "006e7980",
      "incomplete_value": true,
      "site": "006e7980",
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
      "definition_site": "006e79c8",
      "incomplete_value": false,
      "site": "006e79d8",
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
      "definition_site": "006e7988",
      "incomplete_value": false,
      "site": "006e7998",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e79d0",
      "incomplete_value": false,
      "site": "006e79d8",
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
      "definition_site": "006e7990",
      "incomplete_value": false,
      "site": "006e7998",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e79bc",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006e79c8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e79d0",
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
      "006e79bc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006e79c8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e79d0",
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


#### 変更候補の命令位置

- 旧版 [`006e7998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md#insn-006e7998) · [`006e79e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md#insn-006e79e0) · [`006e7a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md#insn-006e7a20)
- 新版 [`006e79d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md#insn-006e79d8) · [`006e7a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md#insn-006e7a20) · [`006e7a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md#insn-006e7a60)

~~~diff
- 006e7998 ["INT_ADD", "register:40f0:8", ["const:6e7998:8", "const:4:8"]]
- 006e7998 ["CALL", null, ["callee:00c58610:8"]]
+ 006e79d8 ["INT_ADD", "register:40f0:8", ["const:6e79d8:8", "const:4:8"]]
+ 006e79d8 ["CALL", null, ["callee:00c58610:8"]]
- 006e7998 bytes 1ec21594
+ 006e79d8 bytes 0ec31594
- 006e79e0 ["INT_ADD", "register:40f0:8", ["const:6e79e0:8", "const:4:8"]]
- 006e79e0 ["CALL", null, ["ram:46c984:8"]]
+ 006e7a20 ["INT_ADD", "register:40f0:8", ["const:6e7a20:8", "const:4:8"]]
+ 006e7a20 ["CALL", null, ["ram:46c9c4:8"]]
- 006e79e0 bytes e913f697
+ 006e7a20 bytes e913f697
- 006e7a20 ["INT_ADD", "register:40f0:8", ["const:6e7a20:8", "const:4:8"]]
- 006e7a20 ["CALL", null, ["callee:008514f8:8"]]
+ 006e7a60 ["INT_ADD", "register:40f0:8", ["const:6e7a60:8", "const:4:8"]]
+ 006e7a60 ["CALL", null, ["callee:008514f8:8"]]
- 006e7a20 bytes a6a60594
+ 006e7a60 bytes a6a60594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf2a0e79386dc107ff7efc671143e2c"></a>

### [`006e7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7c00.md) → [`006e7c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7c40.md) FUN_006e7c40

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006e7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md) · 呼出先 15件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md)
- 新版 呼出元 1件 [`006e7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0046af18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af18.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006e7c94",
      "incomplete_value": true,
      "site": "006e7c94",
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
      "definition_site": "006e7c54",
      "incomplete_value": true,
      "site": "006e7c54",
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
      "definition_site": "006e7c9c",
      "incomplete_value": false,
      "site": "006e7cb0",
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
      "definition_site": "006e7c5c",
      "incomplete_value": false,
      "site": "006e7c70",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e7ca4",
      "incomplete_value": false,
      "site": "006e7cb0",
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
      "definition_site": "006e7c64",
      "incomplete_value": false,
      "site": "006e7c70",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e7c90",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006e7c9c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e7ca4",
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
      "006e7c90",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006e7c9c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e7ca4",
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


#### 変更候補の命令位置

- 旧版 [`006e7c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7c00.md#insn-006e7c70) · [`006e7cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7c00.md#insn-006e7cec) · [`006e82d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7c00.md#insn-006e82d8)
- 新版 [`006e7cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7c40.md#insn-006e7cb0) · [`006e7d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7c40.md#insn-006e7d2c) · [`006e8318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7c40.md#insn-006e8318)

~~~diff
- 006e7c70 ["INT_ADD", "register:40f0:8", ["const:6e7c70:8", "const:4:8"]]
- 006e7c70 ["CALL", null, ["callee:00c58610:8"]]
+ 006e7cb0 ["INT_ADD", "register:40f0:8", ["const:6e7cb0:8", "const:4:8"]]
+ 006e7cb0 ["CALL", null, ["callee:00c58610:8"]]
- 006e7c70 bytes 68c11594
+ 006e7cb0 bytes 58c21594
- 006e7cec ["INT_ADD", "register:40f0:8", ["const:6e7cec:8", "const:4:8"]]
- 006e7cec ["CALL", null, ["ram:46c984:8"]]
+ 006e7d2c ["INT_ADD", "register:40f0:8", ["const:6e7d2c:8", "const:4:8"]]
+ 006e7d2c ["CALL", null, ["ram:46c9c4:8"]]
- 006e7cec bytes 2613f697
+ 006e7d2c bytes 2613f697
- 006e82d8 ["INT_ADD", "register:40f0:8", ["const:6e82d8:8", "const:4:8"]]
- 006e82d8 ["CALL", null, ["ram:6e4a84:8"]]
+ 006e8318 ["INT_ADD", "register:40f0:8", ["const:6e8318:8", "const:4:8"]]
+ 006e8318 ["CALL", null, ["ram:6e4ac4:8"]]
- 006e82d8 bytes ebf1ff97
+ 006e8318 bytes ebf1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8386ce7ef247944af285b51c075dea4"></a>

### [`006e8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md) → [`006e8c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8c1c.md) FUN_006e8c1c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 19件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) · 呼出先 19件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.81% / 新版 85.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `call_target` 11件, `store_destination` 14件, `store_value` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e8f1c",
      "incomplete_value": true,
      "site": "006e8f2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006e8edc",
      "incomplete_value": true,
      "site": "006e8eec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f60:8"
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
      "definition_site": "006e8f30",
      "incomplete_value": true,
      "site": "006e8f30",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006e8ef0",
      "incomplete_value": true,
      "site": "006e8ef0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e8f24",
      "incomplete_value": true,
      "site": "006e8f34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "006e8ee4",
      "incomplete_value": true,
      "site": "006e8ef4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:410:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e8c58",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006e8c64",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e8c6c",
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
      "006e8c58",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006e8c64",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e8c6c",
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


#### 変更候補の命令位置

- 旧版 [`006e8c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md#insn-006e8c18) · [`006e8c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md#insn-006e8c38) · [`006e8c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8bdc.md#insn-006e8c58)
- 新版 [`006e8c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8c1c.md#insn-006e8c58) · [`006e8c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8c1c.md#insn-006e8c78) · [`006e8c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e8/006e8c1c.md#insn-006e8c98)

~~~diff
- 006e8c18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 006e8c18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006e8c58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:978:8"]]
+ 006e8c58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006e8c18 bytes 08bd42f9
+ 006e8c58 bytes 08bd44f9
- 006e8c38 ["INT_ADD", "register:40f0:8", ["const:6e8c38:8", "const:4:8"]]
- 006e8c38 ["CALL", null, ["callee:00c58610:8"]]
+ 006e8c78 ["INT_ADD", "register:40f0:8", ["const:6e8c78:8", "const:4:8"]]
+ 006e8c78 ["CALL", null, ["callee:00c58610:8"]]
- 006e8c38 bytes 76bd1594
+ 006e8c78 bytes 66be1594
- 006e8c58 ["INT_ADD", "register:40f0:8", ["const:6e8c58:8", "const:4:8"]]
- 006e8c58 ["CALL", null, ["ram:46c984:8"]]
+ 006e8c98 ["INT_ADD", "register:40f0:8", ["const:6e8c98:8", "const:4:8"]]
+ 006e8c98 ["CALL", null, ["ram:46c9c4:8"]]
- 006e8c58 bytes 4b0ff697
+ 006e8c98 bytes 4b0ff697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b6977b23ae8a4dd8249fe3d2b93fed"></a>

### [`006e9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md) → [`006e9e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e9e64.md) FUN_006e9e64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) · 呼出先 13件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)
- 新版 呼出元 1件 [`006f8a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md) · 呼出先 13件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006e9ea4",
      "incomplete_value": true,
      "site": "006e9ea4",
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
      "definition_site": "006e9e64",
      "incomplete_value": true,
      "site": "006e9e64",
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
      "definition_site": "006e9eac",
      "incomplete_value": false,
      "site": "006e9ec0",
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
      "definition_site": "006e9e6c",
      "incomplete_value": false,
      "site": "006e9e80",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006e9eb4",
      "incomplete_value": false,
      "site": "006e9ec0",
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
      "definition_site": "006e9e74",
      "incomplete_value": false,
      "site": "006e9e80",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e9ea0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006e9eac",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e9eb4",
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
      "006e9ea0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006e9eac",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006e9eb4",
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


#### 変更候補の命令位置

- 旧版 [`006e9e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md#insn-006e9e80) · [`006e9ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md#insn-006e9ecc) · [`006ea444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e9/006e9e24.md#insn-006ea444)
- 新版 [`006e9ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e9e64.md#insn-006e9ec0) · [`006e9f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e9e64.md#insn-006e9f0c) · [`006ea484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e9/006e9e64.md#insn-006ea484)

~~~diff
- 006e9e80 ["INT_ADD", "register:40f0:8", ["const:6e9e80:8", "const:4:8"]]
- 006e9e80 ["CALL", null, ["callee:00c58610:8"]]
+ 006e9ec0 ["INT_ADD", "register:40f0:8", ["const:6e9ec0:8", "const:4:8"]]
+ 006e9ec0 ["CALL", null, ["callee:00c58610:8"]]
- 006e9e80 bytes e4b81594
+ 006e9ec0 bytes d4b91594
- 006e9ecc ["INT_ADD", "register:40f0:8", ["const:6e9ecc:8", "const:4:8"]]
- 006e9ecc ["CALL", null, ["ram:46c984:8"]]
+ 006e9f0c ["INT_ADD", "register:40f0:8", ["const:6e9f0c:8", "const:4:8"]]
+ 006e9f0c ["CALL", null, ["ram:46c9c4:8"]]
- 006e9ecc bytes ae0af697
+ 006e9f0c bytes ae0af697
- 006ea444 ["INT_ADD", "register:40f0:8", ["const:6ea444:8", "const:4:8"]]
- 006ea444 ["CALL", null, ["ram:6dde48:8"]]
+ 006ea484 ["INT_ADD", "register:40f0:8", ["const:6ea484:8", "const:4:8"]]
+ 006ea484 ["CALL", null, ["ram:6dde88:8"]]
- 006ea444 bytes 81ceff97
+ 006ea484 bytes 81ceff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdfcd6f31f2ce820a85d82cca878cca6"></a>

### [`006ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md) → [`006ee740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md) FUN_006ee740

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006eec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006eec6c.md) · 呼出先 10件 [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0063c584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c584.md) [`0063c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063c/0063c58c.md) [`006e4088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4088.md) [`006e43a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e43a8.md)
- 新版 呼出元 1件 [`006eecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006eecac.md) · 呼出先 10件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0063c5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5c4.md) [`0063c5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063c/0063c5cc.md) [`006e40c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e40c8.md) [`006e43e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e43e8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.17% / 新版 96.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ee770",
      "value": [
        "leaf",
        "ram:6e43e8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ee730",
      "value": [
        "leaf",
        "ram:6e43a8:8"
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
      "site": "006ee780",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ee740",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006ee7a0",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ee760",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ee770",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e43a8"
      ]
    ],
    [
      "006ee780",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006ee7a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006ee770",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e43e8"
      ]
    ],
    [
      "006ee780",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006ee7a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ee730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md#insn-006ee730) · [`006ee740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md#insn-006ee740) · [`006ee760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006ee700.md#insn-006ee760)
- 新版 [`006ee770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md#insn-006ee770) · [`006ee780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md#insn-006ee780) · [`006ee7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ee/006ee740.md#insn-006ee7a0)

~~~diff
- 006ee730 ["INT_ADD", "register:40f0:8", ["const:6ee730:8", "const:4:8"]]
- 006ee730 ["CALL", null, ["ram:6e43a8:8"]]
+ 006ee770 ["INT_ADD", "register:40f0:8", ["const:6ee770:8", "const:4:8"]]
+ 006ee770 ["CALL", null, ["ram:6e43e8:8"]]
- 006ee730 bytes 1ed7ff97
+ 006ee770 bytes 1ed7ff97
- 006ee740 ["INT_ADD", "register:40f0:8", ["const:6ee740:8", "const:4:8"]]
- 006ee740 ["CALL", null, ["ram:6e4a84:8"]]
+ 006ee780 ["INT_ADD", "register:40f0:8", ["const:6ee780:8", "const:4:8"]]
+ 006ee780 ["CALL", null, ["ram:6e4ac4:8"]]
- 006ee740 bytes d1d8ff97
+ 006ee780 bytes d1d8ff97
- 006ee760 ["INT_ADD", "register:40f0:8", ["const:6ee760:8", "const:4:8"]]
- 006ee760 ["CALL", null, ["ram:6e4a84:8"]]
+ 006ee7a0 ["INT_ADD", "register:40f0:8", ["const:6ee7a0:8", "const:4:8"]]
+ 006ee7a0 ["CALL", null, ["ram:6e4ac4:8"]]
- 006ee760 bytes c9d8ff97
+ 006ee7a0 bytes c9d8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e7c67ea5ec85c10a7317268558d3c08"></a>

### [`006f0614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md) → [`006f0654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0654.md) FUN_006f0654

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f1648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md) · 呼出先 23件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md)
- 新版 呼出元 1件 [`006f1688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f1688.md) · 呼出先 23件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0046e770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e770.md) [`0046e780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e780.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.91% / 新版 89.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 31件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006f06d8",
      "incomplete_value": true,
      "site": "006f06ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f0698",
      "incomplete_value": true,
      "site": "006f06ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:650:8"
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
      "definition_site": "006f06e4",
      "incomplete_value": true,
      "site": "006f06f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:eaa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f06a4",
      "incomplete_value": true,
      "site": "006f06b0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e6a:8"
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
      "definition_site": "006f06e4",
      "incomplete_value": true,
      "site": "006f06f0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "006f06a4",
      "incomplete_value": true,
      "site": "006f06b0",
      "value": [
        "LOAD",
        "16",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f068c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006f0698",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f06a0",
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
      "006f068c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006f0698",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f06a0",
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


#### 変更候補の命令位置

- 旧版 [`006f066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md#insn-006f066c) · [`006f0728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md#insn-006f0728) · [`006f07a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md#insn-006f07a8)
- 新版 [`006f06ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0654.md#insn-006f06ac) · [`006f0768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0654.md#insn-006f0768) · [`006f07e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0654.md#insn-006f07e8)

~~~diff
- 006f066c ["INT_ADD", "register:40f0:8", ["const:6f066c:8", "const:4:8"]]
- 006f066c ["CALL", null, ["callee:00c58610:8"]]
+ 006f06ac ["INT_ADD", "register:40f0:8", ["const:6f06ac:8", "const:4:8"]]
+ 006f06ac ["CALL", null, ["callee:00c58610:8"]]
- 006f066c bytes e99e1594
+ 006f06ac bytes d99f1594
- 006f0728 ["INT_ADD", "register:40f0:8", ["const:6f0728:8", "const:4:8"]]
- 006f0728 ["CALL", null, ["callee:004700e0:8"]]
+ 006f0768 ["INT_ADD", "register:40f0:8", ["const:6f0768:8", "const:4:8"]]
+ 006f0768 ["CALL", null, ["callee:004700e0:8"]]
- 006f0728 bytes 5efef597
+ 006f0768 bytes 5efef597
- 006f07a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
- 006f07a8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 006f07a8 ["COPY", "register:5010:8", ["const:0:8"]]
- 006f07a8 ["COPY", "register:5018:8", ["const:0:8"]]
+ 006f07e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a0:8"]]
+ 006f07e8 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 006f07e8 ["COPY", "register:5010:8", ["const:0:8"]]
+ 006f07e8 ["COPY", "register:5018:8", ["const:0:8"]]
- 006f07a8 bytes 0099c03d
+ 006f07e8 bytes 00a9c03d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acc737f4ecdac899a87724e5e0be5052"></a>

### [`006f1648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md) → [`006f1688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f1688.md) FUN_006f1688

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b2968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b2968.md) · 呼出先 37件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`006c0d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c0d30.md)
- 新版 呼出元 1件 [`006b29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b29a8.md) · 呼出先 37件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700e0.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`006c0d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0d70.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 11件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006f1798",
      "incomplete_value": true,
      "site": "006f17a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f1758",
      "incomplete_value": true,
      "site": "006f1768",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:160:8"
              ]
            ]
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
      "definition_site": "006f1c84",
      "incomplete_value": false,
      "site": "006f1c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f1c44",
      "incomplete_value": false,
      "site": "006f1c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "definition_site": "006f2228",
      "incomplete_value": false,
      "site": "006f2228",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f21e8",
      "incomplete_value": false,
      "site": "006f21e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 144,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f16c4",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006f16d8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f16e0",
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
      "006f16c4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006f16d8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f16e0",
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


#### 変更候補の命令位置

- 旧版 [`006f16a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md#insn-006f16a8) · [`006f16cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md#insn-006f16cc) · [`006f16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md#insn-006f16e8)
- 新版 [`006f16e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f1688.md#insn-006f16e8) · [`006f170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f1688.md#insn-006f170c) · [`006f1728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f1/006f1688.md#insn-006f1728)

~~~diff
- 006f16a8 ["INT_ADD", "register:40f0:8", ["const:6f16a8:8", "const:4:8"]]
- 006f16a8 ["CALL", null, ["callee:00c58610:8"]]
+ 006f16e8 ["INT_ADD", "register:40f0:8", ["const:6f16e8:8", "const:4:8"]]
+ 006f16e8 ["CALL", null, ["callee:00c58610:8"]]
- 006f16a8 bytes da9a1594
+ 006f16e8 bytes ca9b1594
- 006f16cc ["INT_ADD", "register:40f0:8", ["const:6f16cc:8", "const:4:8"]]
- 006f16cc ["CALL", null, ["callee:00a38bec:8"]]
+ 006f170c ["INT_ADD", "register:40f0:8", ["const:6f170c:8", "const:4:8"]]
+ 006f170c ["CALL", null, ["callee:00a38bec:8"]]
- 006f16cc bytes ca1c0d94
+ 006f170c bytes 381d0d94
- 006f16e8 ["INT_ADD", "register:40f0:8", ["const:6f16e8:8", "const:4:8"]]
- 006f16e8 ["CALL", null, ["callee:006f0654:8"]]
+ 006f1728 ["INT_ADD", "register:40f0:8", ["const:6f1728:8", "const:4:8"]]
+ 006f1728 ["CALL", null, ["callee:006f0654:8"]]
- 006f16e8 bytes cbfbff97
+ 006f1728 bytes cbfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc03d129fd2a8f2938b69e807050f0d"></a>

### [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) → [`006f8a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md) FUN_006f8a08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 30件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)
- 新版 呼出元 1件 [`006b3480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b3/006b3480.md) · 呼出先 30件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f1c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006f8a54",
      "incomplete_value": true,
      "site": "006f8a54",
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
      "definition_site": "006f8a14",
      "incomplete_value": true,
      "site": "006f8a14",
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
      "definition_site": "006f8a5c",
      "incomplete_value": false,
      "site": "006f8a6c",
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
      "definition_site": "006f8a1c",
      "incomplete_value": false,
      "site": "006f8a2c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f8a64",
      "incomplete_value": false,
      "site": "006f8a6c",
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
      "definition_site": "006f8a24",
      "incomplete_value": false,
      "site": "006f8a2c",
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
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f8a40",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8a5c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8a64",
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
      "006f8a40",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8a5c",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8a64",
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


#### 変更候補の命令位置

- 旧版 [`006f8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md#insn-006f8a2c) · [`006f8a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md#insn-006f8a78) · [`006f8d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md#insn-006f8d30)
- 新版 [`006f8a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md#insn-006f8a6c) · [`006f8ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md#insn-006f8ab8) · [`006f8d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f8/006f8a08.md#insn-006f8d70)

~~~diff
- 006f8a2c ["INT_ADD", "register:40f0:8", ["const:6f8a2c:8", "const:4:8"]]
- 006f8a2c ["CALL", null, ["callee:00c58610:8"]]
+ 006f8a6c ["INT_ADD", "register:40f0:8", ["const:6f8a6c:8", "const:4:8"]]
+ 006f8a6c ["CALL", null, ["callee:00c58610:8"]]
- 006f8a2c bytes f97d1594
+ 006f8a6c bytes e97e1594
- 006f8a78 ["INT_ADD", "register:40f0:8", ["const:6f8a78:8", "const:4:8"]]
- 006f8a78 ["CALL", null, ["ram:46c984:8"]]
+ 006f8ab8 ["INT_ADD", "register:40f0:8", ["const:6f8ab8:8", "const:4:8"]]
+ 006f8ab8 ["CALL", null, ["ram:46c9c4:8"]]
- 006f8a78 bytes c3cff597
+ 006f8ab8 bytes c3cff597
- 006f8d30 ["INT_ADD", "register:40f0:8", ["const:6f8d30:8", "const:4:8"]]
- 006f8d30 ["CALL", null, ["ram:46c984:8"]]
+ 006f8d70 ["INT_ADD", "register:40f0:8", ["const:6f8d70:8", "const:4:8"]]
+ 006f8d70 ["CALL", null, ["ram:46c9c4:8"]]
- 006f8d30 bytes 15cff597
+ 006f8d70 bytes 15cff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa185ee4ec991c8f81137e64d5cfa8e"></a>

### [`006f9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9e98.md) → [`006f9ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ed8.md) FUN_006f9ed8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006dab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`006dabac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006dabac.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f9ee4",
      "incomplete_value": false,
      "site": "006f9ee8",
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
      "definition_site": "006f9ea4",
      "incomplete_value": false,
      "site": "006f9ea8",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f9ee4",
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
      "006f9ee4",
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


#### 変更候補の命令位置

- 旧版 [`006f9ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9e98.md#insn-006f9ea8) · [`006f9ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9e98.md#insn-006f9ea4)
- 新版 [`006f9ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ed8.md#insn-006f9ee8) · [`006f9ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ed8.md#insn-006f9ee4)

~~~diff
- 006f9ea8 ["INT_ADD", "register:40f0:8", ["const:6f9ea8:8", "const:4:8"]]
- 006f9ea8 ["CALL", null, ["callee:0043b778:8"]]
+ 006f9ee8 ["INT_ADD", "register:40f0:8", ["const:6f9ee8:8", "const:4:8"]]
+ 006f9ee8 ["CALL", null, ["callee:0043b778:8"]]
- 006f9ea8 bytes 2406f597
+ 006f9ee8 bytes 2406f597
- 006f9ea4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 006f9ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006f9ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006f9ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f9ee4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 006f9ee4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f9ee4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f9ee4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006f9ea4 bytes 00303c91
+ 006f9ee4 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4977cf1a8ccbfff4ccbd07afc468d25"></a>

### [`006f9eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9eb0.md) → [`006f9ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ef0.md) FUN_006f9ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006f9f14",
      "incomplete_value": false,
      "site": "006f9f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9ed4",
      "incomplete_value": false,
      "site": "006f9ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f9f14",
      "DATA",
      [
        "storage",
        "00c76518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006f9f14",
      "DATA",
      [
        "storage",
        "00c76918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9eb0.md#insn-006f9ec4) · [`006f9ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9eb0.md#insn-006f9ed0)
- 新版 [`006f9f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ef0.md#insn-006f9f04) · [`006f9f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9ef0.md#insn-006f9f10)

~~~diff
- 006f9ec4 ["INT_ADD", "register:40f0:8", ["const:6f9ec4:8", "const:4:8"]]
- 006f9ec4 ["CALL", null, ["callee:00c57e90:8"]]
+ 006f9f04 ["INT_ADD", "register:40f0:8", ["const:6f9f04:8", "const:4:8"]]
+ 006f9f04 ["CALL", null, ["callee:00c57e90:8"]]
- 006f9ec4 bytes f3761594
+ 006f9f04 bytes e3771594
- 006f9ed0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 006f9ed0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f9ed0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f9ed0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f9f10 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 006f9f10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9f10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9f10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f9ed0 bytes 08611491
+ 006f9f10 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e90e629b2926dc03d284c4fac69403b9"></a>

### [`006f9ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9ee4.md) → [`006f9f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f24.md) FUN_006f9f24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006f9f30",
      "incomplete_value": false,
      "site": "006f9f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9ef0",
      "incomplete_value": false,
      "site": "006f9ef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:518:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f9f30",
      "DATA",
      [
        "storage",
        "00c76518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006f9f30",
      "DATA",
      [
        "storage",
        "00c76918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9ee4.md#insn-006f9eec)
- 新版 [`006f9f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f24.md#insn-006f9f2c)

~~~diff
- 006f9eec ["COPY", "tmp:0:8", ["const:518:8"]]
- 006f9eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006f9eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006f9eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006f9f2c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 006f9f2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006f9f2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006f9f2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006f9eec bytes 29611491
+ 006f9f2c bytes 29612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32ede7efe5b39ed5d49ce4e88cd11ff2"></a>

### [`006f9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f00.md) → [`006f9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f40.md) FUN_006f9f40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f9f58",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f9f18",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006f9f84",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f9f44",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f9f58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006f9f84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006f9f58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006f9f84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f00.md#insn-006f9f18) · [`006f9f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f00.md#insn-006f9f44) · [`006f9f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f00.md#insn-006f9f50)
- 新版 [`006f9f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f40.md#insn-006f9f58) · [`006f9f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f40.md#insn-006f9f84) · [`006f9f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9f40.md#insn-006f9f90)

~~~diff
- 006f9f18 ["INT_ADD", "register:40f0:8", ["const:6f9f18:8", "const:4:8"]]
- 006f9f18 ["CALL", null, ["ram:47acb4:8"]]
+ 006f9f58 ["INT_ADD", "register:40f0:8", ["const:6f9f58:8", "const:4:8"]]
+ 006f9f58 ["CALL", null, ["ram:47acf4:8"]]
- 006f9f18 bytes 6703f697
+ 006f9f58 bytes 6703f697
- 006f9f44 ["INT_ADD", "register:40f0:8", ["const:6f9f44:8", "const:4:8"]]
- 006f9f44 ["CALL", null, ["ram:47acb4:8"]]
+ 006f9f84 ["INT_ADD", "register:40f0:8", ["const:6f9f84:8", "const:4:8"]]
+ 006f9f84 ["CALL", null, ["ram:47acf4:8"]]
- 006f9f44 bytes 5c03f697
+ 006f9f84 bytes 5c03f697
- 006f9f50 ["INT_ADD", "register:40f0:8", ["const:6f9f50:8", "const:4:8"]]
- 006f9f50 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006f9f90 ["INT_ADD", "register:40f0:8", ["const:6f9f90:8", "const:4:8"]]
+ 006f9f90 ["CALL", null, ["callee:0047cdd4:8"]]
- 006f9f50 bytes 910bf697
+ 006f9f90 bytes 910bf697
~~~


<a id="compare-ba10385c380ccbc04723e9c43316daf0"></a>

### [`006f9f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f9c.md) → [`006f9fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9fdc.md) FUN_006f9fdc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa000",
      "incomplete_value": false,
      "site": "006fa000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9fc0",
      "incomplete_value": false,
      "site": "006f9fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fa000",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fa000",
      "DATA",
      [
        "storage",
        "00c76998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f9c.md#insn-006f9fb0) · [`006f9fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f9c.md#insn-006f9fbc)
- 新版 [`006f9ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9fdc.md#insn-006f9ff0) · [`006f9ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f9/006f9fdc.md#insn-006f9ffc)

~~~diff
- 006f9fb0 ["INT_ADD", "register:40f0:8", ["const:6f9fb0:8", "const:4:8"]]
- 006f9fb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 006f9ff0 ["INT_ADD", "register:40f0:8", ["const:6f9ff0:8", "const:4:8"]]
+ 006f9ff0 ["CALL", null, ["callee:00c57e90:8"]]
- 006f9fb0 bytes b8761594
+ 006f9ff0 bytes a8771594
- 006f9fbc ["COPY", "tmp:0:8", ["const:598:8"]]
- 006f9fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006f9fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006f9fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f9ffc ["COPY", "tmp:0:8", ["const:998:8"]]
+ 006f9ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006f9fbc bytes 08611691
+ 006f9ffc bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06b647e8d59089274300a009fbf5ba7f"></a>

### [`006f9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fd0.md) → [`006fa010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa010.md) FUN_006fa010

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fa01c",
      "incomplete_value": false,
      "site": "006fa01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006f9fdc",
      "incomplete_value": false,
      "site": "006f9fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fa01c",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fa01c",
      "DATA",
      [
        "storage",
        "00c76998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006f9fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fd0.md#insn-006f9fd8)
- 新版 [`006fa018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa010.md#insn-006fa018)

~~~diff
- 006f9fd8 ["COPY", "tmp:0:8", ["const:598:8"]]
- 006f9fd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006f9fd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006f9fd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fa018 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 006fa018 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa018 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fa018 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006f9fd8 bytes 29611691
+ 006fa018 bytes 29612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055f8cede43e8192b1af05a64541773c"></a>

### [`006f9fec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fec.md) → [`006fa02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa02c.md) FUN_006fa02c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa06c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fa02c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fa06c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006fa06c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fa02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fec.md#insn-006fa02c) · [`006fa008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fec.md#insn-006fa008) · [`006fa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fec.md#insn-006fa014)
- 新版 [`006fa06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa02c.md#insn-006fa06c) · [`006fa048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa02c.md#insn-006fa048) · [`006fa054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa02c.md#insn-006fa054)

~~~diff
- 006fa02c ["INT_ADD", "register:40f0:8", ["const:6fa02c:8", "const:4:8"]]
- 006fa02c ["CALL", null, ["ram:46c984:8"]]
+ 006fa06c ["INT_ADD", "register:40f0:8", ["const:6fa06c:8", "const:4:8"]]
+ 006fa06c ["CALL", null, ["ram:46c9c4:8"]]
- 006fa02c bytes 56caf597
+ 006fa06c bytes 56caf597
- 006fa008 ["INT_ADD", "register:40f0:8", ["const:6fa008:8", "const:4:8"]]
- 006fa008 ["CALL", null, ["callee:008b9290:8"]]
+ 006fa048 ["INT_ADD", "register:40f0:8", ["const:6fa048:8", "const:4:8"]]
+ 006fa048 ["CALL", null, ["callee:008b9290:8"]]
- 006fa008 bytes 91fc0694
+ 006fa048 bytes 92fc0694
- 006fa014 ["INT_ADD", "register:40f0:8", ["const:6fa014:8", "const:4:8"]]
- 006fa014 ["CALL", null, ["callee:008b9298:8"]]
+ 006fa054 ["INT_ADD", "register:40f0:8", ["const:6fa054:8", "const:4:8"]]
+ 006fa054 ["CALL", null, ["callee:008b9298:8"]]
- 006fa014 bytes 90fc0694
+ 006fa054 bytes 91fc0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d61a8cfafeda57d7d06cf17de5dd63f"></a>

### [`006fa0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0a0.md) → [`006fa0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa0e0.md) FUN_006fa0e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`006dbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006dbb6c.md) [`006dbda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006db/006dbda8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006fa0ec",
      "incomplete_value": false,
      "site": "006fa0f0",
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
      "definition_site": "006fa0ac",
      "incomplete_value": false,
      "site": "006fa0b0",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fa0ec",
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
      "006fa0ec",
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


#### 変更候補の命令位置

- 旧版 [`006fa0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0a0.md#insn-006fa0b0) · [`006fa0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0a0.md#insn-006fa0ac)
- 新版 [`006fa0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa0e0.md#insn-006fa0f0) · [`006fa0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fa/006fa0e0.md#insn-006fa0ec)

~~~diff
- 006fa0b0 ["INT_ADD", "register:40f0:8", ["const:6fa0b0:8", "const:4:8"]]
- 006fa0b0 ["CALL", null, ["callee:0043b778:8"]]
+ 006fa0f0 ["INT_ADD", "register:40f0:8", ["const:6fa0f0:8", "const:4:8"]]
+ 006fa0f0 ["CALL", null, ["callee:0043b778:8"]]
- 006fa0b0 bytes a205f597
+ 006fa0f0 bytes a205f597
- 006fa0ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 006fa0ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006fa0ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006fa0ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 006fa0ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006fa0ac bytes 00303c91
+ 006fa0ec bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d0042050fa9b9f2b10700820aee222c"></a>

### [`006fb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb0a8.md) → [`006fb0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb0e8.md) FUN_006fb0e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb0fc",
      "incomplete_value": false,
      "site": "006fb100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb0bc",
      "incomplete_value": false,
      "site": "006fb0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb100",
      "DATA",
      [
        "storage",
        "00c76618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb100",
      "DATA",
      [
        "storage",
        "00c76a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb0a8.md#insn-006fb0b4) · [`006fb0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb0a8.md#insn-006fb0bc)
- 新版 [`006fb0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb0e8.md#insn-006fb0f4) · [`006fb0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb0e8.md#insn-006fb0fc)

~~~diff
- 006fb0b4 ["INT_ADD", "register:40f0:8", ["const:6fb0b4:8", "const:4:8"]]
- 006fb0b4 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fb0f4 ["INT_ADD", "register:40f0:8", ["const:6fb0f4:8", "const:4:8"]]
+ 006fb0f4 ["CALL", null, ["callee:00c57e90:8"]]
- 006fb0b4 bytes 77721594
+ 006fb0f4 bytes 67731594
- 006fb0bc ["COPY", "tmp:0:8", ["const:618:8"]]
- 006fb0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb0fc ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 006fb0fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb0fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb0fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb0bc bytes 08611891
+ 006fb0fc bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b9fd8276140a11c66c36eb67e32c56c"></a>

### [`006fb14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb14c.md) → [`006fb18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb18c.md) FUN_006fb18c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb1b0",
      "incomplete_value": false,
      "site": "006fb1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb170",
      "incomplete_value": false,
      "site": "006fb174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb1b4",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb1b4",
      "DATA",
      [
        "storage",
        "00c76a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb14c.md#insn-006fb160) · [`006fb170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb14c.md#insn-006fb170)
- 新版 [`006fb1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb18c.md#insn-006fb1a0) · [`006fb1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb18c.md#insn-006fb1b0)

~~~diff
- 006fb160 ["INT_ADD", "register:40f0:8", ["const:6fb160:8", "const:4:8"]]
- 006fb160 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fb1a0 ["INT_ADD", "register:40f0:8", ["const:6fb1a0:8", "const:4:8"]]
+ 006fb1a0 ["CALL", null, ["callee:00c57e90:8"]]
- 006fb160 bytes 4c721594
+ 006fb1a0 bytes 3c731594
- 006fb170 ["COPY", "tmp:0:8", ["const:698:8"]]
- 006fb170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb1b0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 006fb1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb170 bytes 08611a91
+ 006fb1b0 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-905caf8318dbdc0f9527004f202bd532"></a>

### [`006fb18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb18c.md) → [`006fb1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1cc.md) FUN_006fb1cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb1d0",
      "incomplete_value": false,
      "site": "006fb1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb190",
      "incomplete_value": false,
      "site": "006fb194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb1d4",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb1d4",
      "DATA",
      [
        "storage",
        "00c76a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb18c.md#insn-006fb190)
- 新版 [`006fb1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1cc.md#insn-006fb1d0)

~~~diff
- 006fb190 ["COPY", "tmp:0:8", ["const:698:8"]]
- 006fb190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb1d0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 006fb1d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb1d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb1d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb190 bytes 08611a91
+ 006fb1d0 bytes 08612a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f6da55c740a82f891db83ee18c01527"></a>

### [`006fb1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md) → [`006fb1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1f4.md) FUN_006fb1f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb318",
      "incomplete_value": true,
      "site": "006fb32c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:edf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb2d8",
      "incomplete_value": true,
      "site": "006fb2ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e9f:8"
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
      "definition_site": "006fb378",
      "incomplete_value": true,
      "site": "006fb378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c8b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb338",
      "incomplete_value": true,
      "site": "006fb338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c4b:8"
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
      "definition_site": "006fb37c",
      "incomplete_value": true,
      "site": "006fb37c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006fb33c",
      "incomplete_value": true,
      "site": "006fb33c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fb2a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006edda4"
      ]
    ],
    [
      "006fb2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063c548"
      ]
    ]
  ],
  "added": [
    [
      "006fb240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fb2a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006edde4"
      ]
    ],
    [
      "006fb2c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063c588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md#insn-006fb200) · [`006fb264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md#insn-006fb264) · [`006fb288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md#insn-006fb288)
- 新版 [`006fb240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1f4.md#insn-006fb240) · [`006fb2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1f4.md#insn-006fb2a4) · [`006fb2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb1f4.md#insn-006fb2c8)

~~~diff
- 006fb200 ["INT_ADD", "register:40f0:8", ["const:6fb200:8", "const:4:8"]]
- 006fb200 ["CALL", null, ["ram:47acb4:8"]]
+ 006fb240 ["INT_ADD", "register:40f0:8", ["const:6fb240:8", "const:4:8"]]
+ 006fb240 ["CALL", null, ["ram:47acf4:8"]]
- 006fb200 bytes adfef597
+ 006fb240 bytes adfef597
- 006fb264 ["INT_ADD", "register:40f0:8", ["const:6fb264:8", "const:4:8"]]
- 006fb264 ["CALL", null, ["ram:6edda4:8"]]
+ 006fb2a4 ["INT_ADD", "register:40f0:8", ["const:6fb2a4:8", "const:4:8"]]
+ 006fb2a4 ["CALL", null, ["ram:6edde4:8"]]
- 006fb264 bytes d0caff97
+ 006fb2a4 bytes d0caff97
- 006fb288 ["INT_ADD", "register:40f0:8", ["const:6fb288:8", "const:4:8"]]
- 006fb288 ["CALL", null, ["ram:63c548:8"]]
+ 006fb2c8 ["INT_ADD", "register:40f0:8", ["const:6fb2c8:8", "const:4:8"]]
+ 006fb2c8 ["CALL", null, ["ram:63c588:8"]]
- 006fb288 bytes b004fd97
+ 006fb2c8 bytes b004fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4983c60bd521c50c56084274e7b0ce6"></a>

### [`006fb880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb880.md) → [`006fb8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb8c0.md) FUN_006fb8c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb8e4",
      "incomplete_value": false,
      "site": "006fb8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb8a4",
      "incomplete_value": false,
      "site": "006fb8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb8e4",
      "DATA",
      [
        "storage",
        "00c76708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb8e4",
      "DATA",
      [
        "storage",
        "00c76b08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb880.md#insn-006fb894) · [`006fb8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb880.md#insn-006fb8a0)
- 新版 [`006fb8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb8c0.md#insn-006fb8d4) · [`006fb8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb8c0.md#insn-006fb8e0)

~~~diff
- 006fb894 ["INT_ADD", "register:40f0:8", ["const:6fb894:8", "const:4:8"]]
- 006fb894 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fb8d4 ["INT_ADD", "register:40f0:8", ["const:6fb8d4:8", "const:4:8"]]
+ 006fb8d4 ["CALL", null, ["callee:00c57e90:8"]]
- 006fb894 bytes 7f701594
+ 006fb8d4 bytes 6f711594
- 006fb8a0 ["COPY", "tmp:0:8", ["const:708:8"]]
- 006fb8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fb8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fb8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb8e0 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 006fb8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fb8a0 bytes 08211c91
+ 006fb8e0 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a38514ba18c17f54333b1ff27bc4ff8"></a>

### [`006fb8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8b4.md) → [`006fb8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb8f4.md) FUN_006fb8f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb900",
      "incomplete_value": false,
      "site": "006fb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fb8c0",
      "incomplete_value": false,
      "site": "006fb8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb900",
      "DATA",
      [
        "storage",
        "00c76708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb900",
      "DATA",
      [
        "storage",
        "00c76b08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8b4.md#insn-006fb8bc)
- 新版 [`006fb8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb8f4.md#insn-006fb8fc)

~~~diff
- 006fb8bc ["COPY", "tmp:0:8", ["const:708:8"]]
- 006fb8bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fb8bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fb8bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fb8fc ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 006fb8fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fb8fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fb8fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fb8bc bytes 29211c91
+ 006fb8fc bytes 29212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92bceb9538700e7eb51822c5724546a0"></a>

### [`006fb8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md) → [`006fb910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md) FUN_006fb910

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006b23e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b23e4.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006b2424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2424.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006f0500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0500.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fb93c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fb8fc",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006fb9e4",
      "value": [
        "leaf",
        "ram:6f0500:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fb9a4",
      "value": [
        "leaf",
        "ram:6f04c0:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fb93c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fb9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f04c0"
      ]
    ],
    [
      "006fb9fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea548"
      ]
    ]
  ],
  "added": [
    [
      "006fb93c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fb9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0500"
      ]
    ],
    [
      "006fb9fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fb8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md#insn-006fb8fc) · [`006fb9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md#insn-006fb9a4) · [`006fb908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8d0.md#insn-006fb908)
- 新版 [`006fb93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md#insn-006fb93c) · [`006fb9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md#insn-006fb9e4) · [`006fb948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fb910.md#insn-006fb948)

~~~diff
- 006fb8fc ["INT_ADD", "register:40f0:8", ["const:6fb8fc:8", "const:4:8"]]
- 006fb8fc ["CALL", null, ["ram:47acb4:8"]]
+ 006fb93c ["INT_ADD", "register:40f0:8", ["const:6fb93c:8", "const:4:8"]]
+ 006fb93c ["CALL", null, ["ram:47acf4:8"]]
- 006fb8fc bytes eefcf597
+ 006fb93c bytes eefcf597
- 006fb9a4 ["INT_ADD", "register:40f0:8", ["const:6fb9a4:8", "const:4:8"]]
- 006fb9a4 ["CALL", null, ["ram:6f04c0:8"]]
+ 006fb9e4 ["INT_ADD", "register:40f0:8", ["const:6fb9e4:8", "const:4:8"]]
+ 006fb9e4 ["CALL", null, ["ram:6f0500:8"]]
- 006fb9a4 bytes c7d2ff97
+ 006fb9e4 bytes c7d2ff97
- 006fb908 ["INT_ADD", "register:40f0:8", ["const:6fb908:8", "const:4:8"]]
- 006fb908 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fb948 ["INT_ADD", "register:40f0:8", ["const:6fb948:8", "const:4:8"]]
+ 006fb948 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fb908 bytes 2305f697
+ 006fb948 bytes 2305f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4c9a969f4b8bb12cd95c067639f4ce2"></a>

### [`006fb9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb9f8.md) → [`006fba38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba38.md) FUN_006fba38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fba58",
      "incomplete_value": false,
      "site": "006fba5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fba18",
      "incomplete_value": false,
      "site": "006fba1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fba5c",
      "DATA",
      [
        "storage",
        "00c76798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fba5c",
      "DATA",
      [
        "storage",
        "00c76b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb9f8.md#insn-006fba0c) · [`006fba18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb9f8.md#insn-006fba18)
- 新版 [`006fba4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba38.md#insn-006fba4c) · [`006fba58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba38.md#insn-006fba58)

~~~diff
- 006fba0c ["INT_ADD", "register:40f0:8", ["const:6fba0c:8", "const:4:8"]]
- 006fba0c ["CALL", null, ["callee:00c57e90:8"]]
+ 006fba4c ["INT_ADD", "register:40f0:8", ["const:6fba4c:8", "const:4:8"]]
+ 006fba4c ["CALL", null, ["callee:00c57e90:8"]]
- 006fba0c bytes 21701594
+ 006fba4c bytes 11711594
- 006fba18 ["COPY", "tmp:0:8", ["const:798:8"]]
- 006fba18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fba18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fba18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fba58 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 006fba58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fba18 bytes 08611e91
+ 006fba58 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adc4e9597a31ab9f4df1e7f149a9ab3c"></a>

### [`006fba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba30.md) → [`006fba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba70.md) FUN_006fba70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fba74",
      "incomplete_value": false,
      "site": "006fba78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fba34",
      "incomplete_value": false,
      "site": "006fba38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fba78",
      "DATA",
      [
        "storage",
        "00c76798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fba78",
      "DATA",
      [
        "storage",
        "00c76b98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fba34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba30.md#insn-006fba34)
- 新版 [`006fba74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba70.md#insn-006fba74)

~~~diff
- 006fba34 ["COPY", "tmp:0:8", ["const:798:8"]]
- 006fba34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fba34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fba34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fba74 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 006fba74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fba34 bytes 08611e91
+ 006fba74 bytes 08612e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6978509a43d65f12bf4b0212e585f85"></a>

### [`006fba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba50.md) → [`006fba90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba90.md) FUN_006fba90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbbf8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbbb8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbbf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006fbbf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba50.md#insn-006fbbb8) · [`006fba74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba50.md#insn-006fba74) · [`006fba88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fba50.md#insn-006fba88)
- 新版 [`006fbbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba90.md#insn-006fbbf8) · [`006fbab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba90.md#insn-006fbab4) · [`006fbac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fba90.md#insn-006fbac8)

~~~diff
- 006fbbb8 ["INT_ADD", "register:40f0:8", ["const:6fbbb8:8", "const:4:8"]]
- 006fbbb8 ["CALL", null, ["ram:46c984:8"]]
+ 006fbbf8 ["INT_ADD", "register:40f0:8", ["const:6fbbf8:8", "const:4:8"]]
+ 006fbbf8 ["CALL", null, ["ram:46c9c4:8"]]
- 006fbbb8 bytes 73c3f597
+ 006fbbf8 bytes 73c3f597
- 006fba74 ["INT_ADD", "register:40f0:8", ["const:6fba74:8", "const:4:8"]]
- 006fba74 ["CALL", null, ["callee:008b9290:8"]]
+ 006fbab4 ["INT_ADD", "register:40f0:8", ["const:6fbab4:8", "const:4:8"]]
+ 006fbab4 ["CALL", null, ["callee:008b9290:8"]]
- 006fba74 bytes f6f50694
+ 006fbab4 bytes f7f50694
- 006fba88 ["INT_ADD", "register:40f0:8", ["const:6fba88:8", "const:4:8"]]
- 006fba88 ["CALL", null, ["callee:008b9298:8"]]
+ 006fbac8 ["INT_ADD", "register:40f0:8", ["const:6fbac8:8", "const:4:8"]]
+ 006fbac8 ["CALL", null, ["callee:008b9298:8"]]
- 006fba88 bytes f3f50694
+ 006fbac8 bytes f4f50694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061160da3e8247fa962b97304608c402"></a>

### [`006fbc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc1c.md) → [`006fbc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbc5c.md) FUN_006fbc5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fbc80",
      "incomplete_value": false,
      "site": "006fbc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbc40",
      "incomplete_value": false,
      "site": "006fbc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbc80",
      "DATA",
      [
        "storage",
        "00c76818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbc80",
      "DATA",
      [
        "storage",
        "00c76c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc1c.md#insn-006fbc30) · [`006fbc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc1c.md#insn-006fbc3c)
- 新版 [`006fbc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbc5c.md#insn-006fbc70) · [`006fbc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbc5c.md#insn-006fbc7c)

~~~diff
- 006fbc30 ["INT_ADD", "register:40f0:8", ["const:6fbc30:8", "const:4:8"]]
- 006fbc30 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fbc70 ["INT_ADD", "register:40f0:8", ["const:6fbc70:8", "const:4:8"]]
+ 006fbc70 ["CALL", null, ["callee:00c57e90:8"]]
- 006fbc30 bytes 986f1594
+ 006fbc70 bytes 88701594
- 006fbc3c ["COPY", "tmp:0:8", ["const:818:8"]]
- 006fbc3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fbc3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fbc3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fbc7c ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 006fbc7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbc7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbc7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fbc3c bytes 08612091
+ 006fbc7c bytes 08613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3f7166223047b31af9133f5ca58b10"></a>

### [`006fbc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc50.md) → [`006fbc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbc90.md) FUN_006fbc90

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fbc9c",
      "incomplete_value": false,
      "site": "006fbc9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fbc5c",
      "incomplete_value": false,
      "site": "006fbc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbc9c",
      "DATA",
      [
        "storage",
        "00c76818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbc9c",
      "DATA",
      [
        "storage",
        "00c76c18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc50.md#insn-006fbc58)
- 新版 [`006fbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbc90.md#insn-006fbc98)

~~~diff
- 006fbc58 ["COPY", "tmp:0:8", ["const:818:8"]]
- 006fbc58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fbc58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fbc58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fbc98 ["COPY", "tmp:0:8", ["const:c18:8"]]
+ 006fbc98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fbc98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fbc98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fbc58 bytes 29612091
+ 006fbc98 bytes 29613091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32967e116013e26acd9b20dc906c7762"></a>

### [`006fbc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md) → [`006fbcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md) FUN_006fbcac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006b23e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b23e4.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006b2424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2424.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006f0500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0500.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbcd8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbc98",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006fbd80",
      "value": [
        "leaf",
        "ram:6f0500:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbd40",
      "value": [
        "leaf",
        "ram:6f04c0:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbcd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fbd80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f04c0"
      ]
    ],
    [
      "006fbd98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea548"
      ]
    ]
  ],
  "added": [
    [
      "006fbcd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fbd80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0500"
      ]
    ],
    [
      "006fbd98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbc98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md#insn-006fbc98) · [`006fbd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md#insn-006fbd40) · [`006fbca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md#insn-006fbca4)
- 新版 [`006fbcd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md#insn-006fbcd8) · [`006fbd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md#insn-006fbd80) · [`006fbce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbcac.md#insn-006fbce4)

~~~diff
- 006fbc98 ["INT_ADD", "register:40f0:8", ["const:6fbc98:8", "const:4:8"]]
- 006fbc98 ["CALL", null, ["ram:47acb4:8"]]
+ 006fbcd8 ["INT_ADD", "register:40f0:8", ["const:6fbcd8:8", "const:4:8"]]
+ 006fbcd8 ["CALL", null, ["ram:47acf4:8"]]
- 006fbc98 bytes 07fcf597
+ 006fbcd8 bytes 07fcf597
- 006fbd40 ["INT_ADD", "register:40f0:8", ["const:6fbd40:8", "const:4:8"]]
- 006fbd40 ["CALL", null, ["ram:6f04c0:8"]]
+ 006fbd80 ["INT_ADD", "register:40f0:8", ["const:6fbd80:8", "const:4:8"]]
+ 006fbd80 ["CALL", null, ["ram:6f0500:8"]]
- 006fbd40 bytes e0d1ff97
+ 006fbd80 bytes e0d1ff97
- 006fbca4 ["INT_ADD", "register:40f0:8", ["const:6fbca4:8", "const:4:8"]]
- 006fbca4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fbce4 ["INT_ADD", "register:40f0:8", ["const:6fbce4:8", "const:4:8"]]
+ 006fbce4 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fbca4 bytes 3c04f697
+ 006fbce4 bytes 3c04f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e17e2c12267d791c665fd5b9ebbf701"></a>

### [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) → [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) FUN_006fbdd0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) · 呼出先 5件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006e53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md) [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) [`006fc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md) · 呼出先 5件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) [`006fc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md) [`006fc4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbe28",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbde8",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fbe3c",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbdfc",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fbeb8",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbe78",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fbe28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fbe3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fbeb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fbe28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fbe3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fbeb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fbde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md#insn-006fbde8) · [`006fbdfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md#insn-006fbdfc) · [`006fbe78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md#insn-006fbe78)
- 新版 [`006fbe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md#insn-006fbe28) · [`006fbe3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md#insn-006fbe3c) · [`006fbeb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md#insn-006fbeb8)

~~~diff
- 006fbde8 ["INT_ADD", "register:40f0:8", ["const:6fbde8:8", "const:4:8"]]
- 006fbde8 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fbe28 ["INT_ADD", "register:40f0:8", ["const:6fbe28:8", "const:4:8"]]
+ 006fbe28 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fbde8 bytes 27a3ff97
+ 006fbe28 bytes 27a3ff97
- 006fbdfc ["INT_ADD", "register:40f0:8", ["const:6fbdfc:8", "const:4:8"]]
- 006fbdfc ["CALL", null, ["ram:6e4a84:8"]]
+ 006fbe3c ["INT_ADD", "register:40f0:8", ["const:6fbe3c:8", "const:4:8"]]
+ 006fbe3c ["CALL", null, ["ram:6e4ac4:8"]]
- 006fbdfc bytes 22a3ff97
+ 006fbe3c bytes 22a3ff97
- 006fbe78 ["INT_ADD", "register:40f0:8", ["const:6fbe78:8", "const:4:8"]]
- 006fbe78 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fbeb8 ["INT_ADD", "register:40f0:8", ["const:6fbeb8:8", "const:4:8"]]
+ 006fbeb8 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fbe78 bytes 03a3ff97
+ 006fbeb8 bytes 03a3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eecd4fc6f19bb28c8acc0355e52f944"></a>

### [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) → [`006fc15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md) FUN_006fc15c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) · 呼出先 3件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) · 呼出先 3件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc1ac",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc16c",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fc1c0",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc180",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fc258",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc218",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fc1ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fc1ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fc1c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fc258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fc16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md#insn-006fc16c) · [`006fc180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md#insn-006fc180) · [`006fc218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md#insn-006fc218)
- 新版 [`006fc1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md#insn-006fc1ac) · [`006fc1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md#insn-006fc1c0) · [`006fc258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc15c.md#insn-006fc258)

~~~diff
- 006fc16c ["INT_ADD", "register:40f0:8", ["const:6fc16c:8", "const:4:8"]]
- 006fc16c ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc1ac ["INT_ADD", "register:40f0:8", ["const:6fc1ac:8", "const:4:8"]]
+ 006fc1ac ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc16c bytes 46a2ff97
+ 006fc1ac bytes 46a2ff97
- 006fc180 ["INT_ADD", "register:40f0:8", ["const:6fc180:8", "const:4:8"]]
- 006fc180 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc1c0 ["INT_ADD", "register:40f0:8", ["const:6fc1c0:8", "const:4:8"]]
+ 006fc1c0 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc180 bytes 41a2ff97
+ 006fc1c0 bytes 41a2ff97
- 006fc218 ["INT_ADD", "register:40f0:8", ["const:6fc218:8", "const:4:8"]]
- 006fc218 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc258 ["INT_ADD", "register:40f0:8", ["const:6fc258:8", "const:4:8"]]
+ 006fc258 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc218 bytes 1ba2ff97
+ 006fc258 bytes 1ba2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2fdde16009fc275adee57387f412648"></a>

### [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) → [`006fc4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md) FUN_006fc4ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) · 呼出先 4件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`006fbdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fb/006fbdd0.md) [`006fc4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md) · 呼出先 4件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fc4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc518",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc4d8",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fc52c",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc4ec",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fc5b0",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fc570",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fc518",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc5b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fc518",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fc52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fc5b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md#insn-006fc4d8) · [`006fc4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md#insn-006fc4ec) · [`006fc570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md#insn-006fc570)
- 新版 [`006fc518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md#insn-006fc518) · [`006fc52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md#insn-006fc52c) · [`006fc5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fc4ac.md#insn-006fc5b0)

~~~diff
- 006fc4d8 ["INT_ADD", "register:40f0:8", ["const:6fc4d8:8", "const:4:8"]]
- 006fc4d8 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc518 ["INT_ADD", "register:40f0:8", ["const:6fc518:8", "const:4:8"]]
+ 006fc518 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc4d8 bytes 6ba1ff97
+ 006fc518 bytes 6ba1ff97
- 006fc4ec ["INT_ADD", "register:40f0:8", ["const:6fc4ec:8", "const:4:8"]]
- 006fc4ec ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc52c ["INT_ADD", "register:40f0:8", ["const:6fc52c:8", "const:4:8"]]
+ 006fc52c ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc4ec bytes 66a1ff97
+ 006fc52c bytes 66a1ff97
- 006fc570 ["INT_ADD", "register:40f0:8", ["const:6fc570:8", "const:4:8"]]
- 006fc570 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fc5b0 ["INT_ADD", "register:40f0:8", ["const:6fc5b0:8", "const:4:8"]]
+ 006fc5b0 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fc570 bytes 45a1ff97
+ 006fc5b0 bytes 45a1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d0047a8aaed34f7293a41608dda331"></a>

### [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) → [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) FUN_006fcb74

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) · 呼出先 5件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006e53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md) [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) [`006fcf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md) · 呼出先 5件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) [`006fcf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md) [`006fd250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.48% / 新版 96.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcbcc",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcb8c",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fcbe0",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcba0",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fcc5c",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcc1c",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fcbcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fcbe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fcc5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fcbcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fcbe0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fcc5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fcb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md#insn-006fcb8c) · [`006fcba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md#insn-006fcba0) · [`006fcc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md#insn-006fcc1c)
- 新版 [`006fcbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md#insn-006fcbcc) · [`006fcbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md#insn-006fcbe0) · [`006fcc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md#insn-006fcc5c)

~~~diff
- 006fcb8c ["INT_ADD", "register:40f0:8", ["const:6fcb8c:8", "const:4:8"]]
- 006fcb8c ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcbcc ["INT_ADD", "register:40f0:8", ["const:6fcbcc:8", "const:4:8"]]
+ 006fcbcc ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcb8c bytes be9fff97
+ 006fcbcc bytes be9fff97
- 006fcba0 ["INT_ADD", "register:40f0:8", ["const:6fcba0:8", "const:4:8"]]
- 006fcba0 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcbe0 ["INT_ADD", "register:40f0:8", ["const:6fcbe0:8", "const:4:8"]]
+ 006fcbe0 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcba0 bytes b99fff97
+ 006fcbe0 bytes b99fff97
- 006fcc1c ["INT_ADD", "register:40f0:8", ["const:6fcc1c:8", "const:4:8"]]
- 006fcc1c ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcc5c ["INT_ADD", "register:40f0:8", ["const:6fcc5c:8", "const:4:8"]]
+ 006fcc5c ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcc1c bytes 9a9fff97
+ 006fcc5c bytes 9a9fff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e55dc3c2520c9ad41a258dd3f3148fb"></a>

### [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) → [`006fcf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md) FUN_006fcf00

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) · 呼出先 3件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) · 呼出先 3件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcf50",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcf10",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fcf64",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcf24",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fcffc",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcfbc",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fcf50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fcf64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fcffc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fcf50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fcf64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fcffc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fcf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md#insn-006fcf10) · [`006fcf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md#insn-006fcf24) · [`006fcfbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md#insn-006fcfbc)
- 新版 [`006fcf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md#insn-006fcf50) · [`006fcf64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md#insn-006fcf64) · [`006fcffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcf00.md#insn-006fcffc)

~~~diff
- 006fcf10 ["INT_ADD", "register:40f0:8", ["const:6fcf10:8", "const:4:8"]]
- 006fcf10 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcf50 ["INT_ADD", "register:40f0:8", ["const:6fcf50:8", "const:4:8"]]
+ 006fcf50 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcf10 bytes dd9eff97
+ 006fcf50 bytes dd9eff97
- 006fcf24 ["INT_ADD", "register:40f0:8", ["const:6fcf24:8", "const:4:8"]]
- 006fcf24 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcf64 ["INT_ADD", "register:40f0:8", ["const:6fcf64:8", "const:4:8"]]
+ 006fcf64 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcf24 bytes d89eff97
+ 006fcf64 bytes d89eff97
- 006fcfbc ["INT_ADD", "register:40f0:8", ["const:6fcfbc:8", "const:4:8"]]
- 006fcfbc ["CALL", null, ["ram:6e4a84:8"]]
+ 006fcffc ["INT_ADD", "register:40f0:8", ["const:6fcffc:8", "const:4:8"]]
+ 006fcffc ["CALL", null, ["ram:6e4ac4:8"]]
- 006fcfbc bytes b29eff97
+ 006fcffc bytes b29eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab3f7cd93ab71c2adcd481f90c7cfb89"></a>

### [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) → [`006fd250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md) FUN_006fd250

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) · 呼出先 4件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 2件 [`006fcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fc/006fcb74.md) [`006fd250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md) · 呼出先 4件 [`006e4ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4ac4.md) [`006fd250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd2bc",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd27c",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fd2d0",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd290",
      "value": [
        "leaf",
        "ram:6e4a84:8"
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
      "site": "006fd354",
      "value": [
        "leaf",
        "ram:6e4ac4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd314",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fd2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fd2d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fd354",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ],
  "added": [
    [
      "006fd2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fd2d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ],
    [
      "006fd354",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4ac4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md#insn-006fd27c) · [`006fd290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md#insn-006fd290) · [`006fd314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md#insn-006fd314)
- 新版 [`006fd2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md#insn-006fd2bc) · [`006fd2d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md#insn-006fd2d0) · [`006fd354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd250.md#insn-006fd354)

~~~diff
- 006fd27c ["INT_ADD", "register:40f0:8", ["const:6fd27c:8", "const:4:8"]]
- 006fd27c ["CALL", null, ["ram:6e4a84:8"]]
+ 006fd2bc ["INT_ADD", "register:40f0:8", ["const:6fd2bc:8", "const:4:8"]]
+ 006fd2bc ["CALL", null, ["ram:6e4ac4:8"]]
- 006fd27c bytes 029eff97
+ 006fd2bc bytes 029eff97
- 006fd290 ["INT_ADD", "register:40f0:8", ["const:6fd290:8", "const:4:8"]]
- 006fd290 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fd2d0 ["INT_ADD", "register:40f0:8", ["const:6fd2d0:8", "const:4:8"]]
+ 006fd2d0 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fd290 bytes fd9dff97
+ 006fd2d0 bytes fd9dff97
- 006fd314 ["INT_ADD", "register:40f0:8", ["const:6fd314:8", "const:4:8"]]
- 006fd314 ["CALL", null, ["ram:6e4a84:8"]]
+ 006fd354 ["INT_ADD", "register:40f0:8", ["const:6fd354:8", "const:4:8"]]
+ 006fd354 ["CALL", null, ["ram:6e4ac4:8"]]
- 006fd314 bytes dc9dff97
+ 006fd354 bytes dc9dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3b5ab65ce0f8baf0a15e5217bfda227"></a>

### [`006fd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd8dc.md) → [`006fd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd91c.md) FUN_006fd91c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fd930",
      "incomplete_value": false,
      "site": "006fd934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fd8f0",
      "incomplete_value": false,
      "site": "006fd8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fd934",
      "DATA",
      [
        "storage",
        "00c76898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fd934",
      "DATA",
      [
        "storage",
        "00c76c98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd8dc.md#insn-006fd8e8) · [`006fd8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd8dc.md#insn-006fd8f0)
- 新版 [`006fd928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd91c.md#insn-006fd928) · [`006fd930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd91c.md#insn-006fd930)

~~~diff
- 006fd8e8 ["INT_ADD", "register:40f0:8", ["const:6fd8e8:8", "const:4:8"]]
- 006fd8e8 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fd928 ["INT_ADD", "register:40f0:8", ["const:6fd928:8", "const:4:8"]]
+ 006fd928 ["CALL", null, ["callee:00c57e90:8"]]
- 006fd8e8 bytes 6a681594
+ 006fd928 bytes 5a691594
- 006fd8f0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 006fd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fd930 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 006fd930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fd8f0 bytes 08612291
+ 006fd930 bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e17ed19483022d6e13274731425b29a"></a>

### [`006fd918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd918.md) → [`006fd958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd958.md) FUN_006fd958

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd974",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fd934",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fd974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006fd974",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd918.md#insn-006fd934) · [`006fd940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd918.md#insn-006fd940)
- 新版 [`006fd974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd958.md#insn-006fd974) · [`006fd980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd958.md#insn-006fd980)

~~~diff
- 006fd934 ["INT_ADD", "register:40f0:8", ["const:6fd934:8", "const:4:8"]]
- 006fd934 ["CALL", null, ["ram:47acb4:8"]]
+ 006fd974 ["INT_ADD", "register:40f0:8", ["const:6fd974:8", "const:4:8"]]
+ 006fd974 ["CALL", null, ["ram:47acf4:8"]]
- 006fd934 bytes e0f4f597
+ 006fd974 bytes e0f4f597
- 006fd940 ["INT_ADD", "register:40f0:8", ["const:6fd940:8", "const:4:8"]]
- 006fd940 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fd980 ["INT_ADD", "register:40f0:8", ["const:6fd980:8", "const:4:8"]]
+ 006fd980 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fd940 bytes 15fdf597
+ 006fd980 bytes 15fdf597
~~~


<a id="compare-a1a572564b36c92b9b72f932006a0232"></a>

### [`006fd984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd984.md) → [`006fd9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd9c4.md) FUN_006fd9c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fd9e8",
      "incomplete_value": false,
      "site": "006fd9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fd9a8",
      "incomplete_value": false,
      "site": "006fd9ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fd9ec",
      "DATA",
      [
        "storage",
        "00c76918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fd9ec",
      "DATA",
      [
        "storage",
        "00c76d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fd998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd984.md#insn-006fd998) · [`006fd9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd984.md#insn-006fd9a8)
- 新版 [`006fd9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd9c4.md#insn-006fd9d8) · [`006fd9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fd9c4.md#insn-006fd9e8)

~~~diff
- 006fd998 ["INT_ADD", "register:40f0:8", ["const:6fd998:8", "const:4:8"]]
- 006fd998 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fd9d8 ["INT_ADD", "register:40f0:8", ["const:6fd9d8:8", "const:4:8"]]
+ 006fd9d8 ["CALL", null, ["callee:00c57e90:8"]]
- 006fd998 bytes 3e681594
+ 006fd9d8 bytes 2e691594
- 006fd9a8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 006fd9a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fd9a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fd9a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fd9e8 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 006fd9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fd9a8 bytes 08612491
+ 006fd9e8 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4252470597f0e8260d944559dde0c80"></a>

### [`006fd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md) → [`006fda2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md) FUN_006fda2c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fdb30",
      "incomplete_value": true,
      "site": "006fdb44",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:edf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fdaf0",
      "incomplete_value": true,
      "site": "006fdb04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e9f:8"
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
      "definition_site": "006fdb84",
      "incomplete_value": true,
      "site": "006fdb84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c8b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fdb44",
      "incomplete_value": true,
      "site": "006fdb44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c4b:8"
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
      "definition_site": "006fdb88",
      "incomplete_value": true,
      "site": "006fdb88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006fdb48",
      "incomplete_value": true,
      "site": "006fdb48",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fda78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fdad8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006edda4"
      ]
    ],
    [
      "006fdafc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063c548"
      ]
    ]
  ],
  "added": [
    [
      "006fda78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fdad8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006edde4"
      ]
    ],
    [
      "006fdafc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063c588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fda38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md#insn-006fda38) · [`006fda98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md#insn-006fda98) · [`006fdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md#insn-006fdabc)
- 新版 [`006fda78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md#insn-006fda78) · [`006fdad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md#insn-006fdad8) · [`006fdafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fd/006fda2c.md#insn-006fdafc)

~~~diff
- 006fda38 ["INT_ADD", "register:40f0:8", ["const:6fda38:8", "const:4:8"]]
- 006fda38 ["CALL", null, ["ram:47acb4:8"]]
+ 006fda78 ["INT_ADD", "register:40f0:8", ["const:6fda78:8", "const:4:8"]]
+ 006fda78 ["CALL", null, ["ram:47acf4:8"]]
- 006fda38 bytes 9ff4f597
+ 006fda78 bytes 9ff4f597
- 006fda98 ["INT_ADD", "register:40f0:8", ["const:6fda98:8", "const:4:8"]]
- 006fda98 ["CALL", null, ["ram:6edda4:8"]]
+ 006fdad8 ["INT_ADD", "register:40f0:8", ["const:6fdad8:8", "const:4:8"]]
+ 006fdad8 ["CALL", null, ["ram:6edde4:8"]]
- 006fda98 bytes c3c0ff97
+ 006fdad8 bytes c3c0ff97
- 006fdabc ["INT_ADD", "register:40f0:8", ["const:6fdabc:8", "const:4:8"]]
- 006fdabc ["CALL", null, ["ram:63c548:8"]]
+ 006fdafc ["INT_ADD", "register:40f0:8", ["const:6fdafc:8", "const:4:8"]]
+ 006fdafc ["CALL", null, ["ram:63c588:8"]]
- 006fdabc bytes a3fafc97
+ 006fdafc bytes a3fafc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59f49117ff8fe3a14f8fceac04a2f87"></a>

### [`006fe0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe0f8.md) → [`006fe138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe138.md) FUN_006fe138

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe158",
      "incomplete_value": false,
      "site": "006fe15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe118",
      "incomplete_value": false,
      "site": "006fe11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe15c",
      "DATA",
      [
        "storage",
        "00c76988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe15c",
      "DATA",
      [
        "storage",
        "00c76d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe0f8.md#insn-006fe10c) · [`006fe118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe0f8.md#insn-006fe118)
- 新版 [`006fe14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe138.md#insn-006fe14c) · [`006fe158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe138.md#insn-006fe158)

~~~diff
- 006fe10c ["INT_ADD", "register:40f0:8", ["const:6fe10c:8", "const:4:8"]]
- 006fe10c ["CALL", null, ["callee:00c57e90:8"]]
+ 006fe14c ["INT_ADD", "register:40f0:8", ["const:6fe14c:8", "const:4:8"]]
+ 006fe14c ["CALL", null, ["callee:00c57e90:8"]]
- 006fe10c bytes 61661594
+ 006fe14c bytes 51671594
- 006fe118 ["COPY", "tmp:0:8", ["const:988:8"]]
- 006fe118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe158 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 006fe158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe118 bytes 08212691
+ 006fe158 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbfb3b220b5214e22d5a7c513b04913b"></a>

### [`006fe130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe130.md) → [`006fe170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe170.md) FUN_006fe170

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe174",
      "incomplete_value": false,
      "site": "006fe178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe134",
      "incomplete_value": false,
      "site": "006fe138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe178",
      "DATA",
      [
        "storage",
        "00c76988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe178",
      "DATA",
      [
        "storage",
        "00c76d88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe130.md#insn-006fe134)
- 新版 [`006fe174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe170.md#insn-006fe174)

~~~diff
- 006fe134 ["COPY", "tmp:0:8", ["const:988:8"]]
- 006fe134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe174 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 006fe174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe134 bytes 08212691
+ 006fe174 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c5902020aaa3dd360582de961933d47"></a>

### [`006fe150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe150.md) → [`006fe190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe190.md) FUN_006fe190

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006f0500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0500.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe1bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe17c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006fe210",
      "value": [
        "leaf",
        "ram:6f0500:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe1d0",
      "value": [
        "leaf",
        "ram:6f04c0:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe1bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f04c0"
      ]
    ],
    [
      "006fe228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea548"
      ]
    ]
  ],
  "added": [
    [
      "006fe1bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fe210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0500"
      ]
    ],
    [
      "006fe228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe150.md#insn-006fe17c) · [`006fe1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe150.md#insn-006fe1bc) · [`006fe1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe150.md#insn-006fe1d0)
- 新版 [`006fe1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe190.md#insn-006fe1bc) · [`006fe1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe190.md#insn-006fe1fc) · [`006fe210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe190.md#insn-006fe210)

~~~diff
- 006fe17c ["INT_ADD", "register:40f0:8", ["const:6fe17c:8", "const:4:8"]]
- 006fe17c ["CALL", null, ["ram:47acb4:8"]]
+ 006fe1bc ["INT_ADD", "register:40f0:8", ["const:6fe1bc:8", "const:4:8"]]
+ 006fe1bc ["CALL", null, ["ram:47acf4:8"]]
- 006fe17c bytes cef2f597
+ 006fe1bc bytes cef2f597
- 006fe1bc ["INT_ADD", "register:40f0:8", ["const:6fe1bc:8", "const:4:8"]]
- 006fe1bc ["CALL", null, ["callee:008514f8:8"]]
+ 006fe1fc ["INT_ADD", "register:40f0:8", ["const:6fe1fc:8", "const:4:8"]]
+ 006fe1fc ["CALL", null, ["callee:008514f8:8"]]
- 006fe1bc bytes bf4c0594
+ 006fe1fc bytes bf4c0594
- 006fe1d0 ["INT_ADD", "register:40f0:8", ["const:6fe1d0:8", "const:4:8"]]
- 006fe1d0 ["CALL", null, ["ram:6f04c0:8"]]
+ 006fe210 ["INT_ADD", "register:40f0:8", ["const:6fe210:8", "const:4:8"]]
+ 006fe210 ["CALL", null, ["ram:6f0500:8"]]
- 006fe1d0 bytes bcc8ff97
+ 006fe210 bytes bcc8ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bc9f2a672a1df433db849bd2c9eff84"></a>

### [`006fe230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe230.md) → [`006fe270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe270.md) FUN_006fe270

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe290",
      "incomplete_value": false,
      "site": "006fe294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe250",
      "incomplete_value": false,
      "site": "006fe254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe294",
      "DATA",
      [
        "storage",
        "00c76a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe294",
      "DATA",
      [
        "storage",
        "00c76e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe230.md#insn-006fe244) · [`006fe250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe230.md#insn-006fe250)
- 新版 [`006fe284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe270.md#insn-006fe284) · [`006fe290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe270.md#insn-006fe290)

~~~diff
- 006fe244 ["INT_ADD", "register:40f0:8", ["const:6fe244:8", "const:4:8"]]
- 006fe244 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fe284 ["INT_ADD", "register:40f0:8", ["const:6fe284:8", "const:4:8"]]
+ 006fe284 ["CALL", null, ["callee:00c57e90:8"]]
- 006fe244 bytes 13661594
+ 006fe284 bytes 03671594
- 006fe250 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 006fe250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe290 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 006fe290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe250 bytes 08612891
+ 006fe290 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4adeb6b643fb467e544f8a557d6f81f3"></a>

### [`006fe288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe288.md) → [`006fe2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe2c8.md) FUN_006fe2c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.04% / 新版 99.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe430",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe3f0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006fe430",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe288.md#insn-006fe3f0) · [`006fe2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe288.md#insn-006fe2ac) · [`006fe2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe288.md#insn-006fe2c0)
- 新版 [`006fe430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe2c8.md#insn-006fe430) · [`006fe2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe2c8.md#insn-006fe2ec) · [`006fe300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe2c8.md#insn-006fe300)

~~~diff
- 006fe3f0 ["INT_ADD", "register:40f0:8", ["const:6fe3f0:8", "const:4:8"]]
- 006fe3f0 ["CALL", null, ["ram:46c984:8"]]
+ 006fe430 ["INT_ADD", "register:40f0:8", ["const:6fe430:8", "const:4:8"]]
+ 006fe430 ["CALL", null, ["ram:46c9c4:8"]]
- 006fe3f0 bytes 65b9f597
+ 006fe430 bytes 65b9f597
- 006fe2ac ["INT_ADD", "register:40f0:8", ["const:6fe2ac:8", "const:4:8"]]
- 006fe2ac ["CALL", null, ["callee:008b9290:8"]]
+ 006fe2ec ["INT_ADD", "register:40f0:8", ["const:6fe2ec:8", "const:4:8"]]
+ 006fe2ec ["CALL", null, ["callee:008b9290:8"]]
- 006fe2ac bytes e8eb0694
+ 006fe2ec bytes e9eb0694
- 006fe2c0 ["INT_ADD", "register:40f0:8", ["const:6fe2c0:8", "const:4:8"]]
- 006fe2c0 ["CALL", null, ["callee:008b9298:8"]]
+ 006fe300 ["INT_ADD", "register:40f0:8", ["const:6fe300:8", "const:4:8"]]
+ 006fe300 ["CALL", null, ["callee:008b9298:8"]]
- 006fe2c0 bytes e5eb0694
+ 006fe300 bytes e6eb0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68dd5bd8d8a185fe4c2b70ef0cc5df01"></a>

### [`006fe4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe4ac.md) → [`006fe4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe4ec.md) FUN_006fe4ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`006ea588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ea/006ea588.md) [`006f0500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f0/006f0500.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe514",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe4d4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006fe558",
      "value": [
        "leaf",
        "ram:6f0500:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe518",
      "value": [
        "leaf",
        "ram:6f04c0:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe514",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe558",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f04c0"
      ]
    ],
    [
      "006fe570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea548"
      ]
    ]
  ],
  "added": [
    [
      "006fe514",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fe558",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f0500"
      ]
    ],
    [
      "006fe570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea588"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe4ac.md#insn-006fe4d4) · [`006fe518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe4ac.md#insn-006fe518) · [`006fe4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe4ac.md#insn-006fe4e0)
- 新版 [`006fe514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe4ec.md#insn-006fe514) · [`006fe558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe4ec.md#insn-006fe558) · [`006fe520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe4ec.md#insn-006fe520)

~~~diff
- 006fe4d4 ["INT_ADD", "register:40f0:8", ["const:6fe4d4:8", "const:4:8"]]
- 006fe4d4 ["CALL", null, ["ram:47acb4:8"]]
+ 006fe514 ["INT_ADD", "register:40f0:8", ["const:6fe514:8", "const:4:8"]]
+ 006fe514 ["CALL", null, ["ram:47acf4:8"]]
- 006fe4d4 bytes f8f1f597
+ 006fe514 bytes f8f1f597
- 006fe518 ["INT_ADD", "register:40f0:8", ["const:6fe518:8", "const:4:8"]]
- 006fe518 ["CALL", null, ["ram:6f04c0:8"]]
+ 006fe558 ["INT_ADD", "register:40f0:8", ["const:6fe558:8", "const:4:8"]]
+ 006fe558 ["CALL", null, ["ram:6f0500:8"]]
- 006fe518 bytes eac7ff97
+ 006fe558 bytes eac7ff97
- 006fe4e0 ["INT_ADD", "register:40f0:8", ["const:6fe4e0:8", "const:4:8"]]
- 006fe4e0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fe520 ["INT_ADD", "register:40f0:8", ["const:6fe520:8", "const:4:8"]]
+ 006fe520 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fe4e0 bytes 2dfaf597
+ 006fe520 bytes 2dfaf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa2dff95617518c54a3f58167d954fc"></a>

### [`006fe56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe56c.md) → [`006fe5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe5ac.md) FUN_006fe5ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe5cc",
      "incomplete_value": false,
      "site": "006fe5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe58c",
      "incomplete_value": false,
      "site": "006fe590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe5d0",
      "DATA",
      [
        "storage",
        "00c76b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe5d0",
      "DATA",
      [
        "storage",
        "00c76f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe56c.md#insn-006fe580) · [`006fe58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe56c.md#insn-006fe58c)
- 新版 [`006fe5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe5ac.md#insn-006fe5c0) · [`006fe5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe5ac.md#insn-006fe5cc)

~~~diff
- 006fe580 ["INT_ADD", "register:40f0:8", ["const:6fe580:8", "const:4:8"]]
- 006fe580 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fe5c0 ["INT_ADD", "register:40f0:8", ["const:6fe5c0:8", "const:4:8"]]
+ 006fe5c0 ["CALL", null, ["callee:00c57e90:8"]]
- 006fe580 bytes 44651594
+ 006fe5c0 bytes 34661594
- 006fe58c ["COPY", "tmp:0:8", ["const:b18:8"]]
- 006fe58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe5cc ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 006fe5cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe5cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe5cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe58c bytes 08612c91
+ 006fe5cc bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3ecc58f3d8eb548c5345449c083e7ed"></a>

### [`006fe5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5a4.md) → [`006fe5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe5e4.md) FUN_006fe5e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe5e8",
      "incomplete_value": false,
      "site": "006fe5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe5a8",
      "incomplete_value": false,
      "site": "006fe5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe5ec",
      "DATA",
      [
        "storage",
        "00c76b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe5ec",
      "DATA",
      [
        "storage",
        "00c76f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5a4.md#insn-006fe5a8)
- 新版 [`006fe5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe5e4.md#insn-006fe5e8)

~~~diff
- 006fe5a8 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 006fe5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe5e8 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 006fe5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe5a8 bytes 08612c91
+ 006fe5e8 bytes 08613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5a9df2b9d52dc94264507f3a709bc37"></a>

### [`006fe5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md) → [`006fe604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe604.md) FUN_006fe604

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006ef704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`006e53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e5/006e53d4.md) [`006ef744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ef/006ef744.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 91.45% / 新版 91.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe708",
      "incomplete_value": true,
      "site": "006fe718",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:773:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe6c8",
      "incomplete_value": true,
      "site": "006fe6d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:733:8"
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
      "definition_site": "006fe71c",
      "incomplete_value": true,
      "site": "006fe71c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006fe6dc",
      "incomplete_value": true,
      "site": "006fe6dc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe734",
      "incomplete_value": true,
      "site": "006fe73c",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe6f4",
      "incomplete_value": true,
      "site": "006fe6fc",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ef704"
      ]
    ]
  ],
  "added": [
    [
      "006fe640",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fe660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fe6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ef744"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md#insn-006fe600) · [`006fe620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md#insn-006fe620) · [`006fe648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md#insn-006fe648)
- 新版 [`006fe640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe604.md#insn-006fe640) · [`006fe660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe604.md#insn-006fe660) · [`006fe688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe604.md#insn-006fe688)

~~~diff
- 006fe600 ["INT_ADD", "register:40f0:8", ["const:6fe600:8", "const:4:8"]]
- 006fe600 ["CALL", null, ["ram:47acb4:8"]]
+ 006fe640 ["INT_ADD", "register:40f0:8", ["const:6fe640:8", "const:4:8"]]
+ 006fe640 ["CALL", null, ["ram:47acf4:8"]]
- 006fe600 bytes adf1f597
+ 006fe640 bytes adf1f597
- 006fe620 ["INT_ADD", "register:40f0:8", ["const:6fe620:8", "const:4:8"]]
- 006fe620 ["CALL", null, ["ram:47acb4:8"]]
+ 006fe660 ["INT_ADD", "register:40f0:8", ["const:6fe660:8", "const:4:8"]]
+ 006fe660 ["CALL", null, ["ram:47acf4:8"]]
- 006fe620 bytes a5f1f597
+ 006fe660 bytes a5f1f597
- 006fe648 ["INT_ADD", "register:40f0:8", ["const:6fe648:8", "const:4:8"]]
- 006fe648 ["CALL", null, ["callee:008514f8:8"]]
+ 006fe688 ["INT_ADD", "register:40f0:8", ["const:6fe688:8", "const:4:8"]]
+ 006fe688 ["CALL", null, ["callee:008514f8:8"]]
- 006fe648 bytes 9c4b0594
+ 006fe688 bytes 9c4b0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eca3f1ca30d9c42a5daf5194ca28f44"></a>

### [`006fe854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe854.md) → [`006fe894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe894.md) FUN_006fe894

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe8a8",
      "incomplete_value": false,
      "site": "006fe8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe868",
      "incomplete_value": false,
      "site": "006fe86c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe8ac",
      "DATA",
      [
        "storage",
        "00c76b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe8ac",
      "DATA",
      [
        "storage",
        "00c76f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe854.md#insn-006fe860) · [`006fe868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe854.md#insn-006fe868)
- 新版 [`006fe8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe894.md#insn-006fe8a0) · [`006fe8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe894.md#insn-006fe8a8)

~~~diff
- 006fe860 ["INT_ADD", "register:40f0:8", ["const:6fe860:8", "const:4:8"]]
- 006fe860 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fe8a0 ["INT_ADD", "register:40f0:8", ["const:6fe8a0:8", "const:4:8"]]
+ 006fe8a0 ["CALL", null, ["callee:00c57e90:8"]]
- 006fe860 bytes 8c641594
+ 006fe8a0 bytes 7c651594
- 006fe868 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 006fe868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe8a8 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 006fe8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe868 bytes 08212e91
+ 006fe8a8 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c516bb538c02a2c227a88457490a5d05"></a>

### [`006fe878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe878.md) → [`006fe8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe8b8.md) FUN_006fe8b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe8bc",
      "incomplete_value": false,
      "site": "006fe8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe87c",
      "incomplete_value": false,
      "site": "006fe880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe8c0",
      "DATA",
      [
        "storage",
        "00c76b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe8c0",
      "DATA",
      [
        "storage",
        "00c76f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe878.md#insn-006fe87c)
- 新版 [`006fe8bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe8b8.md#insn-006fe8bc)

~~~diff
- 006fe87c ["COPY", "tmp:0:8", ["const:b88:8"]]
- 006fe87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 006fe8bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe8bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe87c bytes 08212e91
+ 006fe8bc bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bd2f42c232979f9790774dab87f4435"></a>

### [`006fe890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe890.md) → [`006fe8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe8d0.md) FUN_006fe8d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe8ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe8ac",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe8ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006fe8ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe890.md#insn-006fe8ac) · [`006fe8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe890.md#insn-006fe8b8)
- 新版 [`006fe8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe8d0.md#insn-006fe8ec) · [`006fe8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe8d0.md#insn-006fe8f8)

~~~diff
- 006fe8ac ["INT_ADD", "register:40f0:8", ["const:6fe8ac:8", "const:4:8"]]
- 006fe8ac ["CALL", null, ["ram:47acb4:8"]]
+ 006fe8ec ["INT_ADD", "register:40f0:8", ["const:6fe8ec:8", "const:4:8"]]
+ 006fe8ec ["CALL", null, ["ram:47acf4:8"]]
- 006fe8ac bytes 02f1f597
+ 006fe8ec bytes 02f1f597
- 006fe8b8 ["INT_ADD", "register:40f0:8", ["const:6fe8b8:8", "const:4:8"]]
- 006fe8b8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fe8f8 ["INT_ADD", "register:40f0:8", ["const:6fe8f8:8", "const:4:8"]]
+ 006fe8f8 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fe8b8 bytes 37f9f597
+ 006fe8f8 bytes 37f9f597
~~~


<a id="compare-0c01eadf1dc6d9ea03b14f0d9c7c1bdc"></a>

### [`006fe8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe8fc.md) → [`006fe93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe93c.md) FUN_006fe93c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe95c",
      "incomplete_value": false,
      "site": "006fe960",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe91c",
      "incomplete_value": false,
      "site": "006fe920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe960",
      "DATA",
      [
        "storage",
        "00c76c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe960",
      "DATA",
      [
        "storage",
        "00c77018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe8fc.md#insn-006fe910) · [`006fe918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe8fc.md#insn-006fe918) · [`006fe91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe8fc.md#insn-006fe91c)
- 新版 [`006fe950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe93c.md#insn-006fe950) · [`006fe958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe93c.md#insn-006fe958) · [`006fe95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe93c.md#insn-006fe95c)

~~~diff
- 006fe910 ["INT_ADD", "register:40f0:8", ["const:6fe910:8", "const:4:8"]]
- 006fe910 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fe950 ["INT_ADD", "register:40f0:8", ["const:6fe950:8", "const:4:8"]]
+ 006fe950 ["CALL", null, ["callee:00c57e90:8"]]
- 006fe910 bytes 60641594
+ 006fe950 bytes 50651594
- 006fe918 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe958 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe918 bytes c82b0090
+ 006fe958 bytes c82b00b0
- 006fe91c ["COPY", "tmp:0:8", ["const:c18:8"]]
- 006fe91c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe91c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe91c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe95c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 006fe95c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe95c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe95c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe91c bytes 08613091
+ 006fe95c bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-437b3edb9ba60d087425eb5a162022dd"></a>

### [`006fe934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe934.md) → [`006fe974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe974.md) FUN_006fe974

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fe978",
      "incomplete_value": false,
      "site": "006fe97c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe938",
      "incomplete_value": false,
      "site": "006fe93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe97c",
      "DATA",
      [
        "storage",
        "00c76c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe97c",
      "DATA",
      [
        "storage",
        "00c77018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe934.md#insn-006fe934) · [`006fe938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe934.md#insn-006fe938)
- 新版 [`006fe974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe974.md#insn-006fe974) · [`006fe978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe974.md#insn-006fe978)

~~~diff
- 006fe934 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fe974 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fe934 bytes c82b0090
+ 006fe974 bytes c82b00b0
- 006fe938 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 006fe938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fe938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fe938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe978 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 006fe978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fe938 bytes 08613091
+ 006fe978 bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7726459a5b602dac2f736a9ed38bbe7c"></a>

### [`006fe954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe954.md) → [`006fe994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe994.md) FUN_006fe994

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fea34",
      "incomplete_value": true,
      "site": "006fea4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fe9f4",
      "incomplete_value": true,
      "site": "006fea0c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:efc:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe9d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe990",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006fe9ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe9ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe9d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe9ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fea34",
      "READ",
      [
        "storage",
        "002b0efc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006fe9d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fe9ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006fea34",
      "READ",
      [
        "storage",
        "002b0f3c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fe990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe954.md#insn-006fe990) · [`006fe9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe954.md#insn-006fe9ac) · [`006fe9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe954.md#insn-006fe9ec)
- 新版 [`006fe9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe994.md#insn-006fe9d0) · [`006fe9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe994.md#insn-006fe9ec) · [`006fea2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fe994.md#insn-006fea2c)

~~~diff
- 006fe990 ["INT_ADD", "register:40f0:8", ["const:6fe990:8", "const:4:8"]]
- 006fe990 ["CALL", null, ["ram:47acb4:8"]]
+ 006fe9d0 ["INT_ADD", "register:40f0:8", ["const:6fe9d0:8", "const:4:8"]]
+ 006fe9d0 ["CALL", null, ["ram:47acf4:8"]]
- 006fe990 bytes c9f0f597
+ 006fe9d0 bytes c9f0f597
- 006fe9ac ["INT_ADD", "register:40f0:8", ["const:6fe9ac:8", "const:4:8"]]
- 006fe9ac ["CALL", null, ["ram:47acb4:8"]]
+ 006fe9ec ["INT_ADD", "register:40f0:8", ["const:6fe9ec:8", "const:4:8"]]
+ 006fe9ec ["CALL", null, ["ram:47acf4:8"]]
- 006fe9ac bytes c2f0f597
+ 006fe9ec bytes c2f0f597
- 006fe9ec ["COPY", "tmp:0:8", ["const:efc:8"]]
- 006fe9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fe9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fe9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fea2c ["COPY", "tmp:0:8", ["const:f3c:8"]]
+ 006fea2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fea2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fea2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fe9ec bytes 29f13b91
+ 006fea2c bytes 29f13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab855a965f921986a84a19afb20769b"></a>

### [`006feccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006feccc.md) → [`006fed0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed0c.md) FUN_006fed0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fed30",
      "incomplete_value": false,
      "site": "006fed30",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fecf0",
      "incomplete_value": false,
      "site": "006fecf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fed30",
      "DATA",
      [
        "storage",
        "00c76c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fed30",
      "DATA",
      [
        "storage",
        "00c77088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fece0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006feccc.md#insn-006fece0) · [`006fece8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006feccc.md#insn-006fece8) · [`006fecec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006feccc.md#insn-006fecec)
- 新版 [`006fed20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed0c.md#insn-006fed20) · [`006fed28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed0c.md#insn-006fed28) · [`006fed2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed0c.md#insn-006fed2c)

~~~diff
- 006fece0 ["INT_ADD", "register:40f0:8", ["const:6fece0:8", "const:4:8"]]
- 006fece0 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fed20 ["INT_ADD", "register:40f0:8", ["const:6fed20:8", "const:4:8"]]
+ 006fed20 ["CALL", null, ["callee:00c57e90:8"]]
- 006fece0 bytes 6c631594
+ 006fed20 bytes 5c641594
- 006fece8 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fed28 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fece8 bytes c82b0090
+ 006fed28 bytes c82b00b0
- 006fecec ["COPY", "tmp:0:8", ["const:c88:8"]]
- 006fecec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fecec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fecec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fed2c ["COPY", "tmp:0:8", ["const:88:8"]]
+ 006fed2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fecec bytes 08213291
+ 006fed2c bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590d77ebf4676759a97278510ec2fa38"></a>

### [`006fed00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed00.md) → [`006fed40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed40.md) FUN_006fed40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fed4c",
      "incomplete_value": false,
      "site": "006fed4c",
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
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fed0c",
      "incomplete_value": false,
      "site": "006fed0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fed4c",
      "DATA",
      [
        "storage",
        "00c76c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fed4c",
      "DATA",
      [
        "storage",
        "00c77088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fed04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed00.md#insn-006fed04) · [`006fed08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed00.md#insn-006fed08)
- 新版 [`006fed44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed40.md#insn-006fed44) · [`006fed48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed40.md#insn-006fed48)

~~~diff
- 006fed04 ["COPY", "register:4048:8", ["const:c76000:8"]]
+ 006fed44 ["COPY", "register:4048:8", ["const:c77000:8"]]
- 006fed04 bytes c92b0090
+ 006fed44 bytes c92b00b0
- 006fed08 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 006fed08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fed08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fed08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fed48 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 006fed48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fed48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fed48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fed08 bytes 29213291
+ 006fed48 bytes 29210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-443cbfc12a2db2a86e3f4b2c6dabffdc"></a>

### [`006fed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed1c.md) → [`006fed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed5c.md) FUN_006fed5c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fed78",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fed38",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fed78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006fed78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fed38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed1c.md#insn-006fed38) · [`006fed44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed1c.md#insn-006fed44)
- 新版 [`006fed78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed5c.md#insn-006fed78) · [`006fed84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fed5c.md#insn-006fed84)

~~~diff
- 006fed38 ["INT_ADD", "register:40f0:8", ["const:6fed38:8", "const:4:8"]]
- 006fed38 ["CALL", null, ["ram:47acb4:8"]]
+ 006fed78 ["INT_ADD", "register:40f0:8", ["const:6fed78:8", "const:4:8"]]
+ 006fed78 ["CALL", null, ["ram:47acf4:8"]]
- 006fed38 bytes dfeff597
+ 006fed78 bytes dfeff597
- 006fed44 ["INT_ADD", "register:40f0:8", ["const:6fed44:8", "const:4:8"]]
- 006fed44 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fed84 ["INT_ADD", "register:40f0:8", ["const:6fed84:8", "const:4:8"]]
+ 006fed84 ["CALL", null, ["callee:0047cdd4:8"]]
- 006fed44 bytes 14f8f597
+ 006fed84 bytes 14f8f597
~~~


<a id="compare-2f6c6c6d514ce9d0ac9c4ad28ba9e7d6"></a>

### [`006fed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed88.md) → [`006fedc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fedc8.md) FUN_006fedc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006feddc",
      "incomplete_value": false,
      "site": "006fede0",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006fed9c",
      "incomplete_value": false,
      "site": "006feda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fede0",
      "DATA",
      [
        "storage",
        "00c76d18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fede0",
      "DATA",
      [
        "storage",
        "00c77118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fed94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed88.md#insn-006fed94) · [`006fed98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed88.md#insn-006fed98) · [`006fed9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed88.md#insn-006fed9c)
- 新版 [`006fedd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fedc8.md#insn-006fedd4) · [`006fedd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fedc8.md#insn-006fedd8) · [`006feddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fedc8.md#insn-006feddc)

~~~diff
- 006fed94 ["INT_ADD", "register:40f0:8", ["const:6fed94:8", "const:4:8"]]
- 006fed94 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fedd4 ["INT_ADD", "register:40f0:8", ["const:6fedd4:8", "const:4:8"]]
+ 006fedd4 ["CALL", null, ["callee:00c57e90:8"]]
- 006fed94 bytes 3f631594
+ 006fedd4 bytes 2f641594
- 006fed98 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fedd8 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fed98 bytes c82b0090
+ 006fedd8 bytes c82b00b0
- 006fed9c ["COPY", "tmp:0:8", ["const:d18:8"]]
- 006fed9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fed9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fed9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006feddc ["COPY", "tmp:0:8", ["const:118:8"]]
+ 006feddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006feddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006feddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fed9c bytes 08613491
+ 006feddc bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323ffa6853204e61ff2a1ebcd06534f7"></a>

### [`006fedc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fedc4.md) → [`006fee04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fee04.md) FUN_006fee04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fee20",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fede0",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fee20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006fee20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fedc4.md#insn-006fede0) · [`006fedec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fedc4.md#insn-006fedec)
- 新版 [`006fee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fee04.md#insn-006fee20) · [`006fee2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fee04.md#insn-006fee2c)

~~~diff
- 006fede0 ["INT_ADD", "register:40f0:8", ["const:6fede0:8", "const:4:8"]]
- 006fede0 ["CALL", null, ["ram:47acb4:8"]]
+ 006fee20 ["INT_ADD", "register:40f0:8", ["const:6fee20:8", "const:4:8"]]
+ 006fee20 ["CALL", null, ["ram:47acf4:8"]]
- 006fede0 bytes b5eff597
+ 006fee20 bytes b5eff597
- 006fedec ["INT_ADD", "register:40f0:8", ["const:6fedec:8", "const:4:8"]]
- 006fedec ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fee2c ["INT_ADD", "register:40f0:8", ["const:6fee2c:8", "const:4:8"]]
+ 006fee2c ["CALL", null, ["callee:0047cdd4:8"]]
- 006fedec bytes eaf7f597
+ 006fee2c bytes eaf7f597
~~~


<a id="compare-3474235bbbc8138390f0daea7d59c6c6"></a>

### [`006fef58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fef58.md) → [`006fef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fef98.md) FUN_006fef98

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fefbc",
      "incomplete_value": false,
      "site": "006fefbc",
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
    "old": {
      "definition_site": "006fef7c",
      "incomplete_value": false,
      "site": "006fef7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fefbc",
      "DATA",
      [
        "storage",
        "00c76e18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fefbc",
      "DATA",
      [
        "storage",
        "00c77218",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fef58.md#insn-006fef6c) · [`006fef74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fef58.md#insn-006fef74) · [`006fef78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fef58.md#insn-006fef78)
- 新版 [`006fefac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fef98.md#insn-006fefac) · [`006fefb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fef98.md#insn-006fefb4) · [`006fefb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fef98.md#insn-006fefb8)

~~~diff
- 006fef6c ["INT_ADD", "register:40f0:8", ["const:6fef6c:8", "const:4:8"]]
- 006fef6c ["CALL", null, ["callee:00c57e90:8"]]
+ 006fefac ["INT_ADD", "register:40f0:8", ["const:6fefac:8", "const:4:8"]]
+ 006fefac ["CALL", null, ["callee:00c57e90:8"]]
- 006fef6c bytes c9621594
+ 006fefac bytes b9631594
- 006fef74 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006fefb4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006fef74 bytes c82b0090
+ 006fefb4 bytes c82b00b0
- 006fef78 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 006fef78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fef78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fef78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fefb8 ["COPY", "tmp:0:8", ["const:218:8"]]
+ 006fefb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fefb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fefb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fef78 bytes 08613891
+ 006fefb8 bytes 08610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9402af2f57c3092702f6845beac3736"></a>

### [`006fefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md) → [`006fefe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fefe8.md) FUN_006fefe8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff018",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fefd8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006ff040",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff000",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006ff040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006ff018",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006ff040",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fefd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md#insn-006fefd8) · [`006ff000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md#insn-006ff000) · [`006ff00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md#insn-006ff00c)
- 新版 [`006ff018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fefe8.md#insn-006ff018) · [`006ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fefe8.md#insn-006ff040) · [`006ff04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006fe/006fefe8.md#insn-006ff04c)

~~~diff
- 006fefd8 ["INT_ADD", "register:40f0:8", ["const:6fefd8:8", "const:4:8"]]
- 006fefd8 ["CALL", null, ["ram:47acb4:8"]]
+ 006ff018 ["INT_ADD", "register:40f0:8", ["const:6ff018:8", "const:4:8"]]
+ 006ff018 ["CALL", null, ["ram:47acf4:8"]]
- 006fefd8 bytes 37eff597
+ 006ff018 bytes 37eff597
- 006ff000 ["INT_ADD", "register:40f0:8", ["const:6ff000:8", "const:4:8"]]
- 006ff000 ["CALL", null, ["ram:47acb4:8"]]
+ 006ff040 ["INT_ADD", "register:40f0:8", ["const:6ff040:8", "const:4:8"]]
+ 006ff040 ["CALL", null, ["ram:47acf4:8"]]
- 006ff000 bytes 2deff597
+ 006ff040 bytes 2deff597
- 006ff00c ["INT_ADD", "register:40f0:8", ["const:6ff00c:8", "const:4:8"]]
- 006ff00c ["CALL", null, ["callee:0047cdd4:8"]]
+ 006ff04c ["INT_ADD", "register:40f0:8", ["const:6ff04c:8", "const:4:8"]]
+ 006ff04c ["CALL", null, ["callee:0047cdd4:8"]]
- 006ff00c bytes 62f7f597
+ 006ff04c bytes 62f7f597
~~~


<a id="compare-e5460080a53e343717bc76838d31463e"></a>

### [`006ff04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff04c.md) → [`006ff08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff08c.md) FUN_006ff08c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff0a0",
      "incomplete_value": false,
      "site": "006ff0a4",
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
    "old": {
      "definition_site": "006ff060",
      "incomplete_value": false,
      "site": "006ff064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff0a4",
      "DATA",
      [
        "storage",
        "00c76e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff0a4",
      "DATA",
      [
        "storage",
        "00c77298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff04c.md#insn-006ff058) · [`006ff05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff04c.md#insn-006ff05c) · [`006ff060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff04c.md#insn-006ff060)
- 新版 [`006ff098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff08c.md#insn-006ff098) · [`006ff09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff08c.md#insn-006ff09c) · [`006ff0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff08c.md#insn-006ff0a0)

~~~diff
- 006ff058 ["INT_ADD", "register:40f0:8", ["const:6ff058:8", "const:4:8"]]
- 006ff058 ["CALL", null, ["callee:00c57e90:8"]]
+ 006ff098 ["INT_ADD", "register:40f0:8", ["const:6ff098:8", "const:4:8"]]
+ 006ff098 ["CALL", null, ["callee:00c57e90:8"]]
- 006ff058 bytes 8e621594
+ 006ff098 bytes 7e631594
- 006ff05c ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006ff09c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006ff05c bytes a82b00f0
+ 006ff09c bytes c82b0090
- 006ff060 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 006ff060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff0a0 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006ff0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff060 bytes 08613a91
+ 006ff0a0 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7760a9009744696d4c3cc3adc313749b"></a>

### [`006ff16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff16c.md) → [`006ff1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1ac.md) FUN_006ff1ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff1d0",
      "incomplete_value": false,
      "site": "006ff1d0",
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
    "old": {
      "definition_site": "006ff190",
      "incomplete_value": false,
      "site": "006ff190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff1d0",
      "DATA",
      [
        "storage",
        "00c76f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff1d0",
      "DATA",
      [
        "storage",
        "00c77318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff16c.md#insn-006ff180) · [`006ff188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff16c.md#insn-006ff188) · [`006ff18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff16c.md#insn-006ff18c)
- 新版 [`006ff1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1ac.md#insn-006ff1c0) · [`006ff1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1ac.md#insn-006ff1c8) · [`006ff1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1ac.md#insn-006ff1cc)

~~~diff
- 006ff180 ["INT_ADD", "register:40f0:8", ["const:6ff180:8", "const:4:8"]]
- 006ff180 ["CALL", null, ["callee:00c57e90:8"]]
+ 006ff1c0 ["INT_ADD", "register:40f0:8", ["const:6ff1c0:8", "const:4:8"]]
+ 006ff1c0 ["CALL", null, ["callee:00c57e90:8"]]
- 006ff180 bytes 44621594
+ 006ff1c0 bytes 34631594
- 006ff188 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006ff1c8 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006ff188 bytes a82b00f0
+ 006ff1c8 bytes c82b0090
- 006ff18c ["COPY", "tmp:0:8", ["const:f18:8"]]
- 006ff18c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff18c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff18c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff1cc ["COPY", "tmp:0:8", ["const:318:8"]]
+ 006ff1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff18c bytes 08613c91
+ 006ff1cc bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ef9d04cb9926420229ebf0b887ad495"></a>

### [`006ff1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff1bc.md) → [`006ff1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md) FUN_006ff1fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046bd54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046b/0046bd54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`004700b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004700b4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff238",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff1f8",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "006ff268",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff228",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff238",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006ff268",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006ff238",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006ff268",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff1bc.md#insn-006ff1e8) · [`006ff1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff1bc.md#insn-006ff1f8) · [`006ff228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff1bc.md#insn-006ff228)
- 新版 [`006ff228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff228) · [`006ff238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff238) · [`006ff268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff1fc.md#insn-006ff268)

~~~diff
- 006ff1e8 ["INT_ADD", "register:40f0:8", ["const:6ff1e8:8", "const:4:8"]]
- 006ff1e8 ["CALL", null, ["callee:004700b4:8"]]
+ 006ff228 ["INT_ADD", "register:40f0:8", ["const:6ff228:8", "const:4:8"]]
+ 006ff228 ["CALL", null, ["callee:004700b4:8"]]
- 006ff1e8 bytes a3c3f597
+ 006ff228 bytes a3c3f597
- 006ff1f8 ["INT_ADD", "register:40f0:8", ["const:6ff1f8:8", "const:4:8"]]
- 006ff1f8 ["CALL", null, ["ram:46c984:8"]]
+ 006ff238 ["INT_ADD", "register:40f0:8", ["const:6ff238:8", "const:4:8"]]
+ 006ff238 ["CALL", null, ["ram:46c9c4:8"]]
- 006ff1f8 bytes e3b5f597
+ 006ff238 bytes e3b5f597
- 006ff228 ["INT_ADD", "register:40f0:8", ["const:6ff228:8", "const:4:8"]]
- 006ff228 ["CALL", null, ["ram:46c984:8"]]
+ 006ff268 ["INT_ADD", "register:40f0:8", ["const:6ff268:8", "const:4:8"]]
+ 006ff268 ["CALL", null, ["ram:46c9c4:8"]]
- 006ff228 bytes d7b5f597
+ 006ff268 bytes d7b5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eadba4d73167862844e62df21a64acc"></a>

### [`006ff288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff288.md) → [`006ff2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff2c8.md) FUN_006ff2c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff2ec",
      "incomplete_value": false,
      "site": "006ff2ec",
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
    "old": {
      "definition_site": "006ff2ac",
      "incomplete_value": false,
      "site": "006ff2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff2ec",
      "DATA",
      [
        "storage",
        "00c76f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff2ec",
      "DATA",
      [
        "storage",
        "00c77398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff288.md#insn-006ff29c) · [`006ff2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff288.md#insn-006ff2a4) · [`006ff2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff288.md#insn-006ff2a8)
- 新版 [`006ff2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff2c8.md#insn-006ff2dc) · [`006ff2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff2c8.md#insn-006ff2e4) · [`006ff2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff2c8.md#insn-006ff2e8)

~~~diff
- 006ff29c ["INT_ADD", "register:40f0:8", ["const:6ff29c:8", "const:4:8"]]
- 006ff29c ["CALL", null, ["callee:00c57e90:8"]]
+ 006ff2dc ["INT_ADD", "register:40f0:8", ["const:6ff2dc:8", "const:4:8"]]
+ 006ff2dc ["CALL", null, ["callee:00c57e90:8"]]
- 006ff29c bytes fd611594
+ 006ff2dc bytes ed621594
- 006ff2a4 ["COPY", "register:4040:8", ["const:c76000:8"]]
+ 006ff2e4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006ff2a4 bytes a82b00f0
+ 006ff2e4 bytes c82b0090
- 006ff2a8 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 006ff2a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff2a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff2a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff2e8 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 006ff2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff2a8 bytes 08613e91
+ 006ff2e8 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a482f71194fdb776a205eade3b08187"></a>

### [`006ff2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md) → [`006ff318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md) FUN_006ff318

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047cde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cde8.md) [`006b23e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b23e4.md) [`006b23f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b23f0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`006b2424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2424.md) [`006b2430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b2430.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff4a8",
      "incomplete_value": false,
      "site": "006ff4b0",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff468",
      "incomplete_value": false,
      "site": "006ff470",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff35c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff31c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "006ff494",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff454",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff35c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006ff494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006ff4b0",
      "DATA",
      [
        "storage",
        "00c77008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff35c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006ff494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006ff4b0",
      "DATA",
      [
        "storage",
        "00c77408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md#insn-006ff31c) · [`006ff454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md#insn-006ff454) · [`006ff4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff2d8.md#insn-006ff4b0)
- 新版 [`006ff35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md#insn-006ff35c) · [`006ff494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md#insn-006ff494) · [`006ff4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff318.md#insn-006ff4f0)

~~~diff
- 006ff31c ["INT_ADD", "register:40f0:8", ["const:6ff31c:8", "const:4:8"]]
- 006ff31c ["CALL", null, ["ram:47acb4:8"]]
+ 006ff35c ["INT_ADD", "register:40f0:8", ["const:6ff35c:8", "const:4:8"]]
+ 006ff35c ["CALL", null, ["ram:47acf4:8"]]
- 006ff31c bytes 66eef597
+ 006ff35c bytes 66eef597
- 006ff454 ["INT_ADD", "register:40f0:8", ["const:6ff454:8", "const:4:8"]]
- 006ff454 ["CALL", null, ["ram:47acb4:8"]]
+ 006ff494 ["INT_ADD", "register:40f0:8", ["const:6ff494:8", "const:4:8"]]
+ 006ff494 ["CALL", null, ["ram:47acf4:8"]]
- 006ff454 bytes 18eef597
+ 006ff494 bytes 18eef597
- 006ff4b0 ["INT_ADD", "register:40f0:8", ["const:6ff4b0:8", "const:4:8"]]
- 006ff4b0 ["CALL", null, ["callee:008514f8:8"]]
+ 006ff4f0 ["INT_ADD", "register:40f0:8", ["const:6ff4f0:8", "const:4:8"]]
+ 006ff4f0 ["CALL", null, ["callee:008514f8:8"]]
- 006ff4b0 bytes 02480594
+ 006ff4f0 bytes 02480594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-677a4ddfe41350756b0f41b50053f2c4"></a>

### [`006ff5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5c4.md) → [`006ff604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff604.md) FUN_006ff604

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff618",
      "incomplete_value": false,
      "site": "006ff61c",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff5d8",
      "incomplete_value": false,
      "site": "006ff5dc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff61c",
      "DATA",
      [
        "storage",
        "00c77008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff61c",
      "DATA",
      [
        "storage",
        "00c77408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5c4.md#insn-006ff5d0) · [`006ff5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5c4.md#insn-006ff5d8)
- 新版 [`006ff610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff604.md#insn-006ff610) · [`006ff618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff604.md#insn-006ff618)

~~~diff
- 006ff5d0 ["INT_ADD", "register:40f0:8", ["const:6ff5d0:8", "const:4:8"]]
- 006ff5d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 006ff610 ["INT_ADD", "register:40f0:8", ["const:6ff610:8", "const:4:8"]]
+ 006ff610 ["CALL", null, ["callee:00c57e90:8"]]
- 006ff5d0 bytes 30611594
+ 006ff610 bytes 20621594
- 006ff5d8 ["COPY", "tmp:0:8", ["const:8:8"]]
- 006ff5d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff5d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff5d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff618 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 006ff618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff5d8 bytes 08210091
+ 006ff618 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d919004e7006f2116dece3147f52d62c"></a>

### [`006ff5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5e8.md) → [`006ff628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff628.md) FUN_006ff628

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ff62c",
      "incomplete_value": false,
      "site": "006ff630",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ff5ec",
      "incomplete_value": false,
      "site": "006ff5f0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff630",
      "DATA",
      [
        "storage",
        "00c77008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff630",
      "DATA",
      [
        "storage",
        "00c77408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ff5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5e8.md#insn-006ff5ec)
- 新版 [`006ff62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ff628.md#insn-006ff62c)

~~~diff
- 006ff5ec ["COPY", "tmp:0:8", ["const:8:8"]]
- 006ff5ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ff5ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ff5ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff62c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 006ff62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ff5ec bytes 08210091
+ 006ff62c bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-545f6e44c1ee508301f982097c7948f4"></a>

### [`006ffdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdbc.md) → [`006ffdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffdfc.md) FUN_006ffdfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ffe10",
      "incomplete_value": false,
      "site": "006ffe14",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ffdd0",
      "incomplete_value": false,
      "site": "006ffdd4",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ffe14",
      "DATA",
      [
        "storage",
        "00c77078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffe14",
      "DATA",
      [
        "storage",
        "00c77478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdbc.md#insn-006ffdc8) · [`006ffdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdbc.md#insn-006ffdd0)
- 新版 [`006ffe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffdfc.md#insn-006ffe08) · [`006ffe10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffdfc.md#insn-006ffe10)

~~~diff
- 006ffdc8 ["INT_ADD", "register:40f0:8", ["const:6ffdc8:8", "const:4:8"]]
- 006ffdc8 ["CALL", null, ["callee:00c57e90:8"]]
+ 006ffe08 ["INT_ADD", "register:40f0:8", ["const:6ffe08:8", "const:4:8"]]
+ 006ffe08 ["CALL", null, ["callee:00c57e90:8"]]
- 006ffdc8 bytes 325f1594
+ 006ffe08 bytes 22601594
- 006ffdd0 ["COPY", "tmp:0:8", ["const:78:8"]]
- 006ffdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ffdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ffdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffe10 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 006ffe10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffe10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffe10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ffdd0 bytes 08e10191
+ 006ffe10 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dc21dc63d9397689a530fb0228eeb44"></a>

### [`006ffdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdf8.md) → [`006ffe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffe38.md) FUN_006ffe38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ffe5c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ffe1c",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ffe5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006ffe5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdf8.md#insn-006ffe1c) · [`006ffe28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdf8.md#insn-006ffe28)
- 新版 [`006ffe5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffe38.md#insn-006ffe5c) · [`006ffe68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffe38.md#insn-006ffe68)

~~~diff
- 006ffe1c ["INT_ADD", "register:40f0:8", ["const:6ffe1c:8", "const:4:8"]]
- 006ffe1c ["CALL", null, ["ram:47acb4:8"]]
+ 006ffe5c ["INT_ADD", "register:40f0:8", ["const:6ffe5c:8", "const:4:8"]]
+ 006ffe5c ["CALL", null, ["ram:47acf4:8"]]
- 006ffe1c bytes a6ebf597
+ 006ffe5c bytes a6ebf597
- 006ffe28 ["INT_ADD", "register:40f0:8", ["const:6ffe28:8", "const:4:8"]]
- 006ffe28 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006ffe68 ["INT_ADD", "register:40f0:8", ["const:6ffe68:8", "const:4:8"]]
+ 006ffe68 ["CALL", null, ["callee:0047cdd4:8"]]
- 006ffe28 bytes dbf3f597
+ 006ffe68 bytes dbf3f597
~~~


<a id="compare-689d959f2e3a68a0b67ce726ba667808"></a>

### [`006ffe6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffe6c.md) → [`006ffeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffeac.md) FUN_006ffeac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006ffec0",
      "incomplete_value": false,
      "site": "006ffec4",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ffe80",
      "incomplete_value": false,
      "site": "006ffe84",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ffec4",
      "DATA",
      [
        "storage",
        "00c770f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffec4",
      "DATA",
      [
        "storage",
        "00c774f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffe78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffe6c.md#insn-006ffe78) · [`006ffe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffe6c.md#insn-006ffe80)
- 新版 [`006ffeb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffeac.md#insn-006ffeb8) · [`006ffec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffeac.md#insn-006ffec0)

~~~diff
- 006ffe78 ["INT_ADD", "register:40f0:8", ["const:6ffe78:8", "const:4:8"]]
- 006ffe78 ["CALL", null, ["callee:00c57e90:8"]]
+ 006ffeb8 ["INT_ADD", "register:40f0:8", ["const:6ffeb8:8", "const:4:8"]]
+ 006ffeb8 ["CALL", null, ["callee:00c57e90:8"]]
- 006ffe78 bytes 065f1594
+ 006ffeb8 bytes f65f1594
- 006ffe80 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 006ffe80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ffe80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffec0 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 006ffec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ffe80 bytes 08e10391
+ 006ffec0 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9015cab3f04cd8725b1797395f378c2c"></a>

### [`006ffea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffea8.md) → [`006ffee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffee8.md) FUN_006ffee8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fff0c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ffecc",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fff0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "006fff0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ffecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffea8.md#insn-006ffecc) · [`006ffed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffea8.md#insn-006ffed8)
- 新版 [`006fff0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffee8.md#insn-006fff0c) · [`006fff18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006ffee8.md#insn-006fff18)

~~~diff
- 006ffecc ["INT_ADD", "register:40f0:8", ["const:6ffecc:8", "const:4:8"]]
- 006ffecc ["CALL", null, ["ram:47acb4:8"]]
+ 006fff0c ["INT_ADD", "register:40f0:8", ["const:6fff0c:8", "const:4:8"]]
+ 006fff0c ["CALL", null, ["ram:47acf4:8"]]
- 006ffecc bytes 7aebf597
+ 006fff0c bytes 7aebf597
- 006ffed8 ["INT_ADD", "register:40f0:8", ["const:6ffed8:8", "const:4:8"]]
- 006ffed8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 006fff18 ["INT_ADD", "register:40f0:8", ["const:6fff18:8", "const:4:8"]]
+ 006fff18 ["CALL", null, ["callee:0047cdd4:8"]]
- 006ffed8 bytes aff3f597
+ 006fff18 bytes aff3f597
~~~


<a id="compare-3556097214d533c2041ff10f56728ab7"></a>

### [`006fff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff18.md) → [`006fff58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fff58.md) FUN_006fff58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fff64",
      "incomplete_value": false,
      "site": "006fff68",
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
    "old": {
      "definition_site": "006fff24",
      "incomplete_value": false,
      "site": "006fff28",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fff68",
      "DATA",
      [
        "storage",
        "00c77198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fff68",
      "DATA",
      [
        "storage",
        "00c77598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff18.md#insn-006fff24)
- 新版 [`006fff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fff58.md#insn-006fff64)

~~~diff
- 006fff24 ["COPY", "tmp:0:8", ["const:198:8"]]
- 006fff24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fff24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fff24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fff64 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006fff64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fff64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fff64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fff24 bytes 29610691
+ 006fff64 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c82f860d714280de3cda1bfcf23098c4"></a>

### [`006fff3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff3c.md) → [`006fff7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fff7c.md) FUN_006fff7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fff84",
      "incomplete_value": false,
      "site": "006fff88",
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
    "old": {
      "definition_site": "006fff44",
      "incomplete_value": false,
      "site": "006fff48",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fff88",
      "DATA",
      [
        "storage",
        "00c77198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fff88",
      "DATA",
      [
        "storage",
        "00c77598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fff44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff3c.md#insn-006fff44) · [`006fff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff3c.md#insn-006fff68)
- 新版 [`006fff84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fff7c.md#insn-006fff84) · [`006fffa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fff7c.md#insn-006fffa8)

~~~diff
- 006fff44 ["COPY", "tmp:0:8", ["const:198:8"]]
- 006fff44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006fff44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006fff44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fff84 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006fff84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fff84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fff84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006fff44 bytes 29610691
+ 006fff84 bytes 29611691
- 006fff68 ["INT_ADD", "register:40f0:8", ["const:6fff68:8", "const:4:8"]]
- 006fff68 ["CALL", null, ["callee:00c57eb0:8"]]
+ 006fffa8 ["INT_ADD", "register:40f0:8", ["const:6fffa8:8", "const:4:8"]]
+ 006fffa8 ["CALL", null, ["callee:00c57eb0:8"]]
- 006fff68 bytes d25e1594
+ 006fffa8 bytes c25f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf097cb2521d21d804da4000b9e231a3"></a>

### [`006fff7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md) → [`006fffbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fffbc.md) FUN_006fffbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006fffec",
      "incomplete_value": false,
      "site": "006fffec",
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
    "old": {
      "definition_site": "006fffac",
      "incomplete_value": false,
      "site": "006fffac",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fffec",
      "DATA",
      [
        "storage",
        "00c77198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fffec",
      "DATA",
      [
        "storage",
        "00c77598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006fff94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md#insn-006fff94) · [`006fffa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md#insn-006fffa0) · [`006fffa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md#insn-006fffa4)
- 新版 [`006fffd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fffbc.md#insn-006fffd4) · [`006fffe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ff/006fffbc.md#insn-006fffe0)

~~~diff
- 006fff94 ["INT_ADD", "register:40f0:8", ["const:6fff94:8", "const:4:8"]]
- 006fff94 ["CALL", null, ["callee:00c57e90:8"]]
+ 006fffd4 ["INT_ADD", "register:40f0:8", ["const:6fffd4:8", "const:4:8"]]
+ 006fffd4 ["CALL", null, ["callee:00c57e90:8"]]
- 006fff94 bytes bf5e1594
+ 006fffd4 bytes af5f1594
- 006fffa0 ["COPY", "tmp:0:8", ["const:198:8"]]
- 006fffa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006fffa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006fffa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fffe0 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006fffe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fffe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fffe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006fffa0 bytes 08610691
+ 006fffe0 bytes 08611691
- 006fffa4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 006fffa4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68c7a43fd5919f6aa5b787bf53a8b93"></a>

### [`00700030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700030.md) → [`00700070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700070.md) FUN_00700070

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0070009c",
      "incomplete_value": false,
      "site": "0070009c",
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
    "old": {
      "definition_site": "0070005c",
      "incomplete_value": false,
      "site": "0070005c",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070009c",
      "DATA",
      [
        "storage",
        "00c77198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0070009c",
      "DATA",
      [
        "storage",
        "00c77598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00700054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700030.md#insn-00700054) · [`00700074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700030.md#insn-00700074) · [`0070008c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700030.md#insn-0070008c)
- 新版 [`00700094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700070.md#insn-00700094) · [`007000b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700070.md#insn-007000b4) · [`007000cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700070.md#insn-007000cc)

~~~diff
- 00700054 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00700054 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00700054 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00700054 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00700094 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00700094 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00700094 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00700094 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00700054 bytes 4a610691
+ 00700094 bytes 4a611691
- 00700074 ["INT_ADD", "register:40f0:8", ["const:700074:8", "const:4:8"]]
- 00700074 ["CALL", null, ["callee:00c57e90:8"]]
+ 007000b4 ["INT_ADD", "register:40f0:8", ["const:7000b4:8", "const:4:8"]]
+ 007000b4 ["CALL", null, ["callee:00c57e90:8"]]
- 00700074 bytes 875e1594
+ 007000b4 bytes 775f1594
- 0070008c ["INT_ADD", "register:40f0:8", ["const:70008c:8", "const:4:8"]]
- 0070008c ["CALL", null, ["callee:00c58000:8"]]
+ 007000cc ["INT_ADD", "register:40f0:8", ["const:7000cc:8", "const:4:8"]]
+ 007000cc ["CALL", null, ["callee:00c58000:8"]]
- 0070008c bytes dd5e1594
+ 007000cc bytes cd5f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab082090aa3748505f8d3f611e8d7dfa"></a>

### [`00700304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700304.md) → [`00700344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700344.md) FUN_00700344

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00700350",
      "incomplete_value": false,
      "site": "00700354",
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
      "definition_site": "00700310",
      "incomplete_value": false,
      "site": "00700314",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00700354",
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
      "00700354",
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


#### 変更候補の命令位置

- 旧版 [`00700310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700304.md#insn-00700310)
- 新版 [`00700350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700344.md#insn-00700350)

~~~diff
- 00700310 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00700310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00700310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00700310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00700350 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00700350 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00700350 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00700350 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00700310 bytes 29610891
+ 00700350 bytes 29611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff8a6e74466608ee51f23a9d62fc0ef8"></a>

### [`00700328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700328.md) → [`00700368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700368.md) FUN_00700368

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00700370",
      "incomplete_value": false,
      "site": "00700374",
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
      "definition_site": "00700330",
      "incomplete_value": false,
      "site": "00700334",
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
    "ordinal": 0,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00700374",
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
      "00700374",
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


#### 変更候補の命令位置

- 旧版 [`00700330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700328.md#insn-00700330) · [`00700354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700328.md#insn-00700354)
- 新版 [`00700370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700368.md#insn-00700370) · [`00700394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700368.md#insn-00700394)

~~~diff
- 00700330 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00700330 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00700330 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00700330 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00700370 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00700370 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00700370 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00700370 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00700330 bytes 29610891
+ 00700370 bytes 29611891
- 00700354 ["INT_ADD", "register:40f0:8", ["const:700354:8", "const:4:8"]]
- 00700354 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00700394 ["INT_ADD", "register:40f0:8", ["const:700394:8", "const:4:8"]]
+ 00700394 ["CALL", null, ["callee:00c57eb0:8"]]
- 00700354 bytes d75d1594
+ 00700394 bytes c75e1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15246a421eced5b4159e954f10bc0262"></a>

### [`00700368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700368.md) → [`007003a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/007003a8.md) FUN_007003a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007003d8",
      "incomplete_value": false,
      "site": "007003d8",
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
      "definition_site": "00700398",
      "incomplete_value": false,
      "site": "00700398",
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
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007003d8",
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
      "007003d8",
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


#### 変更候補の命令位置

- 旧版 [`00700380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700368.md#insn-00700380) · [`0070038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700368.md#insn-0070038c) · [`00700390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700368.md#insn-00700390)
- 新版 [`007003c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/007003a8.md#insn-007003c0) · [`007003cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/007003a8.md#insn-007003cc)

~~~diff
- 00700380 ["INT_ADD", "register:40f0:8", ["const:700380:8", "const:4:8"]]
- 00700380 ["CALL", null, ["callee:00c57e90:8"]]
+ 007003c0 ["INT_ADD", "register:40f0:8", ["const:7003c0:8", "const:4:8"]]
+ 007003c0 ["CALL", null, ["callee:00c57e90:8"]]
- 00700380 bytes c45d1594
+ 007003c0 bytes b45e1594
- 0070038c ["COPY", "tmp:0:8", ["const:218:8"]]
- 0070038c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070038c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070038c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007003cc ["COPY", "tmp:0:8", ["const:618:8"]]
+ 007003cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007003cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007003cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070038c bytes 08610891
+ 007003cc bytes 08611891
- 00700390 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00700390 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf43e66e94c7ea4bf54774aacf27f7e3"></a>

### [`0070041c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/0070041c.md) → [`0070045c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/0070045c.md) FUN_0070045c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00700488",
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
      "00700488",
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


#### 変更候補の命令位置

- 旧版 [`00700440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/0070041c.md#insn-00700440) · [`00700460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/0070041c.md#insn-00700460) · [`00700478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/0070041c.md#insn-00700478)
- 新版 [`00700480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/0070045c.md#insn-00700480) · [`007004a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/0070045c.md#insn-007004a0) · [`007004b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/0070045c.md#insn-007004b8)

~~~diff
- 00700440 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00700440 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00700440 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00700440 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00700480 ["COPY", "tmp:0:8", ["const:618:8"]]
+ 00700480 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00700480 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00700480 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00700440 bytes 4a610891
+ 00700480 bytes 4a611891
- 00700460 ["INT_ADD", "register:40f0:8", ["const:700460:8", "const:4:8"]]
- 00700460 ["CALL", null, ["callee:00c57e90:8"]]
+ 007004a0 ["INT_ADD", "register:40f0:8", ["const:7004a0:8", "const:4:8"]]
+ 007004a0 ["CALL", null, ["callee:00c57e90:8"]]
- 00700460 bytes 8c5d1594
+ 007004a0 bytes 7c5e1594
- 00700478 ["INT_ADD", "register:40f0:8", ["const:700478:8", "const:4:8"]]
- 00700478 ["CALL", null, ["callee:00c58000:8"]]
+ 007004b8 ["INT_ADD", "register:40f0:8", ["const:7004b8:8", "const:4:8"]]
+ 007004b8 ["CALL", null, ["callee:00c58000:8"]]
- 00700478 bytes e25d1594
+ 007004b8 bytes d25e1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4eab72c8f0642a5d1015e210c7383c"></a>

### [`00700504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md) → [`00700544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md) FUN_00700544

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`0046a210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a210.md) [`0055a5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5a4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`0046a250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a250.md) [`0055a5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a5e4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007005d4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007005d8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007005e0",
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
      "007005d4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007005d8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007005e0",
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


#### 変更候補の命令位置

- 旧版 [`007005ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md#insn-007005ac) · [`007005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md#insn-007005ec) · [`00700648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md#insn-00700648)
- 新版 [`007005ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md#insn-007005ec) · [`0070062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md#insn-0070062c) · [`00700688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md#insn-00700688)

~~~diff
- 007005ac ["INT_ADD", "register:40f0:8", ["const:7005ac:8", "const:4:8"]]
- 007005ac ["CALL", null, ["callee:00c58610:8"]]
+ 007005ec ["INT_ADD", "register:40f0:8", ["const:7005ec:8", "const:4:8"]]
+ 007005ec ["CALL", null, ["callee:00c58610:8"]]
- 007005ac bytes 195f1594
+ 007005ec bytes 09601594
- 007005ec ["INT_ADD", "register:40f0:8", ["const:7005ec:8", "const:4:8"]]
- 007005ec ["CALL", null, ["callee:008628a8:8"]]
+ 0070062c ["INT_ADD", "register:40f0:8", ["const:70062c:8", "const:4:8"]]
+ 0070062c ["CALL", null, ["callee:008628a8:8"]]
- 007005ec bytes 9f880594
+ 0070062c bytes 9f880594
- 00700648 ["INT_ADD", "register:40f0:8", ["const:700648:8", "const:4:8"]]
- 00700648 ["CALL", null, ["callee:00c58610:8"]]
+ 00700688 ["INT_ADD", "register:40f0:8", ["const:700688:8", "const:4:8"]]
+ 00700688 ["CALL", null, ["callee:00c58610:8"]]
- 00700648 bytes f25e1594
+ 00700688 bytes e25f1594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b6872f90a1249020b2305268bb61681"></a>

### [`00700728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700728.md) → [`00700768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700768.md) _INIT_111

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.31% / 新版 85.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007007a4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007007c8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007007e8",
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
      "007007a4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007007c8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007007e8",
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


#### 変更候補の命令位置

- 旧版 [`007007a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700728.md#insn-007007a0) · [`007007c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700728.md#insn-007007c0) · [`00700754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700728.md#insn-00700754)
- 新版 [`007007e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700768.md#insn-007007e0) · [`00700800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700768.md#insn-00700800) · [`00700794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700768.md#insn-00700794)

~~~diff
- 007007a0 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007007a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007007a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007007a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007007e0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007007e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007007e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007007e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007007a0 bytes 4a093691
+ 007007e0 bytes 4a093791
- 007007c0 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007007c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007007c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007007c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00700800 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00700800 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00700800 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00700800 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007007c0 bytes 4a553a91
+ 00700800 bytes 4a893d91
- 00700754 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00700754 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00700754 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00700754 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00700794 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00700794 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00700794 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00700794 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00700754 bytes 73621f91
+ 00700794 bytes 73622f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3190f45790362da63655d185994c40"></a>

### [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) → [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) FUN_00700af8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 293件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 293件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 97.99% / 新版 97.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00700b30",
      "READ",
      [
        "storage",
        "002b9299",
        null,
        "string"
      ]
    ],
    [
      "00700b48",
      "READ",
      [
        "storage",
        "002b929e",
        null,
        "string"
      ]
    ],
    [
      "00700b90",
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
      "00700b30",
      "READ",
      [
        "storage",
        "002b92d9",
        null,
        "string"
      ]
    ],
    [
      "00700b48",
      "READ",
      [
        "storage",
        "002b92de",
        null,
        "string"
      ]
    ],
    [
      "00700b90",
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


#### 変更候補の命令位置

- 旧版 [`00700ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md#insn-00700ba4) · [`00700bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md#insn-00700bc8) · [`00700bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md#insn-00700bf0)
- 新版 [`00700be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md#insn-00700be4) · [`00700c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md#insn-00700c08) · [`00700c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md#insn-00700c30)

~~~diff
- 00700ba4 ["INT_ADD", "register:40f0:8", ["const:700ba4:8", "const:4:8"]]
- 00700ba4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00700be4 ["INT_ADD", "register:40f0:8", ["const:700be4:8", "const:4:8"]]
+ 00700be4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00700ba4 bytes c35b1594
+ 00700be4 bytes b35c1594
- 00700bc8 ["INT_ADD", "register:40f0:8", ["const:700bc8:8", "const:4:8"]]
- 00700bc8 ["CALL", null, ["callee:00c58610:8"]]
+ 00700c08 ["INT_ADD", "register:40f0:8", ["const:700c08:8", "const:4:8"]]
+ 00700c08 ["CALL", null, ["callee:00c58610:8"]]
- 00700bc8 bytes 925d1594
+ 00700c08 bytes 825e1594
- 00700bf0 ["INT_ADD", "register:40f0:8", ["const:700bf0:8", "const:4:8"]]
- 00700bf0 ["CALL", null, ["callee:0046cc74:8"]]
+ 00700c30 ["INT_ADD", "register:40f0:8", ["const:700c30:8", "const:4:8"]]
+ 00700c30 ["CALL", null, ["callee:0046cc74:8"]]
- 00700bf0 bytes 11b0f597
+ 00700c30 bytes 11b0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c1e9f0f68fcb728a8694cd5a7e53869"></a>

### [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) → [`00707568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md) FUN_00707568

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00934734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00934/00934734.md) · 呼出先 14件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`005e1ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1ad8.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`00664860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664860.md)
- 新版 呼出元 2件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`009348d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00934/009348d0.md) · 呼出先 14件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`005e1b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b18.md) [`005e1b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1b30.md) [`006648a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/006648a0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00707598",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007075a4",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007075ac",
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
      "00707598",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007075a4",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007075ac",
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


#### 変更候補の命令位置

- 旧版 [`00707578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md#insn-00707578) · [`007075c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md#insn-007075c0) · [`0070777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md#insn-0070777c)
- 新版 [`007075b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md#insn-007075b8) · [`00707600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md#insn-00707600) · [`007077bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md#insn-007077bc)

~~~diff
- 00707578 ["INT_ADD", "register:40f0:8", ["const:707578:8", "const:4:8"]]
- 00707578 ["CALL", null, ["callee:00c58610:8"]]
+ 007075b8 ["INT_ADD", "register:40f0:8", ["const:7075b8:8", "const:4:8"]]
+ 007075b8 ["CALL", null, ["callee:00c58610:8"]]
- 00707578 bytes 26431594
+ 007075b8 bytes 16441594
- 007075c0 ["INT_ADD", "register:40f0:8", ["const:7075c0:8", "const:4:8"]]
- 007075c0 ["CALL", null, ["ram:664860:8"]]
+ 00707600 ["INT_ADD", "register:40f0:8", ["const:707600:8", "const:4:8"]]
+ 00707600 ["CALL", null, ["ram:6648a0:8"]]
- 007075c0 bytes a874fd97
+ 00707600 bytes a874fd97
- 0070777c ["COPY", "tmp:0:8", ["const:b38:8"]]
- 0070777c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0070777c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0070777c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007077bc ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 007077bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007077bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007077bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0070777c bytes 00e02c91
+ 007077bc bytes 00e03c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce50c5ffb6d8c2af1ec68d299351b3a"></a>

### [`0070780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/0070780c.md) → [`0070784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070784c.md) FUN_0070784c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 3件 [`00936428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 3件 [`009365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00707880",
      "READ",
      [
        "storage",
        "002b92ca",
        null,
        "string"
      ]
    ],
    [
      "00707884",
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
      "00707880",
      "READ",
      [
        "storage",
        "002b930a",
        null,
        "string"
      ]
    ],
    [
      "00707884",
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


#### 変更候補の命令位置

- 旧版 [`00707838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/0070780c.md#insn-00707838) · [`0070786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/0070780c.md#insn-0070786c) · [`0070788c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/0070780c.md#insn-0070788c)
- 新版 [`00707878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070784c.md#insn-00707878) · [`007078ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070784c.md#insn-007078ac) · [`007078cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/0070784c.md#insn-007078cc)

~~~diff
- 00707838 ["COPY", "tmp:0:8", ["const:2ca:8"]]
- 00707838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00707838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00707838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00707878 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00707878 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00707878 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00707878 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00707838 bytes 29290b91
+ 00707878 bytes 29290c91
- 0070786c ["INT_ADD", "register:40f0:8", ["const:70786c:8", "const:4:8"]]
- 0070786c ["CALL", null, ["callee:009365c4:8"]]
+ 007078ac ["INT_ADD", "register:40f0:8", ["const:7078ac:8", "const:4:8"]]
+ 007078ac ["CALL", null, ["callee:009365c4:8"]]
- 0070786c bytes efba0894
+ 007078ac bytes 46bb0894
- 0070788c ["INT_ADD", "register:40f0:8", ["const:70788c:8", "const:4:8"]]
- 0070788c ["CALL", null, ["callee:00c57eb0:8"]]
+ 007078cc ["INT_ADD", "register:40f0:8", ["const:7078cc:8", "const:4:8"]]
+ 007078cc ["CALL", null, ["callee:00c57eb0:8"]]
- 0070788c bytes 89401594
+ 007078cc bytes 79411594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8aa50dce9a642870fc74e0c7a1a23d"></a>

### [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) → [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) FUN_00707ee0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 174件 [`00467a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467a48.md) [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 174件 [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 97件, `store_value` 4件

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00707f50",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00707f74",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00707f7c",
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
      "00707f50",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00707f74",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00707f7c",
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


#### 変更候補の命令位置

- 旧版 [`007081a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md#insn-007081a4) · [`00708208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md#insn-00708208) · [`00708254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md#insn-00708254)
- 新版 [`007081e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md#insn-007081e4) · [`00708248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md#insn-00708248) · [`00708294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md#insn-00708294)

~~~diff
- 007081a4 ["INT_ADD", "register:40f0:8", ["const:7081a4:8", "const:4:8"]]
- 007081a4 ["CALL", null, ["ram:46c984:8"]]
+ 007081e4 ["INT_ADD", "register:40f0:8", ["const:7081e4:8", "const:4:8"]]
+ 007081e4 ["CALL", null, ["ram:46c9c4:8"]]
- 007081a4 bytes f891f597
+ 007081e4 bytes f891f597
- 00708208 ["INT_ADD", "register:40f0:8", ["const:708208:8", "const:4:8"]]
- 00708208 ["CALL", null, ["ram:46c984:8"]]
+ 00708248 ["INT_ADD", "register:40f0:8", ["const:708248:8", "const:4:8"]]
+ 00708248 ["CALL", null, ["ram:46c9c4:8"]]
- 00708208 bytes df91f597
+ 00708248 bytes df91f597
- 00708254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:768:8"]]
- 00708254 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00708294 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
+ 00708294 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00708254 bytes 73b643f9
+ 00708294 bytes 73b645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cc73844d321a563a92a573edda1d652"></a>

### [`0070e150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e150.md) → [`0070e190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e190.md) FUN_0070e190

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e1b4",
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
      "0070e1b4",
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


#### 変更候補の命令位置

- 旧版 [`0070e164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e150.md#insn-0070e164) · [`0070e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e150.md#insn-0070e170)
- 新版 [`0070e1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e190.md#insn-0070e1a4) · [`0070e1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e190.md#insn-0070e1b0)

~~~diff
- 0070e164 ["INT_ADD", "register:40f0:8", ["const:70e164:8", "const:4:8"]]
- 0070e164 ["CALL", null, ["callee:00c57e90:8"]]
+ 0070e1a4 ["INT_ADD", "register:40f0:8", ["const:70e1a4:8", "const:4:8"]]
+ 0070e1a4 ["CALL", null, ["callee:00c57e90:8"]]
- 0070e164 bytes 4b261594
+ 0070e1a4 bytes 3b271594
- 0070e170 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0070e170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e1b0 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0070e1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e170 bytes 08610a91
+ 0070e1b0 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e721169ddbe4777c9d3c3e57aa18d6fc"></a>

### [`0070e184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e184.md) → [`0070e1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1c4.md) FUN_0070e1c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e1d0",
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
      "0070e1d0",
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


#### 変更候補の命令位置

- 旧版 [`0070e18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e184.md#insn-0070e18c)
- 新版 [`0070e1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1c4.md#insn-0070e1cc)

~~~diff
- 0070e18c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0070e18c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e18c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e18c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e1cc ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0070e1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e18c bytes 29610a91
+ 0070e1cc bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b74c78622d5889e9ac28f40fea7b8d"></a>

### [`0070e1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e1a0.md) → [`0070e1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1e0.md) FUN_0070e1e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e208",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0070e208",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e1a0.md#insn-0070e1c8) · [`0070e1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e1a0.md#insn-0070e1d4)
- 新版 [`0070e208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1e0.md#insn-0070e208) · [`0070e214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e1e0.md#insn-0070e214)

~~~diff
- 0070e1c8 ["INT_ADD", "register:40f0:8", ["const:70e1c8:8", "const:4:8"]]
- 0070e1c8 ["CALL", null, ["ram:47acb4:8"]]
+ 0070e208 ["INT_ADD", "register:40f0:8", ["const:70e208:8", "const:4:8"]]
+ 0070e208 ["CALL", null, ["ram:47acf4:8"]]
- 0070e1c8 bytes bbb2f597
+ 0070e208 bytes bbb2f597
- 0070e1d4 ["INT_ADD", "register:40f0:8", ["const:70e1d4:8", "const:4:8"]]
- 0070e1d4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0070e214 ["INT_ADD", "register:40f0:8", ["const:70e214:8", "const:4:8"]]
+ 0070e214 ["CALL", null, ["callee:0047cdd4:8"]]
- 0070e1d4 bytes f0baf597
+ 0070e214 bytes f0baf597
~~~


<a id="compare-eadf2764121dfeb725bfcd8079bc52a1"></a>

### [`0070e22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e22c.md) → [`0070e26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e26c.md) FUN_0070e26c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e290",
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
      "0070e290",
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


#### 変更候補の命令位置

- 旧版 [`0070e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e22c.md#insn-0070e240) · [`0070e24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e22c.md#insn-0070e24c)
- 新版 [`0070e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e26c.md#insn-0070e280) · [`0070e28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e26c.md#insn-0070e28c)

~~~diff
- 0070e240 ["INT_ADD", "register:40f0:8", ["const:70e240:8", "const:4:8"]]
- 0070e240 ["CALL", null, ["callee:00c57e90:8"]]
+ 0070e280 ["INT_ADD", "register:40f0:8", ["const:70e280:8", "const:4:8"]]
+ 0070e280 ["CALL", null, ["callee:00c57e90:8"]]
- 0070e240 bytes 14261594
+ 0070e280 bytes 04271594
- 0070e24c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0070e24c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0070e24c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0070e24c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0070e28c ["COPY", "tmp:0:8", ["const:718:8"]]
+ 0070e28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0070e28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0070e24c bytes 08610c91
+ 0070e28c bytes 08611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1746c26006b9ebd7d11be95d83ebdb79"></a>

### [`0070e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e260.md) → [`0070e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2a0.md) FUN_0070e2a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e2ac",
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
      "0070e2ac",
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


#### 変更候補の命令位置

- 旧版 [`0070e268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e260.md#insn-0070e268)
- 新版 [`0070e2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2a0.md#insn-0070e2a8)

~~~diff
- 0070e268 ["COPY", "tmp:0:8", ["const:318:8"]]
- 0070e268 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0070e268 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0070e268 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0070e2a8 ["COPY", "tmp:0:8", ["const:718:8"]]
+ 0070e2a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e2a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0070e2a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0070e268 bytes 29610c91
+ 0070e2a8 bytes 29611c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f84e21974bc3401caa571f1cb9ba2d50"></a>

### [`0070e27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e27c.md) → [`0070e2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2bc.md) FUN_0070e2bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0070e2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "0070e2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0070e2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e27c.md#insn-0070e2a4) · [`0070e2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070e/0070e27c.md#insn-0070e2b0)
- 新版 [`0070e2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2bc.md#insn-0070e2e4) · [`0070e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e2bc.md#insn-0070e2f0)

~~~diff
- 0070e2a4 ["INT_ADD", "register:40f0:8", ["const:70e2a4:8", "const:4:8"]]
- 0070e2a4 ["CALL", null, ["ram:47acb4:8"]]
+ 0070e2e4 ["INT_ADD", "register:40f0:8", ["const:70e2e4:8", "const:4:8"]]
+ 0070e2e4 ["CALL", null, ["ram:47acf4:8"]]
- 0070e2a4 bytes 84b2f597
+ 0070e2e4 bytes 84b2f597
- 0070e2b0 ["INT_ADD", "register:40f0:8", ["const:70e2b0:8", "const:4:8"]]
- 0070e2b0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 0070e2f0 ["INT_ADD", "register:40f0:8", ["const:70e2f0:8", "const:4:8"]]
+ 0070e2f0 ["CALL", null, ["callee:0047cdd4:8"]]
- 0070e2b0 bytes b9baf597
+ 0070e2f0 bytes b9baf597
~~~


